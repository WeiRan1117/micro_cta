import pandas as pd

from pycta.performance.drawdown import drawdown, drawdown_periods
from test.config import read_series
from unittest import TestCase

ts = read_series("ts.csv", parse_dates=True)

import pandas.util.testing as pdt


class TestDrawdown(TestCase):
    def test_drawdown(self):
        pdt.assert_series_equal(drawdown(ts), read_series("drawdown.csv", parse_dates=True), check_names=False)

    def test_periods(self):
        x = drawdown_periods(ts)
        self.assertEqual(x[pd.Timestamp("2014-06-20")], 217)
