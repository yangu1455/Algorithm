# 2941번 크로아티아 알파벳

sentence = input("") 
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 

for i in croatia: 
    while(True): 
        if i in sentence: 
            start = sentence.find(i) 
            sentence = sentence.replace(sentence[start:start+len(i)], 'q') 
        else: 
            break 

print(len(sentence))