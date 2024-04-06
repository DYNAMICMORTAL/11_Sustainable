# import pandas as pd
# import os

# # Step 1: Combine Wind Energy Generation Data
# wind_energy_data = pd.DataFrame()
# for year in range(2019, 2024):
#     file_path = f"./Hackathon_data/wind_power_data/power_gen_{year}.csv" # Adjust the path accordingly
#     df = pd.read_csv(file_path)
#     wind_energy_data = pd.concat([wind_energy_data, df])

# wind_energy_data.reset_index(drop=True, inplace=True)

# # Step 2: Combine Smart Grid Data
# smart_grid_data = pd.DataFrame()
# for year in range(2019, 2024):
#     # file_path = f"grid_stability_{year}.csv"
#     file_path = f"./Hackathon_data/Grid_data/grid_stability_2019_2023.csv"
#     df = pd.read_csv(file_path)
#     smart_grid_data = pd.concat([smart_grid_data, df])

# smart_grid_data.reset_index(drop=True, inplace=True)

# # Step 1: Adjust DateTime Columns
# wind_energy_data['DateTime'] = pd.to_datetime(wind_energy_data['DateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')
# smart_grid_data['DateTime'] = pd.to_datetime(smart_grid_data['date'], format='%d-%m-%Y %H:%M')

# # Step 2: Merge the DataFrames
# merged_data = pd.merge(wind_energy_data, smart_grid_data, on='DateTime', how='inner')


# # Step 4: Save the Final Input File
# # merged_data.to_csv('final_input_file.csv', index=False)


# # Step 5: Combine Air Temperature Data
# air_temperature_data = pd.DataFrame()
# for year in range(2019, 2024):
#     # file_path = f"air_temperature_{year}.csv"
#     file_path = f"./Hackathon_data/wind_power_data/air_temperature_{year}.csv"
#     df = pd.read_csv(file_path)
#     air_temperature_data = pd.concat([air_temperature_data, df])

# air_temperature_data.reset_index(drop=True, inplace=True)

# # Step 6: Combine Pressure Data
# pressure_data = pd.DataFrame()
# for year in range(2019, 2024):
#     # file_path = f"pressure_{year}.csv"
#     file_path = f"./Hackathon_data/wind_power_data/pressure_{year}.csv"
#     df = pd.read_csv(file_path)
#     pressure_data = pd.concat([pressure_data, df])

# pressure_data.reset_index(drop=True, inplace=True)

# # Step 7: Combine Wind Speed Data
# wind_speed_data = pd.DataFrame()
# for year in range(2019, 2024):
#     # file_path = f"wind_speed_{year}.csv"
#     file_path = f"./Hackathon_data/wind_power_data/wind_speed_{year}.csv"
#     df = pd.read_csv(file_path)
#     wind_speed_data = pd.concat([wind_speed_data, df])

# wind_speed_data.reset_index(drop=True, inplace=True)

# # Step 8: Merge all Data
# final_merged_data = merged_data.merge(air_temperature_data, on='DateTime', how='inner')
# final_merged_data = final_merged_data.merge(pressure_data, on='DateTime', how='inner')
# final_merged_data = final_merged_data.merge(wind_speed_data, on='DateTime', how='inner')

# # Step 9: Save the Final Input File
# final_merged_data.to_csv('final_input_file.csv', index=False)











import pandas as pd
import os

# Step 1: Combine Wind Energy Generation Data
wind_energy_data = pd.DataFrame()
for year in range(2019, 2024):
    file_path = f"./Hackathon_data/wind_power_data/power_gen_{year}.csv" # Adjust the path accordingly
    df = pd.read_csv(file_path)
    wind_energy_data = pd.concat([wind_energy_data, df])

wind_energy_data.reset_index(drop=True, inplace=True)

# Step 2: Combine Smart Grid Data
smart_grid_data = pd.DataFrame()
for year in range(2019, 2024):
    file_path = f"./Hackathon_data/Grid_data/grid_stability_2019_2023.csv"
    df = pd.read_csv(file_path)
    smart_grid_data = pd.concat([smart_grid_data, df])

smart_grid_data.reset_index(drop=True, inplace=True)

# Step 3: Adjust DateTime Columns
wind_energy_data['DateTime'] = pd.to_datetime(wind_energy_data['DateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')
smart_grid_data['DateTime'] = pd.to_datetime(smart_grid_data['date'], format='%d-%m-%Y %H:%M')

# Step 4: Merge the DataFrames
merged_data = pd.merge(wind_energy_data, smart_grid_data, on='DateTime', how='inner')

# Step 5: Combine Air Temperature Data
air_temperature_data = pd.DataFrame()
for year in range(2019, 2024):
    file_path = f"./Hackathon_data/wind_power_data/air_temperature_{year}.csv"
    df = pd.read_csv(file_path)
    air_temperature_data = pd.concat([air_temperature_data, df])

air_temperature_data.reset_index(drop=True, inplace=True)

# Step 6: Combine Pressure Data
pressure_data = pd.DataFrame()
for year in range(2019, 2024):
    file_path = f"./Hackathon_data/wind_power_data/pressure_{year}.csv"
    df = pd.read_csv(file_path)
    pressure_data = pd.concat([pressure_data, df])

pressure_data.reset_index(drop=True, inplace=True)

# Step 7: Combine Wind Speed Data
wind_speed_data = pd.DataFrame()
for year in range(2019, 2024):
    file_path = f"./Hackathon_data/wind_power_data/wind_speed_{year}.csv"
    df = pd.read_csv(file_path)
    wind_speed_data = pd.concat([wind_speed_data, df])

wind_speed_data.reset_index(drop=True, inplace=True)

# Step 8: Adjust DateTime Columns for the remaining DataFrames
air_temperature_data['DateTime'] = pd.to_datetime(air_temperature_data['DateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')
pressure_data['DateTime'] = pd.to_datetime(pressure_data['DateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')
wind_speed_data['DateTime'] = pd.to_datetime(wind_speed_data['DateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')

# Step 9: Merge all Data
final_merged_data = merged_data.merge(air_temperature_data, on='DateTime', how='inner')
final_merged_data = final_merged_data.merge(pressure_data, on='DateTime', how='inner')
final_merged_data = final_merged_data.merge(wind_speed_data, on='DateTime', how='inner')

# Step 10: Save the Final Input File
final_merged_data.to_csv('final_input_file.csv', index=False)
