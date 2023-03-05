from dataclasses import dataclass

@dataclass
class Payload:
  xml: str
  filename: str
  desc: str
  query: str