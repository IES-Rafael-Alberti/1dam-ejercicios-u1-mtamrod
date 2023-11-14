def grados():
    gradosCelsius = float(input("Introduce una temperatura en ºC: "))
    gradosFarenheit = (gradosCelsius * 9/5) + 32
    return gradosFarenheit


tempFarenheit = grados()
print(f"Son {tempFarenheit} ºF")