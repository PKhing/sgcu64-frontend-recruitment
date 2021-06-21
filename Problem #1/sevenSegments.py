import time
import os

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

#============================Countdown=======================================

# Clear console screen
def clearScreen():
  os.system('cls' if os.name=='nt' else 'clear')

# Display countdown timer
def countdown(timeString):
  [hour,minute,second] = [int(i) for i in timeString.split(':')]
  while True:
    clearScreen()

    # Print time
    timeString = f"{hour:02}:{minute:02}:{second:02}"
    printTime(timeString)

    # Decrease time
    second -=1
    if second < 0:
      second = 59
      minute -= 1
    if minute <0:
      minute = 59
      hour -= 1
    if hour < 0:
      break
    time.sleep(1)
    
#==============================Main========================================

timeString = input()

if not validateTime(timeString):
  printTime('  :  :  ')
  exit()

printTime(timeString)

# Countdown
print("Countdown? (Y/N) ",end="")
isCountdown = input()
if isCountdown != 'Y':
  exit()
else:
  countdown(timeString)

