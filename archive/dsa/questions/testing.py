def max(arr):
  arr.sort()
  return arr[len(arr)-1]

    







print(max([1,2,3,6,7,8,4,9]))


class check:
  def __init__(self, name):
    self.name = name 
  
  def size(self):
    print(f"{self.name} days")

  
checking = check("yes")
checking.size()




    