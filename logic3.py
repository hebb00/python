# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed-= 5
  if speed <= 60:
    return 0
  elif 61 <= speed <= 81:
    return 1
  else: return 2
  
#   Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums)-1]



# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
  clock = "7:00"
  clock0 = "10:00"
  if vacation:
    clock = "10:00"
    clock0 = "off"
  if day in range(1,6):
    return clock
  else: 
    return clock0
  
  
#   Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

# def rotate(nums):
#     a = nums.pop(0)
#     return nums.append(a)

# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


def reverse3(nums):
  ele = []
  for i in range(len(nums)-1, -1,-1):
    ele.append(nums[i]) 
  return ele

# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]
  
def max_end3(nums):
  mx= max(nums[0], nums[len(nums)-1])
  for i in range(len(nums)):
    nums[i]= mx
  return nums

# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
  n = num % 10
  return n in range(3) or 10 - n == 1 or 10 - n == 2 
  
def near_ten(num):
  n = num % 10
  return n in range(3) or  n >= 8 
  
  