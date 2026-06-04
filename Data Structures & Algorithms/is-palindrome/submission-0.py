class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = "".join(char.lower() for char in s if char.isalnum())

        l, r = 0, len(res) - 1

        while l < r:

            if res[l] != res[r]:
                return False
            else:
                l += 1
                r -= 1
        return True      