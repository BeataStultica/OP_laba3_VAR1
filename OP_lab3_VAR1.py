class Item:
	def __init__(self, next__item=None, prev__item=None, elem=None):
		self.next__item = next__item
		self.prev__item = prev__item
		self.elem = elem


class StackList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
#Виводить всі елементи
	def printer(self):
		headitem = self.head
		while headitem is not None:
			print(headitem.elem)
			headitem = headitem.next__item
#Повертає довжину
	def leng(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.next__item
		return count
	def push(self, elem):
#Добавляє елемент в кінець
		if self.tail is None:
			item = Item(None, None, elem)
			self.head = item
			self.tail = self.head
			self.length = 1
		else:
			item = Item(None, self.tail, elem)
			self.tail.next__item = item
			self.tail = item
			self.length += 1
#Видаляє і повертає перший елемент
	def first(self):
		f = self.head.elem
		self.head = self.head.next__item
		if self.head is not None:
			self.head.prev__item = None
		return f
	def pop(self):
#видаляє і повертає останній елемент
		last = self.tail.elem
		self.tail = self.tail.prev__item
		if self.tail is not None:
			self.tail.next__item = None
		return last

class Labyrinth:
	def __init__(self,start = None,end = None):
		self.start = start
		self.end = end
#Зберігає в змінну карту лабіринта з файла
	def opener(self,txt = 'lab.txt'):
		lab = open(txt, 'r')
		self.final_lab = []
		line_list = lab.read().splitlines()
		for i in line_list:
			temp = []
			for j in i:
				temp.append(j)
			self.final_lab.append(temp)
		lab.close()
		return self.final_lab
#Виводить в консоль лабіринт
	def output_matrix(self,matrix):
		for k in matrix:
			for n in k:
				print("{:}".format(n), end=" ")
			print()
#На основі алгоритма Дейкстри проходиться по лабіринту у всіх можливих напрямах поки не дойде до кінцевої точки, далі відновлює найкоротший шлях
	def dijkstra(self,lab):
		queue = [self.end+[0]]
		temp = []
		stack = StackList()
		stack.push(self.end+[0])
		flag = False
		l = 0
		cointer = 1
		lab[self.start[0]][self.start[1]] = 's'
		lab[self.end[0]][self.end[1]] = 'e'
		print("Лабіринт з відміченою точкою старта і кінця(s i e відповідно):")
		self.output_matrix(lab)
		for i in queue:
			temp =[i[0]-1,i[1],cointer], [i[0]+1,i[1],cointer], [i[0],i[1]-1,cointer], [i[0],i[1]+1,cointer]
			temp1 = []
			for k in temp:
				if lab[k[0]][k[1]] == ' ':
					temp1.append(k)
				if k[:-1] == self.start:
					flag = True
				for j in range(len(queue)):
					if k[:-1] == queue[j][:-1] and k[-1] > queue[j][-1]:
						if k in temp1:
							temp1.remove(k)
			if temp1:
				cointer +=1
			queue.extend(temp1)
			for q in temp1:
				stack.push(q)
			if flag:
				break
		print("\nШлях в лабіринті найкоротшим шляхом:\n")
		coint2 = 2
		alph = "abcdefghijklmnopqrstuvwxyz"
		alph = list(alph)
		lab[self.start[0]][self.start[1]] = 1
		leight = stack.leng()
		start = self.start
#Відновлює найкоротший шлях до кінцевої точки
		path = 0
		for i in range(leight):
			go = stack.pop()
			s = [[start[0]-1,start[1]], [start[0]+1,start[1]], [start[0],start[1]-1], [start[0],start[1]+1]]
			for i in s:
				if i == go[:-1]:
#Якщо довжина шляху менша за 10 пройдений шлях відмічається числами від 1 до 9
					if coint2 <10:
						lab[i[0]][i[1]] = coint2
						path +=1
#Якщо більша 9 то відмічається буквами в алфавітному порядку
					elif alph:
						lab[i[0]][i[1]] = alph.pop(0)
						path +=1
#Якщо алфавіт закінчився відмічає прочерками
					else:
						lab[i[0]][i[1]] = '-'
						path +=1
					start = i
					coint2 +=1
		self.output_matrix(lab)
		print("\nДовжина найкоротшого шляху: " + str(path))
def main():
	lab = Labyrinth(start = [5,1],end = [1,14])
	lab_map = lab.opener('lab2.txt')
	lab.dijkstra(lab_map)
main()

