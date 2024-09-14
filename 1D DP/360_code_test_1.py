# 读取输入
n = int(input())  # 天数
a, b, c, d = map(int, input().split())  # 日卡、月卡、年卡、十年卡的价格
rides = list(map(int, input().split()))  # 每天骑行次数

# 动态规划数组，dp[i] 表示前 i 天的最小花费
dp = [float('inf')] * (n + 1)
dp[0] = 0  # 第 0 天的花费为 0

# 动态规划求解最小花费
for i in range(1, n + 1):
    # 当天骑行次数的费用（每次骑行花费1元）
    dp[i] = dp[i-1] + min(rides[i-1] * 1, a)  # 选择骑行费用或购买日卡

    # 购买月卡的情况，回顾前 30 天
    if i >= 30:
        dp[i] = min(dp[i], dp[i-30] + b)
    else:
        dp[i] = min(dp[i], b)

    # 购买年卡的情况，回顾前 365 天
    if i >= 365:
        dp[i] = min(dp[i], dp[i-365] + c)
    else:
        dp[i] = min(dp[i], c)

    # 购买十年卡的情况，回顾前 3650 天
    if i >= 3650:
        dp[i] = min(dp[i], dp[i-3650] + d)
    else:
        dp[i] = min(dp[i], d)

# 输出最小总花费
print(dp[n])