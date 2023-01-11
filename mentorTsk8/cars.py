import typing
import attr
from typeOfCarEnum import TypeOfCar
from transport import Transport


@attr.s
class Cars(Transport):
    type: TypeOfCar = attr.ib(default=TypeOfCar.passenger_car)
    car_capacity: float = attr.ib(default=2000.0, kw_only=True)


if __name__ == '__main__':
    c1 = Cars(4, TypeOfCar.truck)
    print(c1)
