from random import randint

def has_duplicates(lst):
    newlst=[]
    for item in lst:
        for newitem in newlst:
            if item==newitem:
                return True
        newlst.append(item)
    return False

def dup_stu(times):                #times is the number our experiments will be conducted
    count=0

    for test in range(0,times):
        students=[]

        for i in range(0,23):
            students.append(randint(1,365))

        if has_duplicates(students): count+=1

    return float(count)/times

print dup_stu(100000)