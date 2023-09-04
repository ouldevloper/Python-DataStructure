def check(char):
	return char.isalpha() or char.isdigit() or char == '_'


def CodelandUsernameValidation(strParam):
  ret = True
  strLen = len(strParam)
  if strLen < 4 or strLen > 25:
    return False
  if not strParam[0].isalpha() or not strParam[strLen-1].isalpha():
    return False
  
  for char in strParam[1:]:
    if not check(char):
      ret = False
      break
  return ret

# keep this function call here 
print(CodelandUsernameValidation(input()))
