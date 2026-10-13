class calculadora:
    def ejecutar(self):
        op = ""
        while op != "5":
            print("1 sumar, 2 restar, 3 multiplicar, 4 dividir, 5 salir")
            op = input("opcion: ")
            if op == "1" or op == "2" or op == "3" or op == "4":
                a = float(input("primer numero: "))
                b = float(input("segundo numero: "))
                if op == "1":
                    print(a + b)
                elif op == "2":
                    print(a - b)
                elif op == "3":
                    print(a * b)
                elif b != 0:
                    print(a / b)
                else:
                    print("no se puede dividir entre 0")
 
 
calculadora().ejecutar()