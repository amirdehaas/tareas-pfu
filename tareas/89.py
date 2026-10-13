class contador:
    def ejecutar(self):
        cantidad = int(input("cuantos numeros: "))
        positivos = 0
        negativos = 0
        ceros = 0
        for i in range(cantidad):
            n = float(input("numero: "))
            if n > 0:
                positivos += 1
            elif n < 0:
                negativos += 1
            else:
                ceros += 1
        print("positivos:", positivos)
        print("negativos:", negativos)
        print("ceros:", ceros)
 
 
contador().ejecutar()