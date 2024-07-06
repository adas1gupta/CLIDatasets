import click
from data_analyzer.process_data import *

@click.group()
def cli():
    pass

@click.command()
@click.argument('source', type=str)
@click.option('--output', type=str, default='../web/processed_data.csv', help='Output file path.')
def process(source, output):
    try:
        load_data(source)
        process_data()
        save_data(output)
        click.echo(f"Data processed and saved to {output}.")
    except Exception as e:
        raise click.ClickException(f"Error: {str(e)}")

cli.add_command(process)

if __name__ == '__main__':
    cli()
