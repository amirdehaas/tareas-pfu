class estadisticas:
    def ejecutar(self):
        aprobadas = 0
        reprobadas = 0
        suma = 0
        for i in range(10):
            nota = float(input("nota: "))
            suma += nota
            if nota >= 60:
                aprobadas += 1
            else:
                reprobadas += 1
        print("aprobadas:", aprobadas)
        print("reprobadas:", reprobadas)
        print("promedio:", suma / 10)
 
 
estadisticas().ejecutar()