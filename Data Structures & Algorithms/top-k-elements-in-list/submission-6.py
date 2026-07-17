class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newl=[]
       
        newset=list(set(nums))
        if newset == nums:
                return newset
        else:
            for i in range(len(newset)):
                if newset == nums:
                    return newset
                
                count =0
                for j in range(len(nums)):

                    if newset[i]==nums[j]:
                        count+=1

                newl.append((newset[i], count))
            newl.sort(key=lambda x: x[1], reverse=True)

        newl2 = []
        for i in range(k):
            newl2.append(newl[i][0])

        return newl2

