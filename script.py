def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return print ("These numbers are the same")
  
  greater_than(4,4)
  
    
def graduation_reqs (credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

  graduation_reqs (130)
  