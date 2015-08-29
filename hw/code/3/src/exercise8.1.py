def has_duplicates(lst):
    newlst=[]
    for item in lst:
        for newitem in newlst:
            if item==newitem:
                return True
        newlst.append(item)
    return False

print has_duplicates([1,'d',3,'2','sa',2])

print has_duplicates([1,'d',3,'2','sa','2'])