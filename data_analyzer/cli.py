import click
import pandas as panda
from sqlalchemy import create_engine
import requests
from io import StringIO, BytesIO

dataframe = None

@click.group()
def cli():
    pass

@click.command()
@click.argument('source', type=str)
@click.option('--format', type=click.Choice(['csv', 'json', 'excel', 'sql', 'url']), required=True, help='Format of the input file.')
@click.option('--table', type=str, default=None, help='Table name for SQL input.')
@click.option('--db_url', type=str, default=None, help='Database URL for SQL input.')
def load(source, format, table, db_url):
    #globalize dataset for future functions
    global dataframe
    try:
        if format == 'csv':
            dataframe = panda.read_csv(source)
        elif format == 'json':
            dataframe = panda.read_json(source)
        elif format == 'excel':
            dataframe = panda.read_excel(source)
        elif format == 'sql':
            if db_url is None or table is None:
                raise click.ClickException('For SQL input, both --db_url and --table are required.')
            engine = create_engine(db_url)
            dataframe = panda.read_sql_table(table, con=engine)
        elif format == 'url':
            response = requests.get(source)
            if source.endswith('.csv'):
                dataframe = panda.read_csv(StringIO(response.text))
            elif source.endswith('.json'):
                dataframe = panda.read_json(StringIO(response.text))
            elif source.endswith('.xlsx'):
                dataframe = panda.read_excel(BytesIO(response.content))
            else:
                raise click.ClickException('Unsupported URL file format.')
        click.echo(f'Dataset loaded with {dataframe.shape[0]} rows and {dataframe.shape[1]} columns.')
    except Exception as exception:
        raise click.ClickException(str(exception))

@click.command()
@click.argument('destination', type=str)
@click.option('--format', type=click.Choice(['csv', 'json', 'excel', 'sql']), required=True, help='Format of the output file.')
@click.option('--table', type=str, default=None, help='Table name for SQL output.')
@click.option('--db_url', type=str, default=None, help='Database URL for SQL output.')
def save(destination, format, table, db_url):
    #globalize dataset for future functions
    try:
        if dataframe is None:
            raise click.ClickException('No dataset loaded. Please load a dataset first.')

        if format == 'csv':
            dataframe.to_csv(destination, index=False)
        elif format == 'json':
            dataframe.to_json(destination)
        elif format == 'excel':
            dataframe.to_excel(destination, index=False)
        elif format == 'sql':
            if db_url is None or table is None:
                raise click.ClickException('For SQL output, both --db_url and --table are required.')
            engine = create_engine(db_url)
            dataframe.to_sql(table, con=engine, if_exists='replace', index=False)
        click.echo(f'Dataset saved to {destination}.')
    except Exception as exception:
        raise click.ClickException(str(exception))

@click.command()
def summary():
    global dataframe

    if dataframe is not None:
        click.echo(dataframe.describe())
    else:
        raise click.ClickException('No dataset loaded. Please load a dataset first.')

@click.command()
def head():
    """Display the first few rows of the dataset."""
    if dataframe is not None:
        click.echo(dataframe.head())
    else:
        click.echo('No dataset loaded. Please load a dataset first.')

@click.command()
def tail():
    """Display the last few rows of the dataset."""
    if dataframe is not None:
        click.echo(dataframe.tail())
    else:
        click.echo('No dataset loaded. Please load a dataset first.')

cli.add_command(load)
cli.add_command(save)
cli.add_command(summary)
cli.add_command(head)
cli.add_command(tail)

if __name__ == '__main__':
    cli()
