import sys
import json
from client import MVCCStorage

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    store = MVCCStorage()
    if method == "read_snapshot":
        for w in params.get("writes", []):
            store.write(w["tx"], w["k"], w["v"])
        return store.read_snapshot(params.get("tx_snapshot", 1), params.get("k", ""))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
