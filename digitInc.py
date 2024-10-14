# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = ''.join(str(x) for x in digits)
        incr= int(d) + 1
        i = [int(s) for s in str(incr)]
        return i
# another way
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        apnd = 0
        summed = False
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i]+= 1
                summed = True
                break
            else:
                digits[i] = 0                    
                
        if not summed:
            digits.insert(0,1)
        return digits

#3d way so i added summed bu ti dont actually need it since i can return 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i]+= 1
                return digits
            else:
                digits[i] = 0                    
                
            digits.insert(0,1)
        return digits
