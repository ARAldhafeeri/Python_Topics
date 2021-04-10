"""
Problem:
You want to eliminate the duplicate values in a sequence but preserve the order of the remaining items.
If the values are hashable then easy:
use set and a generator.
"""


def dedupe(items, key=None):
    """
     Python method to remove data duplication in hashable sequence
    :param items: hashable sequence
    :param key: key of hashable sequence
    :return:
    items: deduplication of items
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [1,2,2,3,4,5,6,6]
a = list(dedupe(a))
print(a)

hash = [{'a': 1, 'a': 1, 'b': 2}]
hash = list(dedupe(hash, key=lambda x: x['a']))
print(hash)