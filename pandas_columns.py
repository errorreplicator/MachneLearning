ds.rename(columns={'col1':'First','col2':'2nd','col3':'3rd','Unnamed: 4':'4th'}, inplace=True)
ds.drop('Unnamed: 0',1,inplace=True)
print(ds.loc[1:4,'2nd':])
ds = pd.read_csv('census.dat',names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])
print(ds['capital-gain'][ds['capital-gain'] == '?'])


ds = pd.DataFrame(np.random.choice([0.9,4.1,'2ta',np.nan], size=(10,5)),columns=['fir','sec','thir','4th','5th'])