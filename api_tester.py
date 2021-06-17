from bs4 import BeautifulSoup
import lxml
import requests
import time


start = time.perf_counter()
# POST GET on configuration uri
r = requests.get('http://config.cernerasp.com/configuration-1.0/p126.univ_nm.cernerasp.com/urn:cerner:config:xr:network-file-share-1.0')

soup = BeautifulSoup(r.text, 'lxml-xml')
shares = soup.find_all('share')

for share in shares:
    name = share.get('display')
    path = share.get('path')
    print(f'Share:{name} Path:{path}')

# dsn_tns = cx_Oracle.makedsn('univnmdb1.cernerasp.com', '1521', service_name='s77_p126.world')
# conn = cx_Oracle.connect(user='v500', password='Un1v500', dsn=dsn_tns)


end = time.perf_counter()
print(f'Finished in: {round(end - start, 2)} second(s)')
