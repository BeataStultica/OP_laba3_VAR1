def opener(txt = 'graph.txt'):
	lab = open(txt, 'r')
	final_lab = []
	line_list = lab.read().splitlines()
	for i in line_list:
		temp = []
		for j in i:
			temp.append(j)
		final_lab.append(temp)
	output_matrix(final_lab)
	lab.close()
	return final_lab

def output_matrix(matrix):
	for k in matrix:
		for n in k:
			print("{:}".format(n), end=" ")
		print() 

def dijkstra(lab,start = [],end = []):
	perm = [start+[0]]
	temp = []
	flag = False
	l = 0
	cointer = 1
	for i in perm:
		temp =[i[0]-1,i[1],cointer], [i[0]+1,i[1],cointer], [i[0],i[1]-1,cointer], [i[0],i[1]+1,cointer]

		temp1 = []
		print(temp)
		for k in temp:
			if lab[k[0]][k[1]] == ' ':
				temp1.append(k)
			if k[:-1] == end:
				flag = True
			for j in range(len(perm)):
				if k[:-1] == perm[j][:-1] and k[-1] > perm[j][-1]:
					if k in temp1:
						temp1.remove(k)
		print(temp1)

		if temp1:
			cointer +=1
		perm.extend(temp1)
		print(perm)
		if flag:
			break
	print("Final:\n")
	print(perm)

def main():
	lab = opener('lab2.txt')
	dijkstra(lab,start = [5,1],end= [1,14])
main()
