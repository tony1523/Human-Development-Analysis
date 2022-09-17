import pandas as pd
import os
import math
import plotly.express as plx
import plotly.io as pio


def region_by_country():
	"""
	Pandas dataframe with country and region in data
	:return: dataframe
	"""
	return pd.DataFrame(data=[['Afghanistan','Asia & Pacific','Global South'],
	                          ['Aland Islands','Europe','Global North'],
							['Albania','Europe','Global North'],
							['Algeria','Arab States','Global South'],
							['American Samoa','Asia & Pacific','Global South'],
							['Andorra','Europe','Global North'],
							['Angola','Africa','Global South'],
							['Anguilla','South/Latin America','Global South'],
							['Antarctica','Asia & Pacific','Global South'],
							['Antigua and Barbuda','South/Latin America','Global South'],
							['Argentina','South/Latin America','Global South'],
							['Armenia','Europe','Global North'],
							['Aruba','South/Latin America','Global South'],
							['Australia','Asia & Pacific','Global North'],
							['Austria','Europe','Global North'],
							['Azerbaijan','Asia & Pacific','Global North'],
							['Bahamas','South/Latin America','Global South'],
							['Bahrain','Arab States','Global South'],
							['Bangladesh','Asia & Pacific','Global South'],
							['Barbados','South/Latin America','Global South'],
							['Belarus','Europe','Global North'],
							['Belgium','Europe','Global North'],
							['Belize','South/Latin America','Global South'],
							['Benin','Africa','Global South'],
							['Bermuda','South/Latin America','Global South'],
							['Bhutan','Asia & Pacific','Global South'],
							['Bolivia (Plurinational State of)','South/Latin America','Global South'],
							['Bosnia and Herzegovina','Europe','Global North'],
							['Botswana','Africa','Global South'],
							['Bouvet Island','South/Latin America','Global South'],
							['Brazil','South/Latin America','Global South'],
							['British Indian Ocean Territory','Asia & Pacific','Global South'],
							['Brunei Darussalam','Asia & Pacific','Global South'],
							['Bulgaria','Europe','Global North'],
							['Burkina Faso','Africa','Global South'],
							['Burundi','Africa','Global South'],
							['Cambodia','Asia & Pacific','Global South'],
							['Cameroon','Africa','Global South'],
							['Canada','North America','Global North'],
							['Cabo Verde','Africa','Global South'],
							['Cayman Islands','South/Latin America','Global South'],
							['Central African Republic','Africa','Global South'],
							['Chad','Africa','Global South'],
							['Chile','South/Latin America','Global South'],
							['China','Asia & Pacific','Global South'],
							['Christmas Island','Asia & Pacific','Global South'],
							['Cocos (Keeling) Islands','Asia & Pacific','Global South'],
							['Colombia','South/Latin America','Global South'],
							['Comoros','Arab States','Global South'],
							['Congo','Africa','Global South'],
							['Congo (Democratic Republic of the)','Africa','Global South'],
							['Cook Islands','Asia & Pacific','Global South'],
							['Costa Rica','South/Latin America','Global South'],
							["Côte d'Ivoire",'Africa','Global South'],
							['Croatia','Europe','Global North'],
							['Cuba','South/Latin America','Global South'],
							['Cyprus','Europe','Global North'],
							['Czech Republic','Europe','Global North'],
							['Denmark','Europe','Global North'],
							['Djibouti','Arab States','Global South'],
							['Dominica','South/Latin America','Global South'],
							['Dominican Republic','South/Latin America','Global South'],
							['Ecuador','South/Latin America','Global South'],
							['Egypt','Middle east','Global South'],
							['El Salvador','South/Latin America','Global South'],
							['Equatorial Guinea','Africa','Global South'],
							['Eritrea','Africa','Global South'],
							['Estonia','Europe','Global North'],
							['Ethiopia','Africa','Global South'],
							['Falkland Islands (Malvinas)','South/Latin America','Global South'],
							['Faroe Islands','Europe','Global North'],
							['Fiji','Asia & Pacific','Global South'],
							['Finland','Europe','Global North'],
							['France','Europe','Global North'],
							['France, Metropolitan','Europe','Global North'],
							['French Guiana','South/Latin America','Global South'],
							['French Polynesia','Asia & Pacific','Global South'],
							['French Southern Territories','Asia & Pacific','Global South'],
							['Gabon','Africa','Global South'],
							['Gambia','Africa','Global South'],
							['Georgia','Europe','Global North'],
							['Germany','Europe','Global North'],
							['Ghana','Africa','Global South'],
							['Gibraltar','Europe','Global North'],
							['Greece','Europe','Global North'],
							['Greenland','Europe','Global North'],
							['Grenada','South/Latin America','Global South'],
							['Guadeloupe','South/Latin America','Global South'],
							['Guam','Asia & Pacific','Global South'],
							['Guatemala','South/Latin America','Global South'],
							['Guernsey','Europe','Global North'],
							['Guinea','Africa','Global South'],
							['Guinea-Bissau','Africa','Global South'],
							['Guyana','South/Latin America','Global South'],
							['Haiti','South/Latin America','Global South'],
							['Heard Island and McDonald Islands','Asia & Pacific','Global South'],
							['Holy See (Vatican City State)','Europe','Global North'],
							['Honduras','South/Latin America','Global South'],
							['Hong Kong, China (SAR)','Asia & Pacific','Global South'],
							['Hungary','Europe','Global North'],
							['Iceland','Europe','Global North'],
							['India','Asia & Pacific','Global South'],
							['Indonesia','Asia & Pacific','Global South'],
							['Iran (Islamic Republic of)','Middle east','Global South'],
							['Iraq','Middle east','Global South'],
							['Ireland','Europe','Global North'],
							['Isle of Man','Europe','Global North'],
							['Israel','Europe','Global North'],
							['Italy','Europe','Global North'],
							['Jamaica','South/Latin America','Global South'],
							['Japan','Asia & Pacific','Global North'],
							['Jersey','Europe','Global North'],
							['Jordan','Middle east','Global South'],
							['Kazakhstan','Asia & Pacific','Global North'],
							['Kenya','Africa','Global South'],
							['Kiribati','Asia & Pacific','Global South'],
							["Korea, Democratic People's Republic of",'Asia & Pacific','Global South'],
							['Korea (Republic of)','Asia & Pacific','Global North'],
							['Kuwait','Middle east','Global South'],
							['Kyrgyzstan','Asia & Pacific','Global South'],
							["Lao People's Democratic Republic",'Asia & Pacific','Global South'],
							['Latvia','Europe','Global North'],
							['Lebanon','Middle east','Global South'],
							['Lesotho','Africa','Global South'],
							['Liberia','Africa','Global South'],
							['Libya','Middle east','Global South'],
							['Liechtenstein','Europe','Global North'],
							['Lithuania','Europe','Global North'],
							['Luxembourg','Europe','Global North'],
							['Macau','Asia & Pacific','Global South'],
							['The former Yugoslav Republic of Macedonia','Europe','Global North'],
							['Madagascar','Africa','Global South'],
							['Malawi','Africa','Global South'],
							['Malaysia','Asia & Pacific','Global South'],
							['Maldives','Asia & Pacific','Global South'],
							['Mali','Africa','Global South'],
							['Malta','Europe','Global North'],
							['Marshall Islands','Asia & Pacific','Global South'],
							['Martinique','South/Latin America','Global South'],
							['Mauritania','Arab States','Global South'],
							['Mauritius','Africa','Global South'],
							['Mayotte','Africa','Global South'],
							['Mexico','South/Latin America','Global South'],
							['Micronesia (Federated States of)','Asia & Pacific','Global South'],
							['Moldova (Republic of)','Europe','Global North'],
							['Monaco','Europe','Global North'],
							['Mongolia','Asia & Pacific','Global South'],
							['Montenegro','Europe','Global North'],
							['Montserrat','South/Latin America','Global South'],
							['Morocco','Arab States','Global South'],
							['Mozambique','Africa','Global South'],
							['Myanmar','Asia & Pacific','Global South'],
							['Namibia','Africa','Global South'],
							['Nauru','Asia & Pacific','Global South'],
							['Nepal','Asia & Pacific','Global South'],
							['Netherlands','Europe','Global North'],
							['Netherlands Antilles','South/Latin America','Global South'],
							['New Caledonia','Asia & Pacific','Global South'],
							['New Zealand','Asia & Pacific','Global North'],
							['Nicaragua','South/Latin America','Global South'],
							['Niger','Africa','Global South'],
							['Nigeria','Africa','Global South'],
							['Niue','Asia & Pacific','Global South'],
							['Norfolk Island','Asia & Pacific','Global South'],
							['Northern Mariana Islands','Asia & Pacific','Global South'],
							['Norway','Europe','Global North'],
							['Oman','Middle east','Global South'],
							['Pakistan','Asia & Pacific','Global South'],
							['Palau','Asia & Pacific','Global South'],
							['Palestine, State of','Arab States','Global South'],
							['Panama','South/Latin America','Global South'],
							['Papua New Guinea','Asia & Pacific','Global South'],
							['Paraguay','South/Latin America','Global South'],
							['Peru','South/Latin America','Global South'],
							['Philippines','Asia & Pacific','Global South'],
							['Pitcairn Islands','Asia & Pacific','Global South'],
							['Poland','Europe','Global North'],
							['Portugal','Europe','Global North'],
							['Puerto Rico','South/Latin America','Global South'],
							['Qatar','Middle east','Global South'],
							['Reunion','Asia & Pacific','Global South'],
							['Romania','Europe','Global North'],
							['Russian Federation','Europe','Global North'],
							['Rwanda','Africa','Global South'],
							['Saint Barthelemy','South/Latin America','Global South'],
							['Saint Helena','Africa','Global South'],
							['Saint Kitts and Nevis','South/Latin America','Global South'],
							['Saint Lucia','South/Latin America','Global South'],
							['Saint Martin','South/Latin America','Global South'],
							['Saint Pierre and Miquelon','North America','Global North'],
							['Saint Vincent and the Grenadines','South/Latin America','Global South'],
							['Samoa','Asia & Pacific','Global South'],
							['San Marino','Europe','Global North'],
							['Sao Tome and Principe','Africa','Global South'],
							['Saudi Arabia','Middle east','Global South'],
							['Senegal','Africa','Global South'],
							['Serbia','Europe','Global North'],
							['Seychelles','Africa','Global South'],
							['Sierra Leone','Africa','Global South'],
							['Singapore','Asia & Pacific','Global North'],
							['Slovakia','Europe','Global North'],
							['Slovenia','Europe','Global North'],
							['Solomon Islands','Asia & Pacific','Global South'],
							['Somalia','Arab States','Global South'],
							['South Africa','Africa','Global South'],
							['South Georgia and the South Sandwich Islands','South/Latin America','Global South'],
							['South Sudan','Africa','Global South'],
							['Spain','Europe','Global North'],
							['Sri Lanka','Asia & Pacific','Global South'],
							['Sudan','Arab States','Global South'],
							['Suriname','South/Latin America','Global South'],
							['Svalbard and Jan Mayen','Europe','Global North'],
							['Swaziland','Africa','Global South'],
							['Sweden','Europe','Global North'],
							['Switzerland','Europe','Global North'],
							['Syrian Arab Republic','Asia & Pacific','Global South'],
							['Taiwan','Asia & Pacific','Global North'],
							['Tajikistan','Asia & Pacific','Global South'],
							['Tanzania (United Republic of)','Africa','Global South'],
							['Thailand','Asia & Pacific','Global South'],
							['Timor-Leste','Asia & Pacific','Global South'],
							['Togo','Africa','Global South'],
							['Tokelau','Asia & Pacific','Global South'],
							['Tonga','Asia & Pacific','Global South'],
							['Trinidad and Tobago','South/Latin America','Global South'],
							['Tunisia','Arab States','Global South'],
							['Turkey','Europe','Global North'],
							['Turkmenistan','Asia & Pacific','Global South'],
							['Turks and Caicos Islands','South/Latin America','Global South'],
							['Tuvalu','Asia & Pacific','Global South'],
							['Uganda','Africa','Global South'],
							['Ukraine','Europe','Global North'],
							['United Arab Emirates','Middle east','Global South'],
							['United Kingdom','Europe','Global North'],
							['United States','North America','Global North'],
							['United States Minor Outlying Islands','Asia & Pacific','Global South'],
							['Uruguay','South/Latin America','Global South'],
							['Uzbekistan','Asia & Pacific','Global South'],
							['Vanuatu','Asia & Pacific','Global South'],
							['Venezuela (Bolivarian Republic of)','South/Latin America','Global South'],
							['Viet Nam','Asia & Pacific','Global South'],
							['Virgin Islands, British','South/Latin America','Global South'],
							['Virgin Islands, U.S.','South/Latin America','Global South'],
							['Wallis and Futuna','Asia & Pacific','Global South'],
							['Western Sahara','Africa','Global South'],
							['Yemen','Middle east','Global South'],
							['Zambia','Africa','Global South'],
							['Zimbabwe','Africa','Global South']], columns=['Country', 'Region', 'Global South'])


def data_wrangglin(path: str = os.getcwd(), files: []=None):
	"""
	Preparing data for data visualization techniques
	:param path: main files location
	:default: int
	:return: pd.Dataframe
	"""
	result = pd.DataFrame.empty
	regions = region_by_country()
	try:
		if files is None:
			# reading all the files in case is need it
			genderDev = pd.read_csv(os.path.join(path, "gender_development.csv"))
			genderIneq = pd.read_csv(os.path.join(path, "gender_inequality.csv"))
			histIndex = pd.read_csv(os.path.join(path, "historical_index.csv"))
			humanDev = pd.read_csv(os.path.join(path, "human_development.csv"))
			ineqAdjust = pd.read_csv(os.path.join(path, "inequality_adjusted.csv"))
			multiPov = pd.read_csv(os.path.join(path, "multidimensional_poverty.csv"))

			# merging all the files into one
			result = pd.merge(genderIneq, genderDev, on='Country', how='outer')
			result = pd.merge(result, histIndex, on='Country', how='outer')
			result = pd.merge(result, humanDev, on='Country', how='outer')
			result = pd.merge(result, ineqAdjust, on='Country', how='outer')
			result = pd.merge(result, multiPov, on='Country', how='outer')
			# converting description airline carrier name with its code
			# getting airline carrier name from IATA code in carrier column
			result["countryRegion"] = result["Country"].apply(lambda country:
			                                                  regions[regions["Country"] == country]["Region"].values)

			result["countryRegion"] = result["countryRegion"].apply(lambda x: str(x).
			                                                  replace("[", "").
			                                                  replace("]", "")).replace("'", "")

			result.to_excel(os.path.join(path, "result1.xlsx"))
		else:
			for counter, fileName in enumerate(files):
				if counter == 0:
					result = pd.read_csv(os.path.join(path, fileName))

				else:
					result = pd.merge(result, pd.read_csv(os.path.join(path, fileName)))

			result["countryRegion"] = result["Country"].apply(lambda country:
			                                                  regions[regions["Country"] == country]["Region"].values)

			result["countryRegion"] = result["countryRegion"].apply(lambda x:
			                                                  str(x).replace("[", "").replace("]", "").replace("'",
			                                                                                                    ""))


	except Exception as e:
		print(str(e))

	return result


def biggest_developmentRegion():
	# what is the Region with biggest development on human development between 2011 and 2013?
	data = data_wrangglin(files=["human_development.csv", "historical_index.csv"])
	countries = data[data["countryRegion"] != ""]
	countries["Gross National Income (GNI) per Capita"] = countries["Gross National Income (GNI) per Capita"].apply(
		lambda value:
		float(str(value).replace(",", ""))
	)
	result = countries.groupby(by=["countryRegion"]).agg(
	    LEB_S=("Life Expectancy at Birth", "sum"),
	    EYE_S=("Expected Years of Education", "sum"),
	    MYE_S=("Mean Years of Education", "sum"),
	    GNI_S=("Gross National Income (GNI) per Capita", "sum"),
		HDI11=("Human Development Index (2011)", "sum"),
		HDI12=("Human Development Index (2012)", "sum"),
		HDI13=("Human Development Index (2013)", "sum"),
		HDI14=("Human Development Index (2014)", "sum"),
		Count=("Country", "count")).reset_index().rename(columns={"countryRegion": "Region"})

	result["Health Index"] = result.apply(lambda value:
	                                     (value["LEB_S"] - (20*value["Count"]))/((85*value["Count"])-(20*value["Count"]))
	                                     ,axis=1)

	result["Education Index"] = result.apply(lambda value:
	                                        (((value["MYE_S"] - (0*value["Count"]))/((15*value["Count"])-(0*value[
		                                     "Count"]))) + ((value["EYE_S"] - (0*value["Count"]))/((18*value[
		                                        "Count"])-(0*value[
		                                     "Count"]))) )/2
	                                     ,axis=1)

	result["Income Index"] = result.apply(lambda value:
	                                        ((math.log(value["GNI_S"]) - math.log(100 * value["Count"])) / (
				                                        math.log(75000 * value["Count"]) - math.log(100 * value[
			                                        "Count"])))
	                                        , axis=1)

	result["HDI"] = result.apply(lambda r:
	                             pow((r["Health Index"]*r["Education Index"]*r["Income Index"]) ,1/3), axis=1)
	result["HDI Var 12vs11"] = result["HDI12"] - result["HDI11"]
	result["HDI Var 13vs12"] = result["HDI13"] - result["HDI12"]
	result["HDI Var 14vs12"] = result["HDI14"] - result["HDI13"]
	result["HDI 3Y Var"] = result["HDI Var 14vs12"]+result["HDI Var 13vs12"]+result["HDI Var 12vs11"]
	result["Rank 3Y Var"] = result["HDI 3Y Var"].rank(method="max", ascending=False)
	result["Rank Education"] = result["Education Index"].rank(method="max", ascending=False)
	result["Rank Income"] = result["Income Index"].rank(method="max", ascending=False)
	result["Rank Health"] = result["Health Index"].rank(method="max", ascending=False)
	result["Rank HDI"] = result["HDI"].rank(method="max", ascending=False)
	print(result)

	fig = plx.scatter_3d(result, x="Health Index",
	                     y="Education Index",
	                     z="Income Index",
	                     size= "HDI",
	                     color="HDI 3Y Var",
	                     symbol="Region")
	fig.update_layout(

	)
	fig.update_layout(title={'text': "2014 Human Development Index by Region(calc)", 'y': 0.9, 'x': 0.5, 'xanchor':
		'center', 'yanchor': 'auto'},
		legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1})
	fig.show()


def biggest_developmentCountry():
	data = data_wrangglin(files=["human_development.csv", "historical_index.csv"])
	countries = data[data["countryRegion"] != ""]
	countries["Gross National Income (GNI) per Capita"] = countries["Gross National Income (GNI) per Capita"].apply(
		lambda value:
		float(str(value).replace(",",""))
	)
	fig = plx.scatter(countries, x="Human Development Index (HDI)",
	                 y="Country", color="countryRegion",
#	                 range_x=[0, 1],
#	                 range_y=[0, 0],
#	                 text="Human Development Index (HDI)",
	                 title="Human Development Index 2014",
	                 labels={"Country": "Countries",
	                         "countryRegion": "Region",
	                         "Human Development Index (HDI)": "HDI"
	                         }
	                 )
	fig.update_layout(title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20}},
	                   xaxis=dict(title=dict(font=dict(size=20))),
	                   yaxis={'title': {'text': None}},
	                   legend={'font': {'size': 18}, 'title': {'font': {'size': 18}}})

	# fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 750
	# fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
	fig.update_traces(textposition='top center')
	pio.show(fig)


def humanDev():
	#
	data = data_wrangglin(files=["human_development.csv"])
	data.columns = data.columns.str.replace(' ', '')
	data["GrossNationalIncome(GNI)perCapita"] = data["GrossNationalIncome(GNI)perCapita"].apply(
		lambda value:
		float(str(value).replace(",", "")))
	nan_value = float("NaN")
	data.replace("", nan_value, inplace=True)
	fig = plx.scatter(data, x='GrossNationalIncome(GNI)perCapita', y='HumanDevelopmentIndex(HDI)')
	fig.update_layout(title="Relationship between Gross National income and Human Development Index",
	                  xaxis_title="Gross National income",
	                  yaxis_title="Human Development Index")
	fig.show()
	#
	fig = plx.scatter(data, x='ExpectedYearsofEducation', y='HumanDevelopmentIndex(HDI)')
	fig.update_layout(title="Relationship between Expected Years of Education and Human Development Index",
	                  xaxis_title="Expected Years of Education",
	                  yaxis_title="Human Development Index")
	fig.show()

def main():
	biggest_developmentRegion()
	biggest_developmentCountry()
	humanDev()


if __name__ == "__main__":
	main()