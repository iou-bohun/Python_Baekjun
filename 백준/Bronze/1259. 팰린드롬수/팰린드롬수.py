while True:
    word = input()
    
    if word == "0":
        break
        
    lenght = len(word)
    stop = 0

    for i in range(lenght // 2):
        if stop == 1:
            break
        if word[i] != word[lenght-i-1]:
            print("no")
            stop = 1
            
    if stop == 1:
        continue
        
    print("yes")