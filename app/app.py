num1 = input('Enter a number: ')
operator = input('Enter an operator: ')
num2 = input('Enter another number: ')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)

result = float(num1) + operator + float(num2)

print(result)