trials = int(input())
for i in range(trials):
    line = input().split(" ")
    if line[len(line)-1] == '':
        line = line[:len(line)-1 ]

    bag_num = int(line[0])
    minus_coins = int(line[1])
    bag_lst = input().split(" ")

    if bag_lst[len(bag_lst)-1] == '':
        bag_lst = bag_lst[:len(bag_lst)-1 ]
    
    bag_lst = [int(i) for i in bag_lst] #converting to int list
    bag_lst.sort()
    bag_lst[bag_num-1] = bag_lst[bag_num-1] - minus_coins
    prod = 1
    for each_bag in bag_lst:
        prod *= each_bag
    print(prod)
    
