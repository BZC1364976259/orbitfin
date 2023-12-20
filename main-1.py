import json
import os.path
import time

import urllib3
from urllib3.util.ssl_ import create_urllib3_context

if __name__ == '__main__':
    ctx = create_urllib3_context()
    ctx.load_default_certs()
    ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
    url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'AlteonP10=CZb6Hyw/F6yzIGEUNnEUCA$$; Cookie_1=value; Cookie_2=value; ags=b168c5dd63e5c0bebdd4fb78b2b4704a'
    }
    index = 1
    fn = 'demo.csv'
    if os.path.exists(fn):
        os.remove(fn)
    f = open(fn, 'a')
    f.write('ISIN,Bond Code,Bond Type,Issue Start Date,Issue Start Date\n')
    while index < 10:
        payload = 'pageNo=' + str(
            index) + '&pageSize=15&isin=&bondCode=&issueEnty=&bondType=100001&couponType=&issueYear=2023&rtingShrt=&bondSpclPrjctVrty='
        with urllib3.PoolManager(ssl_context=ctx) as http:
            response = http.request(method="POST", url=url, body=payload, headers=headers)
            data = json.loads(str(response.data, encoding='utf-8'))
            record = data['data']['resultList']
            # print(record)
            i = 0
            while i < len(record):
                dat = str(record[i]['isin']) + ',' + str(record[i]['bondCode']) + ',' + str(record[i]['bondType'])\
                      + ',' + str(record[i]['issueStartDate']) + ',' + str(record[i]['issueStartDate']) + '\n'
                f.write(dat)
                i += 1
            time.sleep(2)
            index += 1
    f.close()
