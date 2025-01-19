nums = [25,12,36,95,14]
print(nums[0])
print(nums[1:])
print(nums[-1])


nums2 = ['4','5']

fs = [nums,nums2]
print(fs)

fs.clear()
print(fs)
nums2.append(65)
nums2.insert(0,'first')
print(nums2)
nums2.pop(1) # first 4 5 65
print(nums2)
nums2.pop()
print(nums2)

print(min(nums))

