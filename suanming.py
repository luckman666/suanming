#coding:utf-8
import re

'''算命脚本，提取π的数字'''
new_filename = 'F:\python\\test\文件\\new_pi_ten_million_digits_string.txt'
#格式化源文件，将其变成一行数字
with open(new_filename) as file_objeck:
    pi=file_objeck.read().replace(" ", "").replace("\n","")

'''每次起始值都往前动一位，初始是0'''
start = 0
search = input('pleace enter your birthday: ')
''''''
numstr=''
newstr=''
while True:
    #在π上进行循环比对
    index = pi.find(search,start)
    if index ==-1:
        break
    #将索引值重新组成一个新的字符串
    numstr += str(index)
    print("%s found at index %s" % (index, chr(index)) )
    #整个数在π上进行比对，每次比对后向后面错一位再比对
    start = index +1
#将新组成的串分成4个一组
numList=re.findall(r'.{4}', numstr)
for num in numList:
    #因为只有2开头的5位十进制是能看懂的汉字所以重新拼接字符串
    newnum="2"+num
    #得到的汉字再拼接成一句话
    newstr +=chr(int(newnum))

print('上苍送给你的一句话是：',newstr)
