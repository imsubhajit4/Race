import time
import random

def display_race(car_positions):
    for i in range(1, 6):
        print("|" + " " * car_positions[0] + "🚗" + " " * (50 - car_positions[0]) + "|")
        print("|" + " " * car_positions[1] + "🚕" + " " * (50 - car_positions[1]) + "|")
        print("-" * 52)
        time.sleep(0.5)

def race():
    car_positions = [0, 0]

    print("Get ready for the race!")
    time.sleep(1)

    while max(car_positions) < 50:
        display_race(car_positions)

        # Get player input to accelerate
        for i in range(2):
            if input(f"Press Enter to accelerate Car {i + 1}! (or Q to quit)").lower() == 'q':
                print("You quit the race!")
                return

            # Accelerate the car
            car_positions[i] += random.randint(1, 5)

    display_race(car_positions)

    # Determine the winner
    if car_positions[0] > car_positions[1]:
        print("Car 1 wins!")
    elif car_positions[1] > car_positions[0]:
        print("Car 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    race()
