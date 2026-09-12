words = ["apple", "banana"]
words[0] = "kalyan"
print(words)

servers = {"web-01", "app-01", "web-01"}

print(servers)

servers = ["web-01", "web-02", "web-01", "db-01", "web-02"]

uniq = set(servers)

print(uniq)

system_a = ["web-01", "web-02", "db-01", "web-01"]

system_b = ["web-02", "app-01", "db-01", "app-01"]

set_a = set(system_a)

set_b = set(system_b)

print(set_a | set_b)

print(set_a & set_b)

print(set_a - set_b)


