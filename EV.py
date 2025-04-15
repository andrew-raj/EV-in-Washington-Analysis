import pandas as pd
import matplotlib.pyplot as plt


csv_path = 'Electric_Vehicle_Population_Data.csv'

df=pd.read_csv(csv_path)

max = df['Model Year'].max()
min = df['Model Year'].min()
makes = df['Make'].value_counts()
population = df['VIN (1-10)'].count()
maxMake = df['Make'].value_counts().idxmax()
model = df['Model'].value_counts()
popModel = df['Model'].value_counts().idxmax()

makes.plot(kind = 'pie',autopct = '%1.1f%%',startangle=0,figsize=(10,10))


print('The make of the vehicles range from', min, 'to', max)
print("The car brand with the most was", maxMake, "with", makes.max(), "out of the", population, "cars. This is", str(round((makes.max()/population)*100,1)) + "% ", "of the cars.")
print('The most popular model was the', popModel + ", which was", model.max(), "of the", makes.max(), "from", maxMake)


plt.title('EV Makes')
plt.ylabel('')
plt.show()