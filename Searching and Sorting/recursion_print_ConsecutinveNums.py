'''
This program implements print_nums(n) function from 1 through n.
'''

print('-'*20)
def print_nums(N):
    assert N >= 0
    
    line_gap = True
    end = '\n' if line_gap else ""

    if N <= 1: 
        print(N, end=end)
    else:
        print_nums(N-1)
        print(' ',N, end=end)
        
    # print('\n')
    
        



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



#a =
print_nums(5)
#print('\n')
#print_nums(-4)
#print('\n a:', a)