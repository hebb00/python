
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    st = s[::-1].lstrip()

    for i in range(len(st)):
        if st[i] == " ":
            return i
    
    return i +1
    
if __name__ == '__main__':
    print(lengthOfLastWord("   rrd  "))