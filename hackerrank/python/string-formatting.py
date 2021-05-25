# https://www.hackerrank.com/challenges/python-string-formatting

# WRONG (todo: fix print alignment)

def print_formatted(number):
    
    w = len(str(number))
    
    for i in range(1, number+1):
        print("{: <{width}}  {: <{width}}  {: <{width}}  {: >{width}}".format(i, rp(oct(i)), rp(hex(i)), rp(bin(i)), width=w))
    
def rp(number): # remove prefix, like 0x, 0o, 0b 
    return int(str(number)[2:]) 
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)