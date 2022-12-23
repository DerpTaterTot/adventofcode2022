filein = open("day11/input.txt", "r")

lines = filein.readlines()

class Monkey:
    def __init__(self, name, items, multiply, number, test, trueMonkey, falseMonkey) -> None:
        self.name = name
        
        self.items = items 
        
        self.multiply = multiply # add if false, multiply if true
        self.number = number # number to add or multiply
        
        self.same = number == "old" 
            
        self.test = test # number to check divisibility by
        
        self.trueMonkey = trueMonkey # number to jump to if true
        self.falseMonkey = falseMonkey # number to jump to if false
        
        self.inspects = 0 # number of times inspected

    def addItem(self, item):
        self.items.append(item)
    
    def editItem(self, index):
        self.inspects += 1
        
        if self.same:
            self.number = self.items[index]
        
        self.number = int(self.number)
        # print("number: " + str(self.number))
        
        if self.multiply:
            self.items[index] = self.items[index] * self.number
        else:
            self.items[index] = self.items[index] + self.number 
        
        self.items[index] = self.items[index] % 9699690 
            
        # divide each item by 3 and round to nearest integer
        # self.items[index] //= 3 
    
    # def editAllItems(self):
    #     for i in range(len(self.items)):
    #         self.editItem(i)
    
    def checkItem(self, index):
        if self.items[index] % self.test == 0:
            return self.trueMonkey
        else:
            return self.falseMonkey
    
    def transferItem(self, index):
        self.checkItem(index).addItem(self.items.pop(0)) # check item and transfer to other monkey

        
    # def transferAllItems(self):
    #     if len(self.items) == 0:
    #         return
        
    #     for _ in range(len(self.items) - 1):
    #         self.transferItem(-1)
            
    def compute(self):
        while self.items: # for each item
            # print("before: " + str(self.name), str(self.items))
            
            self.editItem(0)
            self.transferItem(0)
            
            # printAllMonkeys()

monkeys = []

for line in lines:
    if "Monkey" in line:
        name = int(line.split()[1].strip(":"))
        items = []
        multiply = False
        number = 0
        test = 0
        trueMonkey = None
        falseMonkey = None
        
    if "Starting items:" in line:
        items = line.split()[2:]
        for i in range(len(items)):
            items[i] = int(items[i].strip(","))
            
        
    if "Operation:" in line:
        multiply = line.split()[4] == "*"
        number = line.split()[5]
    
    if "Test:" in line:
        test = int(line.split()[3])
        
    if "true:" in line:
        trueMonkey = int(line.split()[5])
    
    if "false:" in line:
        falseMonkey = int(line.split()[5])
        
        monkeys.append(Monkey(name, items, multiply, number, test, trueMonkey, falseMonkey))        

def getMonkey(name):
    for monkey in monkeys:
        if monkey.name == name:
            return monkey
        
def printAllMonkeys():
    for monkey in monkeys:
        print(monkey.name, monkey.items)

def printMonkeyInspects():
    for monkey in monkeys:
        print(monkey.name, monkey.inspects)

def calculateAnswer():
    # find two max inspects and multiply
    
    max1 = 0
    max2 = 0
    
    inspectsList = []
    
    for monkey in monkeys:
       inspectsList.append(monkey.inspects)
    
    max1 = max(inspectsList)
    inspectsList.remove(max1)
    max2 = max(inspectsList)
    
    return max1 * max2

def assignMonkeys():
    for monkey in monkeys:
        monkey.trueMonkey = getMonkey(monkey.trueMonkey)
        monkey.falseMonkey = getMonkey(monkey.falseMonkey)

def findProductOfAllTests():
    product = 1
    
    for monkey in monkeys:
        product *= monkey.test
        
    return product

assignMonkeys()

# print(findProductOfAllTests())
rounds = 10000
for _ in range(rounds):
    for i in range(len(monkeys)):
        monkeys[i].compute()
       
print("-----Monkey Items-----") 
printAllMonkeys()

print("-----Monkey Inspects-----")
printMonkeyInspects()

print("-----Final Ansswer-----")
print(calculateAnswer())

