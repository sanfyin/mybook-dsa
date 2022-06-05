
def fruits_into_baskets(fruits):
  max_len, win_start = 0, 0
  dict_fruits={}

  for win_end in range(len(fruits)):
    if fruits[win_end] not in dict_fruits:
      dict_fruits[fruits[win_end]] = 1
    else: 
      dict_fruits[fruits[win_end]] += 1
    
    while len(dict_fruits) >2:
      if dict_fruits[fruits[win_start]] == 1:
        del dict_fruits[fruits[win_start]]
      else:
        dict_fruits[fruits[win_start]] -= 1
      win_start += 1 

    if len(dict_fruits) == 2:
      max_len=max(max_len, sum(dict_fruits.values()))
      
  return max_len


def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

