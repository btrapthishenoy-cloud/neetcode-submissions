class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]

        for n, freq in count.items():
            bucket[freq].append(n)

        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for n in bucket[freq]:
                result.append(n)

                if len(result) == k:
                    return result