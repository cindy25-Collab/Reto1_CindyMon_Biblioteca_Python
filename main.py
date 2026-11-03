ancho = 30
archivo = "libros.txt"
modo = "w"
encoding = "utf-8"

hline = "+" + ("-" + ancho + "+") * 6
with open(archivo, modo , encoding) as f:
    for i in range (7):
        print(hline, file = f)