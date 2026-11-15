from diesel_radar.geo import haversine_km,  dist_to_kehl_km, in_study_region

def test_strasbourg_inside():
    assert in_study_region(48.5734, 7.7521) is True

def test_karlsruhe_outside():
    assert in_study_region(49.0069, 8.4037) is False

def test_haversine_zero():
    assert haversine_km(48.57, 7.81, 48.57, 7.81) == 0.0

def test_haversine_positive():
    assert haversine_km(48.57, 7.81, 49.00, 8.40) > 0

def test_kehl_itself_inside():
    assert in_study_region(48.57, 7.81) is True
