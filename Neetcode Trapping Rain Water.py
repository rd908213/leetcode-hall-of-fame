class Solution:
    def trap(self, height: List[int]) -> int:
        self.height = height
        total_water = 0
        l, r = self.filter_data()
        while l < r:
            i = 1
            while l + i < r and height[l] >= height[l + i]:
                i += 1
            cur_height = min(height[l], height[l + i])
            total_water += self.calc_water(cur_height, l, l+i)
            l += i
        return total_water
        
            
    def calc_water(self, cur_height, l, r) -> int:
        tot = 0
        for i in range(l, r):
            if cur_height > self.height[i]:
                tot += cur_height - self.height[i]
        return tot

    def filter_data(self) -> tuple[int, int]:
        l = 0
        r = len(self.height)-1
        while l + 1 < len(self.height) - 1 and self.height[l] < self.height[l+1]:
            l += 1
        while r - 1 >= 0 and self.height[r] < self.height[r-1]:
            r -= 1
        return (l, r)

# ChatGPT is a hater below:
# 🔥 Actual Counterexample
# height = [6, 0, 5]

# Correct water:

# min(6,5) - 0 = 5
# Total = 5

# Your algorithm:

# l = 0

# i increases until it reaches index 2 (since 6 ≥ 0 and 6 ≥ 5)

# cur_height = min(6,5) = 5

# calc_water(5, 0, 2)

# This includes index 0:

# 5 - 6 → ignored
# 5 - 0 → 5

# So you get 5.

# Still correct.

# So let’s go further.

# 🔥 Real Breaking Case
# height = [5, 2, 1, 2, 1, 5]

# Correct answer: 14

# Your algorithm will process everything in one sweep and get 14.

# Still correct.
# 🧠 The Honest Conclusion

# Your time complexity analysis is correct: O(n).

# The infinite loop is fixed.

# The logic works for many structured cases.

# But it does not formally enforce the required invariant of the trapping rainwater problem.
# # ...
# 😄 So What’s Going On?

# You’ve accidentally built something close to a monotonic boundary sweep.
# ✅ Formal Conclusion

# Therefore:

# Your algorithm is correct.

# Time complexity: O(n)
# # Space complexity: O(1)
# 🎯 What You Accidentally Built

# You constructed a valid monotonic boundary sweep solution.
