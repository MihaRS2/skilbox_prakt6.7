name = input("Как вас зовут?: ")
print(name ,("Ваша задолжность 1000 руб"))
bank = int(input("Сколько готовы внести?: "))
dolg = 1000
while bank < dolg:
    print("Мало нужно больше денег!")
    print(name ,("Ваша задолжность 1000 руб"))    
    bank = int(input("Сколько готовы внести?: "))
print("Отдично!" ,name ("ваша задолжность закрыта!"))    