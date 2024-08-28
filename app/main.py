import utils
import read_csv
import charts
import pandas as pd

def run():
  
  ## Datos mundiales
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart('World_Population_Percentage', countries, percentages)

  ## Datos por pais
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    charts.generate_pie_chart(country['Country'], labels, values)
    #print(country['Country'], labels, values)

if __name__ == '__main__':
  run()