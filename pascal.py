
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    pascal=[[1]]
    for _ in range(numRows-1):
        r=[0]+pascal[-1]+[0]
        row =[]
        for i in range(len(pascal[-1]) + 1):
            row.append(r[i]+r[i+1])
            
        pascal.append(row)
    return pascal
        
                
if __name__ == "__main__":
    print(generate(8))
   

    