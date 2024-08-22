import subprocess
import os

def solve(grid):
    # Convert the grid into a string format suitable for the solver
    grid_str = "\n".join("".join(str(num) if num != 0 else '.' for num in row) for row in grid) + "\n"
    
    # Define the solver path
    solver_path = r"C:\Users\xvann\OneDrive\VSCodeProjects\Sudoku-solver\Solver\a.exe"
    
    # Debugging: Print the solver path and check if it exists
    print(f"Solver path: {solver_path}")
    if not os.path.exists(solver_path):
        raise FileNotFoundError(f"Solver executable not found: {solver_path}")
    
    # Run the solver
    try:
        proc = subprocess.run(solver_path, stdout=subprocess.PIPE, text=True, input=grid_str, check=True)
        
        # Print the raw solver output for debugging
        print("Raw solver output:")
        print(proc.stdout)
        
        # Process the solver output, handling spaces and invalid characters
        solved_grid = []
        for line in proc.stdout.splitlines():
            # Filter out any non-numeric characters and spaces
            cleaned_line = ''.join(ch for ch in line if ch.isdigit() or ch == '.')
            # Convert cleaned line into list of integers
            solved_grid.append([int(num) if num != '.' else 0 for num in cleaned_line])
        
        return solved_grid
    except subprocess.CalledProcessError as e:
        print(f"Solver returned an error: {e}")
        raise
    except OSError as e:
        print(f"An error occurred while running the solver: {e}")
        raise

# Test Sudoku grid (replace with actual test data)
test_grid = [
    [0, 3, 4, 4, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 6, 0, 0, 0, 2],
    [5, 0, 0, 1, 8, 0, 1, 0, 0],
    [5, 7, 7, 7, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 6, 0, 0, 0, 0, 4, 9],
    [0, 0, 0, 0, 1, 0, 0, 5, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 8],
    [7, 0, 0, 0, 0, 0, 4, 0, 0]
]

# Solve the Sudoku puzzle
solved_grid = solve(test_grid)

# Print the solved Sudoku grid
print("Solved Sudoku grid:")
for row in solved_grid:
    print(" ".join(str(cell) for cell in row))
