import sys
import time
import random
from tkinter import *
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk

imagen_aceptada = Image.open("t.png")
imagen_aceptada = imagen_aceptada.resize((150, 150), Image.LANCZOS)

imagen_noaceptada = Image.open("p.png")
imagen_noaceptada = imagen_noaceptada.resize((150, 150), Image.LANCZOS)

class Pila(object):
    def __init__(self):
        super(Pila, self).__init__()
        self.arreglo = []
        self.cnt = 0

    def push(self, objeto):
        self.cnt += 1
        self.arreglo.append(objeto)

    def pop(self):
        if self.cnt == 0:
            return False
        else:
            self.cnt -= 1
            del self.arreglo[self.cnt]
            return True

    def top(self):
        return self.arreglo[self.cnt-1]


def ejecutar_programa(ventana, canv):
    archivo = open("Descripción Instantánea.txt", "w")

    xspeed = 5
    yspeed = 0

    print("\n")
    print("Lenguaje libre de contexto {0^n 1^n | n >= 1}\n")
    print("1)MODO MANUAL. 2)MODO AUTOMÁTICO\n")
    opc = input()

    if opc == "1":
        cad = input("CADENA INGRESADA:\n")
        archivo.write("CADENA INGRESADA: \n\n" + cad + "\n")
    else:
        rand = random.randrange(100000)
        cad = str(bin(rand)[2:])
        print("CADENA GENERADA:", cad)
        archivo.write("CADENA GENERADA:\n\n"+cad + "\n")

    cadc = cad[::-1]

    p = Pila()

    e = "a"
    aux1 = 0

    o = Label(ventana, text="CADENA A EVALUAR. \n\n" + cad).place(x=10, y=10)

    cont = 0

    conta = 0
    contb = 0
    conterr = 0
    cuenta = 0
    canv.create_rectangle(300, 50, 400, 550, width=0, fill='white')

    if len(cad) <= 10:
        for i in cadc:
            u = Label(ventana, text="CARACTER A VERIFICAR \n\n "+cad[0:len(cad)-cont]).place(x=10, y=100)
            ventana.update()
            time.sleep(.5)
            cont = cont + 1

            if cadc[cuenta] == "1":
                cuenta = cuenta + 1
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                e = "c"

                canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='orange', outline='white')
                conterr = conterr+1
                time.sleep(.5)
                conterr = conterr + 1
                continue

            if i == "0" and e == "a":
                p.push(i)
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                canv.create_rectangle(300, 500-conta*25, 400, 550-conta*25, width=1, fill='blue', outline='white')
                conta = conta+1
                time.sleep(.5)
                conta = conta + 1
                continue

            if i == "0" and e == "b":
                e = "c"
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "0" and e == "c":
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "1" and e == "c":
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='orange', outline='white')
                conterr = conterr+1
                time.sleep(.5)
                conterr = conterr + 1
                continue

            if i == "1" and e == "a":
                e = "b"
                p.pop()
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                canv.create_rectangle(300, 550-((conta)*25), 400, 600-(conta)*25, width=1, fill='white', outline='white')
                contb = contb+1
                time.sleep(.5)
                continue

            if i == "1" and len(p.arreglo) < aux1:
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='orange', outline='white')
                conterr = conterr+1
                time.sleep(.5)
                conterr = conterr + 1
                continue

            if i == "1" and e == "b":
                p.pop()
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                canv.create_rectangle(300, 550-((conta)*25)+contb*50, 400, 600-(conta)*25+contb*50, width=1, fill='white', outline='white')
                time.sleep(.5)
                contb = contb + 1
                continue
    else:
        
        for i in cadc:
            if cadc[cuenta] == "1":
                cuenta = cuenta + 1
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                e = "c"
                continue

            if i == "0" and e == "a":
                p.push(i)
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "0" and e == "b":
                e = "c"
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "0" and e == "c":
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "1" and e == "c":
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

            if i == "1" and e == "a":
                e = "b"
                p.pop()
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                continue

            if i == "1" and len(p.arreglo) < aux1:
                p.push("X")
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                aux1 = aux1 + 1
                continue

            if i == "1" and e == "b":
                p.pop()
                print(p.arreglo)
                archivo.write("\n"+str(p.arreglo))
                continue

    a = len(p.arreglo)
    if a == 0:
        print("CADENA ACEPTADA")
        archivo.write("\n\nCADENA ACEPTADA")
        imagen_aceptada_tk = ImageTk.PhotoImage(imagen_aceptada)
        o = Label(ventana, image=imagen_aceptada_tk)
        o.image = imagen_aceptada_tk
        o.place(x=500, y=300)
        canv.create_rectangle(300, 50, 400, 550, width=0, fill='green')
    else:
        print("CADENA INVALIDA")
        archivo.write("\n\nCADENA INVALIDA")
        imagen_noaceptada_tk = ImageTk.PhotoImage(imagen_noaceptada)
        o = Label(ventana, image=imagen_noaceptada_tk)
        o.image = imagen_noaceptada_tk
        o.place(x=500, y=300)
        canv.create_rectangle(300, 50, 400, 550, width=0, fill='red')

    def limpiar_etiquetas(ventana):
        for widget in ventana.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()
        canv.delete(ALL)

    archivo.close()

    respuesta = input("¿DESEA EJECUTAR NUEVAMENTE (S/N): ")
    if respuesta.upper() != 'S':
        limpiar_etiquetas(ventana)
        ventana.destroy()
        sys.exit()
    else:
         limpiar_etiquetas(ventana)    

def main():
    ventana = Tk()
    ventana.title("Lenguaje libre de contexto {0^n 1^n | n >= 1}")
    canv = Canvas(ventana, width=800, height=600)
    ventana.geometry("800x600")
    canv.pack()

    while True:
        ejecutar_programa(ventana, canv)

if __name__ == "__main__":
    main()
