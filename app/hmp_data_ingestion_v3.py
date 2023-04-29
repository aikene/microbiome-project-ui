import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_sra_hmp_uuid(sra_id): # example input is sra_id='"SRP115494"'

    # setting hmp params
    url = "https://portal.hmpdacc.org/api/files"
    params = {
        "fields": "file_format,file_type,file_annotation_pipeline,file_matrix_type,study_srp_id",
        "filters": '{"op":"and","content":[{"op":"in","content":{"field":"file.matrix_type","value":["wgs_community","16s_community"]}},{"op":"in","content":{"field":"sample.body_site","value":["feces"]}},{"op":"in","content":{"field":"file.study_srp_id","value":['+sra_id+']}}]}',
        "from": 0,
        "save": "",
        "size": 20000, # <--- increase the range to gather more data across pages
        "sort": "file_id:asc",
    }

    # scraping hmp data via frontend
    all_dfs = []
    for params['from'] in range(0, 40, params['size']): 
        data = requests.get(url, params=params).json()
        all_dfs.append(pd.DataFrame([h['file'] for h in data['data']['hits']]))
    hmp_df = pd.concat(all_dfs).reset_index(drop=True)
    
    # connecting sra id with hmp id with associated filenames
    hmp_df = hmp_df.rename(columns={"id": "hmp_id"})
    hmp_df['sra_id'] = sra_id
    hmp_df['sra_hmp_uuid'] = hmp_df['sra_id']+'_'+hmp_df['hmp_id']
    hmp_df = hmp_df[['sra_hmp_uuid','sra_id','hmp_id','file_name']]

    return hmp_df

sra_hmp_ids = get_sra_hmp_uuid(sra_id)
