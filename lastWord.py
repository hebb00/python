
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    st = s.rstrip()
    c=0
    for i in range(len(st)-1,-1,-1):
   
        if st[i] == " ":
            return c
        c=c+1
    return c
    
if __name__ == '__main__':
    print(lengthOfLastWord("   rr"))