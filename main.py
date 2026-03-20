import time
import os

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_grid(vehicle_pos):
    grid_size = 6
    for y in range(grid_size):
        row = ""
        for x in range(grid_size):
            if [x, y] == vehicle_pos:
                row += " 🤖 " # Represents the auto-navigator
            elif x == 5 and y == 5:
                row += " 🏁 " # Represents the final destination
            else:
                row += " .  " # Represents empty space
        print(row)
    print("\n" + "="*25)

def simulate_navigation():
    # Pre-defined simple navigation path
    path = [
        [0, 0], [1, 0], [1, 1], [2, 1], 
        [2, 2], [3, 2], [3, 3], [4, 3], 
        [4, 4], [5, 4], [5, 5]
    ]
    
    for step, pos in enumerate(path):
        clear_screen()
        print(f"🚀 Auto-navigation system running... (Step {step + 1}/{len(path)})\n")
        draw_grid(pos)
        time.sleep(0.5) # Control the speed of the animation
        
    print("🎉 Navigation complete. Target destination reached successfully!")

if __name__ == "__main__":
    simulate_navigation()
