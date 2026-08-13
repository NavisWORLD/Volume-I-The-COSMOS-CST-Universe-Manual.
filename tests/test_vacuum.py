from cosmic_memory.vacuum_corridor import compare

def test_anti_locking_reduces_long_runs():
    r=compare(seed=7,steps=6000)
    assert r['anti_locking']['longest_run'] <= r['baseline']['longest_run']
    assert r['anti_locking']['escaped_runs'] >= 0
