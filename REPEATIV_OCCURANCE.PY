class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def count_occurrences(head, target):
    if head is None:
        return 0

    count = 0

    if head.value == target:
        count = 1

    count += count_occurrences(head.next, target)

    return count

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(2)

print("Original Linked List:")
print_linked_list(head)

target = 2
count = count_occurrences(head, target)
print(f"\nThe element {target} occurs {count} times in the linked list.")
