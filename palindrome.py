
# def isPalindrome(x):
#     strX = str(x)
#     print(strX == strX[::-1])

def strStr(haystack, needle):

    for i, v in enumerate(haystack):
        if v == needle[0]:
            if len(haystack) >= i + len(needle):
                if haystack[i:i+len(needle)] == needle:
                    return i
    return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))