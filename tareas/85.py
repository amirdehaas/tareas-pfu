class respuesta:
    def ejecutar(self):
        r = input("s o n: ")
        while r != "s" and r != "n":
            print("opcion no valida")
            r = input("s o n: ")
        print("elegiste:", r)


respuesta().ejecutar()