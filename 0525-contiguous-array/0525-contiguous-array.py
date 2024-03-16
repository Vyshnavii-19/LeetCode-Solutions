sys.stdout = open('user.out', 'w')
for nums in map(loads, stdin):
    totalsum,hashmap=0,{0:-1}
    res,diff=0,0
    for i in range(len(nums)):
        if(nums[i]==0):
            totalsum-=1
        else:
            totalsum+=1
        try:
            diff=i-hashmap[totalsum]
            if(diff>res):
                res=diff
        except:
            hashmap[totalsum]=i
    print(res)