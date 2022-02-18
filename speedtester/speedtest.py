import psycopg2
import dbcreds
import os
import time
import subprocess
import json
from datetime import datetime, timezone


def define_db():
    creds = dbcreds.Credentials()
    directory = os.path.dirname(os.path.realpath(__file__))
    key = 'db.key'
    if not os.path.exists(os.path.join(directory, key)):
        print(f'****No DB credentials found****')
        creds.username = input('Enter your DB password:')
        creds.password = input('Enter your DB password:')
        creds.create_cred()
    else:
        print(f'DB credentials found\n'
              f'username: {creds.getuser()}\n'
              f'password: *********')
    host = 'speedtestdb.postgres.database.azure.com'
    dbname = 'postgres'
    user = creds.getuser()
    password = creds.getpass()
    sslmode = "require"
    # Construct connection string
    conn_string = f'host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}'
    conn = psycopg2.connect(conn_string)
    print(f'Connected to {host}')
    with conn:
        with conn.cursor() as cur:
            # define database for our usage
            cur.execute("""CREATE TABLE IF NOT EXISTS speedtest (
                            collectdatetime timestamptz UNIQUE
                            ,download integer
                            ,upload integer
                            ,latency decimal
                            ,jitter decimal
                            ,packetLoss integer
                            ,result_url text
                            ,server_id text);
                        """)
    return conn


def run_speedtest():
    # speedtest.exe must be in the path of the location of the running script
    # enhancement to auto download etc
    speedtest = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'speedtest.exe')
    try:
        print(f'Running speedtest.exe - This will take a few seconds')
        start = time.perf_counter()
        results = json.loads(subprocess.check_output([speedtest, '--f', 'json'], universal_newlines=True))
        end = time.perf_counter()
        print(f'Finished in {round(end - start, 2)} second(s)')

        # print(results)
        return results
    except subprocess.CalledProcessError as error:
        print(f'Error running speedtest.exe: {error}')


def update_database(insert: dict, connection):
    r = insert
    con = connection
    # uses output of speedtest json for sqlite injection
    formatted_insert = {'collectdatetime': datetime.now(timezone.utc)
        , 'download': r['download']['bandwidth']
        , 'upload': r['upload']['bandwidth']
        , 'latency': r['ping']['latency']
        , 'jitter': r['ping']['jitter']
        , 'packetLoss': r['packetLoss']
        , 'result_url': r['result']['url']
        , 'server_id': r['server']['id']
                        }
    with conn:
        with conn.cursor() as cur:
            print('Inserting results into the db')
            cur.execute("""INSERT into speedtest
                                VALUES(
                                'now'
                                ,%(download)s
                                ,%(upload)s
                                ,%(latency)s
                                ,%(jitter)s
                                ,%(packetLoss)s
                                ,%(result_url)s
                                ,%(server_id)s 
                                )""", formatted_insert)


conn = define_db()
speedtest_results = run_speedtest()
update_database(speedtest_results, conn)
conn.close()
