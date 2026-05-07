import matplotlib.pyplot as plt

class SEVIR:
    # constructor that initializes relevant rates, population, days, and initial numbers
    # todo: break this up to make it more readable if possible
    def __init__ (self, N, infectionRate, incubationRate, recoverRate, vaccinationRate, days, initialSusceptible, initialExposed, initialVaccinated, initialInfected, initialRecovered):
        self.N = N
        self.infectionRate = infectionRate
        self.incubationRate = incubationRate
        self.recoverRate = recoverRate
        self.vaccinationRate = vaccinationRate
        self.days = days
        self.initialSusceptible = initialSusceptible
        self.initialExposed = initialExposed
        self.initialVaccinated = initialVaccinated
        self.initialInfected = initialInfected
        self.initialRecovered = initialRecovered

    # calculates, S, E, V, I, and R values for each day
    # appends the values to a list to be graphed by plot()
    def addCounts(self):
        susceptible = [self.initialSusceptible]
        exposed = [self.initialExposed]
        vaccinated = [self.initialVaccinated]
        infected = [self.initialInfected]
        recovered = [self.initialRecovered]

        for i in range(self.days):
            # calculating rate of change per day, respectively
            dS = -(self.infectionRate * infected[-1] * susceptible[-1])/self.N - self.vaccinationRate * susceptible [-1]
            dE = (self.infectionRate * infected[-1] * susceptible[-1]/self.N) - self.incubationRate * exposed [-1]
            dI = self.incubationRate * exposed[-1] - self.recoverRate * infected[-1]
            dV = self.vaccinationRate * susceptible[-1]
            dR = self.recoverRate * infected[-1]

            # adding new numbers to the list, which shows number of susceptible, infected, and recovered by day
            susceptible.append(susceptible[-1] + dS)
            exposed.append(exposed[-1] + dE)
            vaccinated.append(vaccinated[-1] + dV)
            infected.append(infected[-1] + dI)
            recovered.append(recovered[-1] + dR)

        return susceptible, exposed, vaccinated, infected, recovered

    # helper function to get the days as a list to plot as x
    def getDaysList (self):
        daysList = []
        for i in range(self.days+1):
            daysList.append(i)
        return daysList

    # graphing the lists using matplotlib
    def plot(self, ax, daysList, susceptible, exposed, vaccinated, infected, recovered):
        ax.plot(daysList, susceptible, label = "Susceptible")
        ax.plot(daysList, exposed, label = "Exposed")
        ax.plot(daysList, vaccinated, label = "Vaccinated")
        ax.plot(daysList, infected, label = "Infected")
        ax.plot(daysList, recovered, label = "Recovered")
        ax.set_xlabel("Days", fontsize = 10)
        ax.set_ylabel("Population", fontsize = 10)
        ax.legend()
        ax.grid(True)

# main method that plots four sevir graphs with various vaccination rates
def main():
    # making four separate subplots
    fig, axs = plt.subplots(2,2)
    plt.title = "SEVIR Model Comparison with vaccination rates"

    # subplot #1 (upper left)- 5% vaccination rate
    model1 = SEVIR(100000, 0.35, 0.2, 0.1, 0.05, 100, 59700, 225, 20000, 75, 20000) 
    s1, e1, v1, i1, r1 = model1.addCounts()
    daysList1 = model1.getDaysList()
    model1.plot(axs[0][0], daysList1, s1, e1, v1, i1, r1)
    axs[0][0].set_title("5% vaccination rate", fontsize = 10)

    # subplot #2 (upper right)- 10% vaccination rate
    model2 = SEVIR(100000, 0.35, 0.2, 0.1, 0.1, 100, 59700, 225, 20000, 75, 20000) 
    s2, e2, v2, i2, r2 = model2.addCounts()
    daysList2 = model2.getDaysList()
    model2.plot(axs[0][1], daysList2, s2, e2, v2, i2, r2)
    axs[0][1].set_title("10% vaccination rate", fontsize = 10)

    # subplot #3 (lower left)- 30% vaccination rate
    model3 = SEVIR(100000, 0.35, 0.2, 0.1, 0.3, 100, 59700, 225, 20000, 75, 20000) 
    s3, e3, v3, i3, r3 = model3.addCounts()
    daysList3 = model3.getDaysList()
    model3.plot(axs[1][0], daysList3, s3, e3, v3, i3, r3)
    axs[1][0].set_title("30% vaccination rate", fontsize = 10)

    # subplot #4 (lower right)- 70% vaccination rate
    model4 = SEVIR(100000, 0.35, 0.2, 0.1, 0.7, 100, 59700, 225, 20000, 75, 20000) 
    s4, e4, v4, i4, r4 = model4.addCounts()
    daysList4 = model4.getDaysList()
    model4.plot(axs[1][1], daysList4, s4, e4, v4, i4, r4)
    axs[1][1].set_title("70% vaccination rate", fontsize = 10)

    plt.show()

    #todo: make the arguments more realistic with real data

# run main() if the file is executed properly
if __name__ == "__main__":
    main()
