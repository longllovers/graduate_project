import requests

cookies = {
    'JSESSIONID': '6A2764936C029169B16A14FD2D8AFA8B',
    '_ga_NPHD7M3VS9': 'GS2.1.s1760072255$o1$g0$t1760072415$j60$l0$h0',
    'aliyungf_tc': '2679c50a42fbccdc27cf363ad33a2d22b8a596568e1ca8b03c456f5c16b127ab',
    'acw_tc': '781bad7b17754030486231610e008123e726a35c7362326be01365de177892',
    'JSESSIONID': '437B7E88213A64A56F637A428522D3D4',
    'XSRF-CCKTOKEN': '0559cec8d67006ca586192dd3178a702',
    'CHSICC_CLIENTFLAGYZ': '80d9cc1d6fb6280a4041b60d0103f6e1',
    'Hm_lvt_3916ecc93c59d4c6e9d954a54f37d84c': '1774368268,1775144643,1775403050',
    'HMACCOUNT': 'F1A07FC04AA6343F',
    '_gid': 'GA1.3.249851659.1775403052',
    '_ga_TT7MCH8RRF': 'GS2.1.s1775403062$o6$g0$t1775403064$j58$l0$h0',
    'CHSICC_CLIENTFLAGSYTJ': 'adeca56df1908d8927ea5d9a609a31e2',
    '_ga': 'GA1.1.564919677.1748926996',
    '_ga_YZV5950NX3': 'GS2.1.s1775403052$o5$g1$t1775403101$j11$l0$h0',
    'Hm_lpvt_3916ecc93c59d4c6e9d954a54f37d84c': '1775403101',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://yz.chsi.com.cn',
    'Referer': 'https://yz.chsi.com.cn/sytj/tjyx/qecx.action',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=6A2764936C029169B16A14FD2D8AFA8B; _ga_NPHD7M3VS9=GS2.1.s1760072255$o1$g0$t1760072415$j60$l0$h0; aliyungf_tc=2679c50a42fbccdc27cf363ad33a2d22b8a596568e1ca8b03c456f5c16b127ab; acw_tc=781bad7b17754030486231610e008123e726a35c7362326be01365de177892; JSESSIONID=437B7E88213A64A56F637A428522D3D4; XSRF-CCKTOKEN=0559cec8d67006ca586192dd3178a702; CHSICC_CLIENTFLAGYZ=80d9cc1d6fb6280a4041b60d0103f6e1; Hm_lvt_3916ecc93c59d4c6e9d954a54f37d84c=1774368268,1775144643,1775403050; HMACCOUNT=F1A07FC04AA6343F; _gid=GA1.3.249851659.1775403052; _ga_TT7MCH8RRF=GS2.1.s1775403062$o6$g0$t1775403064$j58$l0$h0; CHSICC_CLIENTFLAGSYTJ=adeca56df1908d8927ea5d9a609a31e2; _ga=GA1.1.564919677.1748926996; _ga_YZV5950NX3=GS2.1.s1775403052$o5$g1$t1775403101$j11$l0$h0; Hm_lpvt_3916ecc93c59d4c6e9d954a54f37d84c=1775403101',
}

data = {
    'mhcx': '1',
    'orderBy': '',
    'ssdm2': '',
    'mldm2': '08',
    'xxfs2': '',
    'zxjh2': '',
    'dwmc2': '',
    'fhbktj': '1',
    'start': '0',
    'pageSize': '20',
}

response = requests.post('https://yz.chsi.com.cn/sytj/stu/tjyxqexxcx.action', cookies=cookies, headers=headers, data=data)