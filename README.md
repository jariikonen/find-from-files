# find-from-files

![SVG animation of using the find-in-files command.](fff.svg)

Simple CLI application for searching keywords/phrases or regular expression patterns from text files.

## Usage

```
usage: find-from-files [-h] [-l] [-r] [-s [SUFFIX ...]] [-S [SKIP ...]] [-a]
  [-q] [-qq] base_directory search_string

This script can be useful, e.g., for analyzing log files. When used without the
--regex flag, it traverses through directories starting from the
<base_directory> and prints the name of the file containing <search_string> and
the line that it is on. This is handy if you want to quickly find the files
that contain the string you are looking for. When used with the --regex flag,
it searches for the <search_string> with Python regular expression function
re.findall() in the files, and prints a summary containing the matches and
their number. This allows you to search for all occurrences of a pattern in
files. If the --whole-line flag is used, the whole line is printed instead of
just the match (does nothing without the --regex flag).

positional arguments:
  base_directory        Base directory to start the search from.
  search_string         String/regex to search for.

options:
  -h, --help            show this help message and exit
  -l, --whole-line      Search for the whole line containing the search string.
                        Only works with the --regexp flag.
  -r, --regexp          Search using regular expression.
  -s, --suffix [SUFFIX ...]
                        File suffix to search for. Files without this suffix
                        will be skipped.
  -S, --skip [SKIP ...]
                        Skip folders that start with this prefix.
  -a, --no-ansi         Do not use ANSI codes for output. Redirections never
                        contain ANSI codes.
  -q, --quiet           Do not print skipped folders or files.
  -qq, --quieter        Do not print skipped folders or files, and only print
                        the files that contain the search string/pattern.
  -V, --version         show program's version number and exit
```
