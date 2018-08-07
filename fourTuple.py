codelang = ("NodeJS", "python", "angularJS")
codelang
('NodeJS', 'python', 'angularJS')
codelang[1]
'python'
codelang[1]= 'ReactJS'
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment
codelang = ("NodeJS", "python", "angularJS", "Python"))
  File "<stdin>", line 1
    codelang = ("NodeJS", "python", "angularJS", "Python"))
                                                          ^
SyntaxError: invalid syntax
>>> codelang = ("NodeJS", "python", "angularJS", "Python")
>>> codelang
('NodeJS', 'python', 'angularJS', 'Python')
>>> codelang = ("NodeJS", "Python", "angularJS", "Python")
>>> codelang
('NodeJS', 'Python', 'angularJS', 'Python')
>>> countries = tuple(("USA", "INDIA", "PAkistan"))
>>> countries
('USA', 'INDIA', 'PAkistan')
>>> len(countries)
3