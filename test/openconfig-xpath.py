from scrapli_netconf.driver import NetconfDriver
from scrapli_info import router

router = router
conn = NetconfDriver(**router)
conn.open()
    
int_xpath =  """
<get xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <filter>
    <components xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-fib-oper"/>
  </filter>
</get>
"""
responsex =  conn.get_config(source="running")
print(responsex.result)

response = conn.get(filter_=int_xpath, filter_type='xpath')
print(response.result)

