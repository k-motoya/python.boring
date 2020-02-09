#cat_names = []
#while True:
#    print('猫' + str(len(cat_names) + 1) + 'の名前を入力してください' +
#          '(終了するにはEnterキーのみ押してください)')
#    name = input()
#    if name == '':
#        break
#    cat_names += [name]
#print('猫の名前は次の通り')
#for name in cat_names:
#    print(' ' + name)


supplies = ['pens', 'staplers', 'frame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
