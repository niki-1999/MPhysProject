import datetime
import numpy as np
import tsyganenko as tsy

trace_dt = datetime.datetime(2001,9,22,12)
lats = np.arange(10, 90, 10)
lons = 180.
rhos = tsy.RE
trac = tsy.Trace(lats, lons, rhos, datetime=trace_dt)

print(trac)
