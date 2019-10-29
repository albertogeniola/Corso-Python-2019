"""
Write a script that, given two lists, determines which one contains the major number of elements and also
tells how many elements the longer list has with respect of the shorter one.

For instance, given the following lists...
list_a = ['orange', 'blue', 'green', 'yellow']
list_b = ['ford', 'toyota', 'fiat']
The script should output: "list_a is longer as it contains 1 element more than list_b"
"""
list_a = ['orange', 'blue', 'green', 'yellow']
list_b = ['ford', 'toyota', 'fiat']

el_a = len(list_a)
el_b = len(list_b)

print("La lista a contiene {} elementi, mentre la lista b ne contiente {}".format(el_a, el_b))
if el_a > el_b:
    delta = el_a - el_b
    print("La lista a contiene {} elementi in più della lista b".format(delta))
elif el_a == el_b:
    delta = 0
    print("La lista a contiene lo stesso numero di elementi della lista b")
else:
    delta = el_b - el_a
    print("La lista b contiene {} elementi in più della lista a".format(delta))
