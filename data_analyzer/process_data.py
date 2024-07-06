import dask.dataframe as daskDataframe

# Global dataframe
dataframe = None

def load_data(source):
    global dataframe
    try:
        print(f"Loading data from {source}")
        # Load data using Dask
        dataframe = daskDataframe.read_csv(source)
        print("Data loaded successfully")
        print(dataframe.head())
    except Exception as e:
        raise Exception(f"Failed to load data: {str(e)}")

def process_data():
    global dataframe
    try:
        if dataframe is None:
            raise Exception("Dataframe is not loaded.")
        
        # Example data cleaning and analysis
        dataframe = dataframe.dropna()  # Drop missing values
        dataframe['mean_salary'] = dataframe['salary'].mean().compute()  # Compute and add a new column with the mean salary
        print("Data processed successfully")
        print(dataframe.head())
    except Exception as e:
        raise Exception(f"Failed to process data: {str(e)}")

def save_data(output):
    global dataframe
    try:
        if dataframe is None:
            raise Exception("Dataframe is not loaded.")
        
        # Compute and save the result
        dataframe.compute().to_csv(output, index=False)
        print(f"Data saved successfully to {output}")
    except Exception as e:
        raise Exception(f"Failed to save data: {str(e)}")
