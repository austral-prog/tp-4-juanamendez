def line():
    print("TO DO")
    A= float(input("Ingrese el coeficiente A: "))
    B= float(input("Ingrese el coeficiente B: "))
    X1= float(input("Ingrese el coeficiente X1: "))
    X2= float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2} \n")

    print(f"Para la siguiente ecuación: \n \t Y = {A}X + {B}\n")

    print(f"Dados los siguientes puntos: \n \t P1 {float(X1)}, {float(Y1)} \n \t P1 {float(X2)}, {float(Y2)}\n")

    Y1=A*X1+B
    Y2=A*X2+B

    distancia=float((((Y2-Y1)**2 )+((X2-X1)**2))**(0.5))

    print(f"La distancia entre ellos es: {distancia}")
