#!/usr/bin/env python
# coding: utf-8


# 合并两个升序的整数数组A和B，形成一个新的数组，新的数组也需要有序

class Solution:
    def mergeSortedArray(self, A, B):
        new_array = A + B
        return sorted(new_array)



if __name__ == '__main__':
    A = [1,2,3,5]
    B = [2,3,5,6]
    s = Solution()
    new_array = s.mergeSortedArray(A, B)
    print(new_array)
