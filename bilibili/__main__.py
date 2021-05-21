import click
from bilibili import data
from bilibili.renderer import ListLayoutRenderer, TableLayoutRenderer

@click.command()
@click.option(
    '--layout',
    '-L',
    type=click.Choice(['list', 'table'], case_sensitive=False),
    help='The output format (list or table), default is list'
)
def cli(layout):
    renderer = ListLayoutRenderer()
    if layout == 'table':
        renderer = TableLayoutRenderer()
    renderer.render_videos(data.get_rank())
    pass

if __name__ == '__main__':
    cli()