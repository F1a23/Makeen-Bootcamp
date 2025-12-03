#------------Linear Search in Python--------------
#Any list
#Checks one by one
#1. checking each element in a list one by one until it finds the target value 
#2. start from first element(index[0])
#3. if a match found it will return the index , if it not found will return -1

def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

num=[1,2,3,4,5]
target=10

result=linear_search(num,target)

if result != -1:
    print(f"Element found at index:",result)
else:
    print("Element not found ")
    
print("---------------------------------------------")

#------------binary Search in Python--------------
#Sorted list only
#Divides list in half each time
#If the middle element equals the target, it’s found.
#If the target is smaller, the search continues in the left half; if larger, in the right half.
#This process continues until the element is found or the list is empty.
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

num=[1,2,3,4,5]
target=3

result=binary_search(num,target)

if result != -1:
    print(f"Element found at index:",result)
else:
    print("Element not found ")