import datetime
#dt = '21/03/2012'
t = int(input())
while(t!=0):
    dt = input()
    day, month, year = (int(x) for x in dt.split(' '))
    ans = datetime.date(year, month, day)
    print(ans.strftime("%A"))
    t-=1