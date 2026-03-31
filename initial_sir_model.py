import matplotlib.pyplot as plt

'''
- initial version of the SIR model's components as derivatives with respect to 
  time
- graphs of dS/dt, dI/dt, and dR/dt show the rate of increase/decrease over time
- set constants for population (n), beta (infection rate), gamma (recovery rate),
  sInitial (initial susceptible #), iInitial (initial infected #), and rInitial 
  (initial recovered #)
'''

# initial constant values 
N = 10000; # number of people in the population
beta = 0.5 # 2 infected people infects roughly 1 person
gamma = 0.07 # average recovery time is 1/0.07 ~ 14 days
days = 30

# lists with the initial values
susceptible = [9999]
infected = [1]
recovered = [0]
daysList = list(range(days+1))

for i in range(days):
    # calculating rate of change per day, respectively
    dS = -(beta * infected[-1] * susceptible[-1])/N
    dI = (beta * infected[-1] * susceptible[-1])/N - gamma * infected[-1]
    dR = gamma * infected[-1]

    # adding new numbers to the list, which shows number of susceptible, infected, and recovered by day
    susceptible.append(susceptible[-1] + dS)
    infected.append(infected[-1] + dI)
    recovered.append(recovered[-1] + dR)

# graphing the lists using matplotlib
plt.plot(daysList, susceptible)
plt.plot(daysList, infected)
plt.plot(daysList, recovered)
plt.xlabel("Days")
plt.ylabel("Population")
plt.grid(True)

plt.show()




 

# todo - make into a function where the user can put in their own values?

    
