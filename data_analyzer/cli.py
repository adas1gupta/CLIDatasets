import click
from data_analyzer.process_data import process_file

@click.group()
def cli():
    pass

@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), default='processed_data.csv')
def process(source, output):
    process_file(source, output)

cli.add_command(process)

if __name__ == '__main__':
    cli()
