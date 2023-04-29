import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_hmp_data():
    
    # setting hmp params
    url = "https://portal.hmpdacc.org/api/files"

    params = {
        "fields": "file_format,file_type,file_annotation_pipeline,file_matrix_type",
        "filters": '{"op":"and","content":[{"op":"in","content":{"field":"file.matrix_type","value":["wgs_community","16s_community"]}},{"op":"in","content":{"field":"sample.body_site","value":["feces"]}}]}',
        "from": 0,
        "save": "",
        "size": 20000,   # <--- increase the range to gather more data across pages
        "sort": "file_id:asc",
    }

    # scraping hmp data via frontend
    all_dfs = []
    for params['from'] in range(0, 40, params['size']):
        data = requests.get(url, params=params).json()
        all_dfs.append(pd.DataFrame([h['file'] for h in data['data']['hits']]))
    hmp_df = pd.concat(all_dfs).reset_index(drop=True)

    return hmp_df

hmp_df = get_hmp_data()
print(hmp_df.tail())

#
# EXAMPLE OUTPUT:
#
#                  format_doc        study  ver organism_type   
# 35  http://biom-format.org/  prediabetes  NaN     bacterial  \
# 36  http://biom-format.org/  prediabetes  NaN     bacterial   
# 37  http://biom-format.org/  prediabetes  NaN     bacterial   
# 38  http://biom-format.org/  prediabetes  NaN     bacterial   
# 39  http://biom-format.org/  prediabetes  NaN     bacterial   

#                            format    data_modality         node_type    size   
# 35  Biological Observation Matrix  marker sequence  abundance_matrix  196000  \
# 36  Biological Observation Matrix  marker sequence  abundance_matrix  196000   
# 37  Biological Observation Matrix  marker sequence  abundance_matrix   81000   
# 38  Biological Observation Matrix  marker sequence  abundance_matrix  204000   
# 39  Biological Observation Matrix  marker sequence  abundance_matrix  120000   

#           subtype                                               fasp   
# 35  16s_community  fasp://aspera.ihmpdcc.org/t2d/genome/microbiom...  \
# 36  16s_community  fasp://aspera.ihmpdcc.org/t2d/genome/microbiom...   
# 37  16s_community  fasp://aspera.ihmpdcc.org/t2d/genome/microbiom...   
# 38  16s_community  fasp://aspera.ihmpdcc.org/t2d/genome/microbiom...   
# 39  16s_community  fasp://aspera.ihmpdcc.org/t2d/genome/microbiom...   

#     data_type    matrix_type abundance_type   
# 35  abundance  16s_community      community  \
# 36  abundance  16s_community      community   
# 37  abundance  16s_community      community   
# 38  abundance  16s_community      community   
# 39  abundance  16s_community      community   

#                                                 https   
# 35  https://downloads.hmpdacc.org/ihmp/t2d/genome/...  \
# 36  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   
# 37  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   
# 38  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   
# 39  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   

#                                   id                               md5   
# 35  76612bd9a41885add4f6b0b7683a65da  70600351056001048c1d42d7268cc6b7  \
# 36  76612bd9a41885add4f6b0b76836df9b  39643700bd4bcf040064c12f1d2b644c   
# 37  6cca313bce90a4392c3d5cf23fdb7ca8  7a33c9809cb98fac4e89aa2d3c151597   
# 38  76612bd9a41885add4f6b0b7681567ac  7a33c9809cb98fac4e89aa2d3c151597   
# 39  6cca313bce90a4392c3d5cf23fdafbcc  9757b64815cbfee3ba188e80b69a023e   

#                                             file_name access   
# 35  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   open  \
# 36  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   open   
# 37  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   open   
# 38  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   open   
# 39  https://downloads.hmpdacc.org/ihmp/t2d/genome/...   open   

#                                               comment  
# 35  Qiime output upload from DCC for HMP2_J45372_1...  
# 36  Qiime output upload from DCC for HMP2_J45281_1...  
# 37  Qiime output upload from DCC for HMP2_J04182_1...  
# 38  Qiime output upload from DCC for HMP2_J04182_1...  
# 39  Qiime output upload from DCC for HMP2_J00840_1... 

