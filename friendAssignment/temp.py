def remove_numbers(inStr):
  result = ""
  for char in inStr:
    if not char.isdigit():
      result += char
  return result

if __name__ == "__main__":
  inStr = input("문자열--> ")
  print("숫자 제거--> " + remove_numbers(inStr))