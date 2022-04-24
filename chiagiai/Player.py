class Player:
	def __init__(self, name = ""):
		self.name = name
		self.picked_time = 0
		self.pre = -1

	def __str___(self):
		  return '{self.name}'.format(self=self)