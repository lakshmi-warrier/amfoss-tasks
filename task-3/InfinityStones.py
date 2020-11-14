trials  = int(input())

for i in range(trials):
    line = input().split(" ")

    stones = int(line[0])
    boxes =int(line[1])
    protect = int(line[2])
    
    curr = input()
    max_cap = input().split(" ")
    max_cap = [int(i) for i in max_cap]
    
    stat = "NO"
    
    box_num = 0

    for box in max_cap:
        stones -= box
        box_num += 1
        if(stones<=0 and box_num<=protect):
            stat = "YES"
            break
    
    print(stat)
