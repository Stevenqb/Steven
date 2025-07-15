
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def stockM(marca):
    marca=marca.lower()
    total=sum(stock[modelo][1]for modelo in productos if productos[modelo][0].lower()==marca and modelo in stock)
    print(f"el stock es:{total}")

def precio(p_min,p_max):
    resultado=[]
    for modelo,(precio,cantidad)in stock.items():
        if p_min<=precio<=p_max and cantidad>0:
            marca=productos.get(modelo)
            resultado.append(f"{marca}--{modelo}")
    if resultado:
        print("el precio del notebooks que consulta son ",sorted(resultado))
    else:
        print("no hay notebooks de ese precio")

def actualizar_precio(modelo,nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    return False

def menu_principal():
    while True:
        print("Menu principal ")
        print("1,stock ")
        print("2,precios ")
        print("3,actualizar precios ")
        print("4,salir ")
        opcion=input("ingrese una opcion ")
        if opcion=="1":
            marca=input("ingrese marca a consultar ")
            stockM(marca)
        elif opcion=="2":
            while True:
                try:
                    p_min=int(input("ingrese el precio minimo "))
                    p_max=int(input("ingrese el precio maximo "))
                    if p_min>p_max:
                        print("el minmo no puede ser mayor que el maximo ")
                        continue
                    break
                except ValueError:
                    print("debe ingresar valores enteros ")
            precio(p_min,p_max)
        elif opcion=="3":
            while True:
                modelo=input("ingrese el modelo a actualizar ")
                try:
                    nuevo_precio=int(input("ingrese el nuevo precio "))
                    if nuevo_precio<=0:
                        print("el precio debe ser mayor a 0 ")
                        continue
                except ValueError:
                    print("debe ingresar un precio valido ")
                    continue
                actulizado=actualizar_precio(modelo,nuevo_precio)
                if actulizado:
                    print("precio actualizado ")
                else:
                    print("el modelo no existe ")
                seguir=input("desea actualizar otro precio si,no ").lower()
                if seguir !="si":
                    break
        elif opcion =="4":
            print("saliendo.....")
            break
        else:
            print("debe seleccionar una opcion valida ")

menu_principal()



            






