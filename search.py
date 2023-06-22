from helpers import get_path, offsets, is_legal_pos
from queue_ll import Queue
from priority_queue import PriorityQueue
from stack import Stack


def heuristic(a, b):
	x1, y1 = a
	x2, y2 = b
	return abs(x1 - x2) + abs(y1 - y2)

def dfsOWN(MAZE, START, GOAL):
	stack = Stack()
	stack.push(START)
	predecessors = {START: None}
	full_path = []
	while not stack.is_empty():
		current_cell = stack.pop()
		full_path.append(current_cell)
		if current_cell == GOAL:
			return full_path
		for direction in ["up", "right", "down", "left"]:
			row_offset, col_offset = offsets[direction]
			neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
			if is_legal_pos(MAZE, neighbour) and neighbour not in predecessors:
				stack.push(neighbour)
				predecessors[neighbour] = current_cell

def bfsOWN(MAZE, START, GOAL):
	queue = Queue()
	queue.enqueue(START)
	predecessors = {START: None}
	full_path = []
	while not queue.is_empty():
		current_cell = queue.dequeue()
		full_path.append(current_cell)
		if current_cell == GOAL:
			return full_path
		for direction in ["up", "right", "down", "left"]:
			row_offset, col_offset = offsets[direction]
			neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
			if is_legal_pos(MAZE, neighbour) and neighbour not in predecessors:
				queue.enqueue(neighbour)
				predecessors[neighbour] = current_cell

def a_starMYOWN(MAZE, START, GOAL):
	pq = PriorityQueue()
	predecessors = {START: None}
	G = {START: 0}
	full_path = []
	pq.put(START, 0)
	while not pq.is_empty():
		current = pq.get()
		full_path.append(current)
		if current == GOAL:
			return full_path
		for direction in ["up", "right", "down", "left"]:
			neighbour = (offsets[direction][0] + current[0], offsets[direction][1] + current[1])
			new_cost = G[current] + 1
			if is_legal_pos(MAZE, neighbour):
				if neighbour not in G or new_cost < G[neighbour]:
					G[neighbour] = new_cost
					pq.put(neighbour, new_cost + heuristic(GOAL, neighbour))
					predecessors[neighbour] = current