# Initialize number pattern
NUMBER_PATTERN = [
  " __      __  __      __  __  __  __  __     ",
  "|  |   | __| __||__||__ |__    ||__||__|    ",
  "|__|   ||__  __|   | __||__|   ||__| __| __ "
]
NUMBER_WIDTH = 4
BLANK_INDEX = 10

# Check if time string is valid or not
def validateTime(timeString):
  [hour,minute,second] = timeString.split(':')
  if int(minute)>59 or int(second)>59:
    return False
  return True

# Return character pattern at the specified line
def getCharacterPattern(char,line):
  # colon
  if char == ':':
    if line != 0:
      return '.'
    else:
      return ' '
  
  # number and blank
  if char == ' ':
    patternIndex = BLANK_INDEX
  else:
    patternIndex = int(char)

  return NUMBER_PATTERN[line][NUMBER_WIDTH*patternIndex:NUMBER_WIDTH*(patternIndex+1)]


# Print time in seven segment pattern
def printTime(timeString):
  for line in range(3):
    text = ""
    for char in timeString:
      text+=getCharacterPattern(char,line)+' '
    print(text)


timeString = input()

if not validateTime(timeString):
  timeString = '  :  :  '

printTime(timeString)