from operator import itemgetter

rows = [
  { 'fname': 'Brain', 'lname': "Jones", 'uid': 1000 },
  { 'fname': 'Ahmed', 'lname': "Aldhafeeri", 'uid': 1002 },
  { 'fname': 'Ahmed', 'lname': "Rakan", 'uid': 1001 },
]
rows_by_fname = sorted(rows, key=itemgetter('fname')) # sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=itemgetter('uid')) # sorted(rows, key=lambda r: r['uid'])
print(rows_by_fname)
print(rows_by_uid)
"""
[
  {'fname': 'Ahmed', 'lname': 'Aldhafeeri', 'uid': 1002},
  {'fname': 'Ahmed', 'lname': 'Rakan', 'uid': 1001},
  {'fname': 'Brain', 'lname': 'Jones', 'uid': 1000}
]
[
  {'fname': 'Brain', 'lname': 'Jones', 'uid': 1000},
  {'fname': 'Ahmed', 'lname': 'Rakan', 'uid': 1001},
  {'fname': 'Ahmed', 'lname': 'Aldhafeeri', 'uid': 1002}
]
"""