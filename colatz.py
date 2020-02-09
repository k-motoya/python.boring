def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1


num = 0
print('数値を入力してください')
while num != 1:
    try:
        num = collatz(int(input()))
    except ValueError:
        print('整数を入力してください')
    print(num)
