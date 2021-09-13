import os
import pickle
import argparse
import pandas as pd

from pathlib import PurePath
from datetime import datetime, timedelta

# base url for category trading, date format: YYYYMMDD
URL = 'https://www.twse.com.tw/exchangeReport/BFIAMU?response=csv&date={}'
DATA_DIR = PurePath('data')

def get_args():
    parser = argparse.ArgumentParser(description='Update daily category trading volume')

    parser.add_argument('--start_date',
                        type=str,
                        default='20040709',
                        help='Starting day to crawl the category trading volume.')
    parser.add_argument('--category_names_file',
                        type=str,
                        default='category_names.p',
                        help='File to store different tuple of category names.')
    parser.add_argument('--category_trading_record_file',
                        type=str,
                        defaul='category_trading_record.csv',
                        help='File to store daily category trading records.')

    args = parser.parse_args()

    return args

def load_category_names(file_path):
    # load category names if exist
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            category_names_set = pickle.load(f)
    else:
        category_names_set = set()
    
    return category_names_set

def main():
    # set arguments
    args = get_args()
    date_format = '%Y%m%d'
    start_date = datetime.strptime(args['start_date'], date_format)
    end_date = datetime.today()
    category_name_path = DATA_DIR / args['category_names_file']
    category_trading_record_path = DATA_DIR / args['category_trading_record_file']
    
    # load category names if exist
    category_names_set = load_category_names(category_name_path)

    while start_date <= end_date:
        start_date += timedelta(days=1)

if __name__ == '__main__':
    main()