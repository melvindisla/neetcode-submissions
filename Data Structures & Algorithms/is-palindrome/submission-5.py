class Solution:
    def isPalindrome(self, s: str) -> bool:

        # convert all letters into lowercase
        # remove spaces
        # remove punctuation
        changed_str = ''.join([char for char in s if char.isalnum()]).lower()
        if s == '':
            return True

        reversed_str = str(changed_str[::-1])
        if changed_str == reversed_str:
            return True
        return False