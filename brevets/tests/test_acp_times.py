"""
tests for acp_times.py
"""
from acp_times import open_time, close_time

import arrow
import nose # Testing framework
from nose.tools import assert_raises

START_TIME = arrow.get(2017, 1, 1).isoformat()  # Arbitrary start time
BREVET_DIST = [200, 300, 400, 600, 1000]


def test_zero_control_open():
    """
    Testing for when control is zero in open
    """
    for dist in BREVET_DIST:
        assert open_time(0.0, dist, START_TIME) == START_TIME


def test_negative_control_open():
    """
    Testing when control is negative in open
    """
    for dist in BREVET_DIST:
        assert_raises(ValueError, open_time, -1.0, dist, START_TIME)


def test_small_brevet_open():
    """
    Testing when the control distance is larger then brevet distance
    """
    for dist in BREVET_DIST:
        assert_raises(ValueError, open_time, 1201.0, dist, START_TIME)


def test_zero_brevet_open():
    """
    Testing when brevet distance is zero
    """
    assert_raises(ValueError, open_time, 0.0, 0, START_TIME)
    assert_raises(ValueError, open_time, 1.0, 0, START_TIME)


def test_time_error_open():
    """
    Testing when time is not formatted right
    """
    assert_raises(TypeError, open_time, 0.0, 200, 0)


def test_200_km_open():
    """
    Testing 200 km times for open_time
    """
    assert open_time(60.0, 200, START_TIME) == "2017-01-01T01:46:00+00:00"
    assert open_time(200.0, 200, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(205.0, 200, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(210.0, 200, START_TIME) == "2017-01-01T05:53:00+00:00"


def test_200_km_close():
    """
    Testing 200 km times for close_time
    """
    assert close_time(60.0, 200, START_TIME) == "2017-01-01T04:00:00+00:00"
    assert close_time(200.0, 200, START_TIME) == "2017-01-01T13:30:00+00:00"
    assert close_time(205.0, 200, START_TIME) == "2017-01-01T13:30:00+00:00"
    assert close_time(210.0, 200, START_TIME) == "2017-01-01T13:30:00+00:00"


def test_300_km_open():
    """
    Testing 300 km times for open_time
    """
    assert open_time(60.0, 300, START_TIME) == "2017-01-01T01:46:00+00:00"
    assert open_time(200.0, 300, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(232.0, 300, START_TIME) == "2017-01-01T06:53:00+00:00"
    assert open_time(300.0, 300, START_TIME) == "2017-01-01T09:00:00+00:00"
    assert open_time(315.0, 300, START_TIME) == "2017-01-01T09:00:00+00:00"
    assert open_time(330.0, 300, START_TIME) == "2017-01-01T09:00:00+00:00"


def test_300_km_close():
    """
    Testing 300 km times for close_time
    """
    assert close_time(60.0, 300, START_TIME) == "2017-01-01T04:00:00+00:00"
    assert close_time(200.0, 300, START_TIME) == "2017-01-01T13:20:00+00:00"
    assert close_time(232.0, 300, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert close_time(300.0, 300, START_TIME) == "2017-01-01T20:00:00+00:00"
    assert close_time(315.0, 300, START_TIME) == "2017-01-01T20:00:00+00:00"
    assert close_time(330.0, 300, START_TIME) == "2017-01-01T20:00:00+00:00"


def test_400_km_open():
    """
    Testing 400 km times for open_time
    """
    assert open_time(60.0, 400, START_TIME) == "2017-01-01T01:46:00+00:00"
    assert open_time(200.0, 400, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(232.0, 400, START_TIME) == "2017-01-01T06:53:00+00:00"
    assert open_time(300.0, 400, START_TIME) == "2017-01-01T09:00:00+00:00"
    assert open_time(332.0, 400, START_TIME) == "2017-01-01T10:00:00+00:00"
    assert open_time(400.0, 400, START_TIME) == "2017-01-01T12:08:00+00:00"
    assert open_time(420.0, 400, START_TIME) == "2017-01-01T12:08:00+00:00"
    assert open_time(440.0, 400, START_TIME) == "2017-01-01T12:08:00+00:00"


def test_400_km_close():
    """
    Testing 400 km times for close_time
    """
    assert close_time(60.0, 400, START_TIME) == "2017-01-01T04:00:00+00:00"
    assert close_time(200.0, 400, START_TIME) == "2017-01-01T13:20:00+00:00"
    assert close_time(232.0, 400, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert close_time(300.0, 400, START_TIME) == "2017-01-01T20:00:00+00:00"
    assert close_time(322.0, 400, START_TIME) == "2017-01-01T21:28:00+00:00"
    assert close_time(400.0, 400, START_TIME) == "2017-01-02T03:00:00+00:00"
    assert close_time(420.0, 400, START_TIME) == "2017-01-02T03:00:00+00:00"
    assert close_time(440.0, 400, START_TIME) == "2017-01-02T03:00:00+00:00"


def test_600_km_open():
    """
    Testing 600 km times for open_time
    """
    assert open_time(60.0, 600, START_TIME) == "2017-01-01T01:46:00+00:00"
    assert open_time(200.0, 600, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(232.0, 600, START_TIME) == "2017-01-01T06:53:00+00:00"
    assert open_time(300.0, 600, START_TIME) == "2017-01-01T09:00:00+00:00"
    assert open_time(332.0, 600, START_TIME) == "2017-01-01T10:00:00+00:00"
    assert open_time(400.0, 600, START_TIME) == "2017-01-01T12:08:00+00:00"
    assert open_time(500.0, 600, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert open_time(600.0, 600, START_TIME) == "2017-01-01T18:48:00+00:00"
    assert open_time(630.0, 600, START_TIME) == "2017-01-01T18:48:00+00:00"
    assert open_time(660.0, 600, START_TIME) == "2017-01-01T18:48:00+00:00"


def test_600_km_close():
    """
    Testing 600 km times for close_time
    """
    assert close_time(60.0, 600, START_TIME) == "2017-01-01T04:00:00+00:00"
    assert close_time(200.0, 600, START_TIME) == "2017-01-01T13:20:00+00:00"
    assert close_time(232.0, 600, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert close_time(300.0, 600, START_TIME) == "2017-01-01T20:00:00+00:00"
    assert close_time(322.0, 600, START_TIME) == "2017-01-01T21:28:00+00:00"
    assert close_time(400.0, 600, START_TIME) == "2017-01-02T02:40:00+00:00"
    assert close_time(420.0, 600, START_TIME) == "2017-01-02T04:00:00+00:00"
    assert close_time(600.0, 600, START_TIME) == "2017-01-02T16:00:00+00:00"
    assert close_time(630.0, 600, START_TIME) == "2017-01-02T16:00:00+00:00"
    assert close_time(630.0, 600, START_TIME) == "2017-01-02T16:00:00+00:00"


def test_1000_km_open():
    """
    Testing 1000 km times for open_time
    """
    assert open_time(60.0, 1000, START_TIME) == "2017-01-01T01:46:00+00:00"
    assert open_time(200.0, 1000, START_TIME) == "2017-01-01T05:53:00+00:00"
    assert open_time(232.0, 1000, START_TIME) == "2017-01-01T06:53:00+00:00"
    assert open_time(300.0, 1000, START_TIME) == "2017-01-01T09:00:00+00:00"
    assert open_time(332.0, 1000, START_TIME) == "2017-01-01T10:00:00+00:00"
    assert open_time(400.0, 1000, START_TIME) == "2017-01-01T12:08:00+00:00"
    assert open_time(500.0, 1000, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert open_time(600.0, 1000, START_TIME) == "2017-01-01T18:48:00+00:00"
    assert open_time(800.0, 1000, START_TIME) == "2017-01-02T01:57:00+00:00"
    assert open_time(1000.0, 1000, START_TIME) == "2017-01-02T09:05:00+00:00"
    assert open_time(1000.0, 1000, START_TIME) == "2017-01-02T09:05:00+00:00"
    assert open_time(1000.0, 1000, START_TIME) == "2017-01-02T09:05:00+00:00"


def test_1000_km_close():
    """
    Testing 1000 km times for close_time
    """
    assert close_time(60.0, 1000, START_TIME) == "2017-01-01T04:00:00+00:00"
    assert close_time(200.0, 1000, START_TIME) == "2017-01-01T13:20:00+00:00"
    assert close_time(232.0, 1000, START_TIME) == "2017-01-01T15:28:00+00:00"
    assert close_time(300.0, 1000, START_TIME) == "2017-01-01T20:00:00+00:00"
    assert close_time(322.0, 1000, START_TIME) == "2017-01-01T21:28:00+00:00"
    assert close_time(400.0, 1000, START_TIME) == "2017-01-02T02:40:00+00:00"
    assert close_time(500.0, 1000, START_TIME) == "2017-01-02T09:20:00+00:00"
    assert close_time(600.0, 1000, START_TIME) == "2017-01-02T16:00:00+00:00"
    assert close_time(800.0, 1000, START_TIME) == "2017-01-03T09:30:00+00:00"
    assert close_time(1000.0, 1000, START_TIME) == "2017-01-04T03:00:00+00:00"
    assert close_time(1050.0, 1000, START_TIME) == "2017-01-04T03:00:00+00:00"
    assert close_time(1100.0, 1000, START_TIME) == "2017-01-04T03:00:00+00:00"


def test_zero_control_close():
    """
    Testing for when control is zero in close
    """
    for dist in BREVET_DIST:
        assert close_time(0.0, dist, START_TIME) == "2017-01-01T01:00:00+00:00"


def test_negative_control_close():
    """
    Testing when control is negative in close
    """
    for dist in BREVET_DIST:
        assert_raises(ValueError, close_time, -1.0, dist, START_TIME)


def test_small_brevet_close():
    """
    Testing when the control distance is larger then brevet distance
    """
    for dist in BREVET_DIST:
        assert_raises(ValueError, close_time, 1201.0, dist, START_TIME)


def test_zero_brevet_close():
    """
    Testing when brevet distance is zero
    """
    assert_raises(ValueError, close_time, 0.0, 0, START_TIME)
    assert_raises(ValueError, close_time, 1.0, 0, START_TIME)


def test_time_error_close():
    """
    Testing when time is not formatted right
    """
    assert_raises(TypeError, close_time, 0.0, 200, 0)
