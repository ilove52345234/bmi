#BMI計算程式
cm = input('請輸入你的身高: ')
kg = input('請輸入你的體重: ')
height = float(cm)
height = height / 100
weight = float(kg)
bmi = weight / (height * height)
print('你的BMI為', bmi )
if bmi < 18.5:
	print('體重過輕喔')
elif bmi >= 18.5 and bmi < 24:
	print('體重很標準喔')
elif bmi >= 24 and bmi < 27:
	print('體重有點過重喔')
elif bmi >= 27 and bmi < 30:
	print('已經算輕度肥胖囉')
elif bmi >= 30 and bmi < 35:
	print('已經是中度肥胖囉')
else:
	print('太胖了 該減肥了')
	