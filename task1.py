def get_gcd(a, b):
  gcd = 1
  for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
      gcd = i
  return gcd
 
 
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
print('НОД от {0} и до {1} равен {2}.'.format(first, second, \
      get_gcd(first, second)))