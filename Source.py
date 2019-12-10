names = ["Fizz", "Buzz"]
vals = [3, 5]

def val(num):
  final = ""
  for i in range(len(names)):
    if num % vals[i] == 0:
      final += names[i]
  if final == "":
    print(num)
  else:
    print(final)

for i in range(100):
  val(i)
