deployment_status = input("Enter deployment status (success/failed): ")

if deployment_status == "failed":
    print("Deployment failed")
else:
    environment = input("Enter environment (dev/staging/production): ")
    cpu_usage = float(input("Enter CPU usage: "))
    memory_usage = float(input("Enter memory usage: "))
    if deployment_status == "success" and (environment == "dev" or environment == "staging") and cpu_usage < 80 and memory_usage < 90:
        print("Deployment validation passed")
    else:
        print("Deployment validation failed")