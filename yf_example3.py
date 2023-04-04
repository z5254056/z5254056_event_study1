import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """
    Download Qantas stock prices from Yahoo Finance for a given year into CSV file. This file will locate under the 'cfg.DATADIR' folder and will be called "qan_prc_YYYY.csv", where 'YYYY' corresponds to the year 'year'.

    Parameters
    ----------
    year :int
        An integer with a four-digit year
    """
    tic = 'QAN.AX'
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    file_path = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(
        tic=tic,
        pth=file_path,
        start=start_date,
        end=end_date)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)