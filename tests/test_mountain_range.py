from app.backend.models.mountain_range import MountainRange
from app.backend.models.orientation import Orientation


def test_create_mountain_vertical():
    initial_position = (1, 2)
    orientation = Orientation.VERTICAL
    mountain_range = MountainRange(initial_position, orientation)
    expected_mountain = [(1, 2), (1, 1), (1, 0)]
    assert mountain_range.mountain.__eq__(expected_mountain)
