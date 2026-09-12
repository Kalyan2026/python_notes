servers = ["web-01", "web-02", "web-03", "db-01"]
statuses = ["healthy", "failed", "healthy", "failed"]
failed_servers = []

for i in range(len(servers)):
    if statuses[i] == "failed":
        failed_servers.append(servers[i])
print(failed_servers)

servers = ["web-01", "web-02", "app-01", "db-01"]
cpu_usage = [45, 92, 70, 96]

high_cpu_servers = []
for i in range(len(servers)):
    if cpu_usage[i] >= 80:
        high_cpu_servers.append(servers[i])

print(f"High CPU servers: {high_cpu_servers} ")

servers = ["web-01", "web-02", "app-01", "db-01"]
cpu_usage = [45, 92, 70, 96]
memory_usage = [60, 85, 75, 91]

critical_servers = []

for i in range(len(servers)):
    if cpu_usage[i] >= 95 or memory_usage[i] >= 90:
        critical_servers.append(servers[i])

print(f"Servers which have more cpu or memory : {critical_servers}")

servers = ["web-01", "web-02", "app-01", "db-01"]
cpu_usage = [45, 92, 70, 96]
memory_usage = [60, 85, 75, 91]
disk_usage = [50, 70, 88, 95]

critical_servers = []
high_load_servers = []

for i in range(len(servers)):
    if cpu_usage[i] >= 95 or memory_usage[i] >= 90 or disk_usage[i] >= 95:
        critical_servers.append(servers[i])
    elif cpu_usage[i] >= 80 or memory_usage[i] >= 80 or disk_usage[i] >= 80:
        high_load_servers.append(servers[i])
print(f"Critical servers : {critical_servers}")
print(f"High load servers: {high_load_servers}")