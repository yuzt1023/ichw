"""currency.py:货币兑换程序，以及测试程序

__author__ = "于中天"
__pkuid__  = "1800011813"
__email__  = "1800011813@pku.edu.cn"
"""

def exchange(cf, ct, af):#cf==currency_from,即需要转换的货币；ct==currency_to，即目标货币；af==amount_from，需要转换的金额
    """输入需转换的货币简写字符串（三位大写字母），目标货币简写字符串（三位大写字母），以及交换金额
    """
    s = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + cf + '&to=' + ct + '&amt=' + str(af)#s==目标网址，即用于将一定金额的货币兑换成目标货币，得到其目标金额
    from urllib.request import urlopen

    doc = urlopen(s)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')#用decode将doc.read()得到的网址信息字节流转换成含有信息的字符串，以便处理
    a = jstr.find(':',11)#由于输出的字符串有一定格式：{ "from" : "输出金额 货币单位", "to" : "输出金额 货币单位", "success" : true, "error" : "" }
    b = jstr.find(' ',a+3)#从11位找到输出金额前的：，加3得到金额首项位置，再找到末尾空格的位置，即得输出金额数
    return(float(jstr[a+3:b]))#返回浮点数

def testAll():
    """测试程序
    """
    q=['USD','SGD','PLN','CLF','FKP','OMR']#输入货币形式的测试数据
    w=['RON','ERN','TOP','GYD','IQD','KYD']#输出货币形式的测试数据
    e=[1.3,4.2,51,6000,0.012,1322.190]#输入金额的测试数据
    r=[5.2000039,45.785340371227,31.663962918178,53718935.414885,18.414277197867,2862.5888337254]#答案
    for i in range(6):
        assert(exchange(q[i],w[i],e[i])==r[i])#判断语句，出现错误将终止程序
    print("All tests passed")
    
def main():
    testAll()
    A=input()
    B=input()
    C=float(input())
    print(exchange(A,B,C))
if __name__ == '__main__':
    main()
