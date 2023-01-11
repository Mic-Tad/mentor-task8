import typing
import attr

from transport import Transport


@attr.s
class Plane(Transport):
    pass


MaxSpeed = typing.NewType('MaxSpeed', float)
PassCapacity = typing.NewType('PassCapacity', int)


@attr.s
class WarPlane(Plane):
    max_speed: MaxSpeed = attr.ib(default=MaxSpeed(2000.0))


@attr.s
class Airliner(Plane):
    pass_capacity: PassCapacity = attr.ib(default=PassCapacity(300))


if __name__ == '__main__':
    wp1 = WarPlane(3, 1600, id='id2000')
    a1 = Airliner(3, 200)
    print(a1)
    print(wp1)
