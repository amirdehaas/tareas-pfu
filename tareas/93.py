class notas:
    def ejecutar(self):
        print("escribe -1 para finalizar")
        suma = 0
        cantidad = 0
        mayor = 0
        menor = 0
        nota = float(input("nota: "))
        while nota != -1:
            if cantidad == 0:
                mayor = nota
                menor = nota
            if nota > mayor:
                mayor = nota
            if nota < menor:
                menor = nota
            suma += nota
            cantidad += 1
            nota = float(input("nota: "))
        if cantidad > 0:
            print("promedio:", suma / cantidad)
            print("mayor:", mayor)
            print("menor:", menor)
 
 
notas().ejecutar()