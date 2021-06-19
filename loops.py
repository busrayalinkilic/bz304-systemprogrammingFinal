#range
genre = ['pasta', 'apple', 'soup']


for i in range(len(genre)):
    print("I like", genre[i])



#while

n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

#for

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum2 = 0

for val in numbers:
    sum2 = sum2+val

print("The sum2 is", sum2)

#while true

weekSalary = 0
dayOfWeek = 1
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while(True):
  if(week[dayOfWeek] == "Sunday"):
    print("Week Over, Its holiday!!")
    break
  weekSalary += 2000
  dayOfWeek += 1 
 
print(str(weekSalary))
