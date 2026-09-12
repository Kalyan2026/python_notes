cpu_usage = 85

if cpu_usage > 80:
    print("High CPU usage")

cpu_usage = 75

if cpu_usage > 80:
    print("High CPU usage")
else:
    print("Normal CPU usage")

cpu_usage = 85

if cpu_usage > 90:
    print("Critical CPU usage")
elif cpu_usage > 80:
    print("High CPU usage")
else:
    print("Normal CPU usage")

disk_usage = 92

if disk_usage > 95:
    print("Critical disk usage")
elif disk_usage > 85:
    print("High disk usage")
else:
    print("Normal disk usage")

memory_usage = 78

if memory_usage > 90:
    print("Critical memory usage")
elif memory_usage > 75:
    print("High memory usage")
else:
    print("Normal memory usage")

cpu_usage = 85
memory_usage = 70

if cpu_usage > 80 and memory_usage > 80:
    print("Server is under high load")
else:
    print("Server is under normal load")

cpu_usage = 70
memory_usage = 85

if cpu_usage > 80 or memory_usage > 80:
    print("Server requires attention")
else:
    print("Server is normal")

cpu_usage = 92
memory_usage = 85

if cpu_usage > 90 and memory_usage > 90:
    print("Server is in critical condition")
elif cpu_usage > 80 or memory_usage > 80:
    print("Server is under high load")
else:
    print("Server is under normal")

cpu_usage = float(input("Enter CPU usage : "))

if cpu_usage > 90:
    print("Critical CPU usage")
elif cpu_usage > 80:
    print("High CPU usage")
else:
    print("Normal CPU usage")

cpu_usage = float(input("Enter CPU usage: "))
memory_usage = float(input("Enter memory usage: "))

if cpu_usage > 90 and memory_usage > 90:
    print("Server is in critical condition")
elif cpu_usage > 80 or memory_usage > 80:
    print("Server is under high load")
else:
    print("Server is under normal")

cpu_usage = float(input("Enter CPU usage : "))
memory_usage = float(input("Enter Memory usage : "))

if cpu_usage >= 90 and memory_usage >= 90:
    print("Server is in critical condition")
elif cpu_usage >= 80 or memory_usage >= 80:
    print("Server is under high load")
else:
    print("Server is normal")

cpu_usage = float(input("Enter CPU usage : "))
memory_usage = float(input("Enter memory usage : "))
disk_usage = float(input("Enter disk usage : "))

if cpu_usage >= 95 or memory_usage >= 95 or disk_usage >= 95:
    print("Server is in critical condition")
elif cpu_usage >=80 or memory_usage >= 80 or disk_usage >= 80:
    print("Server is under high load")
else:
    print("Server is normal")


deployment_status = input("Deployment status (success/failed) : ")

if deployment_status == "failed":
    print("Deployment failed")
else:
    cpu_usage = float(input("Enter CPU usage : "))
    disk_usage = float(input("Enter disk usage : "))
    if cpu_usage >= 95 or disk_usage >= 95:
        print("Critical server condition")
    elif cpu_usage >= 80 or disk_usage >= 80:
        print("High resource usage")
    else:
        print("deployment and server are healthy")