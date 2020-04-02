import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# The SIR model differential equations.
def deriv(y, t, N , beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def compute_sir(N=1000, S0=0, I0=1, R0=0, beta=1.75, gamma=0.5, days=160):
    """
    Total population, N.
    Initial number of infected and recovered individuals, I0 and R0.
    Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
    """
    
    # A grid of time points (in days)
    #t = np.linspace(0, 160, 160)
    t = np.linspace(0, days, days)

    # Initial conditions vector
    y0 = S0, I0, R0
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T

    return (S, I, R)

def plot_sir(S, I, R, days):
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    t = np.linspace(0, days, days)
    plt.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    plt.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
    plt.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    legend = plt.legend()
    legend.get_frame().set_alpha(0.5)


#### BEGIN SEIR BÁSICO
def base_seir_model(N, init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    S = np.array(S)*N
    E = np.array(E)*N
    I = np.array(I)*N
    R = np.array(R)*N
    return (S, E, I, R)

def plot_seir(S, E, I, R, days):
    # Plot the data on three separate curves for S(t), E(t), I(t) and R(t)
    t = np.linspace(0, days, days)
    plt.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    plt.plot(t, E/1000, 'k', alpha=0.5, lw=2, label='Exposed')
    plt.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
    plt.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    legend = plt.legend()
    legend.get_frame().set_alpha(0.5)
#### END SEIR BÁSICO

#### BEGIN SEIR COM DISTANCIAMENTO SOCIAL
def seir_model_with_soc_dist(N, init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma, rho = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (rho*beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (rho*beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    S = np.array(S)*N
    E = np.array(E)*N
    I = np.array(I)*N
    R = np.array(R)*N
    return (S, E, I, R)

def plot_seir_with_soc_dist(S, E, I, R, days):
    # Plot the data on three separate curves for S(t), E(t), I(t) and R(t)
    t = np.linspace(0, days, days)
    plt.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    plt.plot(t, E/1000, 'k', alpha=0.5, lw=2, label='Exposed')
    plt.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
    plt.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    plt.grid
    legend = plt.legend()
    legend.get_frame().set_alpha(0.5)
#### END SEIR COM DISTANCIAMENTO SOCIAL