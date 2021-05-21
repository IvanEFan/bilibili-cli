import click
from bilibili import data
from bilibili.renderer import Renderer

@click.command()
def cli():
    pass

if __name__ == '__main__':
    renderer = Renderer()
    renderer.render_videos(data.get_rank())
    cli()