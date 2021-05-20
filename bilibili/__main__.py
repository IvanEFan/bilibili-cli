import click
from bilibili import data

@click.command()
def cli():
    pass

if __name__ == '__main__':
    data.get_rank()
    # data.get_popular_weekly()
    cli()