  """
  প্রদত্ত তথ্য থেকে প্রয়োজনীয় রানের হার গণনা করে।

  Args:
    opponent_runs: প্রতিপক্ষের মোট রান
    current_runs: ব্যাটসম্যানদের বর্তমান রান
    balls_remaining: খেলার বাকি বল

  Returns:প্রয়োজনীয় রানের হার
  """
def required_run_rate(opponent_runs, current_runs, balls_remaining):
  required_runs = opponent_runs - current_runs
  required_overs = balls_remaining / 6

  return required_runs / required_overs

def print_run_rates(test_cases):
  """
  প্রদত্ত তথ্যের জন্য বর্তমান এবং প্রয়োজনীয় রানের হার প্রিন্ট করে।

  Args:
    test_cases: পরীক্ষার ক্ষেত্রের একটি তালিকা
  """

  for t in test_cases:
    opponent_runs, current_runs, balls_remaining = t

    current_run_rate = current_runs / (balls_remaining / 6)
    required_run_rate = required_run_rate(opponent_runs, current_runs, balls_remaining)

    print(f"{current_run_rate:.2f} {required_run_rate:.2f}")

"""পরীক্ষার ক্ষেত্রের একটি তালিকা তৈরি করুন"""
test_cases = [
  (100, 50, 10),
  (50, 20, 20),
  (100, 0, 50),
  (100, 100, 0),
]

""" বর্তমান এবং প্রয়োজনীয় রানের হার প্রিন্ট করুন"""
print_run_rates(test_cases)
