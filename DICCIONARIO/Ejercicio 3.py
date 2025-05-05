usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
                "apellido": "Perurena",
                "password": "123123"
            },
        "fmuguruza": {
            "nombre": "Fermín",
                "apellido": "Muguruza",
                "password": "654321"
            },
        "aolaizola": {
             "nombre": "Aimar",
                 "apellido": "Olaizola",
                 "password": "123456"
            }
    }

intentos=3
for i in range(intentos+1):
    usser=input("ingrese su usuario: ")
    contraseña=input("ingrese su contraseña: ")
    if usser in usuarios and usuarios[usser]["password"] == contraseña:
        print(f"acceso concedido, {usuarios[usser]["nombre"]} {usuarios[usser]["apellido"]}")
        break
    else:
        print("usuario o contraseña incorrectos")
        if (i == intentos-1):
            print("intentos agostados")