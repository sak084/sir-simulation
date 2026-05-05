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
    def plot(self, daysList, susceptible, exposed, vaccinated, infected, recovered):
        plt.plot(daysList, susceptible, label = "Susceptible")
        plt.plot(daysList, exposed, label = "Exposed")
        plt.plot(daysList, vaccinated, label = "Vaccinated")
        plt.plot(daysList, infected, label = "Infected")
        plt.plot(daysList, recovered, label = "Recovered")
        plt.xlabel("Days")
        plt.ylabel("Population")
        plt.title("Initial SEVIR Model with Estimated Parameters")
        plt.legend()
        plt.grid(True)
        plt.show()

# main method that calls the methods methodically, eventually producing a graph
def main():
    model1 = SEVIR(100000, 0.35, 0.2, 0.1, 0.005, 100, 59700, 225, 20000, 75, 20000) 
    s1, e1, v1, i1, r1 = model1.addCounts()
    daysList1 = model1.getDaysList()
    model1.plot(daysList1, s1, e1, v1, i1, r1)

    #todo: generate more plots to compare vaccination scenarios

# run main() if the file is executed properly
if __name__ == "__main__":
    main()


    
