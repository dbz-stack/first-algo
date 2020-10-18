# Python program for implementation of Bubble Sort 

def bubbleSort(arr): 
	n = len(arr) 

	# Traverse through all array elements 
	for i in range(n): 


# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 
