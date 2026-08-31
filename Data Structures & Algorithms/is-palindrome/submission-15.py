class Solution:
    def alphanum(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord("z")) or (ord('A') <= ord(s) <= ord("Z")) or (ord('0') <= ord(s) <= ord("9"))
        
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while left < right:

            while left < right and not self.alphanum(s[left]):
                left += 1
            while right > left and not self.alphanum(s[right]):
                right -= 1
            # if the elements that are equidistant from one another are NOT equal
            if s[left].lower() != s[right].lower():
                # this is not a valid palindrome
                return False
            left, right = left + 1, right - 1
        return True


        # convert all letters into lowercase
        # remove spaces
        # remove punctuation
        # changed_str = ''.join([char for char in s if char.isalnum()]).lower()
        # return changed_str == changed_str[::-1]

        # what is the time complexity? why?
        # what is the space complexity? why?