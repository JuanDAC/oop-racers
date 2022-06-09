
from colorama import init, Fore, Back, Style


init()


class Vehiculos:

    def __init__(self, color, forma):
        self.color = color
        self.position = 0
        self.aceleracion = 0
        self.forma = forma

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if type(color) is not str:
            raise TypeError("mandame un  color valido!")
        self.__color = color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not type(position) in [int, float]:
            raise TypeError("mandame una position valida!")
        self.__position = position

    @property
    def aceleracion(self):
        return self.__aceleracion

    @aceleracion.setter
    def aceleracion(self, aceleracion):
        if not type(aceleracion) in [int, float]:
            raise TypeError("mandame una aceleracion valida!")
        self.__aceleracion = aceleracion

    @property
    def forma(self):
        return self.__forma

    @forma.setter
    def forma(self, forma):
        if type(forma) is not str:
            raise TypeError("mandame una forma valida!")
        self.__forma = forma

    def spaces(self):
        return (" " * round(self.position))

    def render(self):
        self.position += self.aceleracion
        print(f"{self.spaces()} {self.color} {self.forma} {Fore.RESET}")

    def acelerar(self, value):
        self.aceleracion += value

    def frenar(self, value):
        if (self.aceleracion > 0):
            self.aceleracion -= value


class Carros(Vehiculos):
    def __init__(self, color, forma, ventanas):
        super().__init__(color, forma)
        self.ventanas = ventanas

    @property
    def ventanas(self):
        return self.__ventanas

    @ventanas.setter
    def ventanas(self, ventanas):
        if type(ventanas) is not int:
            raise TypeError("mandame unas ventanas valida!")
        self.__ventanas = ventanas

    def frenar(self, value):
        if (value):
            self.aceleracion = 0


class Bicicletas(Vehiculos):
    def __init__(self, color, forma, sillines):
        super().__init__(color, forma)
        self.sillines = sillines

    @property
    def sillines(self):
        return self.__sillines

    @sillines.setter
    def sillines(self, sillines):
        if type(sillines) is not int:
            raise TypeError("mandame unas ventanas valida!")
        self.__sillines = sillines


if __name__ == '__main__':
    from threading import Timer
    from os import system

    mi_carro_bonito = Carros(Fore.BLUE, "ō͡≡o˞̶", 3)
    mi_bici_bonita = Bicicletas(Fore.RED, "o^o", 1)

    def render():
        system('clear')
        mi_carro_bonito.acelerar(1)
        mi_bici_bonita.acelerar(0.3)
        if (mi_bici_bonita.position >= 50):
            mi_bici_bonita.frenar(.8)
        if (mi_carro_bonito.position >= 50):
            mi_carro_bonito.frenar(True)

        mi_carro_bonito.render()
        mi_bici_bonita.render()

        (Timer(1.0, render, )).start()

    render()
