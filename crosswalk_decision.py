
def can_enter_crosswalk(approaching_vehicle: bool) -> int:
    """0: 진입 불가, 1: 진입 가능 (실습용 판단 로직)"""
    if approaching_vehicle:
        return 0
    return 1


assert can_enter_crosswalk(True) == 0
assert can_enter_crosswalk(False) == 1
