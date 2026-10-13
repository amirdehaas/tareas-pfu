class tienda:
    def ejecutar(self):
        total = 0
        op = ""
        while op != "2":
            print("1 agregar producto, 2 finalizar")
            op = input("opcion: ")
            if op == "1":
                nombre = input("producto: ")
                precio = float(input("precio: "))
                total += precio
        print("total:", total)
 
 
tienda().ejecutar()