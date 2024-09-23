# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  if small + big * 5 < goal:
    return False
  if big:
    d = goal % 5 
    return d == 0 or small - d >= 0
  else:
    return small >=  goal 
    

# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):

  if a == b and b == c:
    return 0
  if a == b:
    return c 
  if a == c:
    return b
  if b == c:
    return a
  return a + b + c


# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  arr = [a,b,c]
  sum =0
  for i in range(3):
    if arr[i] == 13:
      break
    sum+= arr[i]
  return sum

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
  
  
def fix_teen(x):
  if 13 <= x <= 19 and  x !=15 and x != 16:
    return 0
  return x

