import pandas as pd
import os 
import glob
#função that join json

def extract_data_and_join(folder: str) -> pd.DataFrame:
    files_json = glob.glob(os.path.join(folder, '*.json'))
    df_list = [pd.read_json(file) for file in files_json]
    df_total = pd.concat(df_list, ignore_index = True)
    return df_total

# a function that transform it

def calculate_total_sales_kpi(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantity"] * df["Price"]
    return df

def load_data(df: pd.DataFrame, output_format: list):
    """
    the parameter can be json or parquet
    """
    for format in output_format:
        if format == 'csv':
            df.to_csv("data.csv", index=False)
        if format == 'parquet':
            df.to_parquet("data.parquet", index=False)

def pipeline(folder: str, output_format: list ):
    data_frame = extract_data_and_join(folder)
    calculated_data_frame = calculate_total_sales_kpi(data_frame)
    load_data(calculated_data_frame,output_format)

    #A function that load csv or parquet