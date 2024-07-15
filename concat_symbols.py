# In algebric expressions , the symbol for multiplication is often left out , as in 3X+4y or 3(x+5). Computers prefer
# those expressions to include the multiplication symbol , like 3*x+4*y or 3*(x+5). Write a program that asks the user
# for an algebric expression and then inserts multiplication synbols where appropriate.

lexpre = input("Enter algebraic expression: ")

l = list(lexpre)
result = ""

i = 0
while i < len(l):
    if l[i] == '(':
        index = l.index(')', i)
        s2 = "".join(l[i:index+1])
        result = result + '*' + s2 if result else s2  # Avoid leading '*'
        i = index + 1
    elif l[i].isalpha():
        result = result + '*' + l[i] if result else l[i]  # Avoid leading '*'
        i += 1
    else:
        result = result + l[i]
        i += 1

print(result)









