def celsius_fahrenheit(temperaturas):
    fahrenheit = map(lambda c: 9 / 5 * c + 32, temperaturas)
    for f in fahrenheit:
        print(f"{f:.2f}")
 
celsius_fahrenheit([0, 37, 100])
 