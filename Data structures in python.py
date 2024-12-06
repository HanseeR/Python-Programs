# l = [10,20,30,40,50]

# print(l)
# print(l[3])
# print(l[-1])
# print(l[-2])

# l = [10,20,30,40,50]

# l.append(30)
# print(l)
# l.insert(1,15)
# print(l)
# print(15 in l)
# print(l.count(30))
# print(l.index(30))
# print(l.index(30,4,7))

# l = [10,20,30,40,50,60,70,80]

# l.remove(20)
# print(l)
# print(l.pop(1))
# print(l)
# print(l.pop(2))
# print(l)
# del l[1]
# print(l)
# del l[0:2]
# print(l)

# l = [10,40,20,50]
# print(max(l))
# print(min(l))
# print(sum(l))
# l.reverse()
# print(l)
# l.sort()
# print(l)
# # max,min,sum,sort willnot wirk if one ekement is string 
# But if the elements are in the form of the stings only then the max, min, sort will give uis the lexographically texts.

# tuples in python 

# Immutable and faster than list 

# t = (10,20,"geek")
# print(t)
# t = ()
# print(type(t))
# print(t)
# t = (10)
# print(type(t))
# t = (10,)
# print(type(t))

# t = 10,20,30,40,10
# print(t[2])
# print(t[-1])
# print(t[1:3])
# print(len(t))
# print(t.count(10))
# print(t.index(20))


# Set in Python 

'''
1. Distinct elements 
2. Unordered
3. No indexing 
4. Union , Intersection , set difference etc are fast 
5. User hashing internally 
'''

# s1 = {10,20,30}
# print(s1)

# s2 = set([20,30,40])
# print(s2)

# s3 = { }
# print(type(s3))

# s4 = set()
# print(type(s4))
# print(s4)


# Insertion in a set 

# s = {10,20}
# s.add(30)
# print(s)
# s.add(30)
# print(s)
# s.update([40,50])
# print(s)
# s.update({60,70},{80,30})
# print(s)

#An example python program 
#for set insertions

# s = {10,30,20,40}
# s.discard(30)
# print(s)
# s.remove(20)
# print(s)
# s.clear()
# print(s)
# s.add(50)
# del s 
# # With del statement whole object is removed
# s = {10,30,20,40}
# print(len(s))
# print(20 in s)
# print(50 in s)

# # Other operations

# s1 = {2,4,6,8}
# s2 = {3,6,9}

# print(s1 | s2)

# print(s1 & s2)

# print(s1 - s2)


# # OPERATIONS on two sets (Part 1)

# # print(s1 ∩ s2 )

# s1.differemce(s2)
# s1 = {2,4,6,8}

# s2 = {4,8}

print(s1.isdisjoint(s2))

print(s1<=s2)
print(s1<s2)
print(s1>=s2)
print(s1>s2)















































