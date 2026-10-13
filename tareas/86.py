class pares_impares:
    def ejecutar(self):
        pares = 0
        impares = 0
        for i in range(10):
            n = int(input("numero: "))
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1
        print("pares:", pares)
        print("impares:", impares)
 
 
pares_impares().ejecutar()