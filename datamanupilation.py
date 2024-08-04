import pandas as pd
import os
from constants import INPUT_FILE_PATH,OUTPUT_FILE_PATH,MASTER_FILE_PATH

def datamanupilation_main():
    file1_path = INPUT_FILE_PATH
    file2_path = MASTER_FILE_PATH
    output_file_path = OUTPUT_FILE_PATH

    df1 = pd.read_excel(file1_path,skiprows=1)
    df2 = pd.read_excel(file2_path)

    df1.head()
    df2.head()

    lookup_column = 'WIID'

    if lookup_column not in df1.columns:
        raise ValueError(f"{lookup_column} not found in df1")
    if lookup_column not in df2.columns:
        raise ValueError(f"{lookup_column} not found in df2")

    merge_df = pd.merge(df1,df2,on=lookup_column,how='inner')
    print(merge_df)

    filter_df = merge_df[(merge_df['Status'] =='Completed') & (merge_df['Type']=='WI2')]
    print(filter_df)

    if os.path.exists(output_file_path):
        # Save the filtered data if output excel already there clear all sheet data
        os.remove(output_file_path) 
        with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
            filter_df.to_excel(writer, sheet_name='FilteredData', index=False)
        print("Output File prepared Successfully")

    else:
        # Save the filtered data to a new Excel file
        with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
            filter_df.to_excel(writer, sheet_name='FilteredData', index=False)
        print("Output File prepared Successfully")

if __name__ == "__main__":
    datamanupilation_main()
    