import time

# print(number)
# f.write(str(number))
def out():
	t = open("number_of_player.txt", 'r')
	f = open("PlayerList.txt", 'w')
	number = int(t.read())
	t.close()
	for i in range(number):
		f.write('[' + str(i + 1) + ']' + '\n')

# while(1):
# 	pass
	f.close()
out()
exit(0)
