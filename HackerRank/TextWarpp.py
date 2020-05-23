"""

Check Tutorial tab to know how to to solve.

You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

import textwrap
def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)
    b = ''
    if( 0< len(string)< 1000):
        if(0 < max_width < len(string)):
            for item in range(0,len(a)):
                A = "{}\n".format(a[item])
                b = b + A

    return b
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
