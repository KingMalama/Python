#Multiple parameters & returns
def get_boundaries(target,margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit
# Time to the action babe
low, high = get_boundaries(100,20)
print(low)
print(high)
