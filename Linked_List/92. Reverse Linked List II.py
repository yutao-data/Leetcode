class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Define left, right pointers
        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # if n > 1, right continue going right
            if n == 1:
                return
            right = right.next

            # left also going to it's position
            if m > 1:
                left = left.next

            recurseAndReverse(right, m - 1, n - 1)

            # check if finish or not
            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val

                left = left.next

        recurseAndReverse(right, m, n)
        return head