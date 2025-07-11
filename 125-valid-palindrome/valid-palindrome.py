class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        formated_string = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(formated_string) -1

        while left < right:
            if formated_string[left] != formated_string[right]:
                return False
            else:
                left+=1
                right-=1
        return True