# -*- coding: utf-8 -*-
"""Data science.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q9WjGGBplvyC-qdColLcYVPdk1C-Vztf

##Link data

### 1. Exploratory variables
- Population: https://worldpopulationreview.com/world-cities
- Population density
- GDP: https://en.wikipedia.org/wiki/List_of_cities_by_GDP
- Average temperature: https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature#cite_note-1
- Altitude:https://en.wikipedia.org/wiki/List_of_capital_cities_by_elevation
- Humidity: https://en.climate-data.org/
- Area:https://en.wikipedia.org/wiki/List_of_national_capitals_by_area
- Congestion level: https://www.tomtom.com/en_gb/traffic-index/ranking/
- Number of high building: https://www.skyscrapercenter.com/cities?list=buildings-150
- Internation visitor: https://en.wikipedia.org/wiki/List_of_cities_by_international_visitors
- sunshine time : https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration

### 2. Response variable
- Air quality: https://www.iqair.com/world-air-quality-ranking

##Data crawling

###1. Population: https://worldpopulationreview.com/world-cities
"""

import pandas as pd
import requests

url = "https://worldpopulationreview.com/world-cities"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df1 = df_list[0]
# print(df1.shape)
#df1.head()

columns = list(df1.columns)
features = columns[1:len(columns)-2]
df1 = df1[features]
df1 = df1.drop(df1.columns[[1]], axis=1)
df1.rename(columns={'Name':'City',"2021 Population":"Population"}, inplace=True)
df1

"""###2. GDP: https://en.wikipedia.org/wiki/List_of_cities_by_GDP"""

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_cities_by_GDP"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df2 = df_list[0]
# print(df2.shape)
# df2.head()

features = ['City proper / Metropolitan area', 'Country/Region',
       'Official est.GDP up to date (billion US$)',
       'Brookings[5]2014 est. PPP-adjusted GDP (billion US$)',
       'Visual Capitalist[6] 2021 est. (billion US$)',
       'Visual Capitalist[7] 2021 est. GDP PPP-adjusted GDP (billion US$)']
df2 = df2[features]
df2 = df2.drop(df2.columns[[1,3,4,5]], axis=1)
df2.rename(columns={'City proper / Metropolitan area':'City',"Official est.GDP up to date (billion US$)":"GDP (billion US$)"}, inplace=True)
print(list(df2.columns[[1]]))

import pandas as pd
import requests

url = "http://www.citymayors.com/statistics/richest-cities-2020.html"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df21 = df_list[2]
df21= df21.drop(df21.columns[[0,2,4]], axis=1)
df21 = df21.set_axis(['City','GDP (billion US$)'], axis=1, inplace=False)
df21=df21.drop(index=0)

df2= pd.concat([df2,df21])
df2=df2.drop_duplicates(subset='City', keep='last')
df2

"""###3. Average temperature: https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature#cite_note-1"""

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature#cite_note-1"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
print(len(df_list))
df3 = pd.concat(df_list)
df3 = df3.drop(df3.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,15]], axis=1)
df3.rename(columns={"City":"City","Year":"Temperature(C)"}, inplace=True)
print(df3.shape)
df3

# df3.sort_values(by=['Country'])

"""###4. Altitude:https://en.wikipedia.org/wiki/List_of_capital_cities_by_elevation"""

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_capital_cities_by_elevation"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
print(len(df_list))
df4 = pd.concat(df_list)
df4 = df4.drop(df4.columns[[0,3,4,5]], axis=1)
df4.rename(columns={"Capital":"City"}, inplace=True)
print(df4.shape)
df4

import pandas as pd
from bs4 import BeautifulSoup
import requests
elevation=[]
city=[]
url = "https://www.kudacity.com/cset/by_elevation"
r = requests.get(url).text
soup=BeautifulSoup(r,'lxml')
list_data=soup.find_all('div',class_='desktop_three_columns')
for data in list_data:
  find_li= data.find_all('li')
  for texts in find_li:
    elevation.append(texts.text.split('m')[0][1:])
    lcity=texts.find_all('a')
    city.append(lcity[0].text)
df41 = pd.DataFrame(list(zip(city, elevation)),
               columns =['City', 'Elevation (m)'])
df41

df4= pd.concat([df4,df41])
df4=df4.drop_duplicates(subset='City', keep='last')
df4

"""###6. Area: https://en.wikipedia.org/wiki/List_of_national_capitals_by_area"""

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_national_capitals_by_area"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df6 = df_list[1]
df6 = df6.drop(df6.columns[[0,1,4,5,6]], axis=1)
df6 = df6.set_axis(['City','Area (km2)' ], axis=1, inplace=False)
print(df6.shape)
df6.head()

"""###7. Congestion level: https://www.tomtom.com/en_gb/traffic-index/ranking/"""

import pandas as pd
import requests

url = "https://www.tomtom.com/en_gb/traffic-index/ranking/"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df7 = df_list[0]
# print(df7.shape)
df7.head()

txt = 'MumbaiIndia'
txt.split()

features = ['City', 'Days with low traffic',
       'Congestion month by month', 'Congestion Level 2020',
       'Change from 2019']
df7 = df7[features]
df7 = df7.drop(df7.columns[[1,2,4]], axis=1)
df7.rename(columns={"City":"City","Congestion Level 2020":"Congestion Level (%)"}, inplace=True)
for i in range(0, df7.shape[0]):
  res = list(filter(lambda c: c.isupper(),str(df7['City'][i])))
  if len(res)>=5:
    df7['City'][i]=str(df7['City'][i]).split(res[-3])[0]
  elif len(res)==4:
    df7['City'][i]=str(df7['City'][i]).split(res[-2])[0]
  else:
    df7['City'][i]=str(df7['City'][i]).split(res[-1])[0]
df7

'''import pandas as pd
import requests

url = "https://ceoworld.biz/2020/01/30/these-are-the-most-traffic-congested-cities-in-the-world-2020/?fbclid=IwAR0Ou7sCVFSRocA6zMUNCKYWaCLBC9asUW5JccG4-D7j5fBfbl7mF6f-t80"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df71 = df_list[0]
df71= df71.drop(df71.columns[[0,2]], axis=1)
df71 = df71.set_axis(['City','Congestion Level (%)'], axis=1, inplace=False)
df71'''

'''
df7= pd.concat([df7,df71])
df7=df7.drop_duplicates(subset='City', keep='first')
df7'''

"""###8. Number of high building: https://www.skyscrapercenter.com/cities?list=buildings-150"""

!pip install requests_html

from requests_html import HTMLSession
import nest_asyncio

nest_asyncio.apply()

s = HTMLSession()
url="https://www.skyscrapercenter.com/cities?list=buildings-150"
r = s.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df8 = df_list[0]
df8 = df8.drop(df8.columns[[0,2,3,4,5,7,8]], axis=1)
df8 = df8.set_axis(['City','150m+ Building' ], axis=1, inplace=False)
print(df8.shape)
df8.head()

import pandas as pd
import requests

url = "https://ceoworld.biz/2020/05/16/revealed-cities-with-the-largest-number-of-skyscrapers-in-2020/"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df81 = df_list[0]
df81= df81.drop(df81.columns[[0,2]], axis=1)
df81 = df81.set_axis(['City','150m+ Building'], axis=1, inplace=False)
df81

df8= pd.concat([df8,df81])
df8=df8.drop_duplicates(subset='City', keep='first')
df8

"""###9. Internation visitor: https://en.wikipedia.org/wiki/List_of_cities_by_international_visitors"""

'''from google.colab import files
uploaded = files.upload()'''

'''import io
import pandas as pd
df91 = pd.read_csv(io.BytesIO(uploaded['arrive.csv']))
df91['Arrivals']=df91['Arrivals'].multiply(1000)
df91'''

'''import pandas as pd
import requests

url = "https://airmundo.com/en/blog/most-visited-cities-in-europe/"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df91 = df_list[0]'''

'''df91 = df91.set_axis(['stt', 'City', '2019', 'Arrivals', 'Closest airports'], axis=1, inplace=False)
df91=df91.drop(index=0)
df91['Arrivals'] = df91['Arrivals'].str.replace('%', '')
df91['Arrivals'] = df91['Arrivals'].str.replace('+', '')
df91['Arrivals'] = df91['Arrivals'].str.replace(',', '.')
df91['2019']=pd.to_numeric(df91['2019'])
df91['Arrivals']=pd.to_numeric(df91['Arrivals'])
df91['Arrivals']=df91['Arrivals']*df91['2019']/100
df91 = df91.drop(df91.columns[[0,2,4]], axis=1)
df91 = df91.reset_index(drop=True)
for i in range(0,df91.shape[0]):
  if str(df91["City"][i]) !="nan":
      df91["City"][i]=str(df91["City"][i]).split(',')[0]
df91'''

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_cities_by_international_visitors"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df9 = df_list[0]
# print(df9.shape)
# df9.head()

features = ['City', 'Country',
       'Arrivals 2018(Euromonitor)', 'Arrivals 2016(Mastercard)',
       'Growthin arrivals(Euromonitor)', 'Income(billions $)(Mastercard)']
df9 = df9[features]
df9 = df9.drop(df9.columns[[1,3,4,5]], axis=1)
df9.rename(columns={"City":"City","Arrivals 2018(Euromonitor)":"Arrivals"}, inplace=True)
df9

'''df9= pd.concat([df9,df91])
df9=df9.drop_duplicates(subset='City', keep='last')
df9'''

"""###10. sunshine time : https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration"""

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
print(len(df_list))
df10 = pd.concat(df_list[1:len(df_list)-1])
df10 = df10.drop(df10.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,15,16]], axis=1)
df10.rename(columns={"City":"City","Year":"hour sunshine"}, inplace=True)
print(df10.shape)
df10

# features = ['Country', 'City', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
#        'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Year']
# df10 = df10[features]
# df10

# df10.columns

"""###11. Air quality: https://www.iqair.com/world-air-quality-ranking"""

# page=2&perPage=50&display=full&units.temperature=celsius&units.distance=kilometer&units.pressure=millibar&AQI=US&language=en

import pandas as pd
import requests

url1 = "https://website-api.airvisual.com/v1/countries/rankings?page=1&perPage=50&display=full&units.temperature=celsius&units.distance=kilometer&units.pressure=millibar&AQI=US&language=en"
url2 = "https://website-api.airvisual.com/v1/countries/rankings?page=2&perPage=50&display=full&units.temperature=celsius&units.distance=kilometer&units.pressure=millibar&AQI=US&language=en"

r1 = requests.get(url1)
r2 = requests.get(url2)

data1 = r1.json()
data2 = r2.json()

df111 = pd.DataFrame(data1)
df112 = pd.DataFrame(data2)

df113 = pd.concat([df111, df112])
# print(df113.shape)
# df113

features = ['city', 'country', 'aqi',]
df115 = df113[features]
len(df115)

features = ['city', 'aqi',]
df11 = df113[features]
# df11 = df11.drop(df11.columns[[1]], axis=1)
df11.rename(columns={"city":"City","aqi":"AQI"}, inplace=True)
df11

df11.iloc[32]

"""###5. Humidity: https://en.climate-data.org/"""

# import requests
from bs4 import BeautifulSoup
d = []
for i in range(len(df115)):
    city = df115.iloc[i].city
    country = df115.iloc[i].country
    temp = []
    try:
        url = f"https://en.climate-data.org/search/?q={city}"
        s=requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r=requests.get(url, headers=headers)

        soup = BeautifulSoup(r.content,"html5lib")
        div = soup.find('div', id="article")
        for x in div.select("a[href]"):
            try:
                if x.div["class"] == ['snippet', 'location']:
                    temp.append(x["href"])
            except:
                pass

        d.append([f'https://en.climate-data.org{temp[0]}', city])

    except:
        url = f"https://en.climate-data.org/search/?q={country}"
        s=requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r=requests.get(url, headers=headers)

        soup = BeautifulSoup(r.content,"html5lib")
        div = soup.find('div', id="article")

        d.append([f'https://en.climate-data.org{div.select("a[href]")[0]["href"]}c/january-1/', city])

len(df115)

import pandas as pd
import requests
df51 = []
for i in d:
    p = 0
    url = i[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        r=requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content,"html5lib")
        table = soup.find('table', id="small_weather_table")
        df222 = pd.read_html(f"{table}")[0]
        # print(d.index(i),url,df222.shape)

    except:
        try:
            url+= 'r/january-1/'
            r=requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content,"html5lib")
            table = soup.find('table', id="small_weather_table")
            df222 = pd.read_html(f"{table}")[0]
            # print(d.index(i),url,df222.shape)
        except:
            # print("loi")
            p = 1
    s = 0
    for j in df222["Humidity (%)"]:
        s +=int(j.replace("%", ""))
    if p == 1:
        df51.append([i[1], None])
    else:
        df51.append([i[1], round(s/len(df222["Humidity (%)"]),2)], )
print(p)

df222

df5 = pd.DataFrame(df51, columns =['City', 'Humidity (%)'])
df5

"""##Data cleaning"""

list_df=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11]

# delete two city have the same name but different country
for i in range(0,len(list_df)):
  list_df[i] = list_df[i].drop_duplicates(subset='City', keep=False)

#merge csv file
final_table=list_df[0]
for i in range(0, len(list_df)-1):
    final_table=final_table.merge(list_df[i+1],on="City",how="outer")

#delete "%" letter in congestion_level column
final_table['Congestion Level (%)'] = final_table['Congestion Level (%)'].str.replace(r'\D', '')

#delete (), [] part of temperature,GDP,area
def take_num(col,letter):
  temp_col=[]
  for i in range(0,final_table.shape[0]):
    if str(final_table[col][i]) !="nan":
        final_table[col][i]=str(final_table[col][i]).split(letter)[0]
take_num("Temperature(C)","(")
take_num('GDP (billion US$)'," (")
take_num('GDP (billion US$)',"[")
take_num('Area (km2)','[')

#delete rows that have NaN value in AQI column
final_table = final_table.dropna(axis=0, subset=['AQI'])

#delete rows that have only AQI is not NaN
final_table = final_table.reset_index(drop=True)
for i in range(0,final_table.shape[0]):
  if final_table.loc[[i]].isna().sum().sum()==10:
    final_table=final_table.drop(index=i)
final_table = final_table.reset_index(drop=True)

#delete "," in number >999, convert string to float number
for i in range(1,final_table.shape[1]):
  for j in range(0,final_table.shape[0]):
    if str(final_table[final_table.columns[i]][j]) !="nan":
        final_table[final_table.columns[i]][j]=str(final_table[final_table.columns[i]][j]).replace(',','')
        final_table[final_table.columns[i]][j]=float(str(final_table[final_table.columns[i]][j]).replace("−", "-"))
  final_table[final_table.columns[i]]=pd.to_numeric(final_table[final_table.columns[i]])
pd.set_option("display.max_rows", None, "display.max_columns", None)
final_table



final_table.isna().sum()

pcorr=final_table.corr(method='pearson')
pcorraqi=pcorr.drop(pcorr.columns[[0,1,2,3,4,5,6,7,8,9]], axis=1)
print(pcorraqi)
pcorr

r_square=pcorr.copy()
for x in range(0,pcorraqi.shape[0]-1):
  for y in range(0,pcorraqi.shape[0]-1):
    xz=pcorr['AQI'][x]
    yz=pcorr['AQI'][y]
    xy=pcorr[pcorr.columns[x]][y]
    r_square[r_square.columns[x]][y] = (abs(xz**2) + abs(yz**2) - 2*xz*yz*xy) / (1-abs(xy**2))
r_square

scorr=final_table.corr(method='spearman')
scorraqi=pcorr.drop(scorr.columns[[0,1,2,3,4,5,6,7,8,9]], axis=1)
print(scorraqi)
scorr

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(final_table.corr(), square=True, annot=True, linewidths=3)

from pandas.plotting import lag_plot

final_table.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

sns.distplot(final_table['AQI'])
plt.show()

sns.scatterplot(final_table["Population"], final_table["AQI"])

sns.scatterplot(final_table["GDP (billion US$)"], final_table["AQI"])

sns.scatterplot(final_table["Temperature(C)"], final_table["AQI"])

sns.scatterplot(final_table["Elevation (m)"], final_table["AQI"])

sns.scatterplot(final_table["Humidity (%)"], final_table["AQI"])

sns.scatterplot(final_table['Area (km2)'], final_table["AQI"])

sns.scatterplot(final_table['150m+ Building'], final_table["AQI"])

sns.scatterplot(final_table['Arrivals'], final_table["AQI"])

sns.scatterplot(final_table['hour sunshine'], final_table["AQI"])

greenAQI = final_table[final_table['AQI']<=50]
yellowAQI = final_table[final_table['AQI']<=100]
yellowAQI = yellowAQI[yellowAQI['AQI']>=51]
orangeAQI = final_table[final_table['AQI']<=150]
orangeAQI = orangeAQI[orangeAQI['AQI']>=101]
redAQI = final_table[final_table['AQI']<=200]
redAQI = redAQI[redAQI['AQI']>=151]
purpleAQI = final_table[final_table['AQI']<=300]
purpleAQI = purpleAQI[purpleAQI['AQI']>=201]
purpleAQI

gpcorr=greenAQI.corr(method='pearson')
gpcorraqi=gpcorr.drop(pcorr.columns[[0,1,2,3,4,5,6,7,8,9]], axis=1)
print(gpcorraqi)
gpcorr

ypcorr=yellowAQI.corr(method='pearson')
ypcorraqi=ypcorr.drop(pcorr.columns[[0,1,2,3,4,5,6,7,8,9]], axis=1)
print(ypcorraqi)
ypcorr

chitable=final_table.copy()
chitable

min_mean_max=[]
for i in range(1,chitable.shape[1]-1):
  k=[]
  k.append(final_table[final_table.columns[i]].min())
  k.append(final_table[final_table.columns[i]].mean())
  k.append(final_table[final_table.columns[i]].max())
  min_mean_max.append(k)
min_mean_max

chitable=final_table.copy()
cate=['low','medium','high']
for i in range(1,chitable.shape[1]):
  for j in range(0,chitable.shape[0]):
    test=float(chitable[chitable.columns[i]][j])
    if str(test) !="nan":
      if i==chitable.shape[1]-1:
        if (test<=50 and test>=0):
          chitable[chitable.columns[i]][j]="green"
        elif (test<=100 and test>=51):
          chitable[chitable.columns[i]][j]="yellow"
        elif (test<=150 and test>=101):
          chitable[chitable.columns[i]][j]="orange"
        elif (test<=200 and test>=151):
          chitable[chitable.columns[i]][j]="red"
        elif (test<=300 and test>=201):
          chitable[chitable.columns[i]][j]="purple"
      else:
        index=min_mean_max[i-1].index((min(min_mean_max[i-1], key=lambda x:abs(x-test))))
        chitable[chitable.columns[i]][j]=cate[index]
chitable

'''chitable=final_table.copy()
for i in range(1,chitable.shape[1]):
  for j in range(0,chitable.shape[0]):
    test=float(chitable[chitable.columns[i]][j])
    if str(test) !="nan":
      if i==11: #aqi
        if (test<=50 and test>=0):
          chitable[chitable.columns[i]][j]="green"
        elif (test<=100 and test>=51):
          chitable[chitable.columns[i]][j]="yellow"
        elif (test<=150 and test>=101):
          chitable[chitable.columns[i]][j]="orange"
        elif (test<=200 and test>=151):
          chitable[chitable.columns[i]][j]="red"
        elif (test<=300 and test>=201):
          chitable[chitable.columns[i]][j]="purple"
      if i==10: #hour sunshine
        if (test<=2400):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=3000 and test>2400):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>3000):
          chitable[chitable.columns[i]][j]="high"
      if i==9: #arrival
        if (test<=2000000):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=10000000 and test>2000000):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>10000000):
          chitable[chitable.columns[i]][j]="high"
      if i==8: #building
        if (test<=100):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=1000 and test>100):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>1000):
          chitable[chitable.columns[i]][j]="high"
      if i==7: #traffic
        if (test<=100):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=200 and test>100):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>200):
          chitable[chitable.columns[i]][j]="high"
      if i==6: #area
        if (test<=1000):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=5000 and test>1000):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>5000):
          chitable[chitable.columns[i]][j]="high"
      if i==5: #humid
        if (test<=50):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=70 and test>50):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>70):
          chitable[chitable.columns[i]][j]="high"
      if i==4: #high
        if (test<=200):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=1000 and test>200):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>1000):
          chitable[chitable.columns[i]][j]="high"
      if i==3: #temperature
        if (test<=10):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=20 and test>10):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>20):
          chitable[chitable.columns[i]][j]="high"
      if i==2: #gdp
        if (test<=100):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=600 and test>100):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>600):
          chitable[chitable.columns[i]][j]="high"
      if i==1: #population
        if (test<=5000000):
          chitable[chitable.columns[i]][j]="low"
        elif (test<=30000000 and test>5000000):
          chitable[chitable.columns[i]][j]="medium"
        elif (test>30000000):
          chitable[chitable.columns[i]][j]="high"
chitable'''

sunaqi= pd.crosstab(chitable['AQI'], chitable['hour sunshine'])
sunaqi

plt.figure(figsize=(12,8))
sns.heatmap(sunaqi, annot=True, cmap="YlGnBu")

!pip install scipy

from scipy.stats import chi2_contingency
c, p, dof, expected = chi2_contingency(sunaqi)
print(c)
print(p)
print(dof)
print(expected)