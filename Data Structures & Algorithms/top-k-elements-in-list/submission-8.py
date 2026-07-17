class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num in count:
            freq = count[num]
            buckets[freq].append(num)

        newl = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                newl.append(num)
                if len(newl) == k:
                    return newl

        return newl