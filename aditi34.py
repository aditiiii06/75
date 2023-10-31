from collections import Counter
dict1={'A':78,'B':89,'C':23,'D':67,'E':35,'F':74,'G':90}
print(dict1)
k=Counter(dict1)
highest=k.most_common(3)

for i in highest:
    print(i[0],":",i[1],)