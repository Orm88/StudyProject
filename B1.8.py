# Блок 1.8 Переменные. Стандартный ввод/вывод
#
# Коля каждый день ложится спать ровно в полночь и недавно узнал,
# что оптимальное время для его сна составляет XX минут.
# Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут после полуночи,
# однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить,
# на какое время завести будильник.
'''
X = int(input('Введите кол-во минут для сна '))
print("Время сна в часах", X//60)
print("Время сна в минутах", X % 60)
'''
# Катя узнала, что ей для сна надо XX минут.
# В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
# Помогите Кате определить, на какое время ей поставить будильник,
# чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
#
# На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
X = int(input('Введите кол-во минут для сна '))
H = int(input('Введите текущее время (час) '))
M = int(input('Введите текущее время (минуты) '))
print("Время сна в часах", ((H*60)+(X+M))//60)
print("Время сна в минутах", (X+M) % 60)
