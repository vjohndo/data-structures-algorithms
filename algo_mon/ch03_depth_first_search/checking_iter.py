s = 'a b c d e'
s_iter = iter(s.split())
# print(next(s_iter))

# Iter is an option
def nexterise(s_iter):
    return next(s_iter)

for i in range(3):
    print(nexterise(s_iter))


#

def test():
    val = 0

    def recur():
        nonlocal val
        if val > 10:
            return
        else: 
            val += 1
            print(val)
            recur()
    
    recur()

test()