class Solution:
    def isPalindrome(self, s: str) -> bool:

        # convert all letters into lowercase
        # remove spaces
        # remove punctuation
        changed_str = ''.join([char for char in s if char.isalnum()]).lower()
        return changed_str == changed_str[::-1]

        # what is the time complexity? why?
        # what is the space complexity? why?
        
        left, right = 0, len(s)-1

        while left < right:

            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            # if the elements that are equidistant from one another are NOT equal
            if s[left].lower() != s[right].lower():
                # this is not a valid palindrome
                return False
            left, right = left + 1, right - 1
            return true