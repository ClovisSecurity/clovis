from scrapli_netconf.driver import NetconfDriver
from scrapli_info import router

router = router
conn = NetconfDriver(**router)
conn.open()
    
int_xpath = '/fib-oper-data/cef-state'

response = conn.get(filter_=int_xpath, filter_type='xpath')
print(response.result)
