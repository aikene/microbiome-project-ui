from selenium import webdriver
import time

import numpy as np
import pandas as pd

# establishing connection to hmp main website and parsing hmp data table information
url = 'https://portal.hmpdacc.org/query/f?query=file.matrix_type%20in%20%5B%22wgs_community%22,%2216s_community%22%5D%20and%20sample.body_site%20in%20%5B%22feces%22%5D&filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22file.matrix_type%22,%22value%22:%5B%22wgs_community%22,%2216s_community%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22sample.body_site%22,%22value%22:%5B%22feces%22%5D%7D%7D%5D%7D#:~:text=Samples%20(3%2C452)-,Files%20(5%2C181),-files'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
html = browser.page_source
hmp_parsed_page = BeautifulSoup(html, "lxml")
hmp_files_table = hmp_parsed_page.find('table', id='files-table')

# gathering hmp meta datatable column headers
hmp_metadata_fields = []
for th in hmp_files_table.find_all('th'):
    col_header = th.text
    hmp_metadata_fields.append(col_header)

# creating dataframe of hmp information scraped
hmp_metadata_df = pd.DataFrame(columns = hmp_metadata_fields)

# appending hmp row data to dataframe
for tr in hmp_files_table.find_all('tr')[1:]:
    row_data = tr.find_all('td')
    row = [data_point.text for data_point in row_data]
    hmp_metadata_df.loc[len(hmp_metadata_df.index)] = row

# dropping unneeded columns
hmp_metadata_df = hmp_metadata_df.drop(hmp_metadata_df.columns[[0,1]], axis = 1)

# adding hmp indicator to front of dataframe
hmp_metadata_df['Data Source'] = 'HMP'
print(hmp_metadata_df)

# closing hmp website connection
browser.close()
browser.quit()
