class Solution:
    def isPalindrome(self, s: str) -> bool:

        # convert all letters into lowercase
        # remove spaces
        # remove punctuation
        changed_str = ''.join([char for char in s if char.isalnum()]).lower()
        return changed_str == changed_str[::-1]