#! /usr/bin/env python
# encoding: utf-8

from __future__ import print_function

from ed1x import XBRLParser, GAAP, GAAPSerializer, DEISerializer

xbrl_parser = XBRLParser(precision=0)

# Parse an incoming XBRL file
# xbrl = xbrl_parser.parse("sam-20130629.xml")
xbrl = xbrl_parser.parse("ubnt-20200331_htm.xml")

# Parse just the Custom data from the xbrl object
custom_obj = xbrl_parser.parseCustom(xbrl)

# Print out the Custom data as an array of tuples
print(custom_obj())
