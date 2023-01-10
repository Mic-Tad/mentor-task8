import typing
import attrs
from attrs import define,field

TransportID = typing.NewType('TransportID', str)
NumOfWheels = typing.NewType('NumOfWheels', int)

@define 
class Transport:
    
    id = field(default = TransportID("id0000"), kw_only = True)
    num_of_wheels = field(factory = NumOfWheels)
    
if __name__ == '__main__':
    tr1 = Transport(id = 'id20201', num_of_wheels = 5)
    print(tr1)
