import pandas as pd


csv_path = 'Electric_Vehicle_Population_Data.csv'

df=pd.read_csv(csv_path)

max = df['Model Year'].max()
min = df['Model Year'].min()
makes = df['Make'].value_counts()
population = df['VIN (1-10)'].count()
maxMake = df['Make'].value_counts().idxmax()
model = df['Model'].value_counts()
popModel = df['Model'].value_counts().idxmax()


print('The make of the vehicles range from', min, 'to', max)
print("The car brand with the most was", maxMake, "with", makes.max(), "out of the", population, "cars.")
print('The most popular model was the', popModel + ", which was", model.max(), "of the", makes.max(), "from", maxMake)