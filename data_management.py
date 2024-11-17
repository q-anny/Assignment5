import sys

try:
  a = float(sys.argv[1]) 
  b = float(sys.argv[2])
  c = float(sys.argv[3])
  d = float(sys.argv[4])
  e = float(sys.argv[5])

except ValueError:
  print("All values must be numeric")
  sys.exit()

numbers = [a, b, c, d, e]

if any(number < 0 for number in numbers):
  print("Negative values is not allowed")
else:
  avg = sum(numbers) / len(numbers)

  if avg > 50:
      avg_message = "Average of numbers is " + str(avg) + " and greater than 50"
  else:
      avg_message = "Average of numbers is " + str(avg) + " and less than or equal to 50"

  positive_count = len(numbers)

  if positive_count & 1 == 0:
    even_odd = "even"
  else:
    even_odd = "odd"

  greater_than_ten = sorted([number for number in numbers if number > 10])
  original_values = ", ".join(map(str, numbers))
  sorted_values = ", ".join(map(str, greater_than_ten))

  html_output = (
    f"<p>{avg_message}</p>"
    f"<p>The count of positive numbers is {even_odd}</p>"
    f"<p>Original values are {original_values}</p>"
    f"<p>Values greater than 10 are {sorted_values}</p>"
  )

  print(html_output)