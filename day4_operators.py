total_servers = 25
new_servers = 5
failed_servers = 3
infrastructure_cost = total_servers * 1000
healthy_servers = total_servers - failed_servers
updated_total_servers = total_servers + new_servers
average_servers = updated_total_servers / 5
remaining_server = total_servers % 4

message = f'---- Server Report ---- \n Updated Total servers: {updated_total_servers} \n Healthy servers: {healthy_servers}\n Infrastructure cost: {infrastructure_cost} \n Average servers across each environment: {average_servers} \n Reaminder : {remaining_server}'
print(message)

cpu_usage = 85
memory_usage = 70

print(cpu_usage > 80)
print(memory_usage < 80)
print(cpu_usage == 85)
print(memory_usage != 70)

disk_usage = 90
cpu_usage = 75
server_status = "running"
print(disk_usage >= 90)
print(cpu_usage <=70)
print(server_status == "running")
print(server_status != "stopped")

cpu_usage = 85

memory_usage = 70

print(cpu_usage < 90 and memory_usage < 80)

print(cpu_usage < 80 and memory_usage < 80)

cpu_usage = 85
memory_usage = 70

# Expected result: True
print(cpu_usage < 80 or memory_usage < 80)

# Expected result: False
print(cpu_usage < 80 or memory_usage < 60)

deployment_successful = False

print(deployment_successful)

print(not deployment_successful)

total_servers = 20

total_servers += 5
print(total_servers)

total_servers -= 3
print(total_servers)

deployment_count = 10

deployment_count *= 3
print(deployment_count)

deployment_count /= 5
print(deployment_count)

total_servers = 20
failed_servers = 3
cpu_usage = 85
memory_usage = 70

# 1. Arthmetic operator
healthy_servers = total_servers - failed_servers

# 2. Comparison operator
comparison = cpu_usage > 80

# 3. Logical AND operator
logical_and = cpu_usage > 80 and memory_usage > 80

# 4. logical OR operator
logical_or = cpu_usage > 80 or memory_usage > 80

# 5. Assignment
total_servers +=5

# 6. Final Report
print(f'----Server Status Report---- \n 1. Arthimetic : {healthy_servers} \n 2. Comparison: {comparison} \n 3. Logical AND: {logical_and} \n 4. Logical OR: {logical_or} \n 5. Assignment: {total_servers}')