#leetcode logic
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode(0)  # dummy node
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    

#user input
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    
    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next


# ---- USER INPUT ----
arr1 = list(map(int, input("Enter first number digits (space separated): ").split()))
arr2 = list(map(int, input("Enter second number digits (space separated): ").split()))

l1 = create_linked_list(arr1)
l2 = create_linked_list(arr2)

result = addTwoNumbers(l1, l2)

print("Result:")
print_linked_list(result)