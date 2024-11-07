class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def count_occurrences(head, counts):
    if head is None:
        return
    value = head.value
    if value in counts:
        counts[value] += 1
    else:
        counts[value] = 1
    count_occurrences(head.next, counts)


def print_occurrence_counts(counts):
    for value, count in counts.items():
        print(f"{value}: {count} times")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next.next.next=ListNode(5)
head.next.next.next.next.next.next.next.next.next=ListNode(6)

element_counts = {}

count_occurrences(head, element_counts)

print_occurrence_counts(element_counts)
