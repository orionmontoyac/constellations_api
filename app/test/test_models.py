from ..constellations.models import Star

def test_new_star():
    """
    GIVEN a Star model
    WHEN a new Star is created
    THEN check all the atts for a Star and check if are defined correctly
    """
    star = Star('α And', 'α', '01h 09m 43.80s', '+35° 37′ 15.0″','2.07','−1.86','199')
    assert star.name == 'α And'
    assert star.bayer_designation == 'α'
    assert star.right_ascension == '01h 09m 43.80s'
    assert star.declination == '+35° 37′ 15.0″'
    assert star.apparent_magnitude == '2.07'
    assert star.absolute_magnitude == '−1.86'
    assert star.distance == '199'
