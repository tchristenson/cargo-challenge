# Trailer Cargo Loader

This is a Python script for loading cargo into a trailer and calculating the highest occupied y-coordinate.

## Usage

1. **Clone the Repository:** Clone or download this repository to your local machine.

2. **Prerequisites:** Make sure you have Python 3 installed on your system.

3. **Run the Script:** Open a terminal/command prompt, navigate to the directory where the script is located, and run the script as follows:

   ```bash
   python main.py

## Constraints

1. Input Format: Enter cargo entries as a comma-separated string with the format x-AxisLetter, where x-Axis is a single-digit number (0-9) representing the x-axis position and Letter is a cargo shape letter (e.g., "0O,2I,3S"). Valid letters are O, I, S, Z, L, J, and T.
2. Input length is 1 to 500 entries long
3. The cargo will not overfill the trailer
4. The input is always well formatted
5. The x-axis portion of the pieces always fit into the width of the trailer

## Error Handling

If there are any issues with the input or loading process, the script will return -1.
