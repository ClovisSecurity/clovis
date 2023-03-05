import lxml.etree as et
from pprint import pprint
import xmltodict
import xml.dom.minidom

# from pandas import DataFrame, read_xml
'/home/xaclovis/Code/devnet/it/clovis/netconf/gets/test/netconftry1.xml'

with open('/home/xaclovis/Code/devnet/it/clovis/netconf/gets/test/netconftry1.xml') as f:

    rpc_xml = f.read()

# We can check that the file has been automatically closed.
# xml_file = BytesIO(b)
f.closed

# df = read_xml(rpc_xml)
# XMLDOM for formatting output to xml
xmlDom = xml.dom.minidom.parseString(str(rpc_xml))
# print(xmlDom.toprettyxml(indent="  "))

query_response = xmltodict.parse(rpc_xml)["rpc-reply"]["data"]["netconf-state"]["sessions"]
pprint(query_response)

# sessions_query = query_response["sessions"]["session"]
# print(df.head(50))

# test_1 = et.XML(rpc_xml)
# print(test_1.root)
# print(type(test_1.root))

# print(rpc_xml)
# future_tree = et.fromstring(str(rpc_xml), encoding='UTF-8')
# print(future_tree)
# tree = et.parse(future_tree)
# print(tree)

