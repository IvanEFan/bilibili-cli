import click
from bilibili import data
from bilibili.renderer import TableLayoutRenderer

@click.command()
def cli():
    pass

if __name__ == '__main__':
    renderer = TableLayoutRenderer()
    renderer.render_videos(data.get_rank())
    cli()