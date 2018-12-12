def deco(func):
  import functools
  import time

  @functools.wraps(func)
  def inner(*args, **kwargs):
    start_time = time.time()  # начало таймера
    result = func(*args, **kwargs)
    end_time = time.time()  # завершение таймера
    time_delta = end_time - start_time
    print(f'Время выполнения кода {func.__name__} заняло: {time_delta}')
    return result
  return inner

@deco
def two_sum_brute(nums, target):  
  length = len(nums)
  for i in range(length):
    for j in range(i+1, length):
      if nums[j] == target - nums[i]:
        return [i, j]



"""
one-pass hash-table
"""
@deco
def two_sum(nums, target):
  dic = {}
  for index, num in enumerate(nums): 
    n = target - num    
    if n not in dic:
      dic[num] = index      
    else:
      return [dic[n], index]  



if __name__ == "__main__":
  print(two_sum_brute([2, 7, 11, 15], 9))
  assert two_sum_brute([2, 7, 11, 15], 9) == [0, 1]
  print(two_sum([2, 7, 11, 15], 9))
  assert two_sum([2, 7, 11, 15], 9) == [0, 1]
