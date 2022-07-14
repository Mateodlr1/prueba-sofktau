from NavesEspaciales import Nave
from Naveslanzaderas import NaveLanzadera #importo las clases para crear los objetos con sus atributos
from NavesNoTripuladas import NavesNoTripuladas
from NavesTripuladas import  NavesTripuladas


#metodo para imprimir los detalles de los objetos
def imprimir_detalles(objeto):
    print(objeto) #mando a imprimir el objeto directamente
    print(type(objeto)) #imprimo el tipo para saber donde estoy apuntando


#creo los objetos de la clase padre y paso los valores del constructor
saturno_v = NaveLanzadera(" lanzadera", "H+O", "110 metros", "Misiones Espaciales")
imprimir_detalles(saturno_v) #llamo el metodo imprimir detalles y paso como parametro el objeto de la nave

atlas_v = NaveLanzadera(" lanzadera", "queroseno","58 metros", "transportar robot perseverance" )
imprimir_detalles(atlas_v)

delta_iv = NaveLanzadera("Lanzadera", "hidrogeno liquido", "72 metros", "sondas espaciales")
imprimir_detalles(delta_iv)

#Naves espaciales no tripuladas ( sondas )

explorer_1 = NavesNoTripuladas("No tripulada", "energia solar", "1,8 metros", "23533 dias")
imprimir_detalles(explorer_1)

galileo = NavesNoTripuladas("No tripulada", "energia solar", "1.3 metros", "11956 dias")
imprimir_detalles(galileo)

mariner_iv = NavesNoTripuladas("No tripulada", "energia solar", "1.2 metros", "21042 dias")
imprimir_detalles(mariner_iv)

#Naves espaciales tripuladas
apolo_xi = NavesTripuladas("Tripulada", "queroseno y oxifeno", "no aplica", "apolo 11")
imprimir_detalles(apolo_xi)

mercury = NavesTripuladas("Tripulada", "solido", "2 metros", "mercury 1-9")
imprimir_detalles(mercury)

gemini = NavesTripuladas("Tripulada", "oxigeno liquido", "2 metros", "gemini 1-12")
imprimir_detalles(gemini)



