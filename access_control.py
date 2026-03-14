# access_control.py

# A decorator function that logs "Authorization Started" before
# and "Authorization Completed" after the function runs.
def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@audit_log
def compute_access_level(control):
    """
    Computes access level based on CONTROL_NUM and len(FAVORITE_ARTIST).
    Importing FAVORITE_ARTIST inside the function to use main's value.
    """
    from __main__ import FAVORITE_ARTIST
    artist_length = len(FAVORITE_ARTIST)
    # Equation from logic: control_num * 3 + len(artist)
    access_level = (control * 3) + artist_length
    return access_level

def validate_access(level):
    """
    Compares computed access level against a threshold.
    """
    from __main__ import CONTROL_NUM
    # Equation from logic: control_num * 5
    threshold = CONTROL_NUM * 5
    
    print(f"Computed Access Level: {level}")
    
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"