import numpy as np
def my_knapsack(weights, values, capacity):
    n = len(weights)
    dp = np.zeros((n+1, capacity+1), dtype=int)
    #第一行和第一列初始化为0
    #从第二行开始，计算dp[i][w]的值
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            # 背包容量无法放入第i个物品
            if w< weights[i-1]:
                dp[i][w] = dp[i-1][w]
            # 尝试放入第i个物品
            else:
                # 不选择第 i 个物品时的最大价值。
                max_value_without_i = dp[i-1][w]
                # 选择第 i 个物品时的最大价值
                weight_i = weights[i-1]
                value_i = values[i-1]
                max_value_with_i = dp[i-1][w-weight_i]+value_i
                dp[i][w] = max(max_value_without_i, max_value_with_i)
    return dp[n][capacity]
              

# 示例数据
weights = [2, 3, 4]
values = [3, 4, 8]
capacity = 5

# 运行函数并打印结果
max_value = my_knapsack(weights, values, capacity)
print("背包的最大价值:", max_value)
