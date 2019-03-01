statement = input().split()
statement.sort()
A = set(statement)
for i in A:
        if(statement.count(i) > 1):
            print(i, statement.count(i))
        else:
            print(i)