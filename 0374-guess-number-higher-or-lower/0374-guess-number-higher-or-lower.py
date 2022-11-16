# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n, left = 1) -> int:
        mid = (left + n)//2
        
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            return self.guessNumber(mid - 1, left)
        else:
            return self.guessNumber(n, mid+1)
        
        
            
        