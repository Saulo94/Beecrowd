from math import floor

nums = [0, 1, 2, 3]

while nums[0] <= 2:
    print("I={0} J={1}\n"
          "I={0} J={2}\n"
          "I={0} J={3}".format(nums[0], nums[1], nums[2], nums[3]))
    
    for i in range(len(nums)):
        nums[i] = round(nums[i] + 0.2, 1)
        if floor(nums[i]) == nums[i]:
            nums[i] = int(nums[i])
