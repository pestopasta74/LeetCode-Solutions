class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        balances = []
        for customer in accounts:
            wealth = 0
            for bank_balance in customer:
                wealth += bank_balance
            balances.append(wealth)
        return max(balances)