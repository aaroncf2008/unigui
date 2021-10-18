import os
commhist = ['nmap -sV -sC', 'echo nub']

while True:
    x = 0
    if True:
        blobb = ''
        for i in commhist:
            x = x + 1
            blobb = blobb + f'{x}. {i}\n'
        print(blobb)
    blob = input('Command: ')
    commhist.insert(0,blob)
    if len(commhist) > 5:
        commhist.pop()
    else:
        pass 