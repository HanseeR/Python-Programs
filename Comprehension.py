# l1 = [x for x in range(11) if x % 2 == 0]

# l2 = [x for x in range(11) if x % 2 != 0]

# print(l1)

# print(l2)

# l1 = []

# for x in range(11):

#  if x%2 == 0:
#     l1.append(x)
    
# l2 = []

# for x in range(11):
#     if x %2 != 0:
#         l2.append(x) 



        # Function to get list that contains
        # all that items if l that are smaller than x 
        
# def getSmaller(l, x):
#     return [e for e in l if e < x]

# l = [9, 10, 12, 3, 7, 11]
# x = 10
# print(getSmaller(l, x))
#  Return two lists , the first list contains 
# all even elements of l , and seconds contains odd 
    
# def getEvenOdd(l):
#     even = [x for x in l if x%2 == 0]
#     odd =  [x for x in l if x%2 != 0]
#     return even,odd

# l = [10,2,20,5,12,22.6,0,84948]
# even,odd = getEvenOdd(l)
# print(even)
# print(odd)
        
# s = "geeksforgeeks"
# l1 = [x for x in s if x in "aeiou"]

# print(l1)

# l2 = ["geeks","ide","courses","gfg"]
# l3 = [x for x in l2 if x.startswith("g")]   

# print(l3)
# l4 = [x*2 for x in range(6)]
# # print(l4)
        
# l1 = ["geeks","for","gfg","ide"]     
# l2 = [x.upper() for x in l1 if x.startswith("g")]

# l = [10,25,3,4,10,20,7,3]
# s1 = [x for x in l if x%2 == 0]
# s2 = [x for x in l if x%2 != 0]
# print(s1)
# print(s2)        
        
# Dictionary comprehension 

# l1 = [1,3,4,2,5]
# d1 = {x:x**3 for x in l1}
# print(d1)

# d2 = {x:f"ID[x]" for x in range(5)}
# print(d2)

# l2 = [101,103,102]
# l3 = ["gfg","ide","courses"]
# d3 = {l2[i]:l3[i] for i in range (len(l2))} 
        
    # Note : Collection of mapping is the collection of the tuples   

        
d1 = {101:"gfg",103:"practice",102:"ide"}
d2 = {v:k for(k,v) in d1.items()}
print(d2)    
        
# d1 = {101: "gfg", 103: "practice", 102: "ide"}
# d2 = {v: k for (k, v) in d1.items()}  # Corrected usage of d1.items()
# print(d2)

        
        
        
        
        