import pytest
from cosmic_memory import HeartBridge, HeartProfile

def test_consent_required():
    with pytest.raises(PermissionError): HeartBridge(HeartProfile('other',''))

def test_interval():
    h=HeartBridge(HeartProfile('self','self-consent'))
    h.add_sample(60,timestamp=100.0)
    assert abs(h.beat_interval_seconds()-1.0)<1e-9
    assert 0 <= h.phase(100.5) < 1
