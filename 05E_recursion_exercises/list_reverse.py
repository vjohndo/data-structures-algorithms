def list_revserse(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        return a_list[-1:-2:-1] + list_revserse(a_list[0:-1])

print(list_revserse([5,4,3,2,1]))