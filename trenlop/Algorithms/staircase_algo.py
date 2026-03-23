## You are climbing a staircase with n steps. You can step 1 or 2 steps at 1 time.
def staircase_ways_2steps(n: int):
    if n == 1: return 1
    elif n == 2: return 2
    else: return staircase_ways_2steps(n - 2) + staircase_ways_2steps(n - 1)

print(staircase_ways_2steps(4))

## You are climbing a staircase with n steps. You can step 1, 2 or 3 steps at a time. With dynamic programming 
#* Dynamic programming is a process where you integrate memory to reduce redundancy from recursive algorithms 
def staircase_ways_3steps(n: int):
    mem = dict()
    mem[1] = 1
    mem[2] = 2
    mem[3] = 4

    ## formula
    if n not in mem.keys():
        mem[n - 3] = staircase_ways_3steps(n - 3)
        mem[n - 2] = staircase_ways_3steps(n - 2)
        mem[n - 1] = staircase_ways_3steps(n - 1)
        return mem[n - 3] + mem[n - 2] + mem[n - 1]
    elif n in mem.keys():
        return mem[n]
    
print(staircase_ways_3steps(6))