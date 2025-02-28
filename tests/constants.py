"""Constants used in the find_it package tests."""

from colorama import Fore, Back, Style

type DirectoryStructure = list[
    dict["root":str, "dirs" : list[str], "files" : list[str]]
]

CHECKING_DIR = f"{Fore.GREEN}Checking folder: {Fore.YELLOW}"
CHECKING_FILE = f"{Fore.BLUE}Checking file: {Fore.YELLOW}"
SKIPPING_DIR = f"{Fore.RED}Skipping folder: {Fore.YELLOW}"
SKIPPING_FILE = f"{Fore.RED}Skipping file: {Fore.YELLOW}"
START_MATCH_STYLE = Back.RED
CLEAR_STYLING = Style.RESET_ALL

DIRECTORY_STRUCTURE: DirectoryStructure = [
    {
        "root": "",
        "dirs": ["dir1", "skipThis", "dir2"],
        "files": ["file1.log", "file2.txt"],
    },
    {"root": "dir1", "dirs": [], "files": ["file3", "file4.py"]},
    {
        "root": "skipThis",
        "dirs": ["dir3"],
        "files": ["file5.py", "file6.log"],
    },
    {"root": "skipThis/dir3", "dirs": [], "files": ["file9.log"]},
    {
        "root": "dir2",
        "dirs": ["dir4", "dir5"],
        "files": ["file7.log", "file8.py"],
    },
    {"root": "dir2/dir4", "dirs": [], "files": []},
    {"root": "dir2/dir5", "dirs": [], "files": ["file10.log", "file11"]},
]

ROOT = "."

DIRECTORIES = [
    "dir1",
    "skipThis",
    "dir2",
    "skipThis/dir3",
    "dir2/dir4",
    "dir2/dir5",
]
FILES_LOG = ["file1.log", "file6.log", "file7.log", "file9.log", "file10.log"]
FILES_TXT = ["file2.txt"]
FILES_PY = ["file4.py", "file5.py", "file8.py"]
FILES_WITHOUT_SUFFIX = ["file3", "file11"]
