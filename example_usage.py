from client import MVCCStorage

def main():
    print("=== MVCC Snapshot Isolation Storage ===")
    store = MVCCStorage()
    store.write(1, "wallet_balance", 100)
    store.write(5, "wallet_balance", 250)

    # Snapshot at Tx 3 sees balance 100
    read_t3 = store.read_snapshot(3, "wallet_balance")
    print("Read at Snapshot Tx 3:", read_t3)
    assert read_t3["value"] == 100

    # Snapshot at Tx 6 sees balance 250
    read_t6 = store.read_snapshot(6, "wallet_balance")
    print("Read at Snapshot Tx 6:", read_t6)
    assert read_t6["value"] == 250

    print("MVCC Storage verified successfully!")

if __name__ == "__main__":
    main()
