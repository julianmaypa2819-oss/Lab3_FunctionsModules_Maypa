# main.py
import access_control as ac
import media_engine as me

# ==========================================
# REQUIRED INPUTS (from Appendix image)
# Based on your logs, SEED_NUM was 6 or 7.
# LYNX has length 4. (7 * 3 + 4 = 25)
# threshold 7 * 5 = 35. 25 < 35 -> Access Denied.
# ==========================================
SEED_NUM = 7 # Student entry
FAVORITE_ARTIST = "LYNX" # must be UPPERCASE

# derived variable
CONTROL_NUM = max(1, SEED_NUM)

# ------------------------------------------
# Exercise 1 Execution
# ------------------------------------------
def exercise_1():
    print("--- Exercise 1 ---")
    
    # Calculate access level (wrapped in decorator)
    access_level = ac.compute_access_level(CONTROL_NUM)
    
    # Run comparison and get decision
    decision = ac.validate_access(access_level)
    
    # The output matching your logs is within compute_access_level
    # and validate_access. We just print the final decision here.
    print(f"Control_Num Used: {CONTROL_NUM}")
    print(f"FAVORITE_ARTIST Length: {len(FAVORITE_ARTIST)}")
    print(f"FINAL Authorization Decision: {decision}\n")

# ------------------------------------------
# Exercise 2 Execution (Recursive Signal Shutdown)
# This one does not use modular logic per setup instructions.
# ------------------------------------------
# Initialize signal strength from logic: CONTROL_NUM + len(artist)
initial_signal = CONTROL_NUM + len(FAVORITE_ARTIST) # 7 + 4 = 11

def signal_shutdown(power):
    """Recursive function to simulate shutdown."""
    # Base case: power == 0
    if power <= 0:
        return 0
    
    # Print current strength (Recursive behavior)
    print(f"Current signal strength: {power}")
    
    # Decrement by 1 and recurse
    return 1 + signal_shutdown(power - 1)

def exercise_2():
    print("--- Exercise 2 ---")
    # Per logic, decorator logs go here too.
    # Manually printing for simplicity since it's not modular.
    print("Authorization Started")
    
    total_calls = signal_shutdown(initial_signal)
    
    print("Authorization Completed")
    
    # Logging outputs match your hand-written logs
    print(f"Initial Signal Strength: {initial_signal}")
    print(f"Base Case Condition: Power == 0")
    print(f"Total Recursive Calls: {total_calls}\n")

# ------------------------------------------
# Exercise 3 Execution
# ------------------------------------------
def exercise_3():
    print("--- Exercise 3 ---")
    
    # Limit definition from logic
    limit = CONTROL_NUM + len(FAVORITE_ARTIST) # 7 + 4 = 11
    
    # Create the generator function, wrapped with the monitor decorator
    # This matches the 'Setup' requirement in image 2.
    @me.monitor
    def process_analytics(l):
        return me.play_count_stream(l)
    
    # Execute and consume generator within the decorator
    generated_counts = process_analytics(limit)
    
    # Aggregation logic
    total_plays = sum(generated_counts)
    num_records = len(generated_counts)
    
    # Output to match log exactly
    print(f"FAVORITE_ARTIST Used: {FAVORITE_ARTIST}")
    print(f"Computed Stream Limit: {limit}")
    print(f"Generated Play Counts: {generated_counts}")
    print(f"Total Plays: {total_plays}")
    print(f"Number of Records Processed: {num_records}\n")

# ==========================================
# Run all exercises
# ==========================================
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()