"""
Problem:
Sometimes you want to create a dictionary and you also want to control the order of items when
iterating or serializing.
OrderedDict maintains a doubly linked list that orders the keys according to insertion order.
Size of OrderedDict is twice as big of a normal dict
"""

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for i,k in d.items():
    print(i,k)

"""
output:
foo 1 
bar 2 
spam 3 
grok 4
"""

# Very useful when you want to serialize or encode into a different format.

import json

json.dump(d)