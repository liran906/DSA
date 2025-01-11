# lst = eval(input())
# lstinput = [1,2,2]
# lst = lstinput.append(-1)
# lst = lstinput.insert(0, -1)
# candy = lst[1:-1]

# lst = [1,2,3,3]

# lst.append(-1)
# lst.insert(0, -1)
# candy = lst[:]
# candy[0] = 0
# candy[-1] = 0

# def minimize(rate):
#     for i,item in enumerate(lst):
#         if item == rate:
#             if lst[i] < lst[i - 1]:
#                 if lst[i] <= lst[i + 1]:
#                     candy[i] = 1
#                 else:
#                     candy[i] = candy[i + 1] + 1
#             elif lst[i] == lst[i - 1]:
#                 if lst[i] <= lst[i + 1]:
#                     candy[i] = 1
#                 else:
#                     candy[i] = candy[i + 1] + 1
#             else:
#                 if lst[i] <= lst[i + 1]:
#                     candy[i] = candy[i - 1] + 1
#                 else:
#                     candy[i] = max(candy[i - 1], candy[i + 1]) + 1

# for n in range(max(lst)):
#     minimize(n)
# sum = 0
# for i in candy:
#     sum += i
# print(sum)

lst = [1,2,2,2,3,4]
candy=[1] * len(lst)

# 从左向右
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        candy[i] = candy[i - 1] + 1

# 从右向左
for i in reversed(range(len(lst) - 1)):
    if lst[i] > lst[i + 1]:
        candy[i] = max(candy[i], candy[i + 1] + 1) # 这里考虑从右向左遍历时，把按从左向右遍历的结果写低了

# 输出结果
print('rate :', lst)
print('candy:', candy)
sum = 0
for i in candy:
    sum += i
print('total:', sum)