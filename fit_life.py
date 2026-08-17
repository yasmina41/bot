name = input("Привет, как вас зовут? ")
age = int(input("Сколько вам лет? "))
weight = float(input("Сколько вы весите (в кг)? "))
height = float(input("Какой у вас рост (в см)? "))
#Переведем рост в метры
height_m = height / 100
#Считаем ИМТ
bmi = weight / (height_m ** 2)
#Норма воды в мл
water_ml = weight * 30
#Норма воды в л
water_l = water_ml / 1000
#Выводим результат
print(f"Приятно познакомиться, {name}!")
print(f"Ваш индекс массы тела (ИМТ): {round(bmi, 1)}")
print(f"Рекомендуемая норма воды в день: {round(water_l, 2)} л.")

