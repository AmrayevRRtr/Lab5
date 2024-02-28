
ex1
import re
a = input()
p = re.compile('ab*')
m = p.fullmatch(a)
print(m)

ex2
import re
a = input()
p = re.compile('ab{2,3}')
m = p.fullmatch(a)
if m:
    print('Match!')
else:
    print('No match!')

ex3
import re
a = input()
p = re.compile('[a-z]+_')
m = p.findall(a)
print(m)

ex4
import re
a = input()
p = re.compile('[A-Z][a-z]+')
f = p.findall(a)
print(f)

ex5
import re
a = input()
p = re.compile('^a.+b$')
m = p.match(a)
print(m)

ex6
import re
a = input()
p = re.compile('.+')
s = re.sub('[ ,.]', ':', a)
print(s)

ex7
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
print(snake_to_camel('snake_string'))

ex8
import re

def split(s):
    return re.findall('[A-Z][^A-Z]*', s)

a = input()
res = split(a)
print(*res)

ex9
import re
def func(a):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', a)
txt = input()
res = func(txt)
print(res)

ex10
import re
def camel_to_snake(camel):
    snake = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
    return snake
camel = "camelString"
snake = camel_to_snake(camel)
print(snake)
