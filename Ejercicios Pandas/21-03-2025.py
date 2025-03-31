import pandas as pd

pd.__version__


df_profesores1=pd.DataFrame({

        "nombre":["Jaime","Alma","Armando","Sergio"],

        "apellido_paterno":["Minor","Vazquez","Alvarez","Moreno"],

         "apellido_materno":["Gomez","Sanchez","Galvan","Soto"]

        })


print(df_profesores1)

print(type(df_profesores1))


df_archivo_1=pd.read_csv("Sacramentorealestatetransactions.csv")

print(df_archivo_1)

# primeros 5 elementos
print('Primeros 5 elementos:')
print(df_archivo_1.head())

# 20 elementos de la lista
print('20 elementos:')
print(df_archivo_1.head(20))

#Los últimos t elementos
print('Últimos 5 elementos:')
print(df_archivo_1.tail())


#Ver los tiposy de datos

print('Tipos de datos:')
print(df_archivo_1.dtypes)

#estadísticas básicas

print('Estadísticas:')
print(df_archivo_1.describe())


print(df_archivo_1.loc[100])


print (df_archivo_1["city"])


print(df_archivo_1["city"]=="SACRAMENTO")

print(df_archivo_1.sort_values(by="city",ascending=True))

print('Ejercicio:')

city="SACRAMENTO"
beds=3
price=100000
print(df_archivo_1.query("city==@city and beds==@beds and price>@price"))

#cama=3
#$>100 000

#print(df_archivo_1.to_excel("Sacramentorealestatetransactions.xlsx",sheet_name="datos"))