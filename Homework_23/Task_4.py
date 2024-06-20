import matplotlib.pyplot as plt

entertainment = ['restaurant', 'taxi', 'excursion']
percentages = [50, 25, 25]

plt.figure()
plt.pie(percentages, labels=entertainment, autopct='%1.1f%%')
plt.axis()

plt.legend(title='Entertainment')
plt.title('Entertainment expenses as a percentage')

plt.show()
