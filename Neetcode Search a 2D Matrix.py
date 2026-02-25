class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        megalist = sum(matrix, [])
        i = len(megalist) // 2
        try:
            if self.RecursiveSrch(i, megalist, target):
                return True
        except IndexError: # Because this is definitely the condition we should be checking lol
            return False

    def RecursiveSrch(self, index, sublist, target):
        if index == 0 and sublist[index] != target:
            index = 1 # Its so dumb it works!
        if sublist[index] > target:
            return self.RecursiveSrch(index // 2, sublist[:index], target)
        elif sublist[index] < target:
            return self.RecursiveSrch(index // 2, sublist[index:], target)
        else:
            return True

"""
Reviews (by ChatGPT)
✅ It works

✅ It passed

❌ It's not optimal

❌ It’s fragile in theory

❌ It copies memory every recursion

But honestly?

“Its so dumb it works” is a legitimate engineering category 😂
"""
