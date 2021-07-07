"""

Runtime: 720 ms, faster than 84.13% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19.1 MB, less than 24.09% of Python3 online submissions for Find the Town Judge.
Concept:
It is a graph problem where  we are given the vertices, all nodes must be directed and point
to the judge node, the judge node point to nobody. Here are graphs are pointing to the judge node
therefore it is a 

"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return n
        if not trust and n > 1:
            return -1
        if len(trust) == 1:
            return trust[0][1]
        ppl = {i: 0 for i in range(1,n+1)}  # person : trusted
        m = -(n -1) # trust nobody
        for i,j in trust:
            ppl[i], ppl[j] = ppl[i] + 1, ppl[j] - 1
        if m not in ppl.values():
            return -1
        for k,v in ppl.items():
            if v == -(n - 1):
                return k

"""
In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

"""