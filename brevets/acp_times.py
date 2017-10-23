"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


ACP_TABLE = [
    (200, 15, 34),
    (200, 15, 32),
    (200, 15, 30),
    (400, 11.428, 28),
    (300, 13.333, 26)
]


SPECIAL_TIMES = {
    200: 13.5,
    300: 20,
    400: 27,
    600: 40,
    1000: 75
}


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
    if not isinstance(control_dist_km, float) or \
            not isinstance(brevet_dist_km, int) or \
            not isinstance(brevet_start_time, str):
        raise TypeError
    if not brevet_dist_km:
        raise ValueError('empty brevet distance')
    if brevet_dist_km * 1.1 < control_dist_km:
        raise ValueError(
            'control distance is over 20% longer than the brevet distance')
    if control_dist_km < 0:
        raise ValueError('negative control distance')

    start_time = arrow.get(brevet_start_time)

    # Cases where control distance is longer
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km

    shift_hours = 0

    for info in ACP_TABLE:
        dist, start, end = info

        # Calculation for remainder length
        if control_dist_km <= dist:
            shift_hours += control_dist_km / end
            # Integer divide by 1 gets numbers after the decimal
            hours = shift_hours // 1
            minutes = round((shift_hours - hours) * 60)
            return start_time.shift(hours=hours, minutes=minutes).isoformat()

        # If there is more length than the interval
        shift_hours += dist / end
        control_dist_km -= dist


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    The calculations will be done in whole minutes, where the seconds are
    rounded in the final iso

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
    if not isinstance(control_dist_km, float) or \
            not isinstance(brevet_dist_km, int) or \
            not isinstance(brevet_start_time, str):
        raise TypeError
    if not brevet_dist_km:
        raise ValueError('empty brevet distance')
    if brevet_dist_km * 1.1 < control_dist_km:
        raise ValueError(
            'control distance is greater than the brevet distance')
    if control_dist_km < 0:
        raise ValueError('invalid control distance')

    start_time = arrow.get(brevet_start_time)

    # Special cases
    if not control_dist_km:
        return start_time.shift(hours=1).isoformat()

    if control_dist_km >= brevet_dist_km:
        return start_time.shift(
            hours=SPECIAL_TIMES[brevet_dist_km]).isoformat()

    shift_hours = 0

    for info in ACP_TABLE:
        dist, start, end = info

        # Calculation for remainder length
        if control_dist_km < dist:
            shift_hours += control_dist_km / start
            # Integer divide by 1 gets numbers after the decimal
            hours = shift_hours // 1
            minutes = round((shift_hours - hours) * 60)
            return start_time.shift(hours=hours, minutes=minutes).isoformat()

        # If there is more length than the interval
        shift_hours += dist / start
        control_dist_km -= dist
