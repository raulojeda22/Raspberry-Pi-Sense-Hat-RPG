from sense_hat import SenseHat
import random
#Functions#
def INICIAR_PANTALLA():
  contadorY = 0
  while tamanyMapaY > contadorY:
    contadorX = 0
    while tamanyMapaX > contadorX:
      objecteAleatori = random.randint(0, 1000)
      if objecteAleatori < 750:
        objecteGenerat=terra
      elif objecteAleatori < 850:
        objecteGenerat=pedra
      elif objecteAleatori < 900:
        objecteGenerat=trampa
      elif objecteAleatori < 930:
        objecteGenerat=enemic
      elif objecteAleatori < 960:
        objecteGenerat=armaBlanca
      elif objecteAleatori < 980:
        objecteGenerat=armaDeFoc
      elif objecteAleatori < 990:
        objecteGenerat=amigable
      elif objecteAleatori < 1000:
        objecteGenerat=tresor
      sense.set_pixel(contadorX, contadorY, objecteGenerat)
      contadorX=contadorX+1
    contadorY=contadorY+1
    
def PERSONATGE():
  sense.set_pixel(posicioX, posicioY, personatge)

def GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga):
  objectePosicionat = sense.get_pixel(posicioX, posicioY)
  objecteAntic = sense.get_pixel(7, 7)
  print (objecteAntic)
  sense.set_pixel(posicioAntiga[0], posicioAntiga[1],objecteAntic)
  sense.set_pixel(7, 7, objectePosicionat)
  
def POSICION_NUEVA_EN_MAPA_IZQUIERDA(posicioX,posicioY):
  posicioX=6
  sense.set_pixel(posicioX, posicioY, personatge)
def POSICION_NUEVA_EN_MAPA_DERECHA(posicioX,posicioY):
  posicioX=0
  sense.set_pixel(posicioX, posicioY, personatge)
def POSICION_NUEVA_EN_MAPA_ARRIBA(posicioX, posicioY, posicioAntiga):
  posicioY=6
  sense.set_pixel(posicioX, posicioY, personatge)
  GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga)
  return
def POSICION_NUEVA_EN_MAPA_ABAJO(posicioX,posicioY):
  posicioY=0
  sense.set_pixel(posicioX, posicioY, personatge)


def MOVIMENT(posicioX,posicioY):
  while True:
    posicioAntiga=(posicioX, posicioY)
    print (posicioAntiga)
    accio=input()
    if accio == 'w':
      posicioY = posicioY - 1
      if posicioY < 0:
        posicioY=6
        INICIAR_PANTALLA()
      GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga)
      
    elif accio == 'a':
      posicioX = posicioX - 1
      if posicioX < 0:
        posicioX=7
        INICIAR_PANTALLA()
      GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga)
      
    elif accio == 's':
      posicioY = posicioY + 1
      if posicioY > 6:
        posicioY=0
        INICIAR_PANTALLA()
      GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga)
      
    elif accio == 'd':
      posicioX = posicioX + 1
      if posicioX > 7:
        posicioX=0
        INICIAR_PANTALLA()
      GUARDAR_OBJETO(posicioX, posicioY, posicioAntiga)
    sense.set_pixel(posicioX, posicioY, personatge)
      
#sense.set_pixel(3, 3, 0, 255, 0)
#Variables#
personatge = (0, 255, 0)
enemic = (255, 0, 0)
armaDeFoc = (169, 169, 169)
armaBlanca = (255, 255, 255)
tresor = (255, 255, 0)
pedra = (105, 105, 105)
trampa = (255, 0, 255)
terra = (160, 82, 45)
amigable = (0, 0, 255)
tamanyMapaX = 8
tamanyMapaY = 7
posicioX = int(tamanyMapaX/2)
posicioY = int(tamanyMapaY/2)
canviarMapa=1
#Main Program#
sense = SenseHat()
sense.clear()
sense.set_pixel(7, 7, terra)
INICIAR_PANTALLA()
PERSONATGE()
hola=2
hola=hola-1
print (hola)
MOVIMENT(posicioX,posicioY)
