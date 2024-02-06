class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans=[]
        # dic={}
        dic=defaultdict(list)
        for i in strs:

            k= ''.join(sorted(i))
            print(k)
            dic[k].append(i)
        return dic.values()
