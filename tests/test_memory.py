from cosmic_memory import RecursiveMemory, PlanetaryMemory

def test_persists_across_reopen(tmp_path):
    db=tmp_path/'m.db'; m=RecursiveMemory(db)
    m.remember('Orion key is cobalt blue', importance=.9); m.close()
    m=RecursiveMemory(db); hits=m.recall('what color is the Orion key?',limit=3,min_similarity=0.0)
    assert any('cobalt blue' in h.memory.text for h in hits); m.close()

def test_duplicate_dedup(tmp_path):
    m=RecursiveMemory(tmp_path/'m.db'); a=m.remember('same memory'); b=m.remember('same memory')
    assert a.id==b.id and m.stats()['memories']==1; m.close()

def test_hebbian_and_dream(tmp_path):
    m=RecursiveMemory(tmp_path/'m.db');
    m.remember('alpha beta gamma'); m.remember('alpha beta delta');
    assert m.stats()['associations']>0
    d=m.dream(); assert d and 'Consolidated association map' in d.text; m.close()

def test_planetary_namespaces(tmp_path):
    p=PlanetaryMemory(tmp_path/'p.db'); a=p.space('alice'); b=p.space('bob')
    a.remember('alice fact'); b.remember('bob fact')
    assert a.stats()['memories']==1 and b.stats()['memories']==1
    a.close(); b.close()
