from NavesEspaciales import Nave #importo la clase nave

class NaveLanzadera(Nave):#defino la clase nave lanzadera y extiende de la clase nave
    def __init__(self, tipo, combustible, medidas, funcion): #inicializo los atributos de la clase padre y la clase naves lanzaderas
        super().__init__(tipo, combustible, medidas)#inicializo el metodo init del objeto de la clase padre
        self.funcion = funcion   #inicializo atribitos de la clase hija


    def __str__(self): #sobreescribo el metodo de la clase padre
        return f'{super().__str__()} [Transport: {self.funcion}]' #imprimo los valores y llamo el metodo super de la clase padre


