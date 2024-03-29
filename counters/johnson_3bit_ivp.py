from models import three_bit_model, get_clock
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
    
# An example of simulation using new scipy solver: solve_ivp


# the model function has Y and T parameters reversed in comparison to odeint:
def three_bit_model_ivp(Y, T, params):
    return three_bit_model(T, Y, params)


"""
    TESTING
"""

# simulation parameters
t_end = 200
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

params_ff = (alpha1, alpha2, alpha3, alpha4, delta1, delta2, Kd, n)


# three-bit counter with external clock
# a1, not_a1, q1, not_q1, a2, not_a2, q2, not_q2, a3, not_a3, q3, not_q3
Y0 = np.array([0]*12) # initial state
T = np.linspace(0, t_end, N) # vector of timesteps

# numerical interation
sol = solve_ivp(three_bit_model_ivp, [0, t_end], Y0, args=(params_ff,), dense_output=True)

z = sol.sol(T)
Y = z.T

# plotting the results
Q1 = Y[:,2]
not_Q1 = Y[:,3]
Q2 = Y[:,6]
not_Q2 = Y[:,7]
Q3 = Y[:,10]
not_Q3 = Y[:,11]


plt.plot(T, Q1, label='q1')
plt.plot(T, Q2, label='q2')
plt.plot(T, Q3, label='q3')
#plt.plot(T, not_Q1, label='not q1')
#plt.plot(T, not_Q2, label='not q2')

plt.plot(T, get_clock(T),  '--', linewidth=2, label="CLK", color='black', alpha=0.25)

plt.legend()
plt.show()
