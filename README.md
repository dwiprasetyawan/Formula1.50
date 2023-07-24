# Formula1.50 - Python Script for Formula 1 Information

This is my final project to complete the CS50P Course. Formula1.50 is a Python script that provides information related to Formula 1 races, driver standings, and constructor standings using the Ergast API. The script presents a menu with various options, allowing the user to view different types of Formula 1 data.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3
- The requests library (install using `pip install requests`)
- The tabulate library (install using `pip install tabulate`)

## Menu Options

The script presents the following options in the menu:

1. **Last Race Result**: Shows the result of the last Formula 1 race, including the driver positions, constructors, points, and more.

2. **Current Constructor Standing**: Displays the current standings of constructors, including their positions and points.

3. **Current Driver Standing**: Shows the current standings of drivers, including their positions, constructors, and points.

4. **Previous Years Constructor Standing**: Allows you to enter a specific year and then displays the standings of constructors for that year.

5. **Previous Years Driver Standing**: Allows you to enter a specific year and then displays the standings of drivers for that year.

## How It Works

The script interacts with the Ergast API to retrieve data related to Formula 1 races, driver standings, and constructor standings. It uses the requests library to send HTTP requests to the Ergast API and fetch JSON data. The data is then processed and displayed in tabular format using the tabulate library.

## Note

The script runs in an infinite loop to present the menu and handle user input. To exit the loop and terminate the script, enter "0" when prompted to do so.

## Usage

To run the script, execute the following command:

```bash
python project.py
