import numpy as np
import pandas as pd
import re

import plotly.graph_objects as go

# This function will convert the url to a download link
def convert_gsheets_url(u):
    try:
        worksheet_id = u.split('#gid=')[1]
    except:
        # Couldn't get worksheet id. Ignore it
        worksheet_id = None
    u = re.findall('https://docs.google.com/spreadsheets/d/.*?/',u)[0]
    u += 'export'
    u += '?format=csv'
    if worksheet_id:
        u += '&gid={}'.format(worksheet_id)
    return u

sample_url = 'https://docs.google.com/spreadsheets/d/1C7xqQrWEz_CSXt9Ih-TahgqVgxrfZITLRa97NajZpYw/edit?usp=sharing'
try:
    url = convert_gsheets_url(URL)
    df = pd.read_csv(url)
    print('Read successfully')
except:
    print(f"Could not read any data from the URL you provided.\nReading from {sample_url} instead.")
    url = convert_gsheets_url(sample_url)
    df = pd.read_csv(url)
df.head(10)
