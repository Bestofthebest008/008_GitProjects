righty = set('yuoiphjlknm')
lefty = set('qwerasdftzxcvb')
word = set(input('Please enter your word : '))
print(not(word.isdisjoint(righty) and not(word.isdisjoint(lefty))))