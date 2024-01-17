"""Classic UNIX-style real-time text formatter with unicode and pipe support

This program allows you to format one / multiple files or piped stream in the format of classic UNIX docs,
splitting them into columns, adding line numbers, header, etc. Formatting is done line by line in real time
(i.e., the output of the program can also be piped to another program)
In fact, this is an improved version of the "pr" command with Unicode support

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Fern Lane"
__copyright__ = "Copyright 2024, Fern Lane"
__date__ = "2024/01/17"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__version__ = "1.0.0"

import argparse
import datetime
import fileinput
import sys
import textwrap

# Default cli argument values
COLUMNS_DEFAULT = 2
WIDTH_DEFAULT = 80
PAGE_SIZE_DEFAULT = 68
SEPARATOR_DEFAULT = "    "
DATE_FORMAT_DEFAULT = "%Y-%m-%d %H:%M"
FIRST_LINE_NUMBER_DEFAULT = 1
FIRST_PAGE_NUMBER_DEFAULT = 1
LINES_BEFORE_HEADER_DEFAULT = 2
LINES_AFTER_HEADER_DEFAULT = 2
LINES_AFTER_PAGE_DEFAULT = 5
LINE_NUMBER_PLACEHOLDER_DEFAULT = "{line:>5}   "
PAGE_NUMBER_PLACEHOLDER_DEFAULT = "Page: {page}"


def parse_args() -> argparse.Namespace:
    """Parses cli arguments

    Returns:
        argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="classic UNIX-style real-time text formatter with unicode and pipe support"
    )
    parser.add_argument(
        "-c",
        "--columns",
        type=int,
        default=COLUMNS_DEFAULT,
        required=False,
        help=f"Number of columns (default: {COLUMNS_DEFAULT})",
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=WIDTH_DEFAULT,
        required=False,
        help=f"total width of each line (default: {WIDTH_DEFAULT})",
    )
    parser.add_argument(
        "-p",
        "--page-size",
        type=int,
        default=PAGE_SIZE_DEFAULT,
        required=False,
        help=f"total lines per page (including header and lines-after-page) (default: {PAGE_SIZE_DEFAULT})",
    )
    parser.add_argument(
        "-t",
        "--title",
        type=str or None,
        default=None,
        required=False,
        help="text title",
    )
    parser.add_argument(
        "-s",
        "--separator",
        type=str,
        default=SEPARATOR_DEFAULT,
        required=False,
        help=f"column separator (default: {len(SEPARATOR_DEFAULT)} whitespaces)",
    )
    parser.add_argument(
        "-j",
        "--justify",
        action="store_true",
        required=False,
        help="justify each line in each column",
    )
    parser.add_argument(
        "-a",
        "--across",
        action="store_true",
        required=False,
        help="print columns across rather than down",
    )
    parser.add_argument(
        "-d",
        "--date",
        type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d:%H:%M"),
        required=False,
        help="title date in YYYY-MM-DD:HH:mm format (default: current date)",
    )
    parser.add_argument(
        "--date-format",
        type=str,
        default=DATE_FORMAT_DEFAULT,
        required=False,
        help=f"title date format (default: {DATE_FORMAT_DEFAULT.replace('%', '%%')})",
    )
    parser.add_argument(
        "--first-line-number",
        type=int,
        default=FIRST_LINE_NUMBER_DEFAULT,
        required=False,
        help=f"counter at first line (default: {FIRST_LINE_NUMBER_DEFAULT})",
    )
    parser.add_argument(
        "--first-page-number",
        type=int,
        default=FIRST_PAGE_NUMBER_DEFAULT,
        required=False,
        help=f"counter at first page (default: {FIRST_PAGE_NUMBER_DEFAULT})",
    )
    parser.add_argument(
        "--lines-before-header",
        type=int,
        default=LINES_BEFORE_HEADER_DEFAULT,
        required=False,
        help=f"number of empty lines before header (default: {LINES_BEFORE_HEADER_DEFAULT})",
    )
    parser.add_argument(
        "--lines-after-header",
        type=int,
        default=LINES_AFTER_HEADER_DEFAULT,
        required=False,
        help=f"number of empty lines after header (default: {LINES_AFTER_HEADER_DEFAULT})",
    )
    parser.add_argument(
        "--lines-after-page",
        type=int,
        default=LINES_AFTER_PAGE_DEFAULT,
        required=False,
        help=f"number of empty lines between pages (default: {LINES_AFTER_PAGE_DEFAULT})",
    )
    parser.add_argument(
        "--line-number-placeholder",
        default=LINE_NUMBER_PLACEHOLDER_DEFAULT,
        required=False,
        help=f'placeholder for line number (default: "{LINE_NUMBER_PLACEHOLDER_DEFAULT}")',
    )
    parser.add_argument(
        "--page-number-placeholder",
        default=PAGE_NUMBER_PLACEHOLDER_DEFAULT,
        required=False,
        help=f'placeholder for page number (default: "{PAGE_NUMBER_PLACEHOLDER_DEFAULT}")',
    )
    parser.add_argument(
        "--no-line-numbers",
        action="store_true",
        required=False,
        help="turn off line numbering",
    )
    parser.add_argument(
        "--no-page-numbers",
        action="store_true",
        required=False,
        help="turn off page numbering",
    )
    parser.add_argument(
        "--no-date",
        action="store_true",
        required=False,
        help="turn off date in header",
    )
    parser.add_argument(
        "--no-header",
        action="store_true",
        required=False,
        help="turn off entire header",
    )
    parser.add_argument(
        "--skip-empty-lines",
        action="store_true",
        required=False,
        help="ignore empty lines",
    )
    parser.add_argument(
        "--single-page",
        action="store_true",
        required=False,
        help="turn off page separation",
    )
    parser.add_argument("files", metavar="FILE", nargs="*", help="files to read, if empty, stdin is used")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    return parser.parse_args()


def justify(sentence: str, width: int) -> str:
    """Justifies text to match width exactly

    Args:
        sentence (str): source text to justify
        width (int): required width

    Returns:
        str: Justified text
    """
    words = sentence.split()
    num_words = len(words)

    if num_words == 1:
        # If there is only one word, just return the word
        return sentence

    total_spaces = width - sum(len(word) for word in words)
    spaces_between_words = total_spaces // (num_words - 1)
    extra_spaces = total_spaces % (num_words - 1)

    justified_sentence = words[0]
    for i in range(1, num_words):
        spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
        justified_sentence += " " * spaces + words[i]

    return justified_sentence


def main():
    # Parse arguments
    args = parse_args()

    # Calculate total width of each column without line number
    column_width = int((args.width - len(args.separator) * (args.columns - 1)) / args.columns)
    if not args.no_line_numbers:
        column_width -= len(args.line_number_placeholder.format(line=0))

    # Check it
    if column_width < 1:
        raise Exception(f"Total width ({args.width}) is too small or too many columns ({args.columns})!")

    # Save and format header date
    if not args.no_header and not args.no_date and args.date_format:
        if args.date:
            header_date = args.date.strftime(args.date_format)
        else:
            header_date = datetime.datetime.today().strftime(args.date_format)
        header_date = header_date[: args.width]
    else:
        header_date = ""

    # Format header title
    if not args.no_header and args.title:
        header_title = args.title.strip()[: args.width]
    else:
        header_title = ""

    # Formatted lines
    # [
    #   [
    #       "1st line, 1st column text",
    #       "1st line, 2nd column text",
    #       ...
    #   ],
    #   ...
    # ]
    lines = []

    # Page position
    page_index = 0
    page_index_prev = -1

    # Active column on page to write to
    column_index = 0

    # Active line in lines list (will be decremented after each completed line)
    line_index = 0

    # Line on page (for --across mode) / line in column (for normal mode)
    line_index_abs = 0

    # Stores only header size (number of lines)
    header_offset = 0

    # Displayed line number
    line_counter = 0

    next_page_request = False

    # Iterate each line from files or stdin
    for line in fileinput.input(args.files):
        # Split into lines
        lines_wrapped = textwrap.wrap(line, width=column_width)

        # Justify each line in needed
        if args.justify:
            lines_wrapped = [justify(line_wrapped, column_width) for line_wrapped in lines_wrapped]

        # Handle empty line
        if len(lines_wrapped) == 0 and not args.skip_empty_lines:
            lines_wrapped.append("")

        # Iterate each wrapped line
        for line_wrapped in lines_wrapped:
            # Page changed
            if page_index != page_index_prev:
                # Save current page
                page_index_prev = page_index

                # Add header
                if not args.no_header:
                    # Format page number
                    if not args.single_page and not args.no_page_numbers:
                        header_page_number = args.page_number_placeholder.format(
                            page=page_index + args.first_page_number
                        )
                        header_page_number = header_page_number[: args.width]
                    else:
                        header_page_number = ""

                    # Format title
                    header_date_and_page_length = len(header_date) + len(header_page_number)

                    # Only date -> title on the right
                    if header_date and not header_page_number:
                        header_title_ = ("{:>" + str(args.width - header_date_and_page_length) + "s}").format(
                            header_title
                        )

                    # Only page number -> title on the left
                    elif header_page_number and not header_date:
                        header_title_ = ("{:<" + str(args.width - header_date_and_page_length) + "s}").format(
                            header_title
                        )

                    # Both date and page number / no date and no page number -> title on center
                    else:
                        header_title_ = ("{:^" + str(args.width - header_date_and_page_length) + "s}").format(
                            header_title
                        )

                    # Empty lines before header
                    for _ in range(args.lines_before_header):
                        sys.stdout.write("\n")
                        header_offset += 1

                    # Header
                    sys.stdout.write(f"{header_date}{header_title_}{header_page_number}"[: args.width] + "\n")
                    header_offset += 1

                    # Empty lines after header
                    for _ in range(args.lines_after_header):
                        sys.stdout.write("\n")
                        header_offset += 1

                    # Flush
                    sys.stdout.flush()

            # Add leading spaces for next column
            if column_index < args.columns:
                line_wrapped = ("{: <" + str(column_width) + "}").format(line_wrapped)

            # Add line number
            if not args.no_line_numbers:
                line_wrapped = (
                    args.line_number_placeholder.format(line=line_counter + args.first_line_number) + line_wrapped
                )
                line_counter += 1

            # Create new line
            if line_index >= len(lines):
                lines.append([])

            # Append wrapped line to column
            lines[line_index].append(line_wrapped)

            # Next page flag
            next_page_request = False

            # Move left to right, then next line
            if args.across:
                # Next column
                column_index += 1

                # Next line and next page
                if column_index >= args.columns:
                    # Next line (and reset column)
                    line_index += 1
                    line_index_abs += 1
                    column_index = 0

                    # Next page
                    if (
                        not args.single_page
                        and line_index_abs + header_offset + args.lines_after_page >= args.page_size
                    ):
                        next_page_request = True

            # Move up to down, then next column
            else:
                # Next line
                line_index += 1
                line_index_abs += 1

                # Next column and next page
                if not args.single_page and line_index_abs + header_offset + args.lines_after_page >= args.page_size:
                    # Next column (and reset line)
                    column_index += 1
                    line_index = 0
                    line_index_abs = 0

                    # Next page
                    if column_index >= args.columns:
                        next_page_request = True

            # Pop and write available lines
            flush_request = False
            while len(lines) != 0:
                if next_page_request or len(lines[0]) >= args.columns:
                    sys.stdout.write(args.separator.join(lines.pop(0)) + "\n")
                    flush_request = True
                    line_index -= 1
                else:
                    break
            if flush_request:
                sys.stdout.flush()

            # Switch to next page
            if next_page_request:
                # Increment page
                page_index += 1

                # Reset positions
                column_index = 0
                line_index = 0
                line_index_abs = 0
                header_offset = 0

                # Add lines after page
                for _ in range(args.lines_after_page):
                    sys.stdout.write("\n")
                sys.stdout.flush()

    # Write all remaining lines
    while len(lines) != 0:
        sys.stdout.write(args.separator.join(lines.pop(0)) + "\n")

    # Finish current page
    if not next_page_request and not args.single_page:
        if args.across or column_index == 0:
            for _ in range(args.page_size - (max(line_index, line_index_abs) + header_offset) - args.lines_after_page):
                sys.stdout.write("\n")
        for _ in range(args.lines_after_page):
            sys.stdout.write("\n")

    # Flush everything
    sys.stdout.flush()


if __name__ == "__main__":
    main()
