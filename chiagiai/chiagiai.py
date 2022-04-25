from Player import *
import random

f = open("PlayerList.txt", encoding = "utf-8")
tmp = f.readlines()
Players = []
old_rounds = []
new_rounds = []

for player in tmp:
	if player[-1:] == '\n':
		player = player[:-1]
	Players.append(Player(player))
f.close()
max_player_each_round = 8
number_of_round = 1
number_of_players = len(Players)
if number_of_players - number_of_players//8 * 8 <= number_of_players//8 and number_of_players % 8 != 0:
	max_player_each_round += 1
number_of_table = number_of_players//max_player_each_round
if number_of_table * max_player_each_round < number_of_players: number_of_table += 1
average_players = number_of_players // number_of_table
Tables = []

for i in range(number_of_table):
	Tables.append(i + 1)

def check_group(group, number):
	count = 0 
	for i in group:
		if i.pre == number:
			count += 1
	return count

def new_round():
	global Players, number_of_round, Tables, number_of_table, old_rounds
	random.shuffle(Players)
	tables = Tables.copy()
	this_round = []
	pop_table = []
	priority = []
	for i in range(number_of_table):
		this_round.append([])

	for player in Players:
		if player.pre == -1:
			temp = 10000000
			Id = -1
			for i in tables:
				if len(this_round[i - 1]) < temp:
					Id = i
					temp = len(this_round[i - 1])
			new_table = Id

		else:
			# new_table = random.choice(tables)
			priority = [0 for i in range(number_of_table)]
			for i in tables:
				 priority[i - 1] = (check_group(old_rounds[i - 1],player.pre))
			temp = 100000000
			Id = -1
			for i in range(len(priority)):
				if (i + 1) not in pop_table:
					if priority[i] < temp and len(this_round[i]) <= average_players:
						temp = priority[i]
						Id = i + 1
					if priority[i] == temp:
						if len(this_round[i]) < len(this_round[Id - 1]):
							Id = i + 1
			new_table = Id
		player.pre = new_table
		this_round[new_table - 1].append(player)
		if len(this_round[new_table - 1]) >= max_player_each_round: 
			# print(tables, new_table)
			try:
				tables.remove(new_table)
			except:
				print(pop_table, Id, priority, tables)
				exit()

			pop_table.append(new_table)
		# print()
	# for i in range(number_of_table):
	# 	if len(this_round[i]) <= 6:
	# 		for j in range(number_of_table):
	# 			if i == j:
	# 				continue
	# 			if len(this_round[i]) >= 8:
	# 				break
	# 			temp = 100000000
	# 			Id = -1
	# 			for player in this_round[j]:
	# 				c = check_group(this_round[i], player)
	# 				if c < temp:
	# 					temp = c
	# 					Id = j
	# 			this_round[i].append(this_round[j][Id])
	# 			this_round[j].pop(Id)
	old_rounds = this_round.copy()
	return this_round

f = open("out.txt", "w", encoding = 'utf-8')

def output():
	global number_of_table
	this_round = new_round()
	for i in range(number_of_table):
		for j in this_round[i]:
			f.write(j.name + '\n')
		f.write('\n')

if number_of_players > 11:
	for i in range(3):
		f.write("round " + str(i + 1) + '\n')
		output()
else:
	for i in range(5):
		f.write("round " + str(i + 1) + '\n')
		for player in Players:
			f.write(player.name + '\n')
		f.write('\n')
f.close()
