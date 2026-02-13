import json
import pandas as pd
import streamlit as st
import requests
import numpy as np






def calculate_percentage_change(old_value2, new_value2):

    old_value=float(old_value2)
    new_value=float(new_value2)
    # st.write(old_value)
    # st.write(new_value)
    if old_value > 0 and new_value > 0:
        percentage_change = (new_value - old_value) / old_value
    elif old_value < 0 and new_value < 0:
        percentage_change = (new_value - old_value) / abs(old_value)

    elif old_value > 0 and new_value < 0:
        percentage_change = (new_value - old_value) / old_value

    elif old_value < 0 and new_value > 0:
        percentage_change = (new_value - old_value) / abs(old_value)

    else:
        # Handle the case when both old_value and new_value are zero
        percentage_change = np.nan
    return round((float(percentage_change)*100),1)
# def calculate_percentage_change_d36(old_value2, new_value2):
#     old_value=float(old_value2)
#     new_value=float(new_value2)
#     st.write(old_value)
#     st.write(new_value)
#     if old_value > 0 and new_value > 0:
#         percentage_change = (new_value - old_value) / old_value
#         # st.write("result")
#         # st.write(percentage_change)
#     elif old_value < 0 and new_value < 0:
#         percentage_change = (old_value - new_value) / abs(old_value)
#     elif old_value > 0 and new_value < 0:
#         percentage_change = (new_value - old_value) / old_value
#     elif old_value < 0 and new_value > 0:
#         percentage_change = (new_value - old_value) / abs(old_value)
#     else:
#         # Handle the case when both old_value and new_value are zero
#         percentage_change = 0.0
#     st.write("result2")
#     st.write(percentage_change)

#     return round(percentage_change*100,1)


# def calculate_d26_d27(row,matching_columns):
    
#     values = row[matching_columns]
#     column_sum = values.sum()
#     d26=column_sum
#     return d26






# def calculate_d19(row):
#     d18=row['D18']
#     d3 = row['D3']
#     d5 = row['D5']
#     d7 = row['D7']
#     return round((float(d18) / (int(d3) + int(d5) + int(d7))),1)



# def calculate_d15(row):    
#     d7 = row['D7']
#     d13 = row['D13']
  
#     return round(float(d13) / int(d7),1)
def calculate_d15(row):    
    d7 = row['D7']
    d13 = row['D13']
    
    try:
        return round(float(d13) / int(d7), 1)
    except ZeroDivisionError:
        return np.nan

    # if d7 != 0 and d13 != 0:
    #     return round(float(d13) / int(d7), 1)
    # else:
    #     return np.nan
    




def calculate_d14(row):    
    d5 = row['D5']
    d12 = row['D12']
    try:
        return round(float(d12) / int(d5),1)
    except ZeroDivisionError:
        return np.nan


def calculate_d11(row):    
    d3 = row['D3']
    d5 = row['D5']
    d7 = row['D7']
    try:
        return round((int(d7) / (int(d3) + int(d5) + int(d7))*100),1)
    except ZeroDivisionError:
        return np.nan
    
def calculate_d10(row):    
    d3 = row['D3']
    d5 = row['D5']
    d7 = row['D7']
    try:
        return round((int(d5) / (int(d3) + int(d5) + int(d7))*100),1)
    except ZeroDivisionError:
        return np.nan

def calculate_d9(row):    
    d3 = row['D3']
    d5 = row['D5']
    d7 = row['D7']
    try:
        return round((int(d3) / (int(d3) + int(d5) + int(d7))*100),1)
    except ZeroDivisionError:
        return np.nan


def format_year(year):
    return "{:d}".format(year)  # Removes the comma separator

# @st.cache_data(experimental_allow_widgets=True)
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# @st.experimental_memo
# @st.cache_data(experimental_allow_widgets=True)
def get_data_from_json(id):
    def _fetch_json(url: str):
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # Your API returns JSON text, so this is fine:
        payload = json.loads(r.text)

        # Sometimes APIs return a JSON string inside JSON
        if isinstance(payload, str):
            payload = json.loads(payload)

        # Unwrap common wrappers
        if isinstance(payload, dict):
            for key in ("data", "result", "results", "payload"):
                if key in payload and isinstance(payload[key], (list, dict)):
                    payload = payload[key]
                    break

        return payload

    def _to_df(payload):
        """
        Make a DataFrame from various JSON shapes safely.
        Avoid max_level (can raise NotImplementedError depending on pandas/version/shape).
        """
        if isinstance(payload, list):
            if len(payload) == 0:
                return pd.DataFrame()
            # list of dicts -> json_normalize
            if all(isinstance(x, dict) for x in payload):
                return pd.json_normalize(payload, sep=".")
            # list of lists/tuples/values -> DataFrame
            return pd.DataFrame(payload)

        if isinstance(payload, dict):
            return pd.json_normalize(payload, sep=".")

        # fallback
        return pd.DataFrame([payload])

    response  = _fetch_json(f"https://app.koispesupport.gr/koispe/api/getkoispe?id={id}")
    response2 = _fetch_json(f"https://app.koispesupport.gr/koispe/api/getemployment?id={id}")
    response3 = _fetch_json(f"https://app.koispesupport.gr/koispe/api/getfinancial?id={id}")

    df  = _to_df(response)
    df2 = _to_df(response2)
    df3 = _to_df(response3)

    # ---- your existing logic stays the same from here ----
    df['year'] = df['year'].map(lambda x: str(x) if pd.notnull(x) else None)
    df['year'] = df['year'].str.split('.').str[0]
    df['year'] = df['year'].astype(str)
    df['year'] = df['year'].str.replace(',', '')

    df2['year'] = df2['year'].map(lambda x: str(x) if pd.notnull(x) else None)
    df2['year'] = df2['year'].str.split('.').str[0]

    df3['year'] = df3['year'].map(lambda x: str(x) if pd.notnull(x) else None)
    df3['year'] = df3['year'].str.split('.').str[0]

    merged = pd.merge(df, df2, left_on=['id', 'year'], right_on=['koispe_id', 'year'], how='inner')
    merged = pd.merge(merged, df3, left_on=['id', 'year'], right_on=['koispe_id', 'year'], how='inner')

    merged.rename(columns={'id': 'koispe_id'}, inplace=True)
    kdata = merged.copy()

    # if these columns sometimes don't exist, this avoids crashes:
    kdata.drop(columns=['uid_x', 'uid_y', 'uid'], inplace=True, errors='ignore')

    kdata = kdata.sort_values(by=['year'], ascending=True).reset_index(drop=True)

    kpdf = kdata[['koispe_id', 'year']].sort_values(by=['year'], ascending=True)

    kpdf['D1'] = kdata['profile.meli_a']
    kpdf['D3'] = kdata['profile.employee_general.sum']
    kpdf['D5'] = kdata['profile.employee.sum']
    kpdf['D7'] = kdata['profile.eko.sum']

    kpdf['D9'] = kpdf.apply(calculate_d9, axis=1)
    kpdf['D10'] = kpdf.apply(calculate_d10, axis=1)
    kpdf['D11'] = kpdf.apply(calculate_d11, axis=1)

    kpdf['D12'] = (kdata['profile.eme.sum'].astype(float)) * 2080
    kpdf['D13'] = (kdata['profile.eme_eko.sum'].astype(float)) * 2080
    kpdf['D14'] = kpdf.apply(calculate_d14, axis=1)
    kpdf['D15'] = kpdf.apply(calculate_d15, axis=1)
    kpdf['D16'] = round((kpdf['D12'].pct_change() * 100), 1)
    kpdf['D17'] = round((kpdf['D13'].pct_change() * 100), 1)

    kpdf['D18'] = round((kdata['profile.sum_eme_kispe'].astype(float)), 2)
    kpdf['D20'] = round((kdata['profile.eme.sum'].astype(float).pct_change() * 100), 1)
    kpdf['D21'] = round((kdata['profile.eme_eko.sum'].astype(float).pct_change() * 100), 1)
    kpdf['D22'] = round(((kdata['profile.eme.sum'].astype(float)) / (kdata['profile.sum_eme_kispe'].astype(float)) * 100), 1)
    kpdf['D23'] = round(((kdata['profile.eme_eko.sum'].astype(float)) / (kdata['profile.sum_eme_kispe'].astype(float)) * 100), 1)

    kpdf['D24'] = kdata['report.turnover_total'].astype(float)
    kpdf['D26'] = kdata['report.outside'].astype(float)
    kpdf['D27'] = kdata['report.inside'].astype(float)
    kpdf['D28'] = kdata['report.turnover_other'].astype(float)

    kpdf['D29'] = round((kdata['report.turnover_total'].astype(float).pct_change() * 100), 1)
    kpdf['D30'] = round((kpdf['D26'].astype(float).pct_change() * 100), 1)
    kpdf['D31'] = round((kpdf['D27'].astype(float).pct_change() * 100), 1)
    kpdf['D32'] = round((kpdf['D28'].astype(float).pct_change() * 100), 1)

    kpdf['D36_overal'] = kdata['report.overall'].astype(float)
    kpdf['D36'] = kpdf.apply(
        lambda row: calculate_percentage_change(kpdf.loc[row.name - 1, 'D36_overal'], row['D36_overal'])
        if row.name != 0 else np.nan,
        axis=1
    )

    kpdf['D38'] = round(((kdata['report.overall'].astype(float)) / (kdata['report.turnover_total'].astype(float))), 2)
    kpdf['D39'] = round(((kdata['report.grants'].astype(float)) / (kdata['report.turnover_total'].astype(float)) * 100), 2)
    kpdf['D40'] = round(((kdata['report.turnover_total'].astype(float)) / (kdata['profile.sum_eme_kispe'].astype(float))), 2)

    kpdf['D18_lipsi'] = kdata['profile.eme.sum'].astype(float)
    kpdf['D18_eko'] = kdata['profile.eme_eko.sum'].astype(float)
    kpdf['D18_general'] = kdata['profile.eme_general.sum'].astype(float)
    kpdf['D22_23_g'] = round(((kdata['profile.eme_general.sum'].astype(float)) / (kdata['profile.sum_eme_kispe'].astype(float)) * 100), 1)
    kpdf['D40_metaboli'] = round((kpdf['D40'].astype(float).pct_change() * 100), 1)

    return kpdf
