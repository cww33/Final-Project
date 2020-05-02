import os

from subscription import to_usd
def test_to_usd(): 
    result= to_usd(73498.82)
    assert result == "$73,498.82"
    assert to_usd(9.8) == "$9.80"