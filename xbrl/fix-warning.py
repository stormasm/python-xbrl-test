"""
how to get rid of warning messages...
https://docs.python.org/3/library/warnings.html#overriding-the-default-filter
"""

import sys

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")

from xbrl import XBRLParser

xbrl_parser = XBRLParser()
xbrl = xbrl_parser.parse(open("sam-20130629.xml"))


xbrl_parser = XBRLParser("xml")
file_to_parse = "sam-20130629.xml"
try:
    xbrl_parser.parse(file_to_parse)
    # except NameError:
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


def test_open_file_handle():
    xbrl_parser = XBRLParser()
    file_to_parse = "sam-20130629.xml"
    try:
        xbrl_parser.parse(file_to_parse)
    except NameError:
        pass


test_open_file_handle()
