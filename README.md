# CLIDatasets
Command Line Interface to handle datasets. 

## Features

- **Data Processing and Analysis**: Load, process, and analyze datasets through the CLI.
- **Data Visualization**: Display processed data in the web browser using charts and graphs.
- **Scalability**: Efficiently handle large datasets with Dask.
- **Database Integration**: Connect to and interact with remote PostgreSQL databases.
- **RESTful APIs**: Use Flask to create endpoints for data processing and visualization.

## Technologies Used

- **Languages**: Python, SQL (PostgreSQL), JavaScript, TypeScript
- **Frameworks**: Flask, React, Dask
- **Developer Tools**: Git, TravisCI, Google Cloud Platform
- **Libraries**: pandas, NumPy, Matplotlib

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL (for remote database integration)

1. **Clone the Repository**
2. **Set Up Python Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Python Dependencies**: pip install -r requirements.txt
4. **Set Up the Frontend**:

    ```sh
    cd web
    npm install
    npm run build
    mkdir static  # Create static directory if it doesn't exist
    mv build/* static/
    mv build/.* static/  # Move hidden files like .gitignore
    cd ..
    ```
5. **Configuration**: 
    Update the database configuration in `web/app.py` to connect to your PostgreSQL database:

    ```python
    # web/app.py

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname:port/database'
    ```
6. **Run Command to Process Datasets**: 
    ```
    data-analyzer process path/to/dataset.csv --output path/to/output.csv
    ```