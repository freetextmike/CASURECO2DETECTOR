import subprocess
import datetime

# Configuration
local_machine_ip = ""  # Replace with the IP address of your local machine
log_file_path = ""  # Replace with the desired path for your log file

power_loss_start_time = None

# Ping the local machine
def ping_local_machine():
    try:
        subprocess.check_output(["ping", "-c", "1", local_machine_ip], timeout=2)
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        return False

# Log power loss events
def log_power_loss(start_time, end_time):
    duration = end_time - start_time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time}: Power loss event. Duration: {duration}\n"

    with open(log_file_path, "a") as file:
        file.write(log_entry)

# Main script
def main():
    global power_loss_start_time

    while True:
        is_reachable = ping_local_machine()

        if not is_reachable and power_loss_start_time is None:
            power_loss_start_time = datetime.datetime.now()

        if is_reachable and power_loss_start_time is not None:
            power_loss_end_time = datetime.datetime.now()
            log_power_loss(power_loss_start_time, power_loss_end_time)
            power_loss_start_time = None

        # Adjust the sleep duration according to your needs
        time.sleep(10)  # Ping every 10 seconds

if __name__ == "__main__":
    main()
