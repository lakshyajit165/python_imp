s = "<html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html>"
A = s.split('src=\'')
print(A[1].split('\'')[0])