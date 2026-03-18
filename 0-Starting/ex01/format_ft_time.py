from datetime import datetime, date
import time

timestamp = time.time()

print("Seconds since January 1, 1970:", f"{timestamp:,}", "or", f"{timestamp:.2e}", "in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
