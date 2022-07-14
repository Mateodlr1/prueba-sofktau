from NavesEspaciales import Nave

class NavesTripuladas(Nave):
    def __init__(self, tipo, combustible, medidas, misiones):
        super().__init__(tipo, combustible, medidas)
        self.misiones = misiones


    def __str__(self):
        return f'{super().__str__()} [Misiones: {self.misiones}]'




