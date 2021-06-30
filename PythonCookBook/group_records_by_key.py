from operator import itemgetter
from itertools import groupby

rows = [
  { 'fname': 'Brain', 'lname': "Jones", 'uid': 1000 },
  { 'fname': 'Ahmed', 'lname': "Aldhafeeri", 'uid': 1002 },
  { 'fname': 'Ahmed', 'lname': "Rakan", 'uid': 1001 },
]
rows.sort(key=itemgetter('uid'))
for uid, items in groupby(rows,key=itemgetter('uid')):
  print(uid)
  for i in items:
    print('    ', i)
"""
output:

1000
     {'fname': 'Brain', 'lname': 'Jones', 'uid': 1000}
1001
     {'fname': 'Ahmed', 'lname': 'Rakan', 'uid': 1001}
1002
     {'fname': 'Ahmed', 'lname': 'Aldhafeeri', 'uid': 1002}

"""