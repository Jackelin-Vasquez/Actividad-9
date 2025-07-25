peliculas=[]
def opcion_uno():
    cantidad_peliculas= input(input("Ingrese cantidad de peliculas a ingresar:"))
    for i in range(cantidad_peliculas):
        titulo= input(f"Ingrese nombre de pelicula {i+1}:")
        año_estreno= int(input(f"Ingrese año de estreño de pelicula {i+1}"))
        genero=input(f"Ingrese genero de pelicula {i+1}")
        peliculas.append([titulo,año_estreno,genero])
while True:
    print("---MENÚ---")
    print("1.Agregar Peliculas.\n 2. MOstras las peliculas registradas\n 3.Buscar pelicula por genero")
    print("4.Eliminar pelicula por titulo\n 4.Ver estadisiticas de catolagos.\n 5.Salir del programa")

    opcion= input("Ingrese una opcion:")

    match opcion:
        case "1":

