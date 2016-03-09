class TwoStackQueue:
	def __init__(self):
		self.stackIn = []
		self.stackOut = []

	def push(self, value):
		self.stackIn.append(value)

	def pop(self):
		for i in range(len(self.stackIn)):
			self.stackOut.append(stackIn.pop())

		return self.stackOut.pop()


