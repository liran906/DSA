# 第一次尝试（不成功）
def seek_pi(init, size):
    if init % 2 == 0: # 由于给的数据文件，每一个数据节点为两位数，所以要先判断奇偶性
        start = int(init / 2)
        odd = False
    else:
        start = (init - 1) / 2
        odd = True

    with open('pi50.4.bin', 'rb') as f:
        if odd: # 奇数情况，由于上面减 1，所以这里要加 1，又由于第几位从 1 开始（而非 0）所以这里再减 1，最后不加不减
            f.seek(start)
        else: # 偶数情况，同上，所以要减 1
            f.seek(start - 1)
        d = f.read(int(size/2) + 1) # 因为一次为两位，开头多读取一位，最后要加一位才能满足要求的 size
        output = ''
        for a in d:
            output += hex(a)[2:4] # 只需要读取后面两位有效数据
    print(output[1:])


# 第二次尝试（成功）
def seek_pi(init, size):

    # 因为输入是BCD码，数据一次包含两个有效数字，所以需要的其实位置和长度都需要除以 2
    start = int(init / 2)
    lenth = int(size / 2)

    with open('pi50.4.bin', 'rb') as f:

        # 要判断奇偶，计算机从 0 开始计数，所以偶数情况要 -1，奇数情况则不变
        if init % 2 == 0:
            f.seek(start - 1)
        else:
            f.seek(start)
        
        # 奇数长度，要多读取一个数据（两个有效数字），后面再删除最后一位；偶数长度则不用管
        if size % 2 == 0:
            txt = f.read(lenth)
        else:
            txt = f.read(lenth + 1)

        output = ''
        for i in txt:
            i = f"{i:02x}" # 这里要格式化一下输出数字：取'0x'之后有效的的数字，不足两位的，前面补‘0’，比如 0x4 格式化为 04
            output += i
        
        if size % 2 == 0:
            print(output)
        else:
            print(output[1:])

# 下面是简化表达的版本，原理一样：
def seek_pi(init, size):
    start, lenth = int(init / 2), int(size / 2)

    with open('pi50.4.bin', 'rb') as f:
        f.seek(start - 1 if init % 2 == 0 else start)
        txt = f.read(lenth if size % 2 == 0 else lenth + 1)
        output = ''.join(f"{i:02x}" for i in txt)
        print(output if size % 2 == 0 else output[1:])

seek_pi(20210316, 25)
seek_pi(20200101, 10)