
# notas=[]

# while True:
#     print('''
#           1.-ingresar notas
#           2.-borrar notas
#           3.-mostrar notas
#           4.-promedio
#           5.-limpiar
#           6.-salir
#           ''')
#     op=int(input("seleccione una opcion "))
#     match op:
#         case 1:
#             nota=float(input("ingrese una nota "))
#             notas.append(notas)
#         case 2:
#           for num, n in enumerate(notas):
#             print(num+1,".- ",n)
#             elim=int(input("ingrese cual quiere eliminar "))
#             notas.pop(elim-1)
#         case 3:
#           len(notas)
#         case 4:
#             if len(notas)==0:
#              print("no hay notas para calcular el promedio ")
#             else:
#              promedio=sum(notas)/len(notas)
#              print(f"promedio {round(promedio, 1)}")
#              print(f"nota mayor {max(notas)}")
#              print(f"nota menor {min(notas)}")
#         case 5:
#           notas.clear()
#         case 6:
#           print("saliendo... ")
#           break
#         case _:
#           print("opcion invalida")


dic={
    "nombre":"alan grant",
    "numero": 123445670,
    "casado": True
}


print(dic["nombre"])
dic["nombre"]="alan brito"
dic["numero"]=12345667
print(dic)

frutas={
    "naranja":400,
    "manzana":500,
    "pera":700
}
print(frutas)
frutas["granada"]=1500
print(frutas)

for key, value in frutas.items():
    print(key,"$", value)





          
            

            
            
             


