#!/usr/bin/env python3
# coding: utf-8

# 反转一个3位整数，输入number=123，输出321，输入number=900，输出9

class Solution(object):
    def reverseInterger(self, number):
        h = int(number/100)  # 输入的数字除以100取整，得到输入数字的百位数
        t = int(number%100/10)  # 先将数字取余得到十位和个位数，然后除以十取整，得到十位数
        z = int(number%10)  # 除以10取余数得到个位数
        return (100*z + 10*t + h)


if __name__ == '__main__':
    solution = Solution()
    number = int(input('请输入一个三位数： '))
    reverseNumber = solution.reverseInterger(number)
    #print(f'输入的三位数为：{number}')
    print('输入的三位数为：{}'.format(number))
    #print(f'反转后为：{reverseNumber}')
    print('反转后为：{}'.format(reverseNumber))






