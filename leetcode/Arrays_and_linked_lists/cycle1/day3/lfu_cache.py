"""
Design and implement a
data structure for a Least Frequently Used (LFU) cache.

sol performance:
Runtime: 804 ms, faster than 75.06% of Python3 online submissions for LFU Cache.
Memory Usage: 76.5 MB, less than 53.76% of Python3 online submissions for LFU Cache.


"""

class LFUCache:
    def __init__(self, capacity: int):
        """
        self.capacity: the maximum capacity of the cache
        self.cache: normal hashtable that maps 1 key to 1 value
        self.freq_keys: one frequently used key to many keys, 
        those many keys are or ordered in a Ordered hashtable.
        For example: with one given key we can find ;
        1- the frequency of the given key in self.freq_keys
        2- using the frequency value we get all other keys with the 
        same frequency!
        3- when there are many frequently used key, OrderDict record 
        values in LRC way, therefore;
        the first item will be popout
        """
        self.capacity = capacity
        self.cache = dict() 
        self.min_freq = None
        self.freq_keys = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        freq=self.cache[key]
        val=self.freq_keys[freq][key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq]:
            if freq==self.min_freq:
                self.min_freq+=1
        self.cache[key]=freq+1
        self.freq_keys[freq+1][key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0:
            return
        if key in self.cache:
            freq=self.cache[key]
            self.freq_keys[freq][key]=value
            self.get(key)
            return
        if self.capacity==len(self.cache):
            delkey,delval=self.freq_keys[self.min_freq].popitem(last=False)
            del self.cache[delkey]
        self.cache[key]=1
        self.freq_keys[1][key]=value
        self.min_freq=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)