
personas={
    1:{"nombre": "liam neeson",
       "telefono": 876765454,
       "estado civil": "soletero",
       "ciudadano": True},
    2:{"nombre":"christian bale",
       "telenofo":999763423,
       "estado civil": "casado",
       "ciudadano": False},
    3:{"nombre":"john doe",
       "telenofo":352689124,
       "estado civil": "soltero",
       "ciudadano": True},
    4:{"nombre":"jane doe",
       "telenofo":678923459,
       "estado civil": "casada",
       "ciudadano": True},   
}

while True:
    try:
        print('''
              1.-ingresar persona
              2.-mostrar listado)
              3.-actualizar persona)
              4.-borrar persona)
              5.-salir
              ''')
        op=int(input("seleccione una opcion "))
        match op:
            case 1:
                nom=input("ingrese su nombre ")
                tel=int(input("ingrese su numero de telefono"))
                est=int(input("1.- casado, 2.- soltero "))
                if est==1:
                    estcivil="casado"
                else:
                    estcivil="soltero"
                est=int(input("es ciudadano 1.- si, 2.- no "))
                if est==1:
                    ciuda=True
                else:
                    ciuda=False
                ld=len(personas)+1
                personas[ld]={{"nombre":nom,
                                "telenofo":tel,
                                "estado civil":estcivil,
                                "ciudadano":ciuda},}
                
            case 2:
                for n, persona in personas.items():
                 print(n,persona)
            case 3: 
                for n, persona in personas.items():
                 print(n,persona)
                perso=int(input("que persona desea actualizar? "))
                while True:
                        print('''
                        1.-ingresar persona
                        2.-mostrar listado)
                        3.-actualizar persona)
                        4.-borrar persona)
                        5.-salir
                        ''')
                dato=int(input("que dato desea actualizar? "))
                match dato:
                    case 1:
                        n=input("ingrese el nombre nuevo ")
                    case 2:
                        num=int(input("ingrese el nuevo numero "))
                    case 3:
                        est=int(input("1.- casado, 2.- soltero "))
                        if est==1
                           estcivil="casado"
                        else:
                            estcivil
                        
                    case 4:
                        est=int(input())
                    case 5:
                        break
                    case .-:
                        print("opcion invalida")
                datonuevo=
                personas[perso][dato]
            case 4:
                for n, persona in personas.items():
                 print(n,persona)
                borrar=int(input("cual persona desea borrar? "))
                del personas[borrar]
                print(f"la persona  {borrar} fue eliminada ")

            case 5:
                break
            case _:
                print("opcion invalida")
    except Exception as e:
        print("el error es ", e)
        