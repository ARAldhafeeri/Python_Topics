"""
Built-in function in python.
Checkts if all charchters of a string full into those domains.
return True or False
str.isalnum() :
a-z, A-Z, 0-9

str.isalpha()
a-z, A-Z

str.isdigit()
(0-9)

str.islower()
(a-z)

isupper()
(A-Z)

Task: Given a string return all the flags:
True if any char in the str applies on domain
False if any char in the str does not apply on domain
Input: single line string. s
Constrains:
0 < len(s) < 1000

Sample input: qA2

Sample Output

True
True
True
True
True

"""





if __name__ == '__main__':
    s = str(input())
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

    """
    any(c.isalnum() for c in s
    
    is equilvent to:
    list = []
    for item in s:
        list.append(item)
    print(any(list))
    Python is pretty.
    
    """

