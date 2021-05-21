# hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lista = list(arr)
    
    lista.sort() # orderna a lista
    
    maximum = lista[-1] # pega o maior valor
    
    for item in reversed(lista):
        if item != maximum:
            print(item) 
            break 