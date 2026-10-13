class banco:
    def __init__(self):
        self.saldo = 0
 
    def ejecutar(self):
        op = ""
        while op != "4":
            print("1 saldo, 2 depositar, 3 retirar, 4 salir")
            op = input("opcion: ")
            if op == "1":
                print("saldo:", self.saldo)
            elif op == "2":
                monto = float(input("monto: "))
                self.saldo += monto
            elif op == "3":
                monto = float(input("monto: "))
                if monto <= self.saldo:
                    self.saldo -= monto
                else:
                    print("fondos insuficientes")
 
 
banco().ejecutar()