def containsNearbyDuplicate(nums, k):
    seen = set()

    for i in range(len(nums)):
        if i > k:
            seen.remove(nums[i - k - 1])

        if nums[i] in seen:
            return True

        seen.add(nums[i])

    return False


nums = [1, 2, 3, 1, 4, 5]
k = 3

if containsNearbyDuplicate(nums, k):
    print("There are duplicates within the range", k)
else:
    print("There are no duplicates within the range", k)

nums = [5, 6, 8, 2, 4, 6, 9]
k = 4

if containsNearbyDuplicate(nums, k):
    print("There are duplicates within the range", k)
else:
    print("There are no duplicates within the range", k)

nums = [5, 6, 8, 2, 4, 6, 9]
k = 2

if containsNearbyDuplicate(nums, k):
    print("There are duplicates within the range", k)
else:
    print("There are no duplicates within the range", k)
