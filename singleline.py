import time

# This will count 1 to 5, updating the same line
for i in range(1, 6):
    # \r moves to start of line
    # end="" prevents new line
    # flush=True shows number immediately
    print(f"\rCounting: {i}", end="", flush=True)
    time.sleep(1)

# Final newline so next prompt appears on new line
print()