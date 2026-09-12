name = input("Enter your name: ")
role = input("Enter your role: ")
print(name)
print(role)

total_servers = int(input("Total number of servers: "))
failed_servers = int(input("Failed number of servers: "))
healthy_servers = total_servers - failed_servers
print(f"Total number of healthy servers :",healthy_servers)

cpu_usage = float(input("Enter CPU usage: "))
memory_usage = float(input("Enter Memory usage: "))
disk_usage = float(input("Enter Disk usage: "))
average_usage = (cpu_usage + memory_usage + disk_usage) / 3
print(f'Average usage of system is {average_usage}')

name = input("Enter server/application name: ")
number_of_servers = int(input("Enter number of servers: "))
message = "Application "+ name +" has " + str(number_of_servers) + " servers"
print(message)

total_servers = int(input("Enter total number of servers: "))
failed_servers = int(input("Enter failed number of servers: "))
healthy_servers = total_servers - failed_servers

messsage = "Out of " + str(total_servers) + " servers, " + str(healthy_servers) + " servers are healthy."
print(messsage)

server_name = input("Enter your server name: ")
server_ip = input("Enter your server ip: ")
cpu_usage = float(input("Enter your cpu usage: "))
message = f'Server {server_name} with {server_ip} has CPU usage of {cpu_usage}%'
print(message)

server_name = input("Enter your server name: ")
total_cpu = float(input("Enter total CPU usage: "))
current_cpu = float(input("Enter current CPU usage: "))
total_memory = float(input("Enter total Memory usage: "))
current_memory = float(input("Enter current Memory usage: "))
available_cpu = total_cpu - current_cpu
available_memory = total_memory - current_memory
message = f'----Server Health Report----\n Server Name: {server_name} \n Available CPU: {available_cpu}% \n Available Memory: {available_memory}GB'
print(message)