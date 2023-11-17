# Stock Daily Price Tracking

## Abstract
This project aims to track desired stocks' prices and automatically store the daily price in BigQuery in the Google Cloud Platform. The data source comes from the [Taiwan Stock Exchange](https://www.twse.com.tw/zh/), and the information on the desired stock is obtained through a Python crawler. The data stored in the BigQuery includes the stock number, date, and the price. 

## Files
- stock.py: the main Python script of this project.
- requirements.txt: the documents that contain the required packages to launch the code.
- stock-query-key.json: the credential key of the Google API to store the daily price.
