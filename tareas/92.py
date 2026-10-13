class figuras:
    def ejecutar(self):
        op = ""
        while op != "5":
            print("1 cuadrado, 2 rectangulo, 3 triangulo, 4 circulo, 5 salir")
            op = input("opcion: ")
            if op == "1":
                lado = float(input("lado: "))
                print("area:", lado * lado)
            elif op == "2":
                base = float(input("base: "))
                altura = float(input("altura: "))
                print("area:", base * altura)
            elif op == "3":
                base = float(input("base: "))
                altura = float(input("altura: "))
                print("area:", base * altura / 2)
            elif op == "4":
                radio = float(input("radio: "))
                print("area:", 3.1416 * radio * radio)
 
 
figuras().ejecutar()