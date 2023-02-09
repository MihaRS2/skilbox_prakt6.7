numbers = int(input("Введите число: "))
chislo_zagadanoe = 9
popitki = 0
while numbers != chislo_zagadanoe:
    if numbers > chislo_zagadanoe:
        print("Число больще , чем нужно!")
        popitki += 1
        numbers = int(input("Введите число: "))
    if numbers < chislo_zagadanoe:
        print("Число меньше загаданного")
        popitki += 1   
        numbers = int(input("Введите число: "))
   
print("Вы угадали!число попыток" , popitki)            

