class Paperboy:
    """class describing a paperboy"""


    def __init__ (self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__ (self):
        return "name: {} experience: {} earnings: ${:.2f}".format(self.name, self.experience, self.earnings)

# Every day, each paperboy is given a house number to start at and a house number to finish at. They get paid $0.25
# for every paper they deliver and $0.50 for every paper over their quota. If at the end of the day they haven't met
# their quota, they lose $2.
#
# The minimum number of papers to deliver is 50. The quota is calculated as half of your experience added to the minimum.
# So the first time a paperboy makes a delivery, the quota is 50. The next time, the quote is 50 plus half the number
# of papers that the paperboy has delivered in the past. In this way the quota should increase after every delivery the
# paperboy makes.

    def deliver(self, start_house, end_house)
        

    def quota(self):
        if self.experience < 50:
            self.earnings -= 2

bob = Paperboy('Tony')

print(bob)
