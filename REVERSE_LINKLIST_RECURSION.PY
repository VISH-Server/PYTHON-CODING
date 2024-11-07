class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)

    head.next.next = head
    head.next = None

    return new_head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("KHALI BHAI KHALI R KI CHAI")

head = ListNode(15)
head.next = ListNode(18)
head.next.next = ListNode(21)
head.next.next.next = ListNode(23)
head.next.next.next.next = ListNode(29)

print("Original Linked List:")
print_linked_list(head)

new_head = reverse_linked_list(head)

print("\nReversed Linked List:")
print_linked_list(new_head)
