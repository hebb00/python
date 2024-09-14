
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  else:
    return b + a +b

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
  if len(a) + len(b)  == 2:
    return ""
  else: 
    return a[1:] + b[1:]

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
  if len(str) == 2:
    return str
  else: 
    return str[2:] + str[:2]

# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

# cigar_party(30, False) → False
# cigar_party(50, False) → True

def cigar_party(cigars, is_weekend):
  return (is_weekend and cigars >= 40) or (not is_weekend and  cigars >= 40 and  cigars <= 60)

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)
#   You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1
  
def date_fashion(you, date):
  if  you >= 8 or  date >= 8:
    if  you <= 2 or date <= 2:
      return 0
    else:
      return 2
  elif  you <= 2 or date <= 2:
    return 0
  else:
    return 1
  
def date_fashion(you, date):
  ## Check the <=2 case first, since it takes precedence
  ## over the >=8 case.
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1