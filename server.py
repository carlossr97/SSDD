# @author Carlos


import socket              #Importar el modulo socket
import sys
import struct
s = socket.socket()                #Crear el objeto socket

host = socket.gethostname()                    #Obtener el nombre local de la maquina
port = int(sys.argv[1])


s.bind((host, port))              #Bindear el puerto
s.listen(5)                      # Esperar por la conexion del cliente

print("El servidor esta corriendo sin problemas")
print("El host es: ",host)
while True:
     c, addr = s.accept()         # Establecer la conexion con el cliente
     print('Obtuve una conexion desde', addr)

     while True:
          try:
               equation=c.recv(1024).decode()
               if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
                    c.send("Quit".encode())
                    break
               else:
                    print("Recibi la siguiente operacion:", equation)
                    result = eval(equation)
                    c.send(struct.pack(">H", len(str(result))))
                    c.send(str(result).encode('UTF-8')) 
                                      #Envia los resultados al cliente
          except (ZeroDivisionError):
               c.send("ZeroDiv".encode())
          except (ArithmeticError):
               c.send("MathError".encode())
          except (SyntaxError):
               c.send("SyntaxError".encode())
          except (NameError):
               c.send("NameError".encode())

     c.close()             # Cerrar la conexion