df1 = pd.DataFrame()
df1['rge'], df1['ht'] = df2['Rge'], df2['Ht']
df_1 = pd.melt(df1, id_vars='ht', value_name='Rge').sort_values(by='ht')
df_1.drop('variable', axis=1, inplace=True)
df_1.set_index('ht', inplace=True)
df_1.head(50)
