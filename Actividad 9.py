peliculas=[]
def opcion_uno():
    cantidad_peliculas= int(input("Ingrese cantidad de peliculas a ingresar:"))
    for i in range(cantidad_peliculas):
        print(f"----PELICULA NO.{i+1}----")
        titulo= input(f"Ingrese nombre de pelicula {i+1}:")
        año_estreno= int(input(f"Ingrese año de estreño de pelicula {i+1}:"))
        genero=input(f"Ingrese genero de pelicula {i+1}:")
        peliculas.append([titulo,año_estreno,genero])

def opcion_dos():
    for i in peliculas:
        print("---"*7)
        print(f"Titulo de pelicula:{i[0]}\nAño:{i[1]}\nGénero:{i[2]}")
        print("---"*7)

def opcion_tres():
    buscar_pelicula= input("Ingrese género a buscar:")
    print(f"Peliculas de {buscar_pelicula}")
    for genero in peliculas:
        if genero[2] == buscar_pelicula:
            print(f"Nombre de pelicula:{genero[0]}")
def opcion_cuatro():
    while True:
        titulo_pelicula= input("Ingrese nombre de pelicula a eliminar:")
        if titulo_pelicula in peliculas:
            peliculas.remove(titulo_pelicula)
            break
        else:
            print("Pelicula no encontrada para eliminar...")

def opcion_cinco():
    total_peliculas= len(peliculas)
    generos=[]
    mayor = peliculas[2]
    menor= peliculas[2]
    for años in peliculas[2]:
        if años > mayor:
            mayor= años
        if años < menor:
            menor = años
    return mayor, menor, total_peliculas

while True:
    print("---MENÚ---")
    print("1.Agregar Peliculas.\n2. MOstras las peliculas registradas\n3.Buscar pelicula por genero")
    print("4.Eliminar pelicula por titulo.\n5.Ver estadisiticas de catolagos.\n6.Salir del programa")

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
        case "4":
            print("---ELIMINAR PELICULAS---")
            opcion_cuatro()
        case "5":
            print("---ESTADÍSTICAS DEL CATÁLOGO---")
            resultado = opcion_cinco()
            print(f"Hay {resultado[2]} peliculas resgistradas.")
            print("h")
            print(f"La pelicula mas antigua es:{resultado[1]}")
        case "6":
            print("Saliendo del programa. Gracias por usarlo!")
            break
        case _:
            print("Opcion no valida...")
