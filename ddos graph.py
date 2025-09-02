import os
import time
import matplotlib.pyplot as plt

# Server/target jo tum monitor karna chahte ho
target = "example.com"

# Data store karne ke liye
latencies = []
timestamps = []

# Plot setup
plt.ion()  # Interactive mode on
fig, ax = plt.subplots()

# X-axis time, Y-axis latency
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Latency (ms)')
ax.set_title(f'Ping Latency Monitoring for {target}')

while True:
    response = os.popen(f"ping -c 1 {target}").read()

    if "time=" in response:
        # Latency extract karna
        latency = response.split("time=")[1].split(" ms")[0]
        print(f"[OK] Server Responding - Latency: {latency} ms")

        # Data ko list me store karna
        latencies.append(float(latency))
        timestamps.append(time.time())

    elif "Name or service not known" in response:
        print("[Error] Domain Not Found")
    else:
        print("[DOWN] No Response from Server")

    # Graph update karna
    ax.clear()
    ax.plot(timestamps, latencies, label="Latency")
    ax.legend(loc="upper right")

    # X-axis ko time ke hisaab se update karna
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Latency (ms)')
    ax.set_title(f'Ping Latency Monitoring for {target}')

    plt.draw()
    plt.pause(2)  # Wait 2 seconds before next ping

    time.sleep(2)  # Ping every 2 seconds