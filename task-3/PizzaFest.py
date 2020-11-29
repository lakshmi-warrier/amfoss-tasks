# Points - 38.10
lst = input().split(" ")
house_pos = input().split(' ')
order_from  = input().split(' ')
answer = [" "]*int(lst[1])


def get_indices(n, lst):
    pos=[]

    ind=0
    for house in lst:
        if house==n:
            pos.append(ind)
        ind += 1
    return pos

for order_num in range(len(order_from)):
    
    if order_from[order_num] not in house_pos:
        #rint("length answr", len(answer), "order_num", order_num)
        answer[order_num] = -1
        print(-1, end=" ")
    else:
        val = get_indices(order_from[order_num], house_pos)
        print(val[-1]+1, end=" ")
        house_pos[val[-1]] = 0
