n=int(input('quantas maçãs vai querer? '))
if n >= 12:
    total=  n*1
    print('foram compradas {} maçãs,o total deu ${}'.format(n,total))
if n < 12:
    total= n*1.30
    print('foram compradas {} maçãs,o total deu ${}'.format(n,total))