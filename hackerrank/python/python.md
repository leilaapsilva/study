# HackerRank
### Resolução de problemas do site, por [leilaapsilva](https://www.hackerrank.com/leilaapsilva)

[Loops](https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true)

~~~python
if __name__ == '__main__':
    n = int(raw_input())
    
    lista = []
    for i in range(0, n):
        print(i**2)
~~~

[Write a function](https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true)

~~~python
def is_leap(year):
    leap = False
    
    # Write your logic here
    if not year%4:
        leap = True
    if not year%100:
        leap = False
    if not year%400:
        leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)
~~~

[Print Function](https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

~~~Python
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
 
for i in range(1,n+1):
    print(i, end='')
~~~

[What's your name?](https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true)

~~~Python
def print_full_name(a, b):
    print ("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
~~~

[Mutations](https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

~~~Python
def mutate_string(string, position, character):
    
    aux_list = list(string)
    aux_list[position] = character
    string = ''.join(aux_list)
    
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
~~~

[String Validators](https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true)

~~~Python
if __name__ == '__main__':
    s = raw_input()
    
    a, b, c, d, e = False, False, False, False, False
    
    
    for i in range(len(s)):
        if s[i].isalnum():
            a = True
    
        if s[i].isalpha():
            b = True
        
        if s[i].isdigit():
            c = True
            
        if s[i].islower():
            d = True
        
        if s[i].isupper():
            e = True    
            
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
~~~

[sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true)

~~~python
def swap_case(s):
    
    aux = ""
    for i in range(len(s)):
        if(s[i].isupper()):
            aux += s[i].lower()
        elif(s[i].islower()):
            aux += s[i].upper()
        else:
            aux += s[i]
    
    return aux

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
~~~

[String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

~~~Python
def split_and_join(line):
    a = "-".join(line.split(" ")) 
    return a
    
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
~~~

[Mod Divmod](https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true)

~~~Python
a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))
~~~

[Power - Mod Power](https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

~~~Python
a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))
~~~

[Integers Come In All Sizes](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

~~~Python
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)
~~~

[Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true)

### Não funcionou para todos os casos por enquanto :c

~~~Python
def solve(s):
    lista = s.split()
    
    aux = []
    for item in lista:
        aux.append(item[0].upper())
        for i in range(1, len(item)):
            
            aux.append(item[i])
        
        aux.append(" ")    
    
    s = ''.join(aux)
    return s
~~~

[Tuples](https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true)

~~~Python
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = ()
    
    for i in range(n):
        t += (integer_list[i],)
        
    print(hash(t))
~~~

[Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true)

~~~Python
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    scores = student_marks[query_name]
    average_score = (scores[0] + scores[1] + scores[2])/3
    
    print(format(average_score, '.2f'))
~~~

[Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true)

~~~Python
import textwrap

def wrap(string, max_width):
    
    wrapper = textwrap.TextWrapper(width=max_width)
    wstring = wrapper.wrap(text=string)
    
    aux = ""
    for i in wstring:
        aux += i+'\n'
            
    return aux

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
~~~

[Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true)

~~~Python
def solve(s):
    
    string_list = s.split(" ")
    aux = ""
    for i in range(len(string_list)):
        aux += string_list[i].capitalize() + " "

    return aux 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
~~~

[Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true)

~~~Python
import calendar 
from datetime import datetime

date_input = raw_input()
date = datetime.strptime(date_input, '%m %d %Y').date() 
day_of_week = calendar.day_name[date.weekday()] 

print(day_of_week.upper())

c = calendar.TextCalendar(calendar.SUNDAY)
~~~

[Introduction to Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true)

~~~Python
from __future__ import division

def average(array):
    
    s = set(array)
    sum_dist = sum(s)
    total_dist = len(s)
    average = sum_dist/total_dist

    return average 

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
~~~

[Set.add()](https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true)

~~~Python
n = int(input())
v = []
s = set('')

for i in range(n):
    v.append(raw_input())
    s.add(v[i])
    
print(len(s))    
~~~
