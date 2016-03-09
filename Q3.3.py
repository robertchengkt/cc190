class SetOfStacks:
	def __init__ (self, capacity):
		self.stackSet = []
		self.cap = capacity

	def push(self, value):
		if (len(self.stackSet) == 0) or (len(self.stackSet[-1]) == self.cap):
			self.stackSet.append([])
		self.stackSet[-1].append(value)

	def pop(self):
		if len(self.stackSet) == 0:
			return None
		else:
			return self.stackSet[-1].pop()
			if len(self.stackSet[-1]) == 0:
				self.stacks.pop()



def test():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print i,
    print ""

test()


