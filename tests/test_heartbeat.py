from cosmic_memory import HeartbeatScheduler

def test_scheduler_fail_soft():
    now=[0.0]; s=HeartbeatScheduler(clock=lambda:now[0]); ran=[]
    s.add('ok',1,lambda:ran.append('ok'),run_immediately=True)
    s.add('bad',1,lambda:1/0,run_immediately=True)
    s.tick(); assert ran==['ok']; assert s.errors and s.errors[0]['task']=='bad'
