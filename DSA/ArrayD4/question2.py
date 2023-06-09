'''

Given two 0-indexed integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

Note that the integers in the lists may be returned in **any** order.

Input: nums1 = [1,2,3], nums2 = [2,4,6]

Output: [[1,3],[4,6]]

Explanation:

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

'''



def merge(nums1,nums2):

    nums1.sort()
    nums2.sort()

    distinct_nums1 = []
    distinct_nums2 = []

    i, j = 0, 0

    n1, n2 = len(nums1), len(nums2)

    while i < n1 or j < n2:

        if i < n1 and (j == n2 or nums1[i] < nums2[j]):
            distinct_nums1.append(nums1[i])
            i += 1

        elif j < n2 and (i == n1 or nums2[j] < nums1[i]):
            distinct_nums2.append(nums2[j])
            j += 1

        else:
            
            i += 1
            j += 1

    return [distinct_nums1, distinct_nums2]
    


nums1 = list(map(int,input("Enter first list : ").split()))

nums2 = list(map(int,input("Enter second list: ").split()))

result = merge(nums1,nums2)

print(result)