from scrapli_netconf.driver import NetconfDriver
from scrapli_info import router

router = router
conn = NetconfDriver(**router)
conn.open()
    

# Here we do a standard get in order to access information that will be used to go into subtrees
# This query allows us to access the cname variable so that we can pass it in the subsequent query.
rpc_filter =  """
<get xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <filter>
    <components xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"/>
  </filter>
</get>
"""

unfiltered_response = conn.rpc(rpc_filter)
print(unfiltered_response.result)

rpc_filter2 = """
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-vlans-oper" type="xpath" select='/vlans/vlan[id=232]' />
</get>
"""

# response = conn.rpc(rpc_filter2)
# print(response.result)
