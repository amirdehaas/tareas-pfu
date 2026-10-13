# ejercicios 85 al 100 - programacion orientada a objetos (version simple)


class ejercicio85:
    def ejecutar(self):
        while 1:
            r = input("deseas continuar? (s/n): ").lower()
            if r == "s" or r == "n":
                break
            print("opcion no valida")
        print("elegiste:", r)


class ejercicio86:
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


class ejercicio87:
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


class ejercicio88:
    def ejecutar(self):
        cantidad = int(input("cuantos numeros: "))
        suma = 0
        for i in range(cantidad):
            suma += float(input("numero: "))
        print("suma:", suma)
        if cantidad > 0:
            print("promedio:", suma / cantidad)


class ejercicio89:
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


class ejercicio90:
    def ejecutar(self):
        while 1:
            n = int(input("numero para la tabla: "))
            for i in range(1, 11):
                print(n, "x", i, "=", n * i)
            r = input("repetir con otro numero? (s/n): ").lower()
            if r != "s":
                break


class ejercicio91:
    def ejecutar(self):
        while 1:
            print("1. sumar  2. restar  3. multiplicar  4. dividir  5. salir")
            op = input("opcion: ")
            if op == "5":
                break
            a = float(input("primer numero: "))
            b = float(input("segundo numero: "))
            if op == "1":
                print("resultado:", a + b)
            elif op == "2":
                print("resultado:", a - b)
            elif op == "3":
                print("resultado:", a * b)
            elif op == "4":
                if b == 0:
                    print("no se puede dividir entre 0")
                else:
                    print("resultado:", a / b)
            else:
                print("opcion no valida")


class ejercicio92:
    def ejecutar(self):
        while 1:
            print("1. cuadrado  2. rectangulo  3. triangulo  4. circulo  5. salir")
            op = input("opcion: ")
            if op == "5":
                break
            if op == "1":
                lado = float(input("lado: "))
                print("area:", lado * lado)
            elif op == "2":
                base = float(input("base: "))
                altura = float(input("altura: "))
                print("area:", base * altura)
            elif op == "3":
                base = float(input("base: "))
                altura = float(input("altura: "))
                print("area:", base * altura / 2)
            elif op == "4":
                radio = float(input("radio: "))
                print("area:", 3.1416 * radio * radio)
            else:
                print("opcion no valida")


class ejercicio93:
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
        else:
            print("no ingresaste notas")


class ejercicio94:
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
        print("mayores de edad:", mayores)
        print("menores de edad:", menores)


class ejercicio95:
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


class ejercicio96:
    def ejecutar(self):
        total = 0
        while 1:
            print("1. agregar producto  2. finalizar")
            op = input("opcion: ")
            if op == "2":
                break
            if op == "1":
                nombre = input("producto: ")
                precio = float(input("precio: "))
                total += precio
                print("agregado:", nombre)
            else:
                print("opcion no valida")
        print("total a pagar:", total)


class ejercicio97:
    def __init__(self):
        self.saldo = 0

    def ejecutar(self):
        while 1:
            print("1. consultar saldo  2. depositar  3. retirar  4. salir")
            op = input("opcion: ")
            if op == "4":
                break
            if op == "1":
                print("saldo:", self.saldo)
            elif op == "2":
                monto = float(input("monto a depositar: "))
                if monto > 0:
                    self.saldo += monto
                    print("deposito realizado")
                else:
                    print("monto no valido")
            elif op == "3":
                monto = float(input("monto a retirar: "))
                if monto > self.saldo:
                    print("fondos insuficientes")
                elif monto <= 0:
                    print("monto no valido")
                else:
                    self.saldo -= monto
                    print("retiro realizado")
            else:
                print("opcion no valida")


class ejercicio98:
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


class ejercicio99:
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


class ejercicio100:
    def ejecutar(self):
        while 1:
            print("1. factorial  2. tabla de multiplicar  3. paridad  4. cuadrado  5. salir")
            op = input("opcion: ")
            if op == "5":
                break
            if op == "1":
                n = int(input("numero: "))
                f = 1
                for i in range(1, n + 1):
                    f = f * i
                print("factorial:", f)
            elif op == "2":
                n = int(input("numero: "))
                for i in range(1, 11):
                    print(n, "x", i, "=", n * i)
            elif op == "3":
                n = int(input("numero: "))
                if n % 2 == 0:
                    print("es par")
                else:
                    print("es impar")
            elif op == "4":
                n = float(input("numero: "))
                print("cuadrado:", n * n)
            else:
                print("opcion no valida")


