import random

def get_answer(answer_number):
    if answer_number == 1:
        return '確かにそうです'
    elif answer_number == 2:
        return '間違いなくそうだ'
    elif answer_number == 3:
        return 'はい'
    elif answer_number == 4:
        return 'なんとも。もう一度やってみて'
    elif answer_number == 5:
        return 'あとでもう一度やってみて'
    elif answer_number == 6:
        return '集中してもう一度やってみて'
    elif answer_number == 7:
        return '私の答えはNOです'
    elif answer_number == 8:
        return '見逃しはそれほどよくない'
    elif answer_number == 9:
        return '疑わしい'

#r = random.randint(1,9)
#fortune = get_answer(r)
#print(fortune)

print(get_answer(random.randint(1,9)))
