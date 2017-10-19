"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

ACP_TABLE = [
    (200, 15, 34),
    (200, 15, 32),
    (200, 15, 30),
    (400, 11.428, 28),
    (300, 13.333, 26)
]


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if not brevet_dist_km:
        raise ValueError('empty brevet distance')
    if brevet_dist_km * 1.2 < control_dist_km:
        raise ValueError(
            'control distance is over 20% longer than the brevet distance')
    if control_dist_km < 0:
        raise ValueError('negative control distance')

    start_time = arrow.get(brevet_start_time)
    for info in ACP_TABLE:
        dist, start, end = info
        if control_dist_km <= dist:
            hours = float(control_dist_km / end)
            return start_time.shift(hours=hours).isoformat()
        hours = float(dist / end)
        start_time = start_time.shift(hours=hours)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if not brevet_dist_km:
        raise ValueError('empty brevet distance')
    if brevet_dist_km < control_dist_km:
        raise ValueError(
            'control distance is greater than the brevet distance')
    if control_dist_km < 0:
        raise ValueError('negative control distance')

    start_time = arrow.get(brevet_start_time)
    for info in ACP_TABLE:
        dist, start, end = info
        if control_dist_km <= dist:
            hours = float(control_dist_km / start)
            return start_time.shift(hours=hours).isoformat()
        hours = float(dist / start)
        start_time = start_time.shift(hours=hours)
