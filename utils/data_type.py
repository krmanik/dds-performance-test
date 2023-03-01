from cyclonedds.idl import IdlStruct
from dataclasses import dataclass

@dataclass
class Message(IdlStruct):
    text: str
    timestamp: float
