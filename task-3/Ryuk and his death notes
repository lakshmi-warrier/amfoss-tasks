"""reqlist = []*int(input())
availablelist = []*len(reqlist)"""

listsize = int(input())

reqlist = input().split(" ")
availablelist = input().split(" ")

reqlist = [ int(i) for i in reqlist]

availablelist = [int(i) for i in availablelist]

possiblelist = []

for i in range(listsize):
    possiblelist.append(int(availablelist[i] / reqlist[i]))

print(min(possiblelist))
