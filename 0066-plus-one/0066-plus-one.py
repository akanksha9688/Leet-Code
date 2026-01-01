class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        curr = []
        # account for the case we need to add a digit 
        if digits[-1] == 9:
          # while there are 9s 
          while digits and digits[-1] == 9:
            curr.append(digits.pop())
          
          # if not all 9s then get the last popped element and increment by 1 
          if digits:
            curr.append(digits.pop())
            digits.append(curr.pop()+1)
          
          # Otherwise add 1 and append zeros to the remaining digits equal to the length of curr
          else:
            digits.append(1)
          
          while curr:
            curr.pop()
            digits.append(0)
        
        # if not a 9 as last digit, just increment the last digit by 1 
        else:
          digits[-1] += 1
        
        return digits 
        