####List
fruits = ["Apple", "mango", "banana"]


fruits = ["Apple", "mango", "banana"]
>>> fruits
['Apple', 'mango', 'banana']
>>> fruits[1]="papaya"
>>> fruits
['Apple', 'papaya', 'banana']
>>> city = list(("london", "newyork", "paris"))
>>> city
['london', 'newyork', 'paris']
>>> city.remove("newyork")
>>> city
['london', 'paris']
>>> city.append("venice")
>>> city
['london', 'paris', 'venice']
>>> len(city)
3
>>> city.sort()
>>> city
['london', 'paris', 'venice']
>>> city.append("Darwin")
>>> city
['london', 'paris', 'venice', 'Darwin']
>>> city.sort()
>>> city
['Darwin', 'london', 'paris', 'venice']
>>> city.reverse()
>>> ciry
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ciry' is not defined
>>> city
['venice', 'paris', 'london', 'Darwin']
>>> city.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (0 given)
>>> city.remove
<built-in method remove of list object at 0x102b6d1c8>
>>> city
['venice', 'paris', 'london', 'Darwin']
>>> city.pop(2)
'london'
>>> city
['venice', 'paris', 'Darwin']
>>> city.pop(2)
'Darwin'
>>> city
['venice', 'paris']
>>> city.pop(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> city = ["london", "paris", "nice", "amsterdam"
... 
... 
... ]
>>> city
['london', 'paris', 'nice', 'amsterdam']
>>> city.pop(3)
'amsterdam'
>>> city
['london', 'paris', 'nice']
>>> city.pop(1)
'paris'
>>> city = ["london", "paris", "nice", "amsterdam"]
>>> city.index(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 2 is not in list
>>> city.index(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list
>>> city.index("nice')
  File "<stdin>", line 1
    city.index("nice')
                     ^
SyntaxError: EOL while scanning string literal
>>> city.index("nice")
2
>>> city.index("london")
0
>>> city.insert(2,"delhi")
>>> city
['london', 'paris', 'delhi', 'nice', 'amsterdam']
>>> city.clear()
>>> city
[]
>>> 
