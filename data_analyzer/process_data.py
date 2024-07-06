import dask.dataframe as daskDataframe

dataframe = None

def load_data(source):
    global dataframe
    dataframe = daskDataframe.read_csv(source)
    dataframe = dataframe.dropna()
    print(f"Data loaded from {source}")

def process_data():
    global dataframe
    if dataframe is not None:
        dataframe['mean_salary'] = dataframe['salary'].mean().compute()
        print("Data processed successfully")
    else:
        raise ValueError("Dataframe is not loaded")

def save_data(output):
    global dataframe
    if dataframe is not None:
        dataframe.compute().to_csv(output, index=False)
        print(f"Data saved to {output}")
    else:
        raise ValueError("Dataframe is not loaded")

def process_file(source, output):
    load_data(source)
    process_data()
    save_data(output)
