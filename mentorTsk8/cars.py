import typing
import attr
from enum import Enum

from transport import Transport

class TypeOfCar (Enum):
    passenger_car = 1
    truck = 2

CarType = typing.NewType('CarType', str)
Weight = typing.NewType('Weight', float)

@attr.s
class Cars (Transport):
    type = attr.ib(factory = CarType)
    car_capacity = attr.ib(default=Weight(2000.0), kw_only = True)

if __name__ == '__main__':
    c1 = Cars(4, TypeOfCar.passenger_car.name)
    print(c1)
