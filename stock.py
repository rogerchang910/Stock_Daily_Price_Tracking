import requests
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account


stocks = ['2330', '0050']
today = datetime.now().strftime('%Y%m%d')
chinese_today = f"{(datetime.now().year - 1911)}/{datetime.now().strftime('%m/%d')}" 
# today = '20231114'
# chinese_today = '112/11/14'

stocks_price = []
for stock in stocks:
	# get access to the information
	url = f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date={today}&stockNo={stock}&response=html'
	response = requests.get(url)
	data = pd.read_html(response.text)[0]
	data.columns = data.columns.droplevel(0)

	# select matched data
	today_price = data.loc[data['日期']==chinese_today].values.tolist()[0]
	today_price.insert(0, stock)
	stocks_price.append(today_price)
df = pd.DataFrame(stocks_price, columns=['stock_no','date', 'price'])

credentials = service_account.Credentials.from_service_account_file('stocks-query-key.json')
client = bigquery.Client(credentials=credentials)
table_id = 'stocks-query.stocks.daily-price'
task = client.load_table_from_dataframe(df, table_id)
task.result()

table = client.get_table(table_id)
print(f'Successfully stores {table.num_rows} data to {table_id}')