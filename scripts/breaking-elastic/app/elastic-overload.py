import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Approximate size of each log line in bytes
log_line_size = 100 # Adjust this as needed

# Number of log lines needed to reach approximately 10MB
lines_per_second = 10000 * 1024 * 1024 // log_line_size

while True:
    for _ in range(lines_per_second):
        print(random_string(log_line_size))