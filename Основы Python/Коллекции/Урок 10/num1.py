num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

nums1 = set(num_string_1.split())
nums2 = set(num_string_2.split())
common = nums1.intersection(nums2)
print(len(common))
