import sys
import os

# Ensure the parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_analyzer.process_data import process_file
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('source', type=str)
@click.option('--output', type=str, default='processed_data.csv', help='Output file path.')
def process(source, output):
    """Process the dataset."""
    process_file(source, output)
    click.echo(f'Data processed and saved to {output}.')

cli.add_command(process)

if __name__ == '__main__':
    cli()
