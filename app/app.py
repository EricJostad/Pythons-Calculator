num1 = float(input('Enter a number: '))
operator = input('Enter an operator: ')
num2 = float (input('Enter another number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*' or 'x':
    print(num1 * num2)
# elif operator == '**':
#     print(num1 ** num2)
else:
    print('Invalid operator')

# result = float(num1) + operator + float(num2)

# print(result)