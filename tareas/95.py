class numeros:
    def ejecutar(self):
        print("escribe 0 para terminar")
        pares = 0
        impares = 0
        positivos = 0
        negativos = 0
        n = int(input("numero: "))
        while n != 0:
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1
            if n > 0:
                positivos += 1
            else:
                negativos += 1
            n = int(input("numero: "))
        print("pares:", pares)
        print("impares:", impares)
        print("positivos:", positivos)
        print("negativos:", negativos)
 
 
numeros().ejecutar()