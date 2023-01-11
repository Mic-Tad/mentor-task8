import typing
import attr

TransportID = typing.NewType('TransportID', str)
NumOfWheels = typing.NewType('NumOfWheels', int)


@attr.s
class Transport:
    id = attr.ib(default=TransportID("id0000"), kw_only=True)
    num_of_wheels = attr.ib(factory=NumOfWheels)


if __name__ == '__main__':
    tr1 = Transport(id='id20201', num_of_wheels=5)
    print(tr1)
