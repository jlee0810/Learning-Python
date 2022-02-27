class Solution:
    def EricisPalindrome(self, x: int) -> bool:
        strx = str(x)
        if (len(strx) % 2 == 0):
            for i in range (len(strx)):
                if (i == len(strx) - i - 2):
                    if (strx[i] == strx[len(strx) - i - 1]):
                        return True
                    else:
                        return False
                if (strx[i]  == strx[len(strx) - i - 1]):
                    continue 
                else: 
                    return False
        if (len(strx) % 2 != 0):
            if (len(strx) == 1):
                return True
            for i in range (len(strx)):
                if (i == len(strx) - i - 1):
                    return True
                if (strx[i]  == strx[len(strx) - i - 1]):
                    continue 
                else: 
                    return False
    
    def AnswerisPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        div = 1
        while x >= 10 * div: 
            div *= 10
        
        while x: 
            right = x % 10
            left = x // div
            
            if left != right:
                return False
            
            x = (x % div) // 10
            div = div // 100

        return True

s = Solution()
