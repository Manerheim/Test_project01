import pandas as pd



nyfil = 'C:\\Users\\danie\\Documents\\Python\\Diverse øvelser\\Test_project01\\Differences in column\\EDE_NEW.csv'
gammelfil = 'C:\\Users\\danie\\Documents\\Python\\Diverse øvelser\\Test_project01\\Differences in column\\EDE_OLD.csv'

nf = pd.read_csv(nyfil)
gf = pd.read_csv(gammelfil)

df_nf = pd.DataFrame(nf)
df_gf = pd.DataFrame(gf)

#df_concat = pd.concat([df_nf, df_gf]).drop_duplicates(keep=False)   
#
#
#df_endring = []

df_unique = (pd.concat([df_nf,df_gf])
       .drop_duplicates(keep=False)
       .drop_duplicates(subset='hei.hei.hei1', keep='last')
      )

df_unique_new = pd.merge(df_unique,df_nf, how='inner')

df_unique_old = pd.merge(df_unique,df_gf, how='inner')


#for index, row in df_concat.iterrows():
#    if row not in df_gf:
#        df_endring.append(row)
        
print(df_unique_new)
print(df_unique_old)

