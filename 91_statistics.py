def find_mean(numbers):
  """a function that finds the mean of the numbers"""
  if not numbers: return 0
  return sum(numbers) / len(numbers)
def find_median(numbers):
  """a function that finds the number which is located in the centre"""
  if not numbers: return 0
  temp_list = sorted(numbers)
  n = len(temp_list)
  index = n // 2
  if index % 2 == 0:
    return (nums[index - 1] + nums[index]) / 2
  return nums[index]
def find_mode(numbers):
  """a function that finds the most repeated element"""
  if not numbers: return []
  counts = {}
  for num in numbers:
    counts[num] = counts.get(num, 0) + 1
  max_count = max(counts.values())
  if max_count == 1:
    return []
  return [num for num, count in counts.items() if count == max_count]
def get_number():
  """a function that only accepts numbers from the user"""
  numbers = []
  while True:
      user_input = input("Enter a number (type 'stop' to stop the project)").strip().lower()
      if user_input == 'stop':
          break
      try:
          numbers.append(float(user_input))
      except ValueError:
          print("Please enter only numbers")
  return numbers
#---Main Part---
nums = get_number()
if nums:
  mean = find_mean(nums)
  median = find_median(nums)
  mode = find_mode(nums)
  print("\n📊---Statistics---")
  print(f"🔹️Arithmetic mean: {mean:.2f}")
  print(f"🔹️Median: {median:.2f}")
  if mode:
    print(f"🔹️Mode: {', '.join([f'{m:.2f}'for m in mode])}")
  else:
    print("️🔹️Mode: There is no repeated elements")
else:
  print("🚫No information entered")