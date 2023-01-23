#remove spaces from string
#reshma
'''
a=input()
k = "   "
for n in a:
    if n!=" ":
        k=k+n
print(k)
 ''' 
#large and small number in a list[1]
'''
num = input("enter the numbers:")
for n in range(num):
    numbers = input(" Enter numbers: ")
    num.append(numbers)
    print("Maximum number is : ", max(num))
    print("Minimum number is : ", min(num))
'''
#fibonacci
#manikanta
'''
num=int(input("enter the number: "))
def fibonacci(i):
    if i<=1:
        return i
    else:
         return(fibonacci(i-1)+fibonacci(i-2))
if num<=0:
    print("enter the positive number  ")
else: 
    print("fibonacci: ",end=" ")
for i in range(num):
    print(fibonacci(i), end= " ")
'''
#min,max
#kranthi
'''
List = []
Number = int(input("Please enter element length in list "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List.append(value)
print("The Smallest Element in this List is : ", min(List))
print("The Largest Element in this List is : ", max(List))


NumList = []
Number = int(input("How many element in list, Please enter num :- "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
smallest = largest = NumList[0]
for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j
print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)
print("The Largest Element in this List is : ", largest)
print("The Index position of Largest Element in this List is : ", max_position)
'''
#list
#omkar
'''
fruits=["apple","banana","mango"]
veggies=["carrot","beatroot","beans"]
print(list(zip(fruits,veggies)))
'''
#prime number
#kiranmayi
'''
lower = int(input("enter the lower number: "))
upper = int(input("enter the upper number: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower,upper+ 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
'''