import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        Push item with assigning priority in a queue.
        [(<-priority0-->, <-index0->, obj_ins0()), (<-priority1-->, <-index1->, obj_ins1()) ].
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """
            Return tuple of queue details of highest priority item
            ( <-priority->, <-index->, obj_ins0() )
            Return object instance only of highest priority item
            ( <-priority->, <-index->, obj_ins0() )[-1]

         """
        return heapq.heappop(self._queue)


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())   # Item(bar)
print(q.pop())   # Item(spam)