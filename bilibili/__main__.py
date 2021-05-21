import click
from bilibili import data
from bilibili.renderer import ListLayoutRenderer

@click.command()
def cli():
    pass

if __name__ == '__main__':
    renderer = ListLayoutRenderer()
    renderer.render_videos(data.get_rank())
    cli()