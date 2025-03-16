# for 循环迭代
def for_loop(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

# while循环迭代
def while_loop(n: int) -> int:
    res = 0
    i = 0
    while i <= n:
        res += i
        i += 1
    return res

def while_loop_ii(n: int) -> int:
    res = 0
    i = 0
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res

if __name__ == "__main__":
    n = 5
    res = for_loop(n)
    print(f"\nfor 循环的求和结果 res = {res}")
