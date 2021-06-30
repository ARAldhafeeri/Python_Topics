"""
unfinished !

"""

from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.counter = dict()

    def get(self, key: int) -> int:
        print('get')
        counter_key = f"count_{key}"
        if key not in self.cache.keys():
            return -1
        self.cache.move_to_end(key)
        if counter_key in self.counter.keys():
            self.counter[counter_key] += 1
        else:
            self.counter[counter_key] = 0
        print(key, counter_key, self.counter[counter_key])
        print(self.cache)
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:
        print('put')
        if len(self.cache) > self.capacity: # cache reached capacity
            counter_sorted = sorted(self.counter.items(), key=lambda x: x[1], reverse=False)
            limit = 0
            two_lfu_keys = list()
            for i in counter_sorted:
                if limit == 2:
                    break
                key = i[0]
                target = key.split("_")
                two_lfu_keys.append(target[1])
                limit += 1
            if two_lfu_keys[0] == two_lfu_keys[1]:
                print(f"dict before pop {self.cache}")
                self.cache.popitem(last= False)
                print(f"popeditem last=true {self.cache}")
            else:
                key = int(two_lfu_keys[0])
                print(self.cache.keys())
                print(f"dict before pop {self.cache}")
                self.cache.pop(key)
                print(f"pop key = {key} dict after pop {self.cache}")
                self.counter.pop(f"count_{key}") 
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.count = collections.defaultdict(collections.OrderedDict)
        self.min = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value, count = self.cache[key]
        del self.count[count][key]
        if count == self.min and not self.count[count]:
            self.min += 1
        self.count[count+1][key] = 0
        self.cache[key] = (value, count+1)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key in self.cache:
            old, count = self.cache[key]
            self.cache[key] = (value, count)
            self.get(key)
        elif len(self.cache) == self.capacity:
            old_key, v = self.count[self.min].popitem(last=False)
            del self.cache[old_key]
            self.min = 1
            self.cache[key] = (value, 1)
            self.count[1][key] = 0
        else:
            self.min = 1
            self.cache[key] = (value, 1)
            self.count[1][key] = 0