def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    output = []
    i = 0
    carry = 0
    a = a[::-1]
    b = b[::-1]

    while i < len(a) or i < len(b) or carry:
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0
        total = bit_a + bit_b + carry
        
        output.append(str(total % 2)) 
        carry = total // 2             

        i += 1

    return ''.join(output[::-1])  





if __name__ == '__main__':
    print(addBinary("1010", "1011"))  # Output: "10101"
    print(addBinary('11','11'))
            
        