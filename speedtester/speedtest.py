import subprocess
import os
import sqlite3
from datetime import datetime
import json
import time


def define_database(db_name):
    try:
        con = sqlite3.connect(db_name,
                              detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        print(f'Checking for speedtest table in {db_name}')
        table_result = cur.execute("""SELECT EXISTS (
                                    SELECT name FROM sqlite_schema
                                     WHERE type = 'table' 
                                     AND name = 'speedtest')""").fetchone()
        if table_result[0] == 0:
            print(f'Creating table speedtest')
            cur.execute("""CREATE TABLE speedtest (
                            collectdatetime timestamp UNIQUE
                            ,download integer
                            ,upload integer
                            ,latency integer
                            ,jitter integer
                            ,packetLoss integer
                            ,result_url text
                            ,server_id text
                            )""")
            con.commit()
        else:
            print('Table already exists')
    except sqlite3.Error as error:
        print(f'SQL connection error: {error}')
    finally:
        if con:
            con.close()


def update_database(insert: dict, db_name: str):
    r = insert
    # uses output of speedtest json for sqlite injection
    formatted_insert = {'collectdatetime': datetime.now()
        , 'download': r['download']['bandwidth']
        , 'upload': r['upload']['bandwidth']
        , 'latency': r['ping']['latency']
        , 'jitter': r['ping']['jitter']
        , 'packetLoss': r['packetLoss']
        , 'result_url': r['result']['url']
        , 'server_id': r['server']['id']
                        }
    try:
        con = sqlite3.connect(db_name,
                              detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        print('Inserting results into the db')
        cur.execute("""INSERT into speedtest 
                        VALUES(
                        :collectdatetime 
                        ,:download
                        ,:upload
                        ,:latency
                        ,:jitter
                        ,:packetLoss
                        ,:result_url
                        ,:server_id
                        )""", formatted_insert)
        con.commit()
    except sqlite3.Error as error:
        print(f'Error inserting data into database: {error}')
    finally:
        if con:
            con.close()


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


def main():
    # defining our database location
    db_location = os.path.dirname(os.path.realpath(__file__))
    db_name = 'speedtest.db'
    db_full = os.path.join(db_location, db_name)
    define_database(db_full)

    # runs speedtest and appends values into db
    update_database(run_speedtest(), db_full)
    print('Completed!')


if __name__ == '__main__':
    main()
