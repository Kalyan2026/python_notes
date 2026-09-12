servers = ["web-01", "web-02", "app-01", "db-01"]
statuses = ["healthy", "failed", "healthy", "failed"]

for i in range(len(servers)):
    if statuses[i] == "failed":
        print(servers[i])

servers = ["web-01", "web-02", "app-01", "db-01"]

for server in servers:
    print(f"Checking {server}")

servers = ["web-01", "web-02", "app-01", "db-01"]
statuses = ["healthy", "failed", "healthy", "failed"]

for server in range(len(servers)):
    print(f"{servers[server]} : {statuses[server]}")


servers = ["web-01", "web-02", "app-01", "db-01"]
cpu_usage = [45, 92, 70, 96]

for i in range(len(servers)):
    if cpu_usage[i] >= 95:
        print(f"{servers[i]} : Critical")
    elif cpu_usage[i] >= 80:
        print(f"{servers[i]} : High load")
    else:
        print(f"{servers[i]} : Normal")