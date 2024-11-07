class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_elements(head, key):
    remove = ListNode(None)
    remove.next = head
    prev, current = remove, head
    while current:
        if current.value == key:
            prev.next = current.next
        else:
            prev = current
        current = current.next

   
    return remove.next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next.next= ListNode(1)
head.next.next.next.next.next.next.next.next= ListNode(1)
head.next.next.next.next.next.next.next.next.next= ListNode(3)
head.next.next.next.next.next.next.next.next.next.next= ListNode(2)
head.next.next.next.next.next.next.next.next.next.next.next= ListNode(1)
head.next.next.next.next.next.next.next.next.next.next.next.next= ListNode(6)
print("Original Linked List:")
print_linked_list(head)


key = 6
new_head = remove_elements(head, key)

print(f"\nLinked List after removing {key}:")
print_linked_list(new_head)
