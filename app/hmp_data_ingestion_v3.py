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
    hmp_df['sra_id'] = sra_id.replace('"', '')
    hmp_df['sra_hmp_uuid'] = hmp_df['sra_id']+'_'+hmp_df['hmp_id']
    hmp_df = hmp_df[['sra_hmp_uuid','sra_id','hmp_id','file_name']]

    return hmp_df

sra_id='"SRP115494"'
sra_hmp_ids = get_sra_hmp_uuid(sra_id)
print(sra_hmp_ids.tail())

#
# EXAMPLE OUTPUT:
#
#                                   sra_hmp_uuid     sra_id                            hmp_id
# 43  SRP115494_7cfd74d6803ea319683df7564432f9bf  SRP115494  7cfd74d6803ea319683df7564432f9bf  \
# 44  SRP115494_56bda9b020293b4b1d65e1eb253ee792  SRP115494  56bda9b020293b4b1d65e1eb253ee792   
# 45  SRP115494_7cfd74d6803ea319683df7564422f960  SRP115494  7cfd74d6803ea319683df7564422f960   
# 46  SRP115494_d39c1941c8f6e8b0f6ead5d7f729e885  SRP115494  d39c1941c8f6e8b0f6ead5d7f729e885   
# 47  SRP115494_d39c1941c8f6e8b0f6ead5d7f72a15d3  SRP115494  d39c1941c8f6e8b0f6ead5d7f72a15d3   

#                                             file_name
# 43  https://downloads.hmpdacc.org/ihmp/t2d/genome/...
# 44  https://downloads.hmpdacc.org/ihmp/t2d/genome/...
# 45  https://downloads.hmpdacc.org/ihmp/t2d/genome/...
# 46  https://downloads.hmpdacc.org/ihmp/t2d/genome/...
# 47  https://downloads.hmpdacc.org/ihmp/t2d/genome/...
