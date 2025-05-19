from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/excercise_data/exercise02_formatted.csv') 

print(data.head())
print(data.describe())

if data['Temperature / °C'].max() > 39:  
    print('The temperature is greater than 39°C at some point')
else:
    print('The temperature is always less than 39°C')

sns.lineplot(x='Time / s', y='A12', data=data)
plt.show()
plt.savefig('data/excercise_data/A12.png', dpi=300, bbox_inches='tight')

