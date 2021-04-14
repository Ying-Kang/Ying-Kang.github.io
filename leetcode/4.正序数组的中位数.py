#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/9/16 14:11
# @Author  : Koin
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            if len1 > len2:
                # 始终保持 len1 <= len2
                return findKthElement(arr2, arr1, k)
            if not arr1:
                # arr1 为空时
                return arr2[k - 1]
            if k == 1:
                # 递归边界
                return min(arr1[0], arr2[0])
            # 比较两个数组中的第 k/2 个元素，
            # key：如果数组1的小于数组2的，则说明数组1中的前 k/2 个元素不可能成为第 k 个元素的候选，
            # 因为就算两个数组的前 k/2 个元素全是整体最小，第 k 小的元素也只是数组2的第 k/2 个元素。
            # 所以将数组1中的前 k/2 个元素去掉，组成新数组和数组2求第 k-k/2 小的元素。
            i, j = min(k // 2, len1) - 1, min(k // 2, len2) - 1
            if arr1[i] > arr2[j]:
                return findKthElement(arr1, arr2[j + 1:], k - (j + 1))
            else:
                return findKthElement(arr1[i + 1:], arr2, k - (i + 1))

        total_len = len(nums1) + len(nums2)
        # 奇数直接找中间，偶数找中间两个
        if total_len % 2:
            kth = (total_len + 1) // 2
            return findKthElement(nums1, nums2, kth)
        else:
            kth = total_len // 2
            return (findKthElement(nums1, nums2, kth) + findKthElement(nums1, nums2, kth + 1)) / 2







