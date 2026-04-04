import matplotlib.pyplot as plt

'''
- graphs of dS/dt, dE/dt, dV/dt, dI/dt, and dR/dt show the rate of increase/decrease over time
- Constants:
  population (n), infectionRate, incubationRate, recoverRate, vaccinationRate
  intial values of S, E, V, I, R in the list
'''

# initial parameters based on COVID-19 estimates (Delta variant, mid-2021 with vaccines ) 
N = 100000; # number of people in the population
infectionRate = 0.35 
incubationRate = 0.2 # 5 days to become infected after exposure
recoverRate = 0.1 # 10 day infectious period
vaccinationRate = 0.005 # 0.5% of susceptibles getting vaccinated per day
# to do: find real CSV dataset for the parameters

days = 100

# lists with the initial values
susceptible = [59700]

exposed = [225]
vaccinated = [20000]
infected = [75]
recovered = [20000]
daysList = list(range(days+1))

for i in range(days):
    # calculating rate of change per day, respectively
    dS = -(infectionRate * infected[-1] * susceptible[-1])/N -vaccinationRate * susceptible [-1]
    dE = (infectionRate * infected[-1] * susceptible[-1]/N) - incubationRate * exposed [-1]
    dI = incubationRate * exposed[-1] - recoverRate * infected[-1]
    dV = vaccinationRate * susceptible[-1]
    dR = recoverRate * infected[-1]

    # adding new numbers to the list, which shows number of susceptible, infected, and recovered by day
    susceptible.append(susceptible[-1] + dS)
    exposed.append(exposed[-1] + dE)
    vaccinated.append(vaccinated[-1] + dV)
    infected.append(infected[-1] + dI)
    recovered.append(recovered[-1] + dR)

# graphing the lists using matplotlib
plt.plot(daysList, susceptible, label = "Susceptible")
plt.plot(daysList, exposed, label = "Exposed")
plt.plot(daysList, vaccinated, label = "Vaccinated")
plt.plot(daysList, infected, label = "Infected")
plt.plot(daysList, recovered, label = "Recovered")
plt.xlabel("Days")
plt.ylabel("Population")
plt.title("Initial SVEIR Model with Estimated Parameters")
plt.legend()
plt.grid(True)
plt.show()



    
