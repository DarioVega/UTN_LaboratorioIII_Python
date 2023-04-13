resultado = None
a = 10
b = 0

try:

    resultado = a / b

except TypeError as e:
    print(f"TypeError - Ocurrió un error: {type(e)}")

# except Exception as e:
except ZeroDivisionError as e:

    print(f"ZeroDivisionError - Ocurrió un error: {type(e)}")

except Exception as e:

    print(f"Exception - Ocurrió un error: {type(e)}")

print(f"El resultado es: {resultado}")
print("seguimos...")