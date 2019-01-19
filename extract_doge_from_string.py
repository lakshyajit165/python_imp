str = input()
count_ = 0
for i in range(97,123):
    s = "do"+chr(i)+"e"
    if(s in str):
        count_ += str.count(s)
print(count_)