class student():
  def __init__(self, name, roll_no):
    self.name=name
    self.roll_no=roll_no
  def names(self):
    return self.name
  def roll(self):
    return self.roll_no

name = input()
rollno = int(input())



obj= student(name, rollno)

print("Name: "+ obj.names())
print("Roll No= "+ str(obj.roll()))

