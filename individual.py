import sys

if __name__ == '__main__':
    n = int(input("Введите число: "))
if n == 1:
    print("Monday")
if n == 2:
    print("Tuesday")
if n == 3:
    print("Wednesday")
if n == 4:
    print("Thursday")
if n == 5:
    print("Friday")
if n == 6:
    print("Saturday")
if n == 7:
    print("Sunday")
else:
    print("Ошибка!", file=sys.stderr)
exit()