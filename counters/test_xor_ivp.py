from models import *
from hill_functions import hybrid

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

    
def xor(in1, in2, Kd, n):
    return hybrid(in1,in2, Kd, n, Kd, n) + hybrid(in2,in1, Kd, n, Kd, n) 

def xor_test(T, Y, params):
    in1, in2, y = Y
    alpha1, alpha2, alpha3, alpha4, delta1, delta2, Kd, n = params

    d_in1 = 0
    d_in2 = 0
    d_y = alpha1*xor(in1, in2, Kd, n) - delta1*y

    return d_in1, d_in2, d_y


"""
    TESTING
"""

# simulation parameters
t_end = 100
N = 1000


# model parameters
alpha1 = 34.73 # protein_production
alpha2 = 49.36 # protein_production
alpha3 = 32.73 # protein_production
alpha4 = 49.54 # protein_production
delta1 = 1.93 # protein_degradation
delta2 = 0.69 # protein_degradation
Kd = 10.44 # Kd
n = 4.35 # hill

params = (alpha1, alpha2, alpha3, alpha4, delta1, delta2, Kd, n)

ins = [(0,0), (0,100), (100,0), (100,100)]

fig, axs = plt.subplots(2,2)

for ax,(in1, in2) in zip(axs.flat,ins):

    Y0 = np.array([in1, in2, 0]) # initial state
    T = np.linspace(0, t_end, N) # vector of timesteps

    # numerical interation
    sol = solve_ivp(xor_test, [0, t_end], Y0, args=(params,), dense_output=True)

    z = sol.sol(T)
    Y = z.T

    #Y_reshaped = np.split(Y, Y.shape[1], 1)

    # plotting the results
    in_1 = Y[:,0] #Y_reshaped[0]
    in_2 = Y[:,1] #Y_reshaped[1]
    y = Y[:,2] # Y_reshaped[2]

    ax.plot(T, in_1, label='in_1')
    ax.plot(T, in_2, label='in_2')
    ax.plot(T, y, label='y')

    ax.legend()
    ax.set_title(f'in1={in1}, in2={in2}')

plt.show()
