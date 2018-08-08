animals = {
    "type": "dog",
    "color": "brown",
    "breed": "pug"
}

animals = {
...     "type": "dog",
...     "color": "brown",
...     "breed": "pug"
... }
>>> animals
{'type': 'dog', 'color': 'brown', 'breed': 'pug'}
>>> animals['type']
'dog'
>>> animals['type']="cat"
>>> animals
{'type': 'cat', 'color': 'brown', 'breed': 'pug'}
>>> revenu = dict(amazone="$1000", apple="$20000", google="$30000")
>>> revenu
{'amazone': '$1000', 'apple': '$20000', 'google': '$30000'}
>>> len(revenu)
3
>>> del(revenu('amazone')
... )
  File "<stdin>", line 1
SyntaxError: can't delete function call
>>> del(revenu['amazone'])
>>> revenu
{'apple': '$20000', 'google': '$30000'}
>>> 



###############
student = {
  "name" : "John",
  "student_id": 123,
  "feedback": None
}

student["lastName"] = "macij"