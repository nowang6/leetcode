def sqrt_binary_search(number, epsilon=1e-10):
  low, high =1, number
  if number < 1:
    low, high = 0, 1
  mid = (0 + number) / 2
  while abs(mid**2 - number) > epsilon:
    if mid**2 < number:
      low = mid
    else:
      high = mid
    mid = (low + high) / 2
  return mid
    
# 重新运行示例
print(sqrt_binary_search(9))  # 输出 9 的平方根
print(sqrt_binary_search(2))  # 输出 2 的平方根
print(sqrt_binary_search(0.25))  # 输出 0.25 的平方根
