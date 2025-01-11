import big_o
from timeit import Timer

def insert_0(lst):
    lst.insert(0, 0)

def append_0(lst):
    lst.append(0)

# timeit 包失败尝试
for i in range(10000, 100001, 10000):
    lst_0 = list(range(i))
    t2 = Timer(f'append_0({lst_0})', 'from __main__ import append_0, lst_0') # 就是这个 f-string 造成的
    append_time = t2.timeit(number=1000)
    print(f'WRONG append time({i}): {append_time:.5f} seconds.')
# Timer(f'append_0({lst_0})', 'from __main__ import append_0, lst_0') 中，lst_0 是在 f-string 里直接传递的，
# 导致 Timer 每次都重新构建 lst_0 列表。这相当于每次测试时都创建了一个新列表，# 再将其传入 append_0() 函数，这带来了
# 额外的开销，而这些开销随列表规模增加而变大，干扰了 append 的性能测量，使得它看起来像是线性复杂度。

# 用 timeit 包
print('---timeit: insert---')
for i in range(10000, 100001, 10000):
    lst_0 = list(range(i))
    t1 = Timer('insert_0(lst_0)', 'from __main__ import insert_0, lst_0')
    insert_time = t1.timeit(number=1000)
    print(f'insert time({i}): {insert_time:.5f} seconds.')

print('---timeit: append---')
for i in range(10000, 100001, 10000):
    lst_0 = list(range(i))
    t2 = Timer('append_0(lst_0)', 'from __main__ import append_0, lst_0')
    append_time = t2.timeit(number=1000)
    print(f'append time({i}): {append_time:.5f} seconds.')


# 用 big_o 包
insert_best, insert_other = big_o.big_o(
    insert_0, # 要估算大O的目标函数，不加括号，可以自己写好再索引进来
    lambda n: big_o.datagen.range_n(n), # 目标函数的参数（本身也是一个函数）；这里的lambda n: big_o.datagen.range_n(n)和外面的range(n)一样
    min_n=10000, # 上面参数函数的 n 的最小值。比如取10000，则代表上面的函数最小是 range_n(10000)
    max_n=100000, # 上面参数函数的 n 的最大值。比如取100000，则代表上面的函数最大是 range_n(100000)
    n_measures=10, # 上面的最大值和最小值之间，有几个n的取值。比如这里写 10，那就是从 10000 到 100000，一共 10个 n 的取值，也就是步长为 10000
    n_repeats=1000 # 重复次数
)

append_best, append_other = big_o.big_o(
    append_0,
    lambda n: big_o.datagen.range_n(n),
    min_n=10000,
    max_n=100000,
    n_measures=10,
    n_repeats=1000
)

print('---big_o: insert---')
print(insert_best)
print('---big_o: append---')
print(append_best)