def create_config(vip, port, pool, members):

    member_config = ""
    for m in members:
        member_config += f"{m.strip()}:{port} "

    # Decide monitor type
    if port == "443":
        monitor = "https"
        profile = "clientssl"
        protocol = "tcp"
    else:
        monitor = "http"
        profile = "http"
        protocol = "tcp"

    return f"""
=========== F5 CONFIG ===========

# Create Health Monitor
tmsh create ltm monitor {monitor} {pool}_monitor

# Create Pool
tmsh create ltm pool {pool} \\
monitor {pool}_monitor \\
members add {{ {member_config}}}

# Create VIP
tmsh create ltm virtual {pool}_vip \\
destination {vip}:{port} \\
ip-protocol {protocol} \\
pool {pool} \\
profiles add {{ {profile} tcp }} \\
vlans-enabled

================================

Verify:
tmsh list ltm monitor {pool}_monitor
tmsh list ltm pool {pool}
tmsh list ltm virtual {pool}_vip
"""


print("=== F5 ADVANCED CONFIG GENERATOR ===")

vip = input("Enter VIP IP: ")
port = input("Enter Port (80/443): ")
pool = input("Enter Pool Name: ")

print("Enter backend server IPs (comma separated):")
members_input = input("Example: 192.168.1.10,192.168.1.11\n")

members = members_input.split(",")

config = create_config(vip, port, pool, members)

print(config)
