# pip install vertica-python
import vertica_python
import time

# Vertica example

conn_info = {'host': 'CERNOCRSVERTDB-QUERY.CERNERASP.com',
             'port': 5433,
             'user': 'jr019593',
             'password': '***password***',
             'database': 'Cerner',
             # default throw error on invalid UTF-8 results
             'unicode_error': 'strict',
             'autocommit': True,
             # using server-side prepared statements is disabled by default
             'use_prepared_statements': False,
             # 5 seconds timeout for a socket operation (Establishing a TCP connection or read/write operation)
             # this might need to be adjusted, it will randomly timeout
             'connection_timeout': 5}

# using with for auto connection closing after usage
query = "select distinct client,domain,instancehost, instancename " \
        "from " \
        "olyprd.oracle_instance " \
        "where instancenum = 1 " \
        "and domain in(select DISTINCT domain " \
        "from OLYPRD.CLIENT_DOMAIN_NODE " \
        "where production_ind = 1 " \
        "and millennium_ind = 1) " \
        "and collectdatetime > sysdate -1 " \
        "order by client"
start = time.perf_counter()
print(f'Running query')
with vertica_python.connect(**conn_info) as connection:
    cur = connection.cursor()
    cur.execute(query)
    for results in cur.fetchall():
        print(results)
end = time.perf_counter()
print(f'Query executed in:{round(end - start, 2)} second(s)')






