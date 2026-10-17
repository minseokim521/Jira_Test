
def crosswalk_decision(approaching_vehicle: bool) -> int:
    """
    접근 차량 존재: 0 (진입 불가)
    접근 차량 부재: 1 (진입 가능)
    """
    if approaching_vehicle:
        return 0
    return 1
