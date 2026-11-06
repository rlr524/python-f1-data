import fastf1

# Enable caching
fastf1.Cache.configure(cache_dir='/Users/rob/Developer/PythonProjects/f1_data/cache')

# Load a specific session
session = fastf1.get_session(2026, 'Monaco', 'R')
session.load()

# Select Antonelli's laps
driver_laps = session.laps.pick_drivers('ANT')

print("Number of laps:", len(driver_laps))

# Select fastest lap
fastest_lap = driver_laps.pick_fastest()

print("\nFastest lap:")
print(fastest_lap[['Driver', 'LapNumber', 'LapTime', 'IsAccurate']]) # type: ignore

# Retrieve the two telemetry sources separately
car_data = fastest_lap.get_car_data() # type: ignore
pos_data = fastest_lap.get_pos_data() # type: ignore

print("\nCar data:")
print("Shape:", car_data.shape)
print("Columns:", car_data.columns.tolist())

print("\nPosition data:")
print("Shape:", pos_data.shape)
print("Columns:", pos_data.columns.tolist())