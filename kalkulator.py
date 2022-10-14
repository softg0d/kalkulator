print("1 Dodawanie")
print('2 Odejmowanie')
print('3 Mnozenie')
print('4 Dzielenie')

wybor = input('Wybierz, jakie obliczenie chcesz wykonac: ')

num1 = float(input('Wybierz 1 numer: '))
num2 = float(input('Wybierz 2 numer: '))

if wybor == "1":
    print(num1, '+', num2, '=', (num1+num2))

elif wybor == '2':
    print(num1, '-', num2, '=', (num1-num2))

elif wybor == '3':
    print(num1, '*', num2, '=', (num1*num2))

elif wybor == '4':
    if num2 == 0.0:
        print('Nieprawidlowosc')
    else:
        print(num1, ':', num2, '=', (num1/num2))

