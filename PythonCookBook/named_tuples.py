from collections import namedtuple
Sub = namedtuple('subscriber', ['addr', 'joined'])
new_sub = Sub('jones@jones.com', '2021-10-19')
print(Sub) # <class '__main__.subscriber'>
print(new_sub) # subscriber(addr='jones@jones.com', joined='2021-10-19')
print(new_sub.addr) # jones@jones.com
print(new_sub.joined) # 2021-10-19

# named tuples make code less expensive
# uses; if code uses large structre of hashmaps
# then using namedtuples is more effcient

# keep in mind tuples are immutable we need to use ._replace
new_sub = new_sub._replace(addr='jj@jj.com')
print(new_sub) # subscriber(addr='jj@jj.com', joined='2021-10-19')

# dict to namedtuple
Sub_prototype = Sub('', [None, None])
s = {'addr': 'kk', 'joined': '2021-10-19'}
new_sub_2 = Sub_prototype._replace(**s)
print(new_sub_2) # subscriber(addr='kk', joined='2021-10-19')