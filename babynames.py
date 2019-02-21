#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = 'jayaimzzz'

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename) as file:
        data = file.read()
        pattern = re.compile(r'Popularity\sin\s(\d{4})')
        matches = pattern.finditer(data)
        for match in matches:
            year = match.group(1)
        pattern = re.compile(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')
        matches = pattern.finditer(data)
        list1 = []
        for match in matches:
            rank = match.group(1)
            bname = match.group(2) + " " + rank
            gname = match.group(3) + " " + rank
            list1.append(bname)
            list1.append(gname)
        return [year] + sorted(list1)
    return


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile
    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for file in file_list:
        data = extract_names(file)
        if create_summary:
            summaryfile = open("summary" + file,"w")
            for item in data:
                summaryfile.write(item + "\n")
        else:
            print data


if __name__ == '__main__':
    main()
