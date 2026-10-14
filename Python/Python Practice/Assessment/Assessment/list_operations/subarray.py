def minimumSub(arr,target):
        l = 0
        curr = 0
        minimum = float("inf")

        for i in range(len(arr)):
            curr += arr[i]
            while curr >= target:
                length = i - l + 1
                minimum = min(minimum, length)

                curr -= arr[l]
                l += 1
                
        return minimum