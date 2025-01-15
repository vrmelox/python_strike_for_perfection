class Unicon:
    def __init__(self):
        self.temperature = 0

    @property
    def celcius(self):
        return Celcius(self.temperature)

    @property
    def fahrenheit(self):
        return Fahrenheit(self.temperature)


class Celcius(Unicon):
    def __init__(self, temperature):
        super().__init__()
        self.temperature = temperature

    def toFahrenheit(self):
        return (self.temperature * 1.8) + 32

    def toKelvin(self):
        return self.temperature + 273.15

    def toRankine(self):
        return (self.temperature + 273.15) * 1.8

    def toReaumur(self):
        return self.temperature * 0.8

    def toDelisle(self):
        return (100 - self.temperature) * 3 / 2

    def toNewton(self):
        return self.temperature * 0.33

    def toRomer(self):
        return (self.temperature * 21 / 40) + 7.5


class Fahrenheit(Unicon):
    def __init__(self, temperature):
        super().__init__()
        self.temperature = temperature

    def toCelcius(self):
        return (self.temperature - 32) * 5 / 9

    def toKelvin(self):
        return ((self.temperature - 32) * 5 / 9) + 273.15

    def toRankine(self):
        return self.temperature + 459.67


unicon = Unicon()
unicon.temperature = 25

temp_in_kelvin = unicon.celcius.toKelvin()
print(f"25 °C en Kelvin : {temp_in_kelvin} K")

