print('Начался 8-часовой рабочий день')
calls_wife = False
hours = 0
number = 0
while hours < 8:
    hours += 1
    print(hours, '-й час')
    number += int(input('Сколько задач решит Максим? '))
    calls = int(input('Звонит жена. Взять трубку? (1-да, 0-нет) '))
    if calls == 1:
        calls_wife = True
print('Рабочий день закончился. Всего выполнено задач:', number)
if calls_wife == True:
    print('Нужно зайти в магазин.')