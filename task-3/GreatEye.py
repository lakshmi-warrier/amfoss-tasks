trials = int(input())

for i in range(trials):
    req = int(input())
    sentence = input()
    sent_list = sentence.split(" ")
    if req >= len(sent_list):
        print(-1)
    else:
        reqword = sent_list[req]
        asciival = 0
        for letter in reqword:
            asciival += ord(letter)
        print(asciival)
