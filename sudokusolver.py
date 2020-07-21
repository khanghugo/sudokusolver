import math

# grid template
# grid = [	[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],

# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],

# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# ]
grid = [	[ 0 , 0 , 0 ,	0 , 1 , 9 , 	0 , 8 , 0 ],
			[ 9 , 0 , 5 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
			[ 0 , 0 , 0 ,	4 , 0 , 0 , 	9 , 0 , 1 ],

			[ 0 , 3 , 0 ,	0 , 0 , 0 , 	0 , 5 , 6 ],
			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	3 , 4 , 0 ],
			[ 7 , 6 , 0 ,	8 , 0 , 0 , 	0 , 0 , 0 ],

			[ 8 , 0 , 1 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
			[ 2 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 4 ],
			[ 0 , 4 , 0 ,	6 , 0 , 7 , 	0 , 0 , 0 ],
]
# error checking grid. it will collects all the numbers that was chosen and moved it here so the same number wont repeat. however, a cell would resets if the pointer moves back
# to make a different combination
zgrid = [	[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []],
			[[] , [] , [] , [] , [] , [] , [] , [] , []]
]

#block divide. it doesnt change according to the grid so it is made to be a function so it will change everytime in a loop
# 0 1 2
# 3 4 5
# 6 7 8
gridBlock = []
def upblock():
	global gridBlock
	gridBlock = []
	for row in range(3):
		srow = row * 3
	
		for col in range(3):
			scol = col * 3
	
			subBlock = []
	
			for moving in range(3):
				for x in grid[srow + moving][scol:scol+3]:
					subBlock.append(x)
	
			gridBlock.append(subBlock)
upblock() # start right after to create the gridBlock

# this will return a list of values in columns
def ccol(row, col):
	selectedCol = []
	for temprow in range(9):
		selectedCol.append(grid[temprow][col])
	return selectedCol

# from the position of row and col, this will determine the block it is in
def findBlock(row, col):
	block = ( math.floor(row / 3) ) * 3 + math.floor(col / 3)
	return block
# im using a list so this makes everything looks neater
def printarray(listA):
	for indexi, i in enumerate(listA):
		if indexi == 3 or indexi == 6:
			print("")
		for indexj, j in enumerate(i):
			print(j, end = ' ')
			if indexj == 2 or indexj == 5:
				print(" ", end="")
		print()
	print("-----------------")
# operations to move forward or backward the block
def mnext():
	global mcol
	global mrow
	if mcol == 8:
		mrow += 1
		mcol = 0
	else:
		mcol += 1
def mpre():
	global mrow
	global mcol
	if mcol == 0:
		mrow -= 1
		mcol = 8
	else:
		mcol -= 1
# update the value in the grid
def uppos():
	grid[mrow][mcol] = pos
def upzpos():
	if zgrid[mrow][mcol]:
		zgrid[mrow][mcol].append(pos)
	else:
		zgrid[mrow][mcol] = [pos]
# reset the value in the grid
def rezpos():
	global mcol
	global mrow
	if (-1) not in zgrid[mrow][mcol]:
		zgrid[mrow][mcol] = [] # before it moves back, it makes sure to reset the list back to do more combinations
def repos():
	global mcol
	global mrow
	grid[mrow][mcol] = 0
# this will show the differences in 2 lists, a number set from 1 to 9 and a chosen in case to show what number is needed to fill in
def setdiff(set1):
	return list(set(nset) - set(set1))

#bunch of presets
mrow = 0
mcol = 0
nset = [1, 2, 3, 4, 5, 6, 7, 8, 9]
isMoveBack = False

#set flag so given values wont be changed
for x in range(9):
	for y in range(9):
		if grid[x][y] != 0: zgrid[x][y] = [-1]

#the entire script
while True:
	#check logic, if it moves too much, break, also defines stuff
	if (0 <= mcol < 9) and (0 <= mrow < 9):
		pos = grid[mrow][mcol]
		zpos = zgrid[mrow][mcol] # todo reset the list after the pos is moved back aka mpre()
	elif mcol == 9 or mrow == 9:
		print('Done!')
		break
	else:
		print('error')
		break
	# defining stuffs
	mblock = findBlock(mrow, mcol)
	indexStart = 0
	#find the numbers missing in each group, n = need
	nrow = setdiff(grid[mrow])
	ncol = setdiff(ccol(mrow, mcol))
	nblock = setdiff(gridBlock[mblock])
	nzpos = setdiff(zgrid[mrow][mcol]) # if the set is empty then nset = nzpos.
	# this list contains the common numbers they dont have so the new block will be filled with it
	commontobepicked = list(set(nrow) & set(ncol) & set(nblock) & set(nzpos)) #nzpos is added to filter out numbers that are tried

	#given number, will be ignored by moving up or back
	if pos != 0 and (-1 in zpos):
		if isMoveBack == False:
			mnext()
		else:
			rezpos() # this deosnt needed because there is a condition to check if the block is fixed or not already. this is jut for consistency sake
			mpre()

	else:
		try:
			pos = commontobepicked[0]
			#print(f"FLASHY {commontobepicked} and {setdiff(zpos)} and {zpos}")
			uppos()
			upzpos()
			isMoveBack = False
			mnext()
		except IndexError:
			repos()
			rezpos()
			mpre()
			isMoveBack = True
		except Exception as e:
			print(f"{e} 		pos != 0 ERROR")
			break

	#since all the number in the grid changes and the gridBlock has no affliiations, it needs to be udpated on its own.
	upblock()

# glory
printarray(grid)

# glossary: n-need, m-move, up-update
# zpos is the numbers that are checked. so if we want the unchecknumber aka potential solution, flip it.

# todo
# check if block fits value: ok
# doesnt need to check if there are empty: if pos is empty, it needs to fill in a suitable numer based of row col block, this is the easiest way. after fill in, if the len() is still not 9 :ok
# it would ignore the checking mechanism and move on. it would need to compare all between row col block to see which number is better to fill in :ok


#guide
# update values before move aka mpre() or mnext() because mcol and mrow are global
# mblock doesnt use those globals so it's okay but still need to be updated.


# problem
# gridBlock needs to be updated to change. so changes of grid outside loop will not make the actual change until you update it with upblock() : ok
# tmp: got error when not use np matrix : ok

# grid = [	[ 0 , 0 , 0 ,	0 , 1 , 9 , 	0 , 8 , 0 ],
# 			[ 9 , 0 , 5 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	4 , 0 , 0 , 	9 , 0 , 1 ],

# 			[ 0 , 3 , 0 ,	0 , 0 , 0 , 	0 , 5 , 6 ],
# 			[ 0 , 0 , 0 ,	0 , 0 , 0 , 	3 , 4 , 0 ],
# 			[ 7 , 6 , 0 ,	8 , 0 , 0 , 	0 , 0 , 0 ],

# 			[ 8 , 0 , 1 ,	0 , 0 , 0 , 	0 , 0 , 0 ],
# 			[ 2 , 0 , 0 ,	0 , 0 , 0 , 	0 , 0 , 4 ],
# 			[ 0 , 4 , 0 ,	6 , 0 , 7 , 	0 , 0 , 0 ],
# ]
# solved in 70.8 sec, probably the printing did not do it justice. 2.1s without any spam
# 4 2 7  3 1 9  6 8 5 
# 9 1 5  7 8 6  4 2 3 
# 6 8 3  4 5 2  9 7 1 

# 1 3 2  9 7 4  8 5 6 
# 5 9 8  2 6 1  3 4 7 
# 7 6 4  8 3 5  1 9 2 

# 8 7 1  5 4 3  2 6 9 
# 2 5 6  1 9 8  7 3 4 
# 3 4 9  6 2 7  5 1 8 

# grid = [	[ 6 , 0 , 0 ,	4 , 0 , 0 , 	2 , 0 , 0 ],
# 			[ 9 , 1 , 0 ,	0 , 6 , 0 , 	0 , 0 , 0 ],
# 			[ 0 , 0 , 7 ,	0 , 0 , 0 , 	0 , 6 , 0 ],

# 			[ 0 , 2 , 0 ,	0 , 8 , 0 , 	7 , 0 , 0 ],
# 			[ 0 , 5 , 0 ,	2 , 0 , 1 , 	0 , 9 , 0 ],
# 			[ 0 , 0 , 9 ,	0 , 4 , 0 , 	0 , 5 , 0 ],

# 			[ 0 , 4 , 0 ,	0 , 0 , 0 , 	5 , 0 , 0 ],
# 			[ 0 , 0 , 0 ,	0 , 1 , 0 , 	0 , 8 , 6 ],
# 			[ 0 , 0 , 8 ,	0 , 0 , 7 , 	0 , 0 , 4 ],
# ]
# solved in 10.4 sec, this time with minimal printing spam. 0.7s with no spam


