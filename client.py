class MVCCStorage:
    """Multi-Version Concurrency Control (MVCC) Storage Engine."""
    def __init__(self):
        # key -> list of (tx_id, value, deleted)
        self.records = {}

    def write(self, tx_id: int, key: str, value: any) -> dict:
        if key not in self.records:
            self.records[key] = []
        self.records[key].append((tx_id, value, False))
        return {"tx_id": tx_id, "key": key, "value": value}

    def read_snapshot(self, snapshot_tx_id: int, key: str) -> dict:
        if key not in self.records:
            return {"key": key, "value": None, "found": False}
        # Find highest tx_id <= snapshot_tx_id
        versions = [v for v in self.records[key] if v[0] <= snapshot_tx_id and not v[2]]
        if not versions:
            return {"key": key, "value": None, "found": False}
        latest = versions[-1]
        return {"key": key, "value": latest[1], "version_tx": latest[0], "found": True}
