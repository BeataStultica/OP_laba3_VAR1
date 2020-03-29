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

def main():
	lab = opener('lab.txt')
main()
