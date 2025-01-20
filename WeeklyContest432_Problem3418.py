# Problem Link : https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/?slug=maximum-amount-of-money-robot-can-earn&region=global_v2

from typing import List
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # Dynamic Programming Solution
        height, width = len(coins), len(coins[0])
        dp = [[[None for _ in range(3)] for _ in range(width)] for _ in range(height)]
        for hi in range(height-1, -1, -1):
            for wi in range(width-1, -1, -1):
                for ki in range(3):
                    if hi==height-1 and wi==width-1:
                        # Base state
                        if ki==0:
                            dp[hi][wi][ki] = coins[hi][wi]
                        else:
                            dp[hi][wi][ki] = max(0, coins[hi][wi])
                        continue
                    if ki == 0:
                        if hi+1<height and wi+1<width:
                            dp[hi][wi][ki] = coins[hi][wi]+max(dp[hi+1][wi][ki], dp[hi][wi+1][ki])
                        elif hi+1<height:
                            dp[hi][wi][ki] = coins[hi][wi]+dp[hi+1][wi][ki]
                        else:
                            dp[hi][wi][ki] = coins[hi][wi]+dp[hi][wi+1][ki]
                    else:
                        if coins[hi][wi] >= 0:
                            if hi+1<height and wi+1<width:
                                dp[hi][wi][ki] = coins[hi][wi]+max(dp[hi+1][wi][ki], dp[hi][wi+1][ki])
                            elif hi+1<height:
                                dp[hi][wi][ki] = coins[hi][wi]+dp[hi+1][wi][ki]
                            else:
                                dp[hi][wi][ki] = coins[hi][wi]+dp[hi][wi+1][ki]
                        else:
                            if hi+1<height and wi+1<width:
                                dp[hi][wi][ki] = max(dp[hi+1][wi][ki-1], dp[hi][wi+1][ki-1], coins[hi][wi] + max(dp[hi+1][wi][ki], dp[hi][wi+1][ki]))
                            elif hi+1<height:
                                dp[hi][wi][ki] = max(dp[hi+1][wi][ki-1], coins[hi][wi]+dp[hi+1][wi][ki])
                            else:
                                dp[hi][wi][ki] = max(dp[hi][wi+1][ki-1], coins[hi][wi]+dp[hi][wi+1][ki])
        return dp[0][0][2]
