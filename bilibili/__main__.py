import click

from bilibili import data
from bilibili.renderer import ListLayoutRenderer, TableLayoutRenderer, GridLayoutRenderer

@click.command()
@click.option(
    '--layout',
    '-L',
    type=click.Choice(['list', 'table', 'grid'], case_sensitive=False),
    help='The output format (list, table or grid), default is list'
)
@click.option(
    "--limit-results",
    "-r",
    type=int,
    default=15,
    help="Limit the number of results. Default: 15",
)
def cli(layout, limit_results):
    renderer = ListLayoutRenderer()
    if layout == 'table':
        renderer = TableLayoutRenderer()
    elif layout == 'grid':
        renderer = GridLayoutRenderer()
    with renderer.console.status('[bold green]Loading data...'):
        renderer.render_videos(data.get_rank(count=limit_results))
    pass

if __name__ == '__main__':
    cli()