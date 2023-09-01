age=int(input("enter the age"))
re=age>=18
out="can vote"*re+"can't vote"*(1-re)
print(out)
