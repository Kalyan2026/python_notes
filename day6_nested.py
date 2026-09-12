deployment_status = input("Deployment status (success/failed): ")

if deployment_status == "failed":
    print("Deployment is failed")
else:
    cpu_usage = float(input("Enter CPU usage: "))
    memory_usage = float(input("Enter Memory usage: "))
    disk_usage = float(input("Enter disk usage: "))
    if cpu_usage >= 95 or memory_usage >= 95 or disk_usage >= 95:
        print("critical state")
    elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
        print("high load")
    else:
        print("Normal load")

deployment_status = input("Deployment status (success/failed): ")

if deployment_status == "failed":
    print("Deployment failed")
else:
    environment = input("Enter environment(dev/staging/production): ")
    cpu_usage = float(input("Enter CPU usage: "))
    memory_usage = float(input("Enter memory usage: "))
    disk_usage = float(input("Enter Disk usage: "))
    if environment == "dev":
        if cpu_usage >= 95 or memory_usage >=95 or disk_usage >= 95:
            print("Dev is in critical state")
        elif cpu_usage >= 80 or memory_usage >=80 or disk_usage >= 80:
            print("Dev is under high load")
        else:
            print("Dev is in Normal state")
    elif environment == "staging":
        if cpu_usage >= 95 or memory_usage >=95 or disk_usage >= 95:
            print("Staging is in critical state")
        elif cpu_usage >= 80 or memory_usage >=80 or disk_usage >= 80:
            print("Staging is under high load")
        else:
            print("Staging is in Normal state")
    elif environment == "production":
        if cpu_usage >= 90 or memory_usage >=90 or disk_usage >= 90:
            print("Production is in critical state")
        elif cpu_usage >= 80 or memory_usage >=80 or disk_usage >= 80:
            print("Production is under high load")
        else:
            print("Production is in Normal state")
    else:
        print("No environment is selected")
