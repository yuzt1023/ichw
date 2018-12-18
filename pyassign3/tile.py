'''__author__ = "Yuzhongtian"

__pkuid__  = "1800011813"

__email__  = "1800011813@pku.edu.cn"'''





def judge(list0, o, a, b, m):#建立一个判断函数

    wall = 0

    wall1 = 0

    for y in range(a):

        for x in range(b):

            i = o + x + m*y#纵向判断

            if i in list0:

                wall = wall + 1
    for y in range(a):

        for x in range(b):

            i = o + y + m*x#横向判断

            if i in list0:

                wall1 = wall1 + 1

    if wall == a*b and wall1 == a*b and o % m + max(a, b) <= m and a != b:

        return 1

    elif wall == a*b and (wall1 != a*b or o % m + a > m or a == b):

        return 2

    elif wall1 == a*b and (wall != a*b or o % m + b > m):

        return 3                                                                       #这里通过给出三种返回值来区分不同的可铺方法

    else:

        return False#此种情况则不能铺开（砖块比墙面大）

def formation(m, n):        #定义一个用来表达墙面的函数

    list0 = []

    for i in range(m*n):

        list0.append(i)

    return list0 #通过这里的操作可以生成整面墙（根据用户的输入值）

def tile(m, n, a, b, lst):#定义一个用铺砖的函数

    import copy#主要思路是每次·遇到转折点就拷贝列表并分为两部分以表达两种可能性

    list_out = []

    if lst == []:

        return []

    wallcover = min(lst)

    if judge(lst, wallcover, a, b, m) = False:

        return []
    if judge(lst, wallcover, a, b, m) == 1:#这里开始通过第一个模块三种不同的判定结果来利用三种不同的策略，使用递归的手段

        part = []

        part1 = []

        q_lst = []

        lstt = copy.copy(lst)

        for y in range(a):

            for x in range(b):

                i = wallcover + x + m*y

                lstt.remove(i)

                q_lst.append(i)

        temp = tile(m, n, a, b, lstt)

        if temp == []:

            part = part + [tuple(tem_lst)]

        else:

            for i in temp:

                if type(i) == list:

                    part.append([tuple(tem_lst)] + i)

                else:

                    part = part + [tuple(tem_lst)] + temp

                    break

        for i in part:

            if type(i) == list:

                list_out.append(i)

            else:

                list_out.append(part)

                break

        q_lst1 = []

        lstt1 = copy.copy(lst)

        for y in range(a):

            for x in range(b):

                i = wallcover + y + m*x

                q_lst1.append(i)

                lstt1.remove(i)

        temp1 = tile(m, n, a, b, lstt1)

        if temp1 == []:

            part1 = part1 + [tuple(tem_lst1)]

        else:

            for ii in temp1:

                if type(ii) == list:

                    part1.append([tuple(tem_lst1)] + ii)

                else:

                    part1 = part1 + [tuple(tem_lst1)] + temp1

                    break

        for i in part1:

            if type(i) == list:

                list_out.append(i)

            else:

                list_out.append(part1)

                break



    elif judge(lst, wallcover, a, b, m) == 2:#第二种返回结果对应的策略

        tem_lst = []

        lstt = copy.copy(lst)

        for y in range(a):

            for x in range(b):

                i = wallcover + x + m*y

                tem_lst.append(i)

                lstt.remove(i)

        temp = tile(m, n, a, b, lstt)

        if temp == []:

            list_out = list_out + [tuple(tem_lst)]

        else:

            for i in temp:

                if type(i) == list:

                    list_out.append([tuple(tem_lst)] + i)

                else:

                    list_out = list_out + [tuple(tem_lst)] + temp

                    break



    elif judge(lst, wallcover, a, b, m) == 3:#第三种返回结果对应的策略

        lstt = copy.copy(lst)

        tem_lst = []

        for y in range(a):

            for x in range(b):

                i = wallcover + y + m*x

                tem_lst.append(i)

                lstt.remove(i)

        temp = tile(m, n, a, b, lstt)

        if temp == []:

            list_out = list_out + [tuple(tem_lst)]

        else:

            for i in temp:

                if type(i) == list:

                    list_out.append([tuple(tem_lst)] + i)

                else:

                    list_out = list_out + [tuple(tem_lst)] + temp

                    break

    return list_out

def wall(m, n):

    import turtle#这一部分用turtle把铺砖的结果以可视化的方式呈现出来''

    t = turtle.Pen()

    t.speed(0)

    for i in range(m*n):

        t.penup()

        t.goto(50*(i//m), 50*(i % m))

        t.pendown()

        for a in range(4):

            t.forward(50)

            t.left(90)

        t.penup()

        t.goto(50*(i//m) + 25, 50*(i % m) + 25)

        t.pendown()

        t.write(str(i), False, "left", ("Arial", 8, "normal"))

def viewing(m, a, b, lst):#开始进行可视化

    import turtle

    t1 = turtle.Pen()

    t1.speed(0)

    t1.pencolor('red')

    t1.pensize(3)

    for i in lst:

        x = min(i)

        y = max(i)

        t1.penup()

        t1.goto(50*(x//m), 50*(x % m))

        t1.pendown()

        if y == x + (a - 1) + (b - 1)*m:

            for i in [1, 2]:

                t1.fd(50*b)

                t1.left(90)

                t1.fd(50*a)

                t1.left(90)

        else:

            for i in [1, 2]:

                t1.fd(50*a)

                t1.left(90)

                t1.fd(50*b)

                t1.left(90)

def main():#给出最终程序的结果

    m = int(input('m='))

    n = int(input('n='))

    a = int(input('a='))

    b = int(input('b='))

    lst = formation(m, n)

    result = tile(m, n, a, b, lst)

    result1 = []

    if type(result[0]) == tuple:

        print('共有1种答案')

        result1.append(result)

        print('1: ' + str(result))

    else:

        for i in range((len(result))):

            if len(result[i]) == m*n/(a*b):

                result1.append(result[i])

        print('共有' + str(len(result1)) + '种答案')

        for i in range((len(result1))):

            print(str(i+1) + ': ' + str(result1[i]))

    if len(result1) != 0:

        wall(m, n)

        kind = input('要可视化的种类：')

        lst0 = result1[(int(kind) - 1)]

        sight(m, a, b, lst0)





if __name__ == '__main__':

    main()
