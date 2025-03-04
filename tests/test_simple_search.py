"""Tests for simple searches with find_from_files.

A simple search here means a keyword/phrase search that does not use regular
expression. In other words, the searches with the --regexp flag are not tested
here.
"""

import os
import sys
from unittest.mock import patch, mock_open
from find_from_files import find_from_files

from tests.constants import (
    DIRECTORIES,
    START_MATCH_STYLE,
    CLEAR_STYLING,
    DIRECTORY_STRUCTURE,
    ROOT,
    FILES_LOG,
    FILES_PY,
    FILES_TXT,
    FILES_WITHOUT_SUFFIX,
)
from tests.mock_walk import MockWalk
from tests.functions import (
    check_dirs_and_files_are_checked,
    check_dirs_and_files_are_skipped,
    check_dirs_are_checked,
    check_dirs_are_not_printed,
    check_files_are_checked,
    check_files_are_not_printed,
    check_files_are_skipped,
)

SIMPLE_MATCH_FOUND = (
    f"Found on line 1: Tämä on {START_MATCH_STYLE}test{CLEAR_STYLING}i."
)


@patch.object(sys, "argv", ["find_from_files", ROOT, "test"])
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_checks_every_file(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug
    check_dirs_and_files_are_checked(DIRECTORY_STRUCTURE, captured.out)
    assert captured.out.count(SIMPLE_MATCH_FOUND) == 11
    assert captured.err == ""
    assert captured.out.count("\n") == 29


@patch.object(
    sys, "argv", ["find_from_files", ROOT, "test", "--skip", "skipThis"]
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_skips_directories_correctly(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    checked_dir_structure = DIRECTORY_STRUCTURE[0:1]
    checked_dir_structure.extend(DIRECTORY_STRUCTURE[4:])
    skipped_dir_structure = DIRECTORY_STRUCTURE[2:3]
    check_dirs_and_files_are_checked(checked_dir_structure, captured.out)
    check_dirs_and_files_are_skipped(skipped_dir_structure, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 8
    assert captured.err == ""
    assert captured.out.count("\n") == 22


@patch.object(
    sys, "argv", ["find_from_files", ROOT, "test", "--suffix", ".log"]
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_skips_files_without_correct_suffix(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY + FILES_TXT
    check_files_are_skipped(DIRECTORY_STRUCTURE, skipped_files, captured.out)
    checked_files = FILES_LOG
    check_files_are_checked(DIRECTORY_STRUCTURE, checked_files, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 5
    assert captured.err == ""
    assert captured.out.count("\n") == 23


@patch.object(
    sys,
    "argv",
    ["find_from_files", ROOT, "test", "--skip", "dir1", "skipThis", "dir5"],
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_skips_multiple_directories_correctly(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    checked_dir_structure = DIRECTORY_STRUCTURE[0:1]
    checked_dir_structure.extend(DIRECTORY_STRUCTURE[4:5])
    skipped_dir_structure = DIRECTORY_STRUCTURE[2:3]
    skipped_dir_structure.extend(DIRECTORY_STRUCTURE[6:6])
    check_dirs_and_files_are_checked(checked_dir_structure, captured.out)
    check_dirs_and_files_are_skipped(skipped_dir_structure, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 4
    assert captured.err == ""
    assert captured.out.count("\n") == 14


@patch.object(
    sys, "argv", ["find_from_files", ROOT, "test", "--suffix", ".log", ".txt"]
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_handles_many_file_suffixes_correctly(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY
    check_files_are_skipped(DIRECTORY_STRUCTURE, skipped_files, captured.out)
    checked_files = FILES_LOG, FILES_TXT
    check_files_are_checked(DIRECTORY_STRUCTURE, checked_files, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 6
    assert captured.err == ""
    assert captured.out.count("\n") == 24


@patch.object(
    sys,
    "argv",
    [
        "find_from_files",
        ROOT,
        "test",
        "--suffix",
        ".log",
        "--skip",
        "dir1",
        "skipThis",
        "--quiet",
    ],
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_quiet_flag_works_correctly(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    skipped_dirs = ["dir1", "skipThis"]
    check_dirs_are_not_printed(DIRECTORY_STRUCTURE, skipped_dirs, captured.out)
    checked_dirs = [dir for dir in DIRECTORIES if dir not in skipped_dirs]
    check_dirs_are_checked(DIRECTORY_STRUCTURE, checked_dirs, captured.out)
    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY + FILES_TXT
    check_files_are_not_printed(
        DIRECTORY_STRUCTURE, skipped_files, captured.out
    )
    checked_files = ["file1.log", "file7.log", "file10.log"]
    check_files_are_checked(DIRECTORY_STRUCTURE, checked_files, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 3
    assert captured.err == ""
    assert captured.out.count("\n") == 10


@patch.object(
    sys,
    "argv",
    [
        "find_from_files",
        ROOT,
        "this is not found",
        "--suffix",
        ".log",
        "--skip",
        "dir1",
        "skipThis",
        "--quiet",
    ],
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_quiet_flag_prints_checked_files_with_no_matches(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    skipped_dirs = ["dir1", "skipThis"]
    check_dirs_are_not_printed(DIRECTORY_STRUCTURE, skipped_dirs, captured.out)
    checked_dirs = [dir for dir in DIRECTORIES if dir not in skipped_dirs]
    check_dirs_are_checked(DIRECTORY_STRUCTURE, checked_dirs, captured.out)
    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY + FILES_TXT
    check_files_are_not_printed(
        DIRECTORY_STRUCTURE, skipped_files, captured.out
    )
    checked_files = ["file1.log", "file7.log", "file10.log"]
    check_files_are_checked(DIRECTORY_STRUCTURE, checked_files, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 0
    assert captured.err == ""
    assert captured.out.count("\n") == 7


@patch.object(
    sys,
    "argv",
    [
        "find_from_files",
        ROOT,
        "test",
        "--suffix",
        ".log",
        "--skip",
        "dir1",
        "skipThis",
        "--quieter",
    ],
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_quieter_flag_prints_files_with_matches(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    # print(captured.out)  # uncomment to debug

    skipped_dirs = ["dir1", "skipThis"]
    check_dirs_are_not_printed(DIRECTORY_STRUCTURE, skipped_dirs, captured.out)
    checked_dirs = [dir for dir in DIRECTORIES if dir not in skipped_dirs]
    check_dirs_are_checked(DIRECTORY_STRUCTURE, checked_dirs, captured.out)
    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY + FILES_TXT
    check_files_are_not_printed(
        DIRECTORY_STRUCTURE, skipped_files, captured.out
    )
    checked_files = ["file1.log", "file7.log", "file10.log"]
    check_files_are_checked(DIRECTORY_STRUCTURE, checked_files, captured.out)

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 3
    assert captured.err == ""
    assert captured.out.count("\n") == 10


@patch.object(
    sys,
    "argv",
    [
        "find_from_files",
        ROOT,
        "this does not match",
        "--suffix",
        ".log",
        "--skip",
        "dir1",
        "skipThis",
        "--quieter",
    ],
)
@patch.object(
    os, "walk", lambda *args, **kwargs: MockWalk(DIRECTORY_STRUCTURE, args[0])
)
@patch.object(find_from_files, "is_binary", lambda x: False)
def test_quieter_flag_does_not_print_files_with_no_matches(capsys):
    with patch("builtins.open", mock_open(read_data="Tämä on testi.\n")):
        find_from_files.main()

    captured = capsys.readouterr()
    print(captured.out)  # uncomment to debug

    skipped_dirs = ["dir1", "skipThis"]
    check_dirs_are_not_printed(DIRECTORY_STRUCTURE, skipped_dirs, captured.out)
    skipped_files = (
        FILES_WITHOUT_SUFFIX
        + FILES_PY
        + FILES_TXT
        + ["file1.log", "file7.log", "file10.log"]
    )
    checked_dirs = [dir for dir in DIRECTORIES if dir not in skipped_dirs]
    check_dirs_are_checked(DIRECTORY_STRUCTURE, checked_dirs, captured.out)
    skipped_files = FILES_WITHOUT_SUFFIX + FILES_PY + FILES_TXT
    check_files_are_not_printed(
        DIRECTORY_STRUCTURE, skipped_files, captured.out
    )

    assert captured.out.count(SIMPLE_MATCH_FOUND) == 0
    assert captured.err == ""
    assert captured.out.count("\n") == 4
