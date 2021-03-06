import csv

# this dialect represents the format used by Microsoft Access,
# which is csv file separated by ';' instead of ','.
ACCDB = 'accdb'
csv.register_dialect(ACCDB, delimiter=';')

# This is the name of the default dialect by the csv library.
CSV = 'excel'

# All the dialects that the harris_county_bookings package cares about.
ALL_DIALECTS = [ACCDB, CSV]
