server = {
    "name": "web-01",
    "ip": "10.0.1.10",
    "environment": "production",
    "cpu": 75,
    "memory": 60,
    "status": "healthy"
}

for key, value in server.items():
    print(key, value)

server = {
    "name": "web-01",
    "cpu": 75,
    "memory": 60,
    "status": "healthy"
}

print(f"CPU = {server.get('cpu')}")
print(f"Memory = {server.get('memory')}")
print(f"Disk = {server.get('disk', 0)}")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60, "status": "healthy"},
    {"name": "web-02", "cpu": 92, "memory": 85, "status": "healthy"},
    {"name": "db-01", "cpu": 96, "status": "healthy"},
]

for server in servers:
    print(f"{server.get('name', 'default')} -> CPU = {server.get('cpu', 0)} Memory = {server.get('memory', 0)}")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60, "status": "healthy"},
    {"name": "web-02", "cpu": 92, "memory": 85, "status": "healthy"},
    {"name": "app-01", "cpu": 96, "memory": 91, "status": "healthy"},
    {"name": "db-01", "cpu": 70, "status": "failed"},
    {"name": "api-01", "cpu": 50, "memory": 82, "status": "healthy"}
]

total_servers = 0
healthy_servers = 0
high_load_servers = 0
critical_servers = 0
failed_servers = 0

for server in servers:
    total_servers += 1
    if server['status'] == "failed":
        failed_servers += 1
    else:
        if server.get('cpu', 0) >= 95 or server.get('memory', 0) >= 90:
            critical_servers += 1
        elif server.get('cpu', 0) >= 80 or server.get('memory', 0) >= 80:
            high_load_servers += 1
        else:
            healthy_servers += 1

print(f" ----System Health Report ---- \n Total servers = {total_servers} \n Healthy servers = {healthy_servers} \n High Load Servers = {high_load_servers} \n Critical Servers = {critical_servers} \n Failed servers = {failed_servers}")