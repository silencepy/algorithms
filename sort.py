#插排
def insert_sort(sort_list):
    for i in range(1,len(sort_list)):
        key=sort_list[i]
        while key<sort_list[i-1] and i-1>=0:
            sort_list[i]=sort_list[i-1]
            i=i-1
        sort_list[i]=key
    return sort_list