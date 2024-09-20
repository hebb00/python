# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2

def count_code(str):
  count = 0

  for i in range(len(str)-1):
    if str[i] + str[i+1 ]== 'co':
      if i + 3 <  len(str): 
        if str[i+3] =='e':
          count+=1
             
        
  return count
  

        
def count_code(str):
  count = 0

  for i in range(len(str)-1):
    if str[i] + str[i+1 ] == 'co' and i + 3 <  len(str) and str[i+3] =='e':
          count+=1
             
  
  return count