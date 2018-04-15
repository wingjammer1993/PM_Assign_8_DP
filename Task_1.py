import numpy as np
import matplotlib.pyplot as plt


def give_unoccupied_crp_distribution(alpha, total_customers):
	probability_unoccupied_table = np.zeros(total_customers)
	for customer in range(1, total_customers):
		probability_unoccupied_table[customer] = alpha / (customer - 1 + alpha)
	plt.plot(probability_unoccupied_table[1:])
	plt.locator_params(axis='x', nbins=20)
	plt.xlabel("Number of customers")
	plt.ylabel("Probability of empty table assignment")
	plt.title("Number of customers in the hotel vs. Probability of empty table assignment with CRP and alpha = 0.5")
	plt.show()


if __name__ == "__main__":
	give_unoccupied_crp_distribution(0.5, 500)

