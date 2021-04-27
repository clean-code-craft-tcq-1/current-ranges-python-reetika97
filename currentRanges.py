def count_min(lt):
    if(len(lt)!=0):
        return [min(lt),lt.count(min(lt))]
    else:
        return [-100,0]
    
def remove_min(lt):
    min_lt=lt.count(min(lt))
    for i in range(0,min_lt):
        lt.remove(min(lt))
    return lt

def def_range_count(lt):
    [min1,count]=count_min(lt)
    max1=min1;
    lt=remove_min(lt)
    [min_nxt,count1]=count_min(lt)
    while(min_nxt-max1==1):
        max1=min_nxt;
        lt=remove_min(lt)
        [min_nxt,count1]=count_min(lt)
        count=count+count1
    return [count,{min1:max1}]

def def_all_ranges(lt,range_count):
    if(len(lt)==0):
        print(range_count)
        return range_count
    else:
        
        range_count.append(def_range_count(lt))
        def_all_ranges(lt,range_count)
