import random
import time

puntaje = random.randint(0,10)
intentos = 0
iniciar_trivia = True
pregunta_correcta = 10
pregunta_incorecta = 5

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BLUE = '\033[34m'
BLACK = '\033[30m'
RESET = '\033[39m'

print (f"{MAGENTA}Bienvenido a la trivia de Henry Ccoillo")
print ("Pondremos a prueba tus conocimientos")
print(f"Tienes {puntaje} puntos")
print(f"Si respondes CORRECTA la pregunta se sumaras {pregunta_correcta} puntos")
print(f"Si respondes INCORRECTA la pregunta se restara {pregunta_incorecta} puntos{RESET}")

nombre = input(f"{BLUE}\nIngresa tu nombre: {RESET}")

print(f"{MAGENTA}\nHola {nombre} responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n{RESET}")

while iniciar_trivia == True:
  for x in range(5,0,-1):
    print(f"{RED}Comienza en {x}...{RESET}")
    time.sleep(1)
    
  intentos +=1
  print(f"{BLACK}\nIntento número: {intentos}{RESET}")
  time.sleep(1)
  print (f"{YELLOW}1) ¿Qué se celebra el 28 de Julio en Perú?")
  print (" a) Día de la Bandera")
  print (" b) Día de la Canción Criolla")
  print (" c) Día de la Independencia")
  print (f" d) Dia del Trabajador{RESET}")

  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "a":
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto!, {nombre} Día de la Bandera se celebra el 7 de Junio{RESET}")
  elif respuesta_1 == "b":
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto!, {nombre} Día de la Canción Criolla se celebra el 31 de Octubre{RESET}")
  elif respuesta_1 == "d":
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto!, {nombre} Día del Trabajador se celebra el 1 de Mayo{RESET}")
  else:
    puntaje += pregunta_correcta
    print(f"{GREEN}Muy bien {nombre}!{RESET}")

  print(f"{GREEN}\nActualmente tienes {puntaje} puntos{RESET}")
  
  time.sleep(1)
  print (f"{YELLOW}\n2) ¿Cúal es la moneda nacional de Perú?")
  print (" a) Euros")
  print (" b) Dolar")
  print (" c) Pesos Peruanos")
  print (f" d) Soles{RESET}")
  
  respuesta_2 = input("\nTu respuesta: ")

  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_2 == "d":
    puntaje += pregunta_correcta
    print(f"{GREEN}Muy bien {nombre}!{RESET}")
  else:
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto {nombre}!{RESET}")
  
  print(f"{GREEN}\nActualmente tienes {puntaje} puntos{RESET}")
  
  print(f"{YELLOW}\nEsta pregunta si respondes correcta se multiplicara x2 los puntos, si tus puntos son negativo sumaras {pregunta_correcta} puntos")
  print("Esta pregunta si respondes cerca a la correcta se sumara 5 puntos")
  print("Esta pregunta si respondes incorrecta se restara 5 puntos")
  print("Esta pregunta si respondes totalmente incorrecta se dividira entre 2 tus puntos")
  
  time.sleep(1)
  print("\n3) ¿Cuál es la ‘capital histórica’ de Perú?")
  print(" a) Cuzco")
  print(" b) Lima")
  print(" c) Ayacucho")
  print(f" d) Arequipa{RESET}")
  
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "b":
    puntaje = puntaje + 5
    print(f"{RED}...{RESET}")
  elif respuesta_3 == "c":
    puntaje = puntaje - 5
    print(f"{RED}Incorrecto{RESET}")
  elif respuesta_3 == "d":
    puntaje = puntaje / 2
    print(f"{RED}Totalmente Incorrecto!{RESET}")
  else:
    if puntaje < 0:
      puntaje += pregunta_correcta
    else:
      puntaje = puntaje * 2
    print(f"{GREEN}Correcto {nombre}!{RESET}")

  print(f"{GREEN}\nActualmente tienes {puntaje} puntos{RESET}")

  print(f"{YELLOW}\nPara la pregunta 4 Digite 2 números")
  pregunta4_1numero = int(input("\nDigite el 1er número: "))
  pregunta4_2numero = int(input("\nDigite el 2do número: "))
  
  print(f"\n4) ¿Cuanto es {pregunta4_1numero}x{pregunta4_2numero}?{RESET}")

  respuesta_4 = int(input("Introduce la respuesta(número): "))
  resultado_4 = pregunta4_1numero * pregunta4_2numero

  if(respuesta_4 == resultado_4):
    puntaje += pregunta_correcta
    print(f"{GREEN}Bien {nombre}!{RESET}")
  else:
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto {nombre}!, {pregunta4_1numero}x{pregunta4_2numero} es : {resultado_4}{RESET}")
    
  print(f"{GREEN}\nActualmente tienes {puntaje} puntos{RESET}")
  
  print(f"{YELLOW}\n5) ¿Cuánto es 4 al cuadrado")
  print("a) 4")
  print("b) 24")
  print("c) 8")
  print(f"d) 16{RESET}")

  respuesta_5 = input("\nTu respuesta: ")
  
  while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_5 == "d":
    puntaje += pregunta_correcta
    print(f"{GREEN}Bien {nombre}{RESET}")
  else:
    puntaje -= pregunta_incorecta
    print(f"{RED}Incorrecto {nombre}!, 4 al cuadrado es: 16{RESET}")
  

  if puntaje < 0:
    print(f"\n{RED}Gracias {nombre} por jugar mi trivia, alcanzaste {puntaje} puntos{RESET}")
  else:
    print(f"{GREEN}Gracias {nombre} por jugar mi trivia, alcanzaste {puntaje} puntos{RESET}")

  
  print(f"{GREEN}\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":
   print(f"\nEspero {nombre} que lo hayas pasado bien, hasta pronto!{RESET}")
   iniciar_trivia = False
