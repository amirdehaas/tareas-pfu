class tabla:
    def ejecutar(self):
        r = "s"
        while r == "s":
            n = int(input("numero: "))
            for i in range(1, 11):
                print(n, "x", i, "=", n * i)
            r = input("repetir? (s/n): ")
 
 
tabla().ejecutar()