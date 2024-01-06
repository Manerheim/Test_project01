import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pa_merge import *

def select_csv_file():
    global csv_file_path
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")    ])
    print(f"Selected CSV file: {csv_file_path}")

def select_knx_pa_bok():
    global knx_pa_bok_path
    knx_pa_bok_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    print(f"KNX PA: {knx_pa_bok_path}")

def select_romliste():
    global romliste_path
    romliste_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    print(f"Romliste: {romliste_path}")

def select_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    print(f"Selected output directory: {output_directory}")

def process_files():
    if csv_file_path and knx_pa_bok_path and romliste_path and output_directory:
        csv_data = pd.read_csv(csv_file_path)
        excel_data1 = pd.read_excel(knx_pa_bok_path)
        excel_data2 = pd.read_excel(romliste_path)
        
        # Process your files here
        # Example: Save a new file in the selected output directory
        # output_file_path = f"{output_directory}/output.xlsx"
        # csv_data.to_excel(output_file_path)

        print("Files processed and output saved successfully!")
    else:
        print("Please select all files and output directory.")

def ede_pa_merge_func(ede_df):
    my_dict = {}
    for index, row in ede_df.iterrows():
        parts = row[0].split('.')
        key = '.'.join(parts[:3])  # Join the first three parts as the key
        value = parts[3]  # The fourth part is the value

        # Append to the list in the dictionary
        if key in my_dict:
            my_dict[key].append(value)
        else:
            my_dict[key] = [value]

    return my_dict


# Path to the Excel files
ede_file_path = 'knx_import\EDE.xlsx'
knx_pa_bok_path = 'knx_import\PA_bok_import.xlsx'

# Loading the Excel files
ede_df = pd.read_excel(ede_file_path)
pa_bok_df = pd.read_excel(knx_pa_bok_path)

# Applying the function to find matching values
ede_dict = ede_pa_merge_func(ede_df)

# Displaying the results
for rows in ede_dict:
    #print(rows, ede_dict[rows])    
    pa_loop(rows, ede_dict[rows], knx_pa_bok_path)
    my_dict = {
    "564.350.SQ404": ['PV1', 'PV2', 'PV3'],
    # ... other key-value pairs ...
}

#testing nr 2

for key, values in ede_dict.items():
    # Code for each key
    # Example: print(f"Processing key: {key}")
    print(key)

    # Check for specific combinations of values
    if 'PV1' in values and 'PV3' in values:
        # Code for when both PV1 and PV3 are present
        # Example: print("PV1 and PV3 are present together")
        print(values)
    
        # Process each value individually
        for value in values:
            # Code for each individual value
            # Example: print(f"Processing value: {value}")
            print(value)

            # You can also add specific conditions for each value
            if value == 'PV1':
                # Code specific to PV1
                pass
            elif value == 'PV3':
                # Code specific to PV3
                pass
            # ... and so on for other specific cases



root = tk.Tk()
root.title("File Selector")

csv_file_path = ''
knx_pa_bok_path = ''
romliste_path = ''
output_directory = ''

tk.Button(root, text="Select CSV File", command=select_csv_file).pack()
tk.Button(root, text="Select KNX PA Bok", command=select_knx_pa_bok).pack()
tk.Button(root, text="Select Romliste", command=select_romliste).pack()
tk.Button(root, text="Select Output Directory", command=select_output_directory).pack()
tk.Button(root, text="Process Files", command=process_files).pack()

root.mainloop()
