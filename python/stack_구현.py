### Node
# - item : 초기 속성값
# - pointer : next Node
### Linked List
# head: first item
# length: property length
### Stack
# push
# pop



from typing import Optional

class Node:
    def __init__(
        self,
        item,
        pointer: Optional["Node"] = None
        ) -> None:
        self.item = item
        self.pointer: Optional["Node"] = pointer

    def __str__(self):
        return f"현재 {self.item}과 {self.pointer}"


class LinkedList:
    def __init__(self) -> None: 
        self.head: Optional["Node"] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node: Node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count


class Stack(LinkedList):

    def push(self, data) -> None:
        new_node: Node = Node(item=data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def pop(self) -> T:
        if self.head is None:
            raise ValueError("stack is empty")
        cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer
        result = cur_node.pointer
        cur_node.pointer = None
        return result.item


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(7)
    stack.push(4)
    print(stack.head.__dict__)
    print(stack.head.item)
    print(stack.length)