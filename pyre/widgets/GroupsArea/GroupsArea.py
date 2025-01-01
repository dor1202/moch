from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import DataTable
from textual.reactive import reactive


class GroupsArea(Widget):
    BORDER_TITLE = "Groups"

    # [Group Name, Position, Match]
    groups = reactive([])

    def compose(self) -> ComposeResult:
        yield DataTable(id="GroupsArea")

    def on_mount(self):
        table = self.query_one(DataTable)
        table.disabled = True
        table.show_cursor = False
        table.cell_padding = 4
        table.add_columns("Group Name", "Position", "Match")

    def watch_groups(self, value):
        table = self.query_one(DataTable)
        table.clear()
        table.add_rows(value)
