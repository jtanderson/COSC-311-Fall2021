import pandas as pd
from matplotlib import pyplot as plt

football_data = { 
    'year': [
        2010, 2011, 2012,
        2010, 2011, 2012,
        2010, 2011, 2012
        ],
    'team': [
        'FCBarcelona', 'FCBarcelona',
        'FCBarcelona', 'RMadrid',
        'RMadrid', 'RMadrid',
        'ValenciaCF', 'ValenciaCF',
        'ValenciaCF'
    ],
    'wins':[30 , 28 , 32 , 29 , 32 , 26 , 21 , 17 , 19] ,
    'draws': [6 , 7 , 4 , 5 , 4 , 7 , 8 , 10 , 8] ,
    'losses': [2 , 3 , 2 , 4 , 2 , 5 , 9 , 11 , 11]
}

football_df = pd.DataFrame(football_data)

print(football_df)

football_df.plot.bar(x='year', y='wins')
plt.show()

a = 'hello world'

print(a)

#plt.plot([1,2,3],[2,3,4])

