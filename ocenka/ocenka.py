pos = 0
neg = 0
n = 1
while n != 0:
  n = int(input('Введите оценку: '))
  if n > 0:
    pos += 1
  if n < 0:
    neg += 1
  if n == 0:
    break
print('Кол-во положительных оценок: ', pos)
print('Кол-во отрицательных чисел:', neg)