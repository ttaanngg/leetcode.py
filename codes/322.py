class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = [coin for coin in coins if coin <= amount]
        result = [0] * (amount + 1)

        for coin in coins:
            result[coin] = 1

        for i in range(1, amount + 1):
            available_coins = [coin for coin in coins if coin <= i]
            if available_coins:
                solutions = [result[i - coin] for coin in available_coins if result[i - coin] != -1]
                if solutions:
                    result[i] = 1 + min(solutions)
                    continue
            result[i] = -1
        return result[amount]


solution = Solution()
print solution.coinChange([3,7,405,436],8839)
