# pip install vertica-python
import vertica_python
import time
from bs4 import BeautifulSoup
import lxml
import requests


# Vertica example

def get_databases() -> list:
    conn_info = {'host': 'CERNOCRSVERTDB-QUERY.CERNERASP.com',
                 'port': 5433,
                 'user': 'jr019593',
                 'password': '',
                 'database': 'Cerner',
                 # default throw error on invalid UTF-8 results
                 'unicode_error': 'strict',
                 'autocommit': True,
                 # using server-side prepared statements is disabled by default
                 'use_prepared_statements': False,
                 # 5 seconds timeout for a socket operation (Establishing a TCP connection or read/write operation)
                 # this might need to be adjusted, it will randomly timeout
                 'connection_timeout': 10}
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
        end = time.perf_counter()
        print(f'Query executed in: {round(end - start, 2)} second(s)')
        return (cur.fetchall())


def get_xrshares(client, domain):
    # POST GET on configuration uri
    try:
        r = requests.get(
            f'http://config.cernerasp.com/configuration-1.0/{domain}.{client}.cernerasp.com/urn:cerner:config:xr:network-file-share-1.0')
    except:
        return f'Failed!'
    soup = BeautifulSoup(r.text, 'lxml-xml')
    shares = soup.find_all('share')
    list = []
    for share in shares:
        list.append({'display': share.get('display'), 'path': share.get('path')})
    return list


def main():
    for client in get_databases():
        mnemonic, domain = client[0], client[1]
        print(f'Getting XR shares for {mnemonic}:{domain}')
        print(get_xrshares(mnemonic, domain))


if __name__ == '__main__':
    main()
