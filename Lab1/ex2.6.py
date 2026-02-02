import timeit



def pow2(number):
    return (2**number)

def pow2_for_loop():
    output = []
    for i in range(1001):
        output.append(pow2(i))
    return output

def pow2_list():
    return[pow2(n) for n in range(1001)]



t1 = timeit.timeit(lambda:pow2(10000), number = 10000)
print(f"Time for 10000 calls of pow2(10000): {t1} seconds")
    
t_for = timeit.timeit(pow2_for_loop, number=1000)
print(f"Time for 1000 runs (for-loop up to 1000): {t_for} seconds")

t_lc = timeit.timeit(pow2_list, number=1000)
print(f"Time for 1000 runs (list-comp up to 1000): {t_lc} seconds")