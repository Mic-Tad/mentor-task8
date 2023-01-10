import typing
import attrs
from attrs import define,field
from transport import Transport

@define
class Plane(Transport):
    pass

MaxSpeed = typing.NewType('MaxSpeed',float)
PassCapacity = typing.NewType('PassCapacity',int)

@define
class WarPlane(Plane):
    max_speed = field(factory=MaxSpeed)

@define
class Airliner(Plane):
    pass_capacity = field(factory=PassCapacity)


if __name__ == '__main__':
    wp1=WarPlane(3, 1600, id = 'id2000')
    a1=Airliner(3, 200)
    print(a1)
    print(wp1)
