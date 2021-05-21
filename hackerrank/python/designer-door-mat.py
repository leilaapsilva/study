# https://www.hackerrank.com/challenges/designer-door-mat

# Wrong 

n, m = input().split()
n, m = int(n), int(m)

traco, ponto_barra_ponto = '-', '.|.'

for i in range (int((n-1)/2)):
    tracos = traco*int((m-3)/2)
    m = m - 6
    print(tracos + ponto_barra_ponto*(i*2+1) + tracos)
        
print(traco * n + 'WELCOME' + traco * n)

for j in reversed(range (int((n-1)/2))):
    m = m + 6
    tracos = traco*int((m-3)/2)
    print(tracos+ ponto_barra_ponto*(j*2+1)+ tracos)