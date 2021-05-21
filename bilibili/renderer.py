from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

from bilibili.data import Video

class Renderer:
    def __init__(self):
        self.console = Console()

    def render_video(self, video: Video):
        pass

    def render_videos(self, videos: [Video]):
        pass

class ListLayoutRenderer(Renderer):
    def __init__(self):
        super().__init__()

    def render_video(self, video: Video):
        self.console.print(Rule(style='bright_yellow'))
        formatted = video.get_formatted()
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column(justify='right')

        grid.add_row(formatted['title'], formatted['stats'])
        grid.add_row()

        up = formatted['up']
        up.stylize('bold')
        grid.add_row(up)
        grid.add_row()

        desc = formatted['desc']
        desc.stylize('green')
        grid.add_row(desc)

        self.console.print(grid)

    def render_videos(self, videos: [Video]):
        for video in videos:
            self.render_video(video)
        self.console.print(Rule(style='bright_yellow'))

class TableLayoutRenderer(Renderer):
    def __init__(self):
        self.table = Table(leading=1)
        super().__init__()

    def render_video(self, video: Video):
        formatted = video.get_formatted()
        self.table.add_row(formatted['title'], formatted['up'], formatted['desc'], formatted['stats'])

    def render_videos(self, videos: [Video]):
        # make the columns
        self.table.add_column("Title", style="bold cyan")
        self.table.add_column("UP", style="green")
        self.table.add_column("Description", style="blue")
        self.table.add_column("Stats", style="magenta")

        for video in videos:
            self.render_video(video)
        self.console.print(self.table)
        self.console.print(Rule(style='bright_yellow'))

class GridLayoutRenderer(Renderer):
    def __init__(self):
        self.panels = []
        super().__init__()

    def render_video(self, video: Video):
        formatted = video.get_formatted()
        title = formatted['title']
        title.stylize('bold')
        stats = formatted['stats']
        stats.stylize('blue')
        up = formatted['up']
        up.stylize('magenta')
        desc = formatted['desc']
        desc.truncate(90, overflow='ellipsis')
        summary = Text.assemble(
            title,
            '\n',
            stats,
            '\n',
            up,
            '\n',
            desc
        )
        self.panels.append(Panel(summary, expand=True))

    def render_videos(self, videos: [Video]):
        for video in videos:
            self.render_video(video)
        self.console.print(Columns(self.panels, width=30, expand=True))