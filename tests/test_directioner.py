from app.backend.models.directioner import Directioner, Direction


def test_create_directioner_right():
    # Arrange
    init_pos = (0, 0)
    direction = Direction.RIGHT

    # Act
    directioner = Directioner(init_pos, direction)

    # Assert
    assert directioner.init_pos == init_pos
    assert directioner.direction == direction
    assert directioner.snd_pos == (0, 1)
    assert directioner.thrd_pos == (0, 2)
    assert directioner.last_pos == (0, 3)


def test_create_directioner_left():
    # Arrange
    init_pos = (0, 0)
    direction = Direction.LEFT

    # Act
    directioner = Directioner(init_pos, direction)

    # Assert
    assert directioner.init_pos == init_pos
    assert directioner.direction == direction
    assert directioner.snd_pos == (0, -1)
    assert directioner.thrd_pos == (0, -2)
    assert directioner.last_pos == (0, -3)


def test_create_directioner_upwards():
    # Arrange
    init_pos = (0, 0)
    direction = Direction.UPWARDS

    # Act
    directioner = Directioner(init_pos, direction)

    # Assert
    assert directioner.init_pos == init_pos
    assert directioner.direction == direction
    assert directioner.snd_pos == (-1, 0)
    assert directioner.thrd_pos == (-2, 0)
    assert directioner.last_pos == (-3, 0)


def test_create_directioner_downwards():
    # Arrange
    init_pos = (0, 0)
    direction = Direction.DOWNWARDS

    # Act
    directioner = Directioner(init_pos, direction)

    # Assert
    assert directioner.init_pos == init_pos
    assert directioner.direction == direction
    assert directioner.snd_pos == (1, 0)
    assert directioner.thrd_pos == (2, 0)
    assert directioner.last_pos == (3, 0)
