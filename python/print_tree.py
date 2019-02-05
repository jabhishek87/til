
li_ = [1,2,3,4,5,6,7,8]

def chunks(my_list, n):
    return [
        my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )
]

def print_tree(list_, level=0):
    #print('#'+str(level))
    for k,v in enumerate(list_):
        if isinstance(v, list):
            print_tree(v, level=k)
        else:
            print('\t'*level + str(v))
#import pdb; pdb.set_trace()
mylist = chunks(li_, 3)
print_tree(mylist)