class mayor_menor:
    def ejecutar(self):
        mayor = 0
        menor = 0
        for i in range(10):
            n = int(input("numero: "))
            if i == 0:
                mayor = n
                menor = n
            if n > mayor:
                mayor = n
            if n < menor:
                menor = n
        print("mayor:", mayor)
        print("menor:", menor)
 
 
mayor_menor().ejecutar()