def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

try:
    temp_celsius = float(input("Leitura atual do sensor em Celsius: "))
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
    print(f"Entrada do Sensor: {temp_celsius:.2f} °C")
    print(f"Saída do Sensor: {temp_fahrenheit:.2f} °F")

    if temp_fahrenheit > 100:
        print("\nAlerta: Temperatura acima do limite seguro!")

except ValueError:
    print("Entrada inválida. Por favor, insira um número válido para a temperatura em Celsius.")
