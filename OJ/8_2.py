def topKFrequent(nums, k):
    freq = {}
    # 建立频率表
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # 按频率排序
    sortfreq = sorted(freq.items(), key= lambda x: (x[1], x[0]))

    # 输出
    out = [str(_[0]) for _ in sortfreq[-k:]]
    print(' '.join(out))

lst = eval(input())
k = int(input())
topKFrequent(lst, k)