from os import mkdir
from pathlib import Path

class Site:
    
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self):
        part1 = self.dest
        part2 = Path.relative_to(self.source)
        directory = part1 + "/" + part2
        Path(directory).mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if Path(path).is_dir():
                self.create_dir(path)