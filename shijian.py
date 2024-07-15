import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        timer_display = f"{minutes:02}:{seconds:02}"
        print(f"Time left: {timer_display}", end='\r')
        time.sleep(1)
    
    print("\nTime's up! Good work!")

if __name__ == "__main__":
    focus_time = 25  # 专注时间，单位为分钟
    focus_timer(focus_time)
