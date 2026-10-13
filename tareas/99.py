class clasificar:
    def ejecutar(self):
        cantidad = int(input("cuantas edades: "))
        ninos = 0
        adolescentes = 0
        adultos = 0
        mayores = 0
        for i in range(cantidad):
            edad = int(input("edad: "))
            if edad <= 11:
                ninos += 1
            elif edad <= 17:
                adolescentes += 1
            elif edad <= 59:
                adultos += 1
            else:
                mayores += 1
        print("ninos:", ninos)
        print("adolescentes:", adolescentes)
        print("adultos:", adultos)
        print("adultos mayores:", mayores)
 
 
clasificar().ejecutar(