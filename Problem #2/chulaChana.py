INITIAL_PLACE_NAME = ["Mahamakut Building","Sara Phra Kaew","CU Sport Complex","Sanum Juub","Samyan Mitr Town"]
places = []
people = {}
#==============================Class====================================
class Place:
  def __init__(self,name):
    self.name = name
    self.people = set()

  def removePerson(self,person):
    self.people.remove(person)

  def addPerson(self,person):
    self.people.add(person)

  def getPopulation(self):
    return len(self.people)

class Person:
  def __init__(self,phoneNumber):
    self.phoneNumber = phoneNumber
    self.place = None

  def checkOut(self):
    if self.place == None:
      return 
    
    print("Checking out "+self.phoneNumber+" from "+self.place.name)
    self.place.removePerson(self)
    self.place = None

  def checkIn(self,place):
    if self.place != None:
      self.checkOut()

    self.place = place
    place.addPerson(self)
    print("Checking in "+self.phoneNumber+" into "+place.name)


#=======================GetInput==============================
def getCommand():
  print('Welcome to Chula Chana!!!')
  print('Available commands:')
  print('  1. Check in user')
  print('  2. Check out user')
  print('  3. Print people count')
  print('Please input any number: ',end='')
  command = input()
  print('------------------------------------------------------')
  return command

def getPhoneNumber():
  print('Enter phone number: ',end='')
  phoneNumber = input()
  return phoneNumber

def getPlace():
  for i,place in enumerate(places):
    print('  '+str(i+1)+'. '+place.name)
  print('Select the place: ',end="")
  try:
    placeIndex = int(input())-1
    return places[placeIndex]
  except:
    print("Invalid Place")
    return None

#=======================Command================================
def checkIn():
  print('Check in')
  phoneNumber = getPhoneNumber()
  place = getPlace()
  if place == None:
    return
  if phoneNumber not in people:
    people[phoneNumber] = Person(phoneNumber)
  people[phoneNumber].checkIn(place)

def checkOut():
  print('Check out')
  phoneNumber = getPhoneNumber()
  if phoneNumber not in people or people[phoneNumber].place == None:
    print("This people is not in any place!")
  else:
    people[phoneNumber].checkOut()

def printPeopleCount():
  print('Current Population')
  for i,place in enumerate(places):
    print('  '+str(i+1)+'. '+place.name+': '+str(place.getPopulation()))


#===========================MAIN================================

# Initialize place
for placeName in INITIAL_PLACE_NAME:
  places.append(Place(placeName))

while True:
  command = getCommand()
  if command == '1':
    checkIn()
  elif command == '2':
    checkOut()
  elif command == '3':
    printPeopleCount()
  else:
    print('Invalid Command')
  print('------------------------------------------------------')
