def test_import():
    import asteroids

def test_get_asteroids():
    from asteroids import get_asteroids
    asteroids = get_asteroids("2021-01-01")
    # Assert for correct types
    assert isinstance(asteroids, list)
    assert all(isinstance(asteroid, dict) for asteroid in asteroids)
    # Assert for correct keys
    assert all(key in asteroids[0] for key in ["name", "distance", "diameter", "approach_date"])