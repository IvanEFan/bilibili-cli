import click
from rich.rule import Rule

from bilibili import data
from bilibili.renderer import ListLayoutRenderer, TableLayoutRenderer, GridLayoutRenderer

@click.group(invoke_without_command=True)
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
@click.pass_context
def cli(ctx, layout, limit_results):
    if ctx.invoked_subcommand is None:
        renderer = ListLayoutRenderer()
        if layout == 'table':
            renderer = TableLayoutRenderer()
        elif layout == 'grid':
            renderer = GridLayoutRenderer()
        with renderer.console.status('[bold green]Loading data...'):
            renderer.render_videos(data.get_rank(count=limit_results))

@cli.command()
@click.argument('vid')
def info(vid):
    video = data.Video(vid)
    renderer = ListLayoutRenderer()
    with renderer.console.status('[bold green]Loading data...'):
        renderer.render_video(video)
        renderer.console.print(Rule(style='bright_yellow'))

if __name__ == '__main__':
    cli()