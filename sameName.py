def spam():
    eggs = 'spam local'
    print(eggs) #'spam local を表示'

def bacon():
    eggas = 'bacon local'
    print(eggs) # 'bacon localを表示'
    spam()
    print(eggs) # 'bacon localを表示'

eggs = 'global'
bacon()
print(eggs) #globalを表示
