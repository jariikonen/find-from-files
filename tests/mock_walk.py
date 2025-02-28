"""A class that can be used for mocking the os.walk function."""

import os

from tests.constants import DirectoryStructure


class MockWalk:
    """A class that can be used for mocking the os.walk function.

    Attributes:
        dir_structure: A DirectoryStructure to be walked.
        current: Current dir_structure index.
        root: Root directory path.
    """

    def __init__(self, dir_structure: DirectoryStructure, root: str = ""):
        self.dir_structure = dir_structure
        self.current = -1
        self.root = root

    def __iter__(self):
        return self

    def __next__(self) -> tuple[str, list[str], list[str]]:
        self.current += 1
        if self.current >= len(self.dir_structure):
            raise StopIteration()
        dir_content = self.dir_structure[self.current]
        root = os.path.join(self.root, dir_content["root"])
        return root, dir_content["dirs"], dir_content["files"]
