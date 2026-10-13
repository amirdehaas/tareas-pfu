class edades:
    def ejecutar(self):
        print("escribe 0 para terminar")
        mayores = 0
        menores = 0
        edad = int(input("edad: "))
        while edad != 0:
            if edad >= 18:
                mayores += 1
            else:
                menores += 1
            edad = int(input("edad: "))
        print("mayores:", mayores)
        print("menores:", menores)
 
 
edades().ejecutar()