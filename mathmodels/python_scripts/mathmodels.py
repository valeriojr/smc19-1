import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

beds = 400      # numero de leitos
icu_beds = 150  # leitos de uti

# numeros absolutos
population_by_age = {
    "0-9":   137952+134131+152581+147534,
    "10-19": 156445+156547+170956+167207,
    "20-29": 130805+141199+140817+149240,
    "30-39": 100073+111840+117491+128978,
    "40-49": 76368+85274+91125+101962,
    "50-59": 51176+60372+62174+71484,
    "60-69": 30936+36630+41368+47640,
    "70-79": 13872+18675+21930+27457,
    "80+":   163+333+776+1229+2066+3195+4251+5881+8442+11919
}

population_total = 0
for age, population in population_by_age.items():
    population_total += population

population_proportion = {
    "0-9":   population_by_age["0-9"] / population_total,
    "10-19": population_by_age["10-19"] / population_total,
    "20-29": population_by_age["20-29"] / population_total,
    "30-39": population_by_age["30-39"] / population_total,
    "40-49": population_by_age["40-49"] / population_total,
    "50-59": population_by_age["50-59"] / population_total,
    "60-69": population_by_age["60-69"] / population_total,
    "70-79": population_by_age["70-79"] / population_total,
    "80+":   population_by_age["80+"] / population_total
}

def proportions(S, I, R, symptomatic=0.2):
  # proporcoes
  Ip = {
      "0-9":   population_proportion["0-9"] * I * symptomatic,
      "10-19": population_proportion["10-19"] * I * symptomatic,
      "20-29": population_proportion["20-29"] * I * symptomatic,
      "30-39": population_proportion["30-39"] * I * symptomatic,
      "40-49": population_proportion["40-49"] * I * symptomatic,
      "50-59": population_proportion["50-59"] * I * symptomatic,
      "60-69": population_proportion["60-69"] * I * symptomatic,
      "70-79": population_proportion["70-79"] * I * symptomatic,
      "80+":   population_proportion["80+"] * I * symptomatic
  }

  Sp = {
      "0-9":   population_proportion["0-9"] * S,
      "10-19": population_proportion["10-19"] * S,
      "20-29": population_proportion["20-29"] * S,
      "30-39": population_proportion["30-39"] * S,
      "40-49": population_proportion["40-49"] * S,
      "50-59": population_proportion["50-59"] * S,
      "60-69": population_proportion["60-69"] * S,
      "70-79": population_proportion["70-79"] * S,
      "80+":   population_proportion["80+"] * S
  }

  Rp = {
      "0-9":   population_proportion["0-9"] * R,
      "10-19": population_proportion["10-19"] * R,
      "20-29": population_proportion["20-29"] * R,
      "30-39": population_proportion["30-39"] * R,
      "40-49": population_proportion["40-49"] * R,
      "50-59": population_proportion["50-59"] * R,
      "60-69": population_proportion["60-69"] * R,
      "70-79": population_proportion["70-79"] * R,
      "80+":   population_proportion["80+"] * R
  }

  H = {
      "0-9":    0.1/100 * Ip["0-9"],
      "10-19":  0.3/100 * Ip["10-19"],
      "20-29":  1.2/100 * Ip["20-29"],
      "30-39":  3.2/100 * Ip["30-39"],
      "40-49":  4.9/100 * Ip["40-49"],
      "50-59": 10.2/100 * Ip["50-59"],
      "60-69": 16.6/100 * Ip["60-69"],
      "70-79": 24.3/100 * Ip["70-79"],
      "80+":   27.3/100 * Ip["80+"]
  }

  ICU = {
      "0-9":      5/100 * H["0-9"],
      "10-19":    5/100 * H["10-19"],
      "20-29":    5/100 * H["20-29"],
      "30-39":    5/100 * H["30-39"],
      "40-49":  6.3/100 * H["40-49"],
      "50-59": 12.2/100 * H["50-59"],
      "60-69": 27.4/100 * H["60-69"],
      "70-79": 43.2/100 * H["70-79"],
      "80+":   70.9/100 * H["80+"]
  }

  # D = {
  #     "0-9":   0.002/100 * ICU["0-9"],
  #     "10-19": 0.006/100 * ICU["10-19"],
  #     "20-29":  0.03/100 * ICU["20-29"],
  #     "30-39":  0.08/100 * ICU["30-39"],
  #     "40-49":  0.15/100 * ICU["40-49"],
  #     "50-59":   0.6/100 * ICU["50-59"],
  #     "60-69":   2.2/100 * ICU["60-69"],
  #     "70-79":   5.1/100 * ICU["70-79"],
  #     "80+":     9.3/100 * ICU["80+"]
  # }
  death_constant = 1e-3
  D = {
      "0-9":   death_constant * Ip["0-9"],
      "10-19": death_constant * Ip["10-19"],
      "20-29": death_constant * Ip["20-29"],
      "30-39": death_constant * Ip["30-39"],
      "40-49": death_constant * Ip["40-49"],
      "50-59": death_constant * Ip["50-59"],
      "60-69": death_constant * Ip["60-69"],
      "70-79": death_constant * Ip["70-79"],
      "80+":   death_constant * Ip["80+"]
  }
  return (Sp, Ip, Rp, H, ICU, D)

# The SIR model differential equations.
def deriv(y, t, N , beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def compute_sir(N=1000, I0=1, R0=0, beta=1.75, gamma=0.5, days=160):
    """
    Total population, N.
    Initial number of infected and recovered individuals, I0 and R0.
    Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
    """
    
    # Everyone else, S0, is susceptible to infection initially.
    S0 = N - I0 - R0
    
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


#### BEGIN COLOCAR NA VIEW
days = 200
infected = 17

S, I, R = compute_sir(N=population_total, I0=infected, days=days)
plot_sir(S, I, R, days)

Sp, Ip, Rp, H, ICU, D = proportions(S, I, R)

for k, v in D.items():
  print(k, sum(D[k]))

for k, v in Ip.items():
  for idx, _infected in enumerate(v):
    if _infected > beds:
      print(k, idx)
      break
#### END


#### BEGIN SEIR BÁSICO
def base_seir_model(init_vals, params, t):
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
    S = np.array(S)*population_total
    E = np.array(E)*population_total
    I = np.array(I)*population_total
    R = np.array(R)*population_total
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

#### BEGIN COLOCAR NA VIEW
# Define parameters
t_max = 200
dt = 1
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = population_total
init_vals = 1 - 1/N, 1/N, 0, 0
alpha = 0.2
beta = 1.75
gamma = 0.5
params = alpha, beta, gamma
# Run simulation
S, E, I, R = base_seir_model(init_vals, params, t)

plot_seir(S, E, I, R, int(t_max/dt)+1)

Sp, Ip, Rp, H, ICU, D = proportions(S, I, R)

for k, v in D.items():
  print(k, sum(D[k]))
#### END COLOCAAR NA VIEW

#### BEGIN SEIR COM DISTANCIAMENTO SOCIAL
def seir_model_with_soc_dist(init_vals, params, t, N):
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

#### BEGIN COLOCAR NA VIEW
# Define parameters
t_max = 200
dt = 1
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = population_total
infected = 300
init_vals = 1-infected/N, 0, infected/N, 0
alpha = 0.2
beta = 1.75
gamma = 0.5
rho = 1  # social distancing: 0=all quarentined, 1=free to walk
params = alpha, beta, gamma, rho
# Run simulation
S, E, I, R = seir_model_with_soc_dist(init_vals, params, t, N)

plot_seir(S, E, I, R, int(t_max/dt)+1)
#### END COLOCAR NA VIEW

#### BEGIN NÃO SEI O QUE SIGNIFICA

#### END NÃO SEI O QUE SIGNIFICA