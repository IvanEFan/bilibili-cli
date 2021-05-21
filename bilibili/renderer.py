from rich.console import Console
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
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column(justify='right')
        title = Text(video.title)
        title.stylize(f'yellow link {video.link}')
        stats = Text(f'👀 {video.view} 🪙 {video.coin} ⭐ {video.favorite}')
        grid.add_row(title, stats)
        grid.add_row()
        up = Text(video.up, style='bold')
        grid.add_row(up)
        grid.add_row()
        desc = Text(video.desc if video.desc else 'no description', style='green')
        grid.add_row(desc)
        self.console.print(grid)

    def render_videos(self, videos: [Video]):
        for video in videos:
            self.render_video(video)
        self.console.print(Rule(style='bright_yellow'))