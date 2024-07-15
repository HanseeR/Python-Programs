def root(x,n=2):
    return(x**(1/n))
x=int(input("Enter 'x' value : "))
n=int(input("Enter 'n' value : "))
ans1=root(x,n)
ans2=root(x)
print("Root value with n value : ",ans1)
print("Root value without n value (Default 2) : ",ans2)