from tkinter import *
from helpers import read_maze, is_legal_pos, MAZE_FILE, Start_Coord
from search import bfsOWN, dfsOWN, a_starMYOWN
import time


root = Tk()
option_frame = Frame(root, bg='black')
maze_frame = Frame(root, width=200, height=200)
I = StringVar()
J = StringVar()
walls=[]
START_POS=(21,21)
GOAL_POS = ()
MAZE = None


def setGoal():
	global GOAL_POS
	GOAL_POS = (int(I.get()), int(J.get()))
	if is_legal_pos(MAZE, GOAL_POS):
		Label(maze_frame, width=3, bg='gold', borderwidth=0, highlightthickness=0).grid(row=int(I.get()),column=int(J.get()))

def color_path(path, color):
	for i in path:
		if i != GOAL_POS and i != START_POS:
			Label(maze_frame,width=3, bg=color, borderwidth=0, highlightthickness=0).grid(row=i[0], column=i[1])
			maze_frame.update()
			time.sleep(.05)

def getCoords():
	Label(option_frame, text="Coordinate: ", bg='red', fg='gold', width=20, font=('hack', 12, 'bold')).grid(row=1, column=0)
	Entry(option_frame, width=20, bg='red', fg='gold', textvariable=I, font=('hack', 12, 'bold')).grid(row=1, column=1)
	Entry(option_frame, width=20, bg='red', fg='gold', textvariable=J, font=('hack', 12, 'bold')).grid(row=1, column=2)
	Button(option_frame, width=20, bg='red', fg='gold', text="SUBMIT", command=setGoal, font=('hack', 12, 'bold')).grid(row=1, column=3)

def dfstemp():
	color_path(dfsOWN(MAZE, START_POS, GOAL_POS), "green")

def bfstemp():
	color_path(bfsOWN(MAZE, START_POS, GOAL_POS), "green")

def a_startemp():
	color_path(a_starMYOWN(MAZE, START_POS, GOAL_POS), "green")

def render(maze):
	for i in range(len(maze)):
		global MAZE
		MAZE = maze
		for j in range(len(maze[i])):
			if maze[i][j] == ' ':
				Label(maze_frame, width=3, bg='white', borderwidth=0, highlightthickness=0).grid(row=i,column=j)
			if maze[i][j] == '*':
				walls.append([i,j])
				Label(maze_frame, width=3, bg='red', state="disabled", highlightthickness=0, highlightbackground='black').grid(row=i,column=j)
	Label(maze_frame,width=3, bg='black', borderwidth=0, highlightthickness=0).grid(row=START_POS[0], column=START_POS[1])
	maze_frame.update()

def createGUI(maze):
	Button(option_frame, text="BFS", bg='red', fg='gold',width=20, command=bfstemp, font=('hack', 12, 'bold')).grid(row=0, column=0)
	Button(option_frame, text="DFS", bg='red', fg='gold', width=20, command=dfstemp, font=('hack', 12, 'bold')).grid(row=0, column=1)
	Button(option_frame, text="A*", bg='red', fg='gold', width=20, command=a_startemp, font=('hack', 12, 'bold')).grid(row=0, column=2)
	Button(option_frame, text="SET GOAL", bg='red', fg='gold', width=20, command=getCoords, font=('hack', 12, 'bold')).grid(row=0, column=3)
	Button(option_frame, text="RESET", bg='red', fg='gold', width=20, command=lambda: render(maze), font=('hack', 12, 'bold')).grid(row=0, column=4)

	render(maze)
	
	option_frame.grid(padx=20, pady=20)
	maze_frame.grid(padx=50, pady=50)
	# root.state('zoomed')
	root.config(bg='black')
	root.mainloop()


if __name__ == "__main__":
	maze = read_maze(MAZE_FILE)
	START_POS = Start_Coord[MAZE_FILE]
	createGUI(maze)