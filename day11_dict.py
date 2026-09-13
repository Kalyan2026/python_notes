server = {
    "name": "web-01",
    "environment": "production",
    "cpu": 92,
    "memory": 75,
    "status": "running"
}

if server["cpu"] >= 95:
    print("CPU is critical")
elif server["cpu"] >= 80:
    print("CPU is under high load")
else:
    print("CPU is normal")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 92, "memory": 85},
    {"name": "db-01", "cpu": 96, "memory": 91}
]

for server in servers:
    if server["cpu"] >= 95:
        print(f"{server['name']} is in Critical")
    elif server["cpu"] >= 80:
        print(f"{server['name']} is under high load")
    else:
        print(f"{server['name']} is healthy")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 92, "memory": 85},
    {"name": "db-01", "cpu": 96, "memory": 91}
]

for server in servers:
    if server['cpu'] >= 95 or server['memory'] >= 90:
        print(f"{server['name']} is critical")
    elif server['cpu'] >= 80 or server['memory'] >= 80:
        print(f"{server['name']} is under high load")
    else:
        print(f"{server['name']} is healthy")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60, "status": "healthy"},
    {"name": "web-02", "cpu": 92, "memory": 85, "status": "failed"},
    {"name": "db-01", "cpu": 96, "memory": 91, "status": "failed"}
]

for server in servers:
        if server['status'] == "failed":
                print(f"Deployment failed for {server['name']}")
        else:
            if server['cpu'] >= 95 or server['memory'] >= 90:
                print(f"{server['name']} is critical")
            elif server['cpu'] >= 80 or server['memory'] >= 80:
                print(f"{server['name']} is under high load")
            else:
                print(f"{server['name']} is healthy")

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60, "status": "healthy"},
    {"name": "web-02", "cpu": 92, "memory": 85, "status": "healthy"},
    {"name": "app-01", "cpu": 96, "memory": 91, "status": "healthy"},
    {"name": "db-01", "cpu": 70, "memory": 65, "status": "failed"},
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
        if server['cpu'] >= 95 or server['memory'] >= 90:
            critical_servers += 1

        elif server['cpu'] >= 80 or server['memory'] >= 80:
            high_load_servers += 1

        else:
            healthy_servers += 1

print(f"----Server health report---- \n total_servers = {total_servers} \n healthy_servers = {healthy_servers} \n high_load_servers = {high_load_servers} \n critical_servers = {critical_servers} \n failed_servers = {failed_servers}")
