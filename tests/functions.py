"""Functions used in the find_it package tests."""

import os
from tests.constants import (
    CHECKING_FILE,
    CHECKING_DIR,
    CLEAR_STYLING,
    ROOT,
    SKIPPING_FILE,
    SKIPPING_DIR,
    DirectoryStructure,
)


def check_dirs_and_files_are_checked(
    dir_structure: DirectoryStructure, output: str
):
    """Asserts that the output is correct when everything is checked.

    Asserts that the output string contains lines stating that the files and
    directories in dir_structure are checked.

    Args:
        dir_structure: A DirectoryStructure to go through.
        output: The output string that should contain the checked statements.
    """
    for entry in dir_structure:
        dir_path = os.path.join(ROOT, entry["root"])
        assert f"{CHECKING_DIR}{dir_path}{CLEAR_STYLING}" in output

        for file in entry.get("files", []):
            file_path = os.path.join(dir_path, file)
            assert f"{CHECKING_FILE}{file_path}{CLEAR_STYLING}" in output


def check_dirs_and_files_are_skipped(
    dir_structure: DirectoryStructure, output: str
):
    """Asserts that the output is correct when directory structure is skipped.

    Asserts that the output string contains a line stating that the root
    directory of the dir_structure is skipped, and that the output does not
    contain any lines related to the other directories and files in the
    dir_structure.

    Args:
        dir_structure: A DirectoryStructure to go through.
        output: The output string that should contain the checked statements.
    """
    for i, entry in enumerate(dir_structure):
        dir_path = os.path.join(ROOT, entry["root"])
        if i == 0:
            assert f"{SKIPPING_DIR}{dir_path}{CLEAR_STYLING}" in output
            assert f"{CHECKING_DIR}{dir_path}{CLEAR_STYLING}" not in output
        else:
            assert dir_path not in output

        for file in entry.get("files", []):
            file_path = os.path.join(dir_path, file)
            assert file_path not in output


def check_files_are_checked(
    dir_structure: DirectoryStructure, files: list[str], output: str
):
    """Asserts that the output is correct when some files are checked.

    Asserts that the output string contains lines stating that the files in
    files list are checked.

    Args:
        dir_structure: A DirectoryStructure to go through.
        files: Names of the files that should be checked.
        output: The output string that should contain the checked statements.
    """
    for entry in dir_structure:
        dir_path = os.path.join(ROOT, entry["root"])

        for file in entry.get("files", []):
            file_path = os.path.join(dir_path, file)
            if file in files:
                assert f"{CHECKING_FILE}{file_path}{CLEAR_STYLING}" in output


def check_files_are_skipped(
    dir_structure: DirectoryStructure, files: list[str], output: str
):
    """Asserts that the output is correct when some files are skipped.

    Asserts that the output string contains lines stating that the files in
    files list are skipped.

    Args:
        dir_structure: A DirectoryStructure to go through.
        files: Names of the files that should be skipped.
        output: The output string that should contain the checked statements.
    """
    for entry in dir_structure:
        dir_path = os.path.join(ROOT, entry["root"])

        for file in entry.get("files", []):
            file_path = os.path.join(dir_path, file)
            if file in files:
                assert f"{SKIPPING_FILE}{file_path}{CLEAR_STYLING}" in output


def check_files_are_not_printed(
    dir_structure: DirectoryStructure, files: list[str], output: str
):
    """Asserts that the output does not contained skipped files.

    Asserts that the output string does not contain lines stating that the
    files in files list are skipped.

    Args:
        dir_structure: A DirectoryStructure to go through.
        files: Names of the files that should be skipped.
        output: The output string to examine.
    """
    for entry in dir_structure:
        dir_path = os.path.join(ROOT, entry["root"])

        for file in entry.get("files", []):
            file_path = os.path.join(dir_path, file)
            if file in files:
                assert (
                    f"{SKIPPING_FILE}{file_path}{CLEAR_STYLING}" not in output
                )
                assert (
                    f"{CHECKING_FILE}{file_path}{CLEAR_STYLING}" not in output
                )


def check_dirs_are_not_printed(
    dir_structure: DirectoryStructure, dirs: list[str], output: str
):
    """Asserts that the output does not contained skipped directories.

    Asserts that the output string does not contain lines stating that the
    directories in dirs list are skipped.

    Args:
        dir_structure: A DirectoryStructure to go through.
        dirs: Names of the files that should be skipped.
        output: The output string to examine.
    """
    for entry in dir_structure:
        parent_path = os.path.join(ROOT, entry["root"])

        for dir_name in entry.get("dirs", []):
            dir_path = os.path.join(parent_path, dir_name)
            if dir in dirs:
                assert f"{SKIPPING_DIR}{dir_path}{CLEAR_STYLING}" not in output
                assert f"{CHECKING_DIR}{dir_path}{CLEAR_STYLING}" not in output


def check_dirs_are_checked(
    dir_structure: DirectoryStructure, dirs: list[str], output: str
):
    """Asserts that the output string containes directories.

    Asserts that the output string contain lines stating that the directories
    in dirs list are checked.

    Args:
        dir_structure: A DirectoryStructure to go through.
        dirs: Names of the files that should be checked.
        output: The output string to examine.
    """
    for entry in dir_structure:
        parent_path = os.path.join(ROOT, entry["root"])

        for dir_name in entry.get("dirs", []):
            dir_path = os.path.join(parent_path, dir_name)
            if dir in dirs:
                assert f"{SKIPPING_DIR}{dir_path}{CLEAR_STYLING}" not in output
                assert f"{CHECKING_DIR}{dir_path}{CLEAR_STYLING}" in output
