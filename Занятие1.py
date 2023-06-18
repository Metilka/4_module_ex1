'''
def stro(string): # сложность О(n*m) n -длина строки, m- количество уникальных символов
    for symbol in set(string):
        cnt = 0
        for sub_sumbol in string:
            if symbol == sub_sumbol:
                cnt+=1
        print(symbol,cnt)
stro('abcdaaaa')
'''

'''
def stro(string): # сложность О(n**2)
    for symbol in string:
        cnt = 0
        for sub_sumbol in string:
            if symbol == sub_sumbol:
                cnt+=1
            print(symbol,cnt)
stro('abcdaaaa')
'''
def stro(string): # сложность 0(n)
    k = {}
    for symbol in string:
        k[symbol] = k.get(symbol, 0)+ 1

    print(k)
stro('abcdaaaa') 