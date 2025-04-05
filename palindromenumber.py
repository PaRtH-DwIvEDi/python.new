list1 = []
l1 = int(input("enter first number :"))
l2 = int(input("enter second number :"))
l3 = int(input("enter third number :"))
l4 = int(input("enter forth number :"))

list1.append(l1)
list1.append(l2)
list1.append(l3)
list1.append(l4)

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")