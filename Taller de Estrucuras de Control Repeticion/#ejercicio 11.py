#ejercicio 11
saldo=2000
while True:
    print("1-) Depositar dinero")
    print("2-) Retirar Dinero")
    print("3-) Consultar saldo")
    print("4-) Salir") 
    dato=int(input())
    if(dato==1):
        depositiar=int(input("Cuanto va a depositiar: "))
        saldo=saldo+depositiar
        print(f"ha depositado: {depositiar}, su nuevo saldo es: {saldo}")
        
    elif(dato==2):
        retirar=int(input("cuanto dinero quiere retirar: "))
        if(saldo>=retirar):
            saldo=saldo-retirar
            print(f"saldo restante: {saldo}")
        elif(saldo<retirar):
            print("monto solicitado excede el saldo en la cuenta")

    elif(dato==3):
        print(f"Su saldo es: {saldo}")   

    elif(dato == 4):
        break 