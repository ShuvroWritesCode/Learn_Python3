num1 = float(input('Enter first number: '))
operator = input('Enter Operator: ')
num2 = float(input('Enter second number: '))

print("\n")

if operator == '+':
    print(f'Result: {num1 + num2}')
elif operator == '-':
    print(f'Result: {num1 - num2}')
elif operator == '*':
    print(f'Result: {num1 * num2}')
elif operator == '/':
    print(f'Result: {num1 / num2}')
elif operator == '**':
    print(f'Result: {num1 ** num2}')
elif operator == '%':
    print(f'Result: {num1 % num2}')
else:
    print("Invalid Operation!")
