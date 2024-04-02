def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_odd_numbers(start, end):
    if start < 0 or end <0:
        print("numero invalido, el numero debe ser postivo")
        return
    print("numeros impares entre", start, "y", end, "son:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)

def print_prime_numbers(num):
    print("numeros primos entre 0 y ", num, "son:")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i)

def main():
    while True:
        num = int(input("ingrese un numero "))
        if num > 0:
            break
        print("ingrse un numero entero positivo.")

    print_odd_numbers(-num, num)
    print_prime_numbers(100)

if __name__ == "__main__":
    main() 
    
