
from crosswalk_decision import crosswalk_decision


def test_approaching_vehicle():
    # 접근 차량이 있으면 진입 불가
    result = crosswalk_decision(True)
    assert result == 0


def test_no_approaching_vehicle():
    # 접근 차량이 없으면 진입 가능
    result = crosswalk_decision(False)
    assert result == 1
