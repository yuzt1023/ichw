'''__author__ = "Yuzhongtian"
__pkuid__  = "1800011813"
__email__  = "1800011813@pku.edu.cn"'''


def judge(list0, o, a, b, m):
    wall = 0
    wall1 = 0
    for y in range(a):
        for x in range(b):
            i = o + x + m*y
            if i in list0:
                wall = wall + 1

    for y in range(a):
        for x in range(b):
            i = o + y + m*x
            if i in list0:
                wall1 = wall1 + 1
    if wall == a*b and tim1 == a*b and o % m + max(a, b) <= m and a != b:
        return 1
    elif wall == a*b and (wall1 != a*b or o % m + a > m or a == b):
        return 2
    elif wall1 == a*b and (wall != a*b or o % m + b > m):
        return 3
    else:
        return False
'''用作判断的代码部分
本部分可以用来评估用户输入信息中砖块和墙面的信息，
来判断瓷砖在该墙面上能不能铺开（是否比墙面小）
以及可以以什么养的方式铺开'''


def formation(m, n):
    list0 = []
    for i in range(m*n):
        list0.append(i)
    return list0
'''生成列表的部分
这一部分是为了把墙面以列表的形式表达出来'''


def tile(m, n, a, b, lst):
    import copy
    list_out = []
    if lst == []:
        return []
    wallcover = min(lst)
    if judge(lst, wallcover, a, b, m) is False:
        return []

    if judge(lst, wallcover, a, b, m) == 1:
        part = []
        part1 = []
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = wallcover + x + m*y
                lstt.remove(i)
                tem_lst.append(i)
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
        tem_lst1 = []
        lstt1 = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = wallcover + y + m*x
                tem_lst1.append(i)
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

    elif judge(lst, wallcover, a, b, m) == 2:
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

    elif judge(lst, wallcover, a, b, m) == 3:
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
'''这一部分用递归生成铺砖的结果并且呈现出来'''


def wall(m, n):
    import turtle
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
'''这一部分用turtle把铺砖的结果以可视化的方式呈现出来'''


def sight(m, a, b, lst):
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
'''这部分用于对用户选定的铺砖结果进行可视化'''


def main():
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
'''执行上述函数，给出最后的结果'''


if __name__ == '__main__':
    main()
