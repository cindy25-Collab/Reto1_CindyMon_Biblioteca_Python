
with open("libros.txt", "r") as datos:
    valores = []
    for linea in datos:
        valores.append([str(x) for x in linea.strip().split("\n")])
    print(valores)