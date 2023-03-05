#! /usr/bin/env python
import traceback
from xmlrpc.client import TRANSPORT_ERROR
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

router = {"host": "10.10.20.48", "port": "830",
          "username": "developer", "password": "C1sco12345"}

payload = [
'''
<get-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <source>
    <running/>
  </source>
  <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name/>
      </interface>
    </interfaces>
  </filter>
</get-config>
''',
]

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False, device_params={'name': 'csr'}) as m:
    for rpc in payload:
        # print('*' * 50)
        # print(capability)
        try:
          response = m.dispatch(et.fromstring(rpc))
          print("Printing Response:")
          print("This is the response:", response)
          print("end of response")
          data = response.xml
          print("PRINTING DATA")
          print(data)
          
        except RPCError as e:
          data = e.xml
          pass
        except Exception as e:
          traceback.print_exc()
          exit(1)
        
        # in the video he uses .get(netconf_filter) 
        
       # interface_netconf = m.get(netconf_filter)
        print('getting running config')
        exit()
    m.close_session()
