'''
This program implements print_nums(n) function from 1 through n.
'''
print('-'*20)

def print_nums(n):
    assert n >= 0
    temp = n
    if n <= 1: 
        print(n, end='')
        return n+1
    
    else:
        print(',',print_nums(n-1), end='')
        return n+1



#------------Alternative Implementaion-----------------------------
# count = 1  
# def print_nums(n):
#     global count
#     if count <= n:
#         print(count)
#         count += 1
#         print_nums(n)
#     return
# #_____________________________________    



a = print_nums(5)
print('\n a:', a)