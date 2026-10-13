class menu:
    def ejecutar(self):
        op = ""
        while op != "5":
            print("1 factorial, 2 tabla, 3 paridad, 4 cuadrado, 5 salir")
            op = input("opcion: ")
            if op == "1":
                n = int(input("numero: "))
                f = 1
                for i in range(1, n + 1):
                    f = f * i
                print("factorial:", f)
            elif op == "2":
                n = int(input("numero: "))
                for i in range(1, 11):
                    print(n, "x", i, "=", n * i)
            elif op == "3":
                n = int(input("numero: "))
                if n % 2 == 0:
                    print("es par")
                else:
                    print("es impar")
            elif op == "4":
                n = float(input("numero: "))
                print("cuadrado:", n * n)
 
 
menu().ejecutar()
 