import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://portal.hmpdacc.org/api/files"

params = {
    "fields": "file_format,file_type,file_annotation_pipeline,file_matrix_type",
    "filters": '{"op":"and","content":[{"op":"in","content":{"field":"file.matrix_type","value":["wgs_community","16s_community"]}},{"op":"in","content":{"field":"sample.body_site","value":["feces"]}}]}',
    "from": 0,
    "save": "",
    "size": "20",
    "sort": "file_id:asc",
}

all_dfs = []
for params['from'] in range(0, 40, 20): # <--- increase the range for next pages
    data = requests.get(url, params=params).json()
    all_dfs.append(pd.DataFrame([h['file'] for h in data['data']['hits']]))

df = pd.concat(all_dfs).reset_index(drop=True)
print(df.tail())
