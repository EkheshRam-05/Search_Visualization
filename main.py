from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from helpers import read_maze, is_legal_pos, MAZE_FILE, Start_Coord
from search import bfsOWN, dfsOWN, a_starMYOWN
import time


root = Tk()
frame_style = Style()
frame_style.configure('Frame1.TFrame', background='black')
option_frame = ttk.Frame(root,style='Frame1.TFrame')
maze_frame = ttk.Frame(root, width=200, height=200)
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
		ttk.Label(maze_frame, width=3, background='gold', borderwidth=0,).grid(row=int(I.get()),column=int(J.get()))

def color_path(path, color):
	for i in path:
		if i != GOAL_POS and i != START_POS:
			ttk.Label(maze_frame,width=3, background=color, borderwidth=0).grid(row=i[0], column=i[1])
			maze_frame.update()
			time.sleep(.04)

def getCoords():
	entry = Style()
	entry.configure('TEntry', background='white', foreground='red', font=('hack', 12, 'bold'))
	ttk.Label(option_frame, text="Coordinate: ", background='white', foreground='red', width=20, font=('hack', 12, 'bold')).grid(row=1, column=0)
	ttk.Entry(option_frame, width=20, textvariable=I, style='TEntry').grid(row=1, column=1)
	ttk.Entry(option_frame, width=20, textvariable=J, style='TEntry').grid(row=1, column=2)
	bs = Style()
	bs.configure('W.TButton', background='red', foreground='red', font=('hack', 12, 'bold'))
	ttk.Button(option_frame, width=20, text="SUBMIT", command=setGoal, style='W.TButton').grid(row=1, column=3)

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
				ttk.Label(maze_frame, width=3, background='white', borderwidth=0).grid(row=i,column=j)
			if maze[i][j] == '*':
				walls.append([i,j])
				ttk.Label(maze_frame, width=3, background='red', state="disabled").grid(row=i,column=j)
	ttk.Label(maze_frame,width=3, background='black', borderwidth=0).grid(row=START_POS[0], column=START_POS[1])
	maze_frame.update()

def createGUI(maze):
	style = Style()
	style.configure('W.TButton', font=('hack', 12, 'bold'), foreground='red')
	ttk.Button(option_frame, text="BFS", style='W.TButton',width=20, command=bfstemp).grid(row=0, column=0)
	ttk.Button(option_frame, text="DFS", style='W.TButton', width=20, command=dfstemp).grid(row=0, column=1)
	ttk.Button(option_frame, text="A*", style='W.TButton', width=20, command=a_startemp).grid(row=0, column=2)
	ttk.Button(option_frame, text="SET GOAL", style='W.TButton', width=20, command=getCoords).grid(row=0, column=3)
	ttk.Button(option_frame, text="RESET", style='W.TButton', width=20, command=lambda: render(maze)).grid(row=0, column=4)

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