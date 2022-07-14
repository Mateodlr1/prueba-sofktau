from NavesEspaciales import Nave

class NavesNoTripuladas(Nave):
    def __init__(self, tipo, combustible, medidas, duracion):
        super().__init__(tipo, combustible, medidas)
        self.duracion = duracion

    def __str__(self):
        return f'{super().__str__()} [Duracion: {self.duracion}]'

