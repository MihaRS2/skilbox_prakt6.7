#Напишите робота для коллекторов. В самом начале он спрашивает имя должника и сумму долга, 
#а затем начинает требовать у него погашения до тех пор, пока должник не введёт нужную сумму (равную сумме долга или больше).
#После погашения долга робот сообщает об этом пользователю и благодарит его.

name = input("Как вас зовут?: ")
print(name ,("Ваша задолжность 1000 руб"))
bank = int(input("Сколько готовы внести?: "))
dolg = 1000
while bank < dolg:
    print("Мало нужно больше денег!")
    print(name ,("Ваша задолжность 1000 руб"))    
    bank = int(input("Сколько готовы внести?: "))
print("Отлично!" ,str(name) ,("ваша задолжность закрыта!"))    