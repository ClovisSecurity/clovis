#! /usr/bin/env python
import traceback
import lxml.etree as et
from ncclient import manager
from ncclient.operations import RPCError
from router_info import router
from pprint import pprint
import xmltodict
from script27 import payload


with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False, device_params={'name': 'csr'}) as m:
    for rpc in payload:
        # print('*' * 50)
        # print(capability)
        try:
          response = m.dispatch(et.fromstring(rpc))
          # print(response)
          data = response.xml
          
          query_response = xmltodict.parse(data)["rpc-reply"]["data"]
          pprint(query_response)
          
          # with open('netconftry1.xml', 'w') as f:
          #  f.write(str(data))
          
          #tree = ElementTree()
          #tree.parse(data)
          #tree.write("netconftry2.xml")
          
        except RPCError as e:
          data = e.xml
          pass
        except Exception as e:
          traceback.print_exc()
          exit(1)
        # in the video he uses .get(netconf_filter) 
        
       # interface_netconf = m.get(netconf_filter)
        exit()
    m.close_session()