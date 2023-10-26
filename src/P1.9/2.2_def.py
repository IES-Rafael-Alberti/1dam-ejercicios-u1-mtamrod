def servicio():
    horas=float(input("Introduce las horas de trabajo: "))
    coste=float(input("Introduce el coste del trabajo por hora: "))
    servicio=horas*coste
    round (servicio, 2)
    return servicio

print(f"Importe total: {servicio()}€")