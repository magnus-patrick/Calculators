import numpy as np
from scipy.stats import mode

l = []
print("Your current list:",l)

def list():
    choice = input("\nWhat do you want to do with your data set?\n1. Insert\n2. Append\n3. Remove\n4. View\nResponse: \n")

    if choice == "1" or choice.lower() == "insert":
        for value, num in enumerate(l, start = 1):
            print("Data value {}. {}".format(value, num))
        new_element = float(input("\nInsert a new data value: "))
        position = int(input("\nWhat position do you want your data value to be in?: "))
        if len(l) > 0:
          if position >= 1 and position <= len(l):
            l.insert(position - 1, new_element)
            print("\nData value inserted.")
          else:
            print("\nYou're putting your data value out of bounds. Try again.")
        elif len(l) == 0:
           l.insert(position - 1, new_element)
           print("\nData value inserted.")

    elif choice == "2" or choice.lower() == "append":
      def append():    
          try:
            new_element = float(input("Insert a new data value: "))
            l.append(new_element)
            print("\nThis is your new data set:\n",l)
          except ValueError:
            print("\nPlease type a number, Thanks!")

      def keep_append():
         cont = input("\nDo you want to keep adding data values? (y/n) Response: ")
         if cont.lower() == "y" or cont.lower() == "yes":
            return True
         else:
            return False

      append()

      while keep_append():
         append()        

    elif choice == "3" or choice.lower() == "remove":
        for value, num in enumerate(l, start = 1):
            print("Data value {}: {}".format(value, num))
        removed_task = int(input("\nWhich data value do you want to remove? (Type the number beside the data value): "))
        if removed_task >= 1 and removed_task <= len(l):
          l.pop(removed_task - 1)
          print("\nData value removed.")
        else:
           print(f"Please choose a number between 1 and {len(l)}.")

    elif choice == "4" or choice.lower() == "view":
        if not l:
            print("\nYou got no data values in your data set!")
        else:
            print("\nList: ",l)

def restart_1():
    restart_1 = input("\nDo you want to go back to the menu or do statistics with your data set? (Type 1 to go back or 2 to do statistics): ")
    if restart_1.lower() == "1":
        return True
    else:
        return False

list()

while restart_1():
    list()

def stats():
  stat = input("\nDo you want to calculate the mode, the median, the mean, or the standard deviation of your dataset?\n1. Mode\n2. Median\n3. Mean\n4. Standard Deviation\nResponse: ")
  
  if stat == "1" or stat.lower() == "mode":
    mode_result = mode(l, keepdims = True) #mode_result is a tuple ModeResult(mode=array([2]), count=array([2]))
    print("\nThe mode of your dataset is:",mode_result.mode[0]) #mode_result.mode[0] accesses the mode value. Because .mode is an array, [0] is used to get the scalar, 2.
    print("\nIt occurs",mode_result.count[0],"times.") #Counts number of times the mode appears.
  
  elif stat == "2" or stat.lower() == "median":
    median = np.median(l)
    print("\nThe median of your dataset is:",median)
  
  elif stat == "3" or stat.lower() == "mean":
    mean = np.mean(l)
    print("\nThe mean of your dataset is:",mean)

  elif stat == "4" or stat.lower() == "standard deviation":
     std = np.std(l)
     print("\nThe standard deviation of your dataset is:",std)

def restart_2():
    restart_2 = input("\nDo you want to do more statistics with your list? (Type 1 to do more statistics or 2 to exit): ")
    if restart_2.lower() == "1":
      return True
    else:
      return False

stats()

while restart_2():
  stats()
