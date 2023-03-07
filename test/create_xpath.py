from scrapli_netconf.driver import NetconfDriver
from scrapli_info import router

router = router
conn = NetconfDriver(**router)
conn.open()
    
rpc_filter = """
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper" type="xpath" select='/interfaces/interface[name="GigabitEthernet1"]' />
</get>
"""

response = conn.rpc(rpc_filter)
print(response.result)
