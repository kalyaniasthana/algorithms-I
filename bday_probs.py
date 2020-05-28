import matplotlib.pyplot as plt

def bday_probability(k):
	prob = 1
	for i in range(1, k + 1):
		#print(365 - i + 1, i)
		prob *= (365 - i + 1)/365
		#prob_dict[k] = prob
	return prob

def prob_list(k):
	probs = []
	for i in range(1, k + 1):
		probs.append(bday_probability(i))

	return probs

def plot_bday_probs(bday_list):
	y = [i+1 for i in range(len(bday_list))]
	plt.scatter(bday_list, y)
	plt.xlabel('Probabilty of having different birth dates')
	plt.ylabel('Number of people')
	plt.show()

l = prob_list(366)
plot_bday_probs(l)

