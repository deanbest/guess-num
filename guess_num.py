import random
start = input('由您決定隨機數字範圍開始值: ')
end = input('由您決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(1, 100)
count = 0
while True:
	count += 1  #count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('蒸蚌, 猜對惹~')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
