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
def cli(layout):
    renderer = ListLayoutRenderer()
    if layout == 'table':
        renderer = TableLayoutRenderer()
    elif layout == 'grid':
        renderer = GridLayoutRenderer()
    renderer.render_videos(data.get_rank())
    pass

if __name__ == '__main__':
    cli()