Celsius = float(input("Qual a temperatura em Celsius (°C): "))
medida = str(input("Para qual medida deseja converter? (Fahrenheit ou Kelvin): "))

Fahrenheit = 1.8 * Celsius + 32
Kelvin = Celsius + 273

if medida == "Fahrenheit":
    print (f"Sua temperatura em Fahrenheit é: {Fahrenheit:.1f}°F")
elif medida == "Kelvin":
    print (f"Sua temperatura em Kelvin é: {Kelvin:.1f}°K")