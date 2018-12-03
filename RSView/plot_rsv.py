import pandas as pd
import numpy as np
import glob
import country_converter as coco
import plotly 
import plotly.plotly as py
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='jillianeb', api_key='eOsTljd6vVMiyuy4Msy0')
plotly.tools.set_config_file(world_readable=False,
							 sharing='private')


df_health_all = pd.read_csv('./data/health_data_all.csv')
df_health_summary = pd.read_csv('./data/health_data_summary.csv')

COLOR_DICT = ['rgba(204,204,204,1)'] * len(df_health_summary)

DATA_DICT = {
		' nnd ':'Total Neonatal Deaths', 
		' pnd ':'Total Post-Neonatal Deaths', 
		' neo9 ':'Neonatal deaths due to Acute Respiratory Infection', 
		' post9 ':'Post-neonatal deaths due to Acute Respiratory Infection', 
		' ufive9 ':'Underfive deaths due to Acute Respiratory Infection',
		' rneo9 ':'Neonatal death rate from Acute Respiratory Infection (per 1000 live births)',
		' rpost9 ':'Post-neonatal death rate from Acute Respiratory Infection (per 1000 live births)',
		' rufive9 ':'Underfive death rate from Acute Respiratory Infection (per 1000 live births)',
		'fneo9':'Percent Neonatal deaths due to Acute Respiratory Infection',
		'fpost9':'Percent Post-neonatal deaths due to Acute Respiratory Infection',
		'fufive9':'Percent Underfive deaths due to Acute Respiratory Infection'}

def input_to_country(country_input):
	if country_input == 'Global':
		return 'Global'
	else:
		country =  coco.convert(names=country_input, to='name_short')
		return country


def is_country_present(country):
	iso3 = coco.convert(names=country, to='ISO3')
	# process some error if coco can't convert to a country
	
	in_dataset = iso3 in country_codes
	return in_dataset




def plot_summary(column, country=None):
	##
	# default: plot 
	
	COLOR_HIGHLIGHT = COLOR_DICT.copy()
	
	df_sorted = df_health_summary.sort_values(column)
	df_sorted = df_sorted.reset_index(drop=True)

	if country != None:
		country_short = input_to_country(country)
		highlight_index = df_sorted.index[df_sorted['country_short'] == country_short].values[0]
		#highlight_index = 186
		COLOR_HIGHLIGHT[highlight_index] = 'rgba(222,45,38,0.8)'

	trace1 = go.Bar(
		x= df_sorted['country_short'],
		y=df_sorted[column],
		name='neo9',
		marker=dict(
			color=COLOR_HIGHLIGHT
			),
	)

	data = [trace1]
	layout = go.Layout(
		title = DATA_DICT[column] + '<br> Averaged from 2000-2016',
		yaxis=dict(
			#title='Percent',
			titlefont=dict(
				size=16,
				color='rgb(107, 107, 107)'
			),
			tickfont=dict(
				size=14,
				color='rgb(107, 107, 107)'
			)
		),
	)

	fig = go.Figure(data=data, layout=layout)

	return py.iplot(fig, filename='stacked-bar', world_readable=True)


def plot_country(column, country):
	
	country_short = input_to_country(country)

	df_country1 = df_health_all[(df_health_all['country_short'] == country_short)]

	trace1 = go.Bar(
		x= df_country1['year'],
		y=df_country1[column],
		name=DATA_DICT[column] + ' in ' + country,
		marker=dict(
			color=COLOR_DICT
			),
	)

	data = [trace1]
	layout = go.Layout(
		title = DATA_DICT[column] + ' in ' + country,
		yaxis=dict(
			#title='Averaged from 2000-2016',
		),
	)


	fig = go.Figure(data=data, layout=layout)
	
	return py.iplot(fig, filename='stacked-bar', world_readable=True)
