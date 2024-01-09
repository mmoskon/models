# Repository of code for NPMP 2023/2024

## Relevant files
* [`models.py`](models.py): the implementation of models of the Master-Slave Flip-Flop, Johnson counter, etc.
* [`johnson_3bit.py`](johnson_3bit.py): the implementation of the simulation-based analysis of a 3-bit Johnson counter.
* [`johnson_3bit_ivp.py`](johnson_3bit_ivp.py): the same as above but using a newer solver: `solve_ivp` instead of `odeint`.
* [`test_xor.py`](test_xor.py): the implementation of xor function model and its simulation.
* [`test_xor_ivp.py`](test_xor_ivp.py): the same as above but using a newer solver: `solve_ivp` instead of `odeint`.
* [`params.py`](params.py): ranges of parameter values for the optimisation of the response of a circuit.
* [`hill_functions.py`](hill_functions.py): Hill functions of different types of biological parts (e.g., activator, repressor, inducer, etc.). Used by [`models.py`](models.py).

## Questions
Please direct your question to miha.moskon@fri.uni-lj.si.