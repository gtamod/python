list1=[4,7,6,3,8,1]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_ind=list1.index(min_val)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]#or use temp
print(list1)
    
