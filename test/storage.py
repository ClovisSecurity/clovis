from dataclasses import dataclass

@dataclass
class DefaultInfo:
  interface: str
  vlan: str
  payload: str
  desc: str