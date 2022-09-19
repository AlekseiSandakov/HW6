class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class Car:
    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
                return 'Завожу авто!'
            else:
                raise LowFuelError('Топливо на нуле!')
        else:
            return 'Уже тарахтит!'

    def move(self, distance):
        need_fuel = distance * self.fuel_consumption
        if need_fuel > self.fuel:
            raise NotEnoughFuel('Топлива не хватит!')
        else:
            self.fuel -= need_fuel
            return f'Топлива на остатке {self.fuel}'


def main():
    car = Car(2500, False, 500, 5)

    print(car.start())

    print(car.move(10))

    print(car.start())

    print(car.move(10))


if __name__ == '__main__':
    main()
