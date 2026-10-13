class suma_promedio:
    def ejecutar(self):
        cantidad = int(input("cuantos numeros: "))
        suma = 0
        for i in range(cantidad):
            suma += float(input("numero: "))
        print("suma:", suma)
        if cantidad > 0:
            print("promedio:", suma / cantidad)
 
 
suma_promedio().ejecutar()