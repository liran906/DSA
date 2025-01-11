# 第一题

# 先用遍历写一个算法
def find_date(date, size = 500000):

    find_len = len(date) + 1 # find_len 就是查找数据的长度，用于数据切分时候的冗余覆盖
    index = 0 # 指针

    while True:
        with open('pi50.4.bin', 'rb') as f:
            f.seek(index)
            d = f.read(size) # 十六进制内容
            content = '' # 圆周率str，十进制
            if d: # 确保有内容
                index += size - find_len
            else:
                break
            for i in d:
                var = f"{i:02x}" # 这里要格式化一下输出数字：取'0x'之后有效的的数字，不足两位的，前面补‘0’，比如 0x4 格式化为 04
                content += var # 全部写入 content 变量中
    pass
# 写到这里我觉得有更好的方法：指针往前移动的时候，同步检查是否符合，每次检查两个字符（符合给定的数据格式）

# 用上面提到的思路
# 改为一次读取 2 个数据（4 位数字）
def find_date(date):
    print('Starting to find', date, '...')
    index = 0
    str_date = str(date)
    date_list = [str_date[2 * i : 2 * i + 2] for i in range(len(str_date)) if i < len(str_date) / 2]
    # 把 date 拆分为 2 个字符为一个元素的 list

    with open('pi50.4.bin', 'rb') as f:
        small_index = 0
        d = f.read(1)
        while d:
            num = int.from_bytes(d, byteorder='big')  # 为了把 byte 格式转换为 int。也可以用 for 循环实现
            d_format = f"{num:02x}"
            if d_format == date_list[small_index]:
                if small_index == len(date_list) - 1: # len(date_list) 从 1 开始，small_index 从 0 开始，所以要 -1
                    index_found = index - small_index # 找到的第一位角标
                    print('FOUND, index starting at', index_found)

                    # 下面这几行都是为了输出结果，与逻辑无关
                    f.seek(index_found)
                    outcome = f.read(small_index + 1)
                    for _, i in enumerate(outcome):
                        print('Index:', index_found + _, 'Value:', hex(i))
                    
                    return
                else:
                    small_index += 1 # 还没有全对，则small_index + 1，继续
            else:
                # 出现错误了，则small_index清零，继续
                if small_index != 0 :
                    small_index = 0
            d = f.read(1)
            index += 1
            # if index % 5000000 == 0: # 类似进度条，与逻辑无关
            #     print('gone through', int(index/500000), 'million data, still finding...')
        print('NOT FOUND') # 穷尽d了，那就not found啦

# 修好了上面的漏洞，顺便完善了逻辑
def find_date(date_input, detail = True):
    if type(date_input) != int:
        print('Type in correctly')
        return
    
    if detail:
        print(f'Starting to find {date_input} in data...')
    date_str = str(date_input)
    date_len = len(date_str) if date_input % 2 == 0 else len(date_str) + 1
    mark_lst = []
    
    with open('pi50.4.bin', 'rb') as f:
        index = 0
        d_n = f.read(int(date_len / 2 + 1)) # 这里要多一位，读取 5 个数据，10 个数字，这样才能保证 1:9 的情况可读取
        while d_n:
            d_read = ''.join(f"{_:02x}" for _ in d_n)[:-1] # 去掉最后一位防止读取 10 个数字时候直接匹配了 2:10
            if date_str in d_read:
                mark_lst.append(index)
                # 下面为展示代码，与逻辑无关：
                print(f'FOUND, index starting at {index}')
                if detail:
                    for _ in range(int(date_len / 2) if date_str in d_read[:-1] else int(date_len / 2) + 1): # 验算，if 为了避免 0:8 时多输出一行
                        find_index(index + _, 1)
            index += 1
            f.seek(index)
            d_n = f.read(int(date_len / 2 + 1))
            if index % 5000000 == 0 and detail: # 类似进度条，与逻辑无关
                print('gone through', int(index/500000), 'million data, still finding...')
        if detail:
            print('NOT FOUND' if len(mark_lst) == 0 else f'COMPLETE, FOUND {len(mark_lst)} RESULTS.') # 穷尽d了，那就not found啦
        return mark_lst


# 第二题

import datetime
import calendar

def find_dates_in_year(year_input):
    if type(year_input) != int or len(str(year_input)) != 4: # 要求是四位数阿拉伯数字年份格式输入
        print('Type in correctly')
        return


    # 初始变量
    start_time = datetime.datetime.now()
    days_in_year = 366 if calendar.isleap(year_input) else 365 # 判断是否闰年并统计这一年多少天
    init_dct_key = [str(year_input)+f"{(_+1):02}" for _ in range(12)] # dict 的 key 值：年份+月份，一共 12 个值（str格式）
    final_dct_key = [(datetime.datetime(year_input,1,1) + datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(days_in_year)]
    # 最终 dict的key：年+月+日
    init_dct = {key:[] for key in init_dct_key} # 初始 dict，key 是年+月，value 是 index 值
    final_dct = {key:[] for key in final_dct_key} # 最终 dict，key 是年月日，value 是 index 值


    print(f'Starting to find dates of {year_input} in data...')
    with open('pi50.4.bin', 'rb') as f:
        index = 0
        d4 = f.read(4) # 以八位数为一个单位，后面检测八位数中是否含有“年份+月份”
        while d4:
            small_index = 0 # 小指针，指向年份+月份的第一位数字，在八位数中的前三位游走
            d4_read = ''.join(f"{_:02x}" for _ in d4) # 读取的八位数的数值
            for small_index in [0, 1]:
                for month_index, month_str in enumerate(init_dct_key): # 遍历，每两个数字24次，5000 万数据 = 6 亿次计算
                    if d4_read[small_index:small_index+6] == month_str:
                        input_index = index * 2 + small_index # 存储为实际 index 的双倍（为了保证整数）
                        init_dct[str(year_input)+f"{(month_index + 1):02}"].append(input_index) # 符合的就写入 init_dct 对应月份的 value 中
            index += 1 # 两位数结束，指针向前一位
            f.seek(index)
            d4 = f.read(4)

            if index % 5000000 == 0:
                print(f'Preliminarily processed through {index / 500000} million data...Spent {(datetime.datetime.now() - start_time).total_seconds():.2f} seconds.') # 每五百万数据提示下进度
        pp_time = datetime.datetime.now() - start_time
        print(f'Preliminarily processed through all {index / 500000:.2f} million data, spent {pp_time.total_seconds():.2f} seconds. Now organizing...')

        # 现在有{年月份：index}的数据了，下面就是要遍历这些 index，将符合的放入 finaldct
        for v in init_dct.values():
            for v_month_index in v:
                f.seek(int(v_month_index / 2))
                if v_month_index % 2 == 1: # 开始于索引中第二位数字的情况
                    add_one = True
                    d5 = f.read(5)
                    d5_read = ''.join(f"{_:02x}" for _ in d5)[1:9]
                else:
                    add_one = False
                    d5 = f.read(4)
                    d5_read = ''.join(f"{_:02x}" for _ in d5)
                
                if d5_read in final_dct: # 写到这里发现 initdct 不需要用字典，用 list 也可。
                    final_dct[d5_read].append(v_month_index / 2 if not add_one else v_month_index / 2)
        og_time = datetime.datetime.now() - start_time
        print(f'Organizing complete, spent {og_time.total_seconds():.2f} seconds.')

    # 现在输出结果就行了
    valid_count = 0
    valid_lst = []
    unvalid_count = 0
    unvalid_lst = []
    for k, v in final_dct.items():
        if len(v) == 0:
            unvalid_count += 1
            unvalid_lst.append(k)
        else:
            valid_count += 1
            valid_lst.append(k)
    final_time = datetime.datetime.now() - start_time
    # 至此统计已经结束

    print(f'{valid_count} dates found and {unvalid_count} dates unfound of year {year_input} in data, spent {final_time.total_seconds():.2f} seconds')
    qu = input('View Details?  Y/N\n')
    if qu in ['Y','y']:
        print('----------------DETAILS----------------')
        print('Found dates:')
        for i in valid_lst:
            print('\nDate', i, end = ', index: ')
            for v in final_dct[i]:
                print(v, end = ', ')
        print('\n\nUnfound dates:')
        for i in unvalid_lst:
            print(i, end=', ')
    else:
        return

# 再写一个更加直接的函数(去掉先比较年月 再筛查具体日期的思路。直接比较年月日)
def find_dates_in_year_2(year_input):
    if type(year_input) != int or len(str(year_input)) != 4: # 要求是四位数阿拉伯数字年份格式输入
        print('Type in correctly')
        return

    # 初始变量
    start_time = datetime.datetime.now()
    days_in_year = 366 if calendar.isleap(year_input) else 365 # 判断是否闰年并统计这一年多少天
    final_dct_key = [(datetime.datetime(year_input,1,1) + datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(days_in_year)]
    # 最终 dict的key：年+月+日
    final_dct = {key:[] for key in final_dct_key} # 最终 dict，key 是年月日，value 是 index 值
    valid_count = 0
    valid_lst = []
    unvalid_count = 0
    unvalid_lst = []

    with open('pi50.4.bin', 'rb') as f:
        index = 0
        d_n = f.read(5) # 这里要多一位，读取 5 个数据，10 个数字，这样才能保证 1:9 的情况可读取
        while d_n:
            d_read = ''.join(f"{_:02x}" for _ in d_n)
            if d_read[:-2] in final_dct:
                final_dct[d_read[:-2]].append(index)
            elif d_read[1:-1] in final_dct:
                final_dct[d_read[1:-1]].append(index+0.5)
            index += 1
            f.seek(index)
            d_n = f.read(5)
            if index % 5000000 == 0:
                print(f'Processed through {index / 500000} million data...Spent {(datetime.datetime.now() - start_time).total_seconds():.2f} seconds.') # 每五百万数据提示下进度
        for key, value in final_dct.items():
            if value == []:
                unvalid_count += 1
                unvalid_lst.append(key)
            else:
                valid_count += 1
                valid_lst.append(key)
        pp_time = datetime.datetime.now() - start_time

        # 以下为输出，与逻辑无关
        print(f'Processed through all {index / 500000} million data, spent {pp_time.total_seconds():.2f} seconds.')
        print(f'{valid_count} dates found and {unvalid_count} dates unfound of year {year_input} in data.')
    qu = input('View Details?  Y/N\n')
    if qu in ['Y','y']:
        print('----------------DETAILS----------------')
        print(f'Found dates of {year_input}:')
        for i in valid_lst:
            print('\nDate', i[4:], end = ', index: ')
            for v in final_dct[i]:
                print(v, end = ', ')
        print(f'\n\nUnfound dates of {year_input}:')
        for i in unvalid_lst:
            print(i[4:], end=', ')
    else:
        return

# 根据 gpt 的建议，再写一个一次性读取所有数据的算法，减少 seek 和 read 这种耗时的 IO 操作
def find_dates_in_year_3(year_input):
    if type(year_input) != int or len(str(year_input)) != 4: # 要求是四位数阿拉伯数字年份格式输入
        print('Type in correctly')
        return

    # 初始变量
    start_time = datetime.datetime.now()
    days_in_year = 366 if calendar.isleap(year_input) else 365 # 判断是否闰年并统计这一年多少天
    final_dct_key = [(datetime.datetime(year_input,1,1) + datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(days_in_year)]
    # 最终 dict的key：年+月+日
    final_dct = {key:[] for key in final_dct_key} # 最终 dict，key 是年月日，value 是 index 值
    valid_count = 0
    valid_lst = []
    unvalid_count = 0
    unvalid_lst = []

    with open('pi50.4.bin', 'rb') as f:
        dataset = f.read()
    d_read = ''.join(f"{_:02x}" for _ in dataset)
    print(f'Dataset read, time spent{(datetime.datetime.now() - start_time).total_seconds():.2f} seconds')
    
    index = 0 # 这里的 index 比起前面两个方法，是他们的两倍。
    check = d_read[index : index + 8]
    while check:
        if check in final_dct:
            final_dct[check].append(index)
        index += 1
        check = d_read[index : index + 8]
        if index % 10000000 == 0:
            print(f'Processed through {index / 1000000} million data...Spent {(datetime.datetime.now() - start_time).total_seconds():.2f} seconds.') # 每五百万数据提示下进度
    
    for key, value in final_dct.items():
        if value == []:
            unvalid_count += 1
            unvalid_lst.append(key)
        else:
            valid_count += 1
            valid_lst.append(key)

    pp_time = datetime.datetime.now() - start_time
    # 以下为输出，与逻辑无关
    print(f'Processed through all {index / 500000} million data, spent {pp_time.total_seconds():.2f} seconds.')
    print(f'{valid_count} dates found and {unvalid_count} dates unfound of year {year_input} in data.')
    qu = input('View Details?  Y/N\n')
    if qu in ['Y','y']:
        print('----------------DETAILS----------------')
        print(f'Found dates of {year_input}:')
        for i in valid_lst:
            print('\nDate', i[4:], end = ', index: ')
            for v in final_dct[i]:
                print(v, end = ', ')
        print(f'\n\nUnfound dates of {year_input}:')
        for i in unvalid_lst:
            print(i[4:], end=', ')

# 按陈斌的算法，复刻一下
def find_dates_in_year_cb(year_input):
    if type(year_input) != int or len(str(year_input)) != 4: # 要求是四位数阿拉伯数字年份格式输入
        print('Type in correctly')
        return

    # 初始变量
    start_time = datetime.datetime.now()
    days_in_year = 366 if calendar.isleap(year_input) else 365 # 判断是否闰年并统计这一年多少天
    days = {
        ((datetime.datetime(year_input,1,1) + datetime.timedelta(days=i)).strftime('%m%d')).encode()
        for i in range(days_in_year)
        }

    with open('pi50.4.bin', 'rb') as f:
        dataset = f.read()
    d_read = ''.join(f"{_:02x}" for _ in dataset).encode()
    print(f'Dataset read, time spent{(datetime.datetime.now() - start_time).total_seconds():.4f} seconds')
    
    y = str(year_input).encode()
    found = 0
    idx = d_read.find(y)
    while idx >= 0:
        p_days = d_read[idx + 4 : idx + 8]
        if p_days in days:
            found += 1
            days.remove(p_days)
        idx = d_read.find(y, idx + 1)
    
    unfound = len(days)
    pp_time = datetime.datetime.now() - start_time

    print(f'found {found}, unfound {unfound}, spent{pp_time.total_seconds():.4f} seconds.')

# 用我的算法，再改一下，主要差距在于 find 方法
def find_dates_in_year_4(year_input):
    if type(year_input) != int or len(str(year_input)) != 4: # 要求是四位数阿拉伯数字年份格式输入
        print('Type in correctly')
        return

    # 初始变量
    start_time = datetime.datetime.now()
    days_in_year = 366 if calendar.isleap(year_input) else 365 # 判断是否闰年并统计这一年多少天
    final_dct_key = [(datetime.datetime(year_input,1,1) + datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(days_in_year)]
    # 最终 dict的key：年+月+日
    final_dct = {key:[] for key in final_dct_key} # 最终 dict，key 是年月日，value 是 index 值
    valid_count = 0
    valid_lst = []
    unvalid_count = 0
    unvalid_lst = []

    with open('pi50.4.bin', 'rb') as f:
        dataset = f.read()
    d_read = ''.join(f"{_:02x}" for _ in dataset)
    print(f'Dataset read, time spent{(datetime.datetime.now() - start_time).total_seconds():.2f} seconds')
    
    index = d_read.find(str(year_input))
    check = d_read[index : index + 8]
    while index >= 0:
        if check in final_dct:
            final_dct[check].append(index)
        index = d_read.find(str(year_input), index + 1)
        check = d_read[index : index + 8]
        # 这里不需要进度条了，因为 find 方法 index 不是连续增加的。这也是这个方法快的本质原因。

    for key, value in final_dct.items():
        if value == []:
            unvalid_count += 1
            unvalid_lst.append(key)
        else:
            valid_count += 1
            valid_lst.append(key)

    pp_time = datetime.datetime.now() - start_time
    # 以下为输出，与逻辑无关
    print(f'Processed through data, spent {pp_time.total_seconds():.2f} seconds.')
    print(f'{valid_count} dates found and {unvalid_count} dates unfound of year {year_input} in data.')
    qu = input('View Details?  Y/N\n')
    if qu in ['Y','y']:
        print('----------------DETAILS----------------')
        print(f'Found dates of {year_input}:')
        for i in valid_lst:
            print('\nDate', i[4:], end = ', index: ')
            for v in final_dct[i]:
                print(v, end = ', ')
        print(f'\n\nUnfound dates of {year_input}:')
        for i in unvalid_lst:
            print(i[4:], end=', ')

# 写个根据索引读取值的功能
def find_index(idx, lenth = 5):
    with open('pi50.4.bin', 'rb') as f:
        f.seek(int(idx))
        o = f.read(lenth)
        oo = ''.join(f"{_:02x}" for _ in o)
    print(f'INDEX: {idx} ---- LENTH: {lenth} ---- VALUE: {oo}')

# find_date(20220106)
# find_dates_in_year(2022) # 60s
# find_dates_in_year_2(2022) # 25s
# find_dates_in_year_3(2022) # 8s
# find_dates_in_year_cb(2022) # 3s
find_dates_in_year_4(2022) # 3s
# find_index(4304206)