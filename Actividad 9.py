peliculas=[]
def opcion_uno():
    cantidad_peliculas= int(input("Ingrese cantidad de peliculas a ingresar:"))
    for i in range(cantidad_peliculas):
        titulo= input(f"Ingrese nombre de pelicula {i+1}:")
        año_estreno= int(input(f"Ingrese año de estreño de pelicula {i+1}:"))
        genero=input(f"Ingrese genero de pelicula {i+1}:")
        peliculas.append([titulo,año_estreno,genero])

def opcion_dos():
    for i in peliculas:
        print(f"Titulo de pelicula:{i[0]}\nAño:{i[1]}\nGénero:{i[2]}")

def opcion_tres():
    buscar_pelicula= input("Ingrese género a buscar:")
    print(f"Peliculas de {buscar_pelicula}")
    for genero in peliculas:
        if peliculas[2] == buscar_pelicula:
            print(genero[0])
        else:
            print("Peliculas no encontradas...")

while True:
    print("---MENÚ---")
    print("1.Agregar Peliculas.\n 2. MOstras las peliculas registradas\n 3.Buscar pelicula por genero")
    print("4.Eliminar pelicula por titulo\n 4.Ver estadisiticas de catolagos.\n 5.Salir del programa")

    opcion= input("Ingrese una opcion:")

    match opcion:
        case "1":
            opcion_uno()
        case "2":
            print("---Peliculas Disponibles----")
            opcion_dos()
        case "3":
            print("---PELICULAS POR SU GENERO---")
            opcion_tres()

