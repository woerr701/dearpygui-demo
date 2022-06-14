from dearpygui_demo import __version__
from dearpygui_demo import app

def test_version():
    assert __version__ == '0.1.0'


def test_calculate_windchill_for_low_range():
    expected = 36.0
    results = app.calculate_windchill(5,40)
    assert expected == results