import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dask.dataframe as daskDataframe
from web.app import app, db, Data
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.exc import OperationalError
from dask.diagnostics import ProgressBar

dataframe = None

def load_data(source):
    global dataframe
    dataframe = daskDataframe.read_csv(source)
    dataframe = dataframe.dropna()
    print(f"Data loaded from {source}")

def process_data():
    global dataframe
    if dataframe is not None:
        numeric_columns = dataframe.select_dtypes(include=['number']).columns
        for col in numeric_columns:
            mean_col_name = f'mean_{col}'
            dataframe[mean_col_name] = dataframe[col].mean().compute()
        print("Data processed successfully")
    else:
        raise ValueError("Dataframe is not loaded")

def save_data(output):
    global dataframe
    if dataframe is not None:
        # Save to CSV
        with ProgressBar():
            dataframe.compute().to_csv(output, index=False)
        print(f"Data saved to {output}")
        
        with app.app_context():
            # Drop the existing table
            Data.__table__.drop(db.engine, checkfirst=True)
            
            # Clear all columns except 'id'
            for col in list(Data.__table__.columns):
                if col.name != 'id':
                    Data.__table__.c.pop(col.name)
            
            # Dynamically create table columns based on dataframe
            for column in dataframe.columns:
                if column != 'id':
                    if dataframe[column].dtype == 'float64':
                        setattr(Data, column, Column(Float))
                    elif dataframe[column].dtype == 'int64':
                        setattr(Data, column, Column(Integer))
                    else:
                        setattr(Data, column, Column(String(255)))
            
            # Create the table with the new structure
            db.create_all()
            
            # Compute the entire dataframe
            with ProgressBar():
                df_computed = dataframe.compute()
            
            # Insert data in chunks to avoid memory issues
            chunk_size = 1000
            total_rows = len(df_computed)
            for i in range(0, total_rows, chunk_size):
                chunk = df_computed.iloc[i:i+chunk_size]
                db.session.bulk_insert_mappings(Data, chunk.to_dict(orient="records"))
                db.session.commit()
                print(f"Inserted rows {i+1} to {min(i+chunk_size, total_rows)} of {total_rows}")
        
        print("Data saved to database")
    else:
        raise ValueError("Dataframe is not loaded")

def process_file(source, output):
    load_data(source)
    process_data()
    save_data(output)