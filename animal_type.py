ime=input()

if ime == 'dog':
    print('mammal')
elif ime == 'crocodile' or ime  == 'tortoise' or ime == 'snake':
    print('reptile')
elif ime != 'mammal' or ime != 'reptile':
    print('unknown')