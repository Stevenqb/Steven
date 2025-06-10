
# numeros=[4,3,8,66,41]

# print(numeros[3])

# numeros.append(20)
# print(numeros)

# for numero in numeros:
#     print("numero",numero*3)

# frutas=["manzana","frambueza","durazno"]

# for fruta in frutas:
#     print(frutas)



# nombres=["carlos","maria","seba"]
# apellidos=["martinez","aranda","gonzales"]
# while True:
#     print('''
#           1.-insetar nombre y apellido
#           2.-buscar nombres
#           3.-mostrar nombres y apellidos 
#           4.-salir
#           ''')
#     op=int(input("selecione una opcion "))
#     match op:
#         case 1:
#             nom=input("ingrese un nombre ")
#             nombres.append(nom)
#             ape=input("ingrese un apellido ")
#             apellidos.append(ape)
           
#             print(nombres)
#             print(apellidos)
#         case 2:
#             buscar=input("ingrese el nombre a buscar ")
#             if buscar in nombres:
#               input(f"el nombre {buscar} se encuentra en la lista ") 
#             else:

#              input(f"el nombre {buscar} no encuentra en la lista ")   
#         case 3:
#            cont=0
#            for i in nombres:
#               print(cont+1, ".-", nombres[cont],apellidos[cont])
#               cont+=1
#         case 4:
#             print("saliendo... ")
#             break
#         case _:
#             print("opcion invalida ")


productos=["chocolate","arroz","papas",]
precios=[1000,1600,900]
carrito=[]

while True:
    print('''
          1.-ingresar productos
          2.-comprar
          3.-crear boleta
          4.-salir
          ''')
    op=int(input("seleccione  una opcion "))
    match op:
        case 1:
            nom=input("ingrese un producto: ")
            productos.append(nom)
            ape=int("ingrese un precio: ")
            precios.append(ape)
        case 2:
            while True:
                for i in range(len(productos)):
                    print(1+1,  ".-", productos [i], "$",productos )
                pro=int(input("selecione que quiere comprar"))
                carrito.append(pro-1)
                print(carrito)
        case 3:
            total=0
            print("------------------0------------------")
            print("bienvenido a lider ")
            for i in range(len(carrito)):
                print( productos [i], "-------$",productos )
                total=total+precios[i]
            print("su total en productos es ",len(carrito))
            print("su total neto es ", total)
            print("su total mas IVA es ", total+1.19)

            
            

        case 4:
            print("gracias por comprar en lider... ")
            break
        case _:
            print("opcion invalida ")
            