from __future__ import annotations
import argparse, json, os
from .memory import RecursiveMemory
from .heart_bridge import HeartBridge, HeartProfile
from .vacuum_corridor import compare

def _mem(args): return RecursiveMemory(args.db, namespace=args.namespace)

def main(argv=None):
    p = argparse.ArgumentParser(prog="cosmic-memory", description="COSMOS/CST persistent synaptic memory toolkit")
    p.add_argument("--db", default=os.getenv("COSMIC_MEMORY_DB", "cosmic_memory.db"))
    p.add_argument("--namespace", default=os.getenv("COSMIC_MEMORY_NAMESPACE", "default"))
    s = p.add_subparsers(dest="cmd", required=True)
    a=s.add_parser("remember"); a.add_argument("text"); a.add_argument("--importance",type=float,default=.5)
    a=s.add_parser("recall"); a.add_argument("query"); a.add_argument("--limit",type=int,default=5)
    s.add_parser("stats"); s.add_parser("dream")
    a=s.add_parser("export"); a.add_argument("path")
    a=s.add_parser("import"); a.add_argument("path")
    a=s.add_parser("heart-csv"); a.add_argument("path"); a.add_argument("--label",default="loved-one"); a.add_argument("--consent",required=True)
    a=s.add_parser("vacuum-test"); a.add_argument("--seed",type=int,default=7); a.add_argument("--steps",type=int,default=5000)
    args=p.parse_args(argv)
    if args.cmd == "vacuum-test": print(json.dumps(compare(args.seed,args.steps),indent=2)); return
    if args.cmd == "heart-csv":
        hb=HeartBridge.from_csv(args.path, HeartProfile(args.label,args.consent,"csv"))
        print(json.dumps({"samples":len(hb.samples),"latest":None if not hb.latest else hb.latest.__dict__,"interval":hb.beat_interval_seconds(),"fingerprint":hb.fingerprint()},indent=2)); return
    m=_mem(args)
    try:
        if args.cmd=="remember": print(json.dumps(m.remember(args.text,importance=args.importance).to_dict(),indent=2))
        elif args.cmd=="recall": print(json.dumps([{"text":h.memory.text,"score":h.score,"similarity":h.similarity,"id":h.memory.id} for h in m.recall(args.query,limit=args.limit)],indent=2))
        elif args.cmd=="stats": print(json.dumps(m.stats(),indent=2))
        elif args.cmd=="dream":
            r=m.dream(); print(json.dumps(None if r is None else r.to_dict(),indent=2))
        elif args.cmd=="export": print(m.export_jsonl(args.path))
        elif args.cmd=="import": print(m.import_jsonl(args.path))
    finally: m.close()

if __name__ == "__main__": main()
