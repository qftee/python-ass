#test = []
with open('temporary.txt','r') as read:
    for line in read:
        test = line.strip().split(',')
        #print(line)
        #test.append(line)
        #print(test)
        for b in range(len(test)):
            print(test[b])