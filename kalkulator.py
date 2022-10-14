# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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

