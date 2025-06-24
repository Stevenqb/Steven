#crud de diccionarios


def mostrar_juegos(dic):
    for j, datos in dic.items():
         print(j,datos)

juegos={
    1:{"nombre":"metroid dread",
       "precio": 50000,
       "code": "MMdd2023"
    },
    2:{ 
        "nombre":"pikmin 4",
        "precio": 55000,
        "code": "pKMn2022"    
    }
}
mostrar_juegos(juegos)

def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    espacios=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4  :
        print("el codigo  está bien escrito")
        return True
    else:
        print("el codigo está mal escrita")
        return False
    
def valida_precio(precio):
    if precio<8000 or precio>100000:
        return False
    else:
        return True
def valida_nombre(frase):
    if " " in frase:
        return True
    else:
        return False


def agregar_juego(dic):
    ultima=list(juegos.keys())[-1]
    
    nombre=input("ingrese el nombre del juego ")
    precio=int(input("ingrese el precio del juego "))
    while True:
        code=input("ingrese el codigo del juego ")
        if valida_code(code):
            dic[ultima+1]={
                 "nombre":nombre,
                 "precio": precio,
                 "code":code 
                }
            print("Juego ingresado con exito ")
            break
        else:
            print("codigo invalido. debe tener 2 mayuscular, 2 minusculas y 2 digitos ")

def act_juego(dic):
    mostrar_juegos(dic)
    act=int(input("Seleccione el juego a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dic[act]["nombre"]=n
            case 2:
                n=input("ingrese la nueva raza")
                dic[act]["precio"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dic[act]["codigo"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def borrar_juego(dict):
    mostrar_juegos(dict)
    borrar=int(input("seleccione el juego a borrar "))
    if borrar in dict:
        del dict[borrar]
    else:
        print("el juego no existe ")

'''el codigo debe tener 2 mayusculas,"
2 minuculas y 4 numeros '''



while True:
    try:
        print('''
              1.-agregar juego
              2.-mostrar juegos
              3.-actualiazar juego 
              4.-borrar juego
              5.-salir
              ''')
        op=int(input("seleccione una opcion "))
        match op:
            case 1:
                agregar_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                act_juego(juegos)
            case 4:
              borrar_juego(juegos)
            case 5:
                break
            case _:
                print("opcion invalida")
    except Exception:
        print("solo numeros enteros")


mostrar_juegos(juegos)
