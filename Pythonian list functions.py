import random



list=[44,44,44,44,2]#<------------------            1. This is your original list. If you want to add duplicate numbers to your list, you will add them here.
left=[]
right=[]
middle=[]

onofflist=[0,1,0,1,0,1]


last=(len(list))
mid= int(len(list)/2)
shuffled_list=[]


def make_list_long_afff(list, length):

     for num in range(length):
         list.append(num)
      
    
     return(list)

def shuffle_list(list):
 
     for item in list:
          indexnum= random.randint(0,last)
          shuffled_list.insert(indexnum, item)    
          
     return(shuffled_list)
   

#                                                    2. make_a_list_numbered 1-x long like make_list_long_afff(list, <INSERT INT HERE>)

make_list_long_afff(list, 100)
shuffle_list(list)###<----------------------------       a. As the name implies, this shuffles your list for you. As the list gets larger
#print(shuffled_list)                              #        shuffle_list(list) inserts it into a random location within the list. 

def quicksort1(list):
    if len(list) <= 1:
        return list
    miditem= list[len(list)//2]
    left= [x for x in list if x < miditem]
    middle= [x for x in list if x == miditem]
    right= [x for x in list if x > miditem]
    return quicksort1(left)+ middle + quicksort1(right)


def merge_sort(list): 
    
    if len(list) > 1: 
        mid = len(list)//2
        left_half = list[:mid]  
        right_half = list[mid:] 
  
        merge_sort(left_half)  
        merge_sort(right_half)  
  
        i = j = k = 0
          
        while i < len(left_half) and j < len(right_half): 
            if left_half[i] < right_half[j]: 
                list[k] = left_half[i] 
                i += 1
            else: 
                list[k] = right_half[j] 
                j += 1
            k += 1
          
        while i < len(left_half): 
            list[k] = left_half[i] 
            i += 1
            k += 1
          
        while j < len(right_half): 
            list[k] = right_half[j] 
            j += 1
            k += 1

    return list
  


def binary_search(ordered_list, item):
  count=0
  
  on=True
  item=input("Enter a number and find its corresponding index....")
  item= int(item)

  #low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(ordered_list) - 1

  #while you haven't narrowed it down to one element ...
  while low <= high:
    #check the middle element
    mid = (low + high) // 2
    guess = ordered_list[mid]
    scopeleft=mid-10
    scoperight=mid+10
    count=0
    staticcount=0
    #IF AN ITEM IS FOUND
    if guess == item:

      ##HANDELING RANGE ERRORS
      if scopeleft < 0:
           scopeleft = 0
           #print(scopeleft,scoperight)
      if scoperight > len(ordered_list):
           scoperight = len(ordered_list)

      myview= ordered_list[scopeleft:scoperight]
      index_list=[]
      #print(scopeleft,scoperight)
      for guess in myview:
           #print(staticcount)
           staticcount=staticcount+1
           if guess == item:
                count=count+1
                index=scopeleft+staticcount-1
                index_list.append(index)
                
                

      return print("ITEM: ", item, "found at.." ,index_list)
    #the guess was too high
    if guess > item:
      high = mid - 1
    #the guess was too low
    else:
      low = mid + 1

  #the item doesn't exist
  return print("This item is not in the list")


def heapify(list, n, i): 
	largest = i # Initialize largest as root 
	l = 2 * i + 1	 # left = 2*i + 1 
	r = 2 * i + 2	 # right = 2*i + 2 

	# See if left child of root exists and is 
	# greater than root 
	if l < n and list[i] < list[l]: 
		largest = l 

	# See if right child of root exists and is 
	# greater than root 
	if r < n and list[largest] < list[r]: 
		largest = r 

	# Change root, if needed 
	if largest != i: 
		list[i],list[largest] = list[largest],list[i] # swap 

		# Heapify the root. 
		heapify(list, n, largest) 


def heapSort(list): 
	n = len(list) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(list, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		list[i], list[0] = list[0], list[i] # swap 
		heapify(list, i, 0)


def recursive_binary_search(list, x, start, end): 
  
    # Base Condition 
    if start > end: 
        return -1
  
    # Find the mid index 
    mid = (start + end)//2
  
    # Compare mid with given key x 
    if list[mid] == x: 
        return mid 
  
    # If element at mid is greater than x, 
    # search in the left half of mid 
    elif list[mid] > x: 
        return recursive_binary_search(list, x, start, mid-1) 
  
    # If element at mid is smaller than x, 
    # search in the right half of mid 
    else: 
        return recursive_binary_search(list, x, mid + 1, end) 
    


def call_rbs(list, x):
     result = recursive_binary_search(list, x, 0, len(list)-1) 
     if result != -1: 
          print("Element is present at index", str(result)) 
     else: 
          print("Element is not present in array")
    
#merge_sorted_list=(merge_sort(list))
#print(merge_sorted_list)


#quicksortedlist=quicksort1(shuffled_list)

#heap sort#######################USE THIS SECTION TO CALL HEAPSORT########################################################
#heap_sorted_list=[]

#heapSort(shuffled_list) 
#n = len(shuffled_list) 
#for i in range(n): 
#	heap_sorted_list.append(shuffled_list[i]),

#print(heap_sorted_list)
##########################################################################################################################




#####################################################Quick sort##########################################################
#quick_sorted_list=(quicksort1(shuffled_list))

##########################################################################################################################




#####################################################merge_sort###########################################################
merge_sorted_list=(merge_sort(shuffled_list))

##########################################################################################################################



#####################################USE THIS SECTION TO CALL ---Binary Search---########################################
print(merge_sorted_list)
print(binary_search(merge_sorted_list, 7))


##################################USE THIS SECTION TO CALL Recursive Binary Search #######################################
#call_rbs(quicksortedlist, 54)



#call_rbs(merge_sorted_list,7)
    
##########################################################################################################################


num_to_search=("")


#call_rbs(merge_sorted_list,7)
    

#binary_search(merge_sorted_list, num_to_search)











