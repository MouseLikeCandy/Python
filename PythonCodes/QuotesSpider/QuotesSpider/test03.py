# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 15:51
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
队列
'''
from collections import deque
from typing import Any, Optional

class FifoMemoryQueue:
    """In-memory FIFO queue, API compliant with FifoDiskQueue."""

    def __init__(self) -> None:
        self.q = deque()  # type: # deque 双端队列   可以看成列表

    def push(self, obj: Any) -> None:
        """增加数据"""
        self.q.append(obj)

    def pop(self) -> Optional[Any]:
        """弹出数据"""
        return self.q.popleft() if self.q else None

    def peek(self) -> Optional[Any]:
        """提取第一个数据"""
        return self.q[0] if self.q else None

    def close(self) -> None:
        pass

    def __len__(self):
        """当你的代码len(xxx) 会运行这一段代码"""
        return len(self.q)


class LifoMemoryQueue(FifoMemoryQueue):
    """In-memory LIFO queue, API compliant with LifoDiskQueue."""

    def pop(self) -> Optional[Any]:
        return self.q.pop() if self.q else None     # 右侧弹出

    def peek(self) -> Optional[Any]:
        return self.q[-1] if self.q else None


if __name__ == '__main__':
    fifo_memory_queue = LifoMemoryQueue()
    fifo_memory_queue.push(1)
    fifo_memory_queue.push(3)
    fifo_memory_queue.push(7)
    print(fifo_memory_queue.pop())
    print(fifo_memory_queue.pop())
    print(fifo_memory_queue.pop())

