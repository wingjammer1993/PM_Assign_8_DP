import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


def draw_from_crp(alpha, sigma, num_samples):
	k = 1
	customer_table = {1: 1}
	x_0 = np.random.uniform()
	y_0 = np.random.uniform()
	covariance = [[sigma, sigma*sigma], [sigma*sigma, sigma]]
	g0_params = [x_0, y_0]
	customer_x = OrderedDict()
	customer_y = OrderedDict()
	theta_1 = np.random.multivariate_normal([g0_params[0], g0_params[1]], covariance)
	customer_x[1], customer_y[1] = np.random.multivariate_normal([theta_1[0], theta_1[1]], covariance)
	params = {1: theta_1}
	for customer in range(2, num_samples):
		probability_new = alpha / (customer - 1 + alpha)
		if np.random.rand() < probability_new:
			k = k + 1
			theta = np.random.multivariate_normal([g0_params[0], g0_params[1]], covariance)
			customer_x[customer], customer_y[customer] = np.random.multivariate_normal([theta[0], theta[1]], covariance)
			params[k] = theta
			customer_table[k] = 1
		else:
			probability_old = []
			for table in customer_table:
				probability_old.append(customer_table[table] / (customer - 1 + alpha))
			idx_max = np.argmax(np.random.multinomial(1, probability_old, size=1))
			theta = params[int(idx_max)]
			customer_x[customer], customer_y[customer] = np.random.multivariate_normal([theta[0], theta[1]], covariance)
			customer_table[int(idx_max)] = customer_table[int(idx_max)] + 1


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
	# Part 1
	#give_unoccupied_crp_distribution(0.5, 500)

	# Part 2
	draw_from_crp(0.5, 0.1, 500)


