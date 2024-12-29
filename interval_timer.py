import timer_controls
import input_valid


def main():
    user_minutes = input_valid.get_valid_float("\nDesired minutes per loop: ")
    interval_seconds = int(user_minutes * 60)
    interval_count = input_valid.get_valid_int("\nDesired number of timer repetitions: ")
    
    timer_controls.timer(interval_seconds, interval_count)
    print('\nAll loops complete!\n')
    

if __name__ == "__main__":
    main()


# BUGS:
# 
# plays both spotify and music if both are open

# TODO:
# 
# will need to start over, most likely! YAY
