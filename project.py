import requests
from tabulate import tabulate

ascii_logo = """
  __                           _       __
 / _|                         | |     /  |
| |_ ___  _ __ _ __ ___  _   _| | __ _`| |
|  _/ _ \| '__| '_ ` _ \| | | | |/ _` || |
| || (_) | |  | | | | | | |_| | | (_| || |_
|_| \___/|_|  |_| |_| |_|\__,_|_|\__,_\___/
"""

def main():
    menu()

def menu():
    x = 1
    while True:
        try:
            if int(x) == 1:
                print(ascii_logo)
                print("")
                print("FORMULA1.50")
                print("")
                print("Menu")
                print("1 For Last Race Result")
                print("2 For Current Constructor Standing")
                print("3 For Current Driver Standing")
                print("4 For Previous Years Constructor Standing")
                print("5 For Previous Years Driver Standing")

                while True:
                    try:
                        i = int(input("Answer: "))
                        match i:
                            case 1:
                                last_race_result()
                                x = input("Enter 1 to go back to the menu, 0 to exit: ")
                                break
                            case 2:
                                current_constructor_standing()
                                x = input("Enter 1 to go back to the menu, 0 to exit: ")
                                break
                            case 3:
                                current_driver_standing()
                                x = input("Enter 1 to go back to the menu, 0 to exit: ")
                                break
                            case 4:
                                constructor_standing()
                                x = input("Enter 1 to go back to the menu, 0 to exit: ")
                                break
                            case 5:
                                driver_standing()
                                x = input("Enter 1 to go back to the menu, 0 to exit: ")
                                break
                            case _:
                                print("Invalid Command")
                    except (ValueError, TypeError):
                        print("Invalid Command")
                        pass

            elif int(x) == 0:
                break
            else :
                print("Invalid Command")
                x = input("Enter 1 to go back to the menu, 0 to exit: ")

        except (ValueError, TypeError):
            print("Invalid Command")
            x = input("Enter 1 to go back to the menu, 0 to exit: ")
    return True

def current_driver_standing():
    response = requests.get("http://ergast.com/api/f1/current/driverStandings.json")
    data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
    driver_standings = []
    for standing in data:
        for driver in standing["DriverStandings"]:
            driver_info = {
                "Position": driver["position"],
                "Driver Name": f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}",
                "Constructor": driver["Constructors"][0]["name"],
                "Points": driver["points"],
            }
            driver_standings.append(driver_info)
    print("")
    print("Current Driver Standing")
    print(tabulate(driver_standings, headers="keys", tablefmt="heavy_outline"))


def driver_standing():
    while True:
        try:
            years = int(input("Enter a year: "))
            if 1950 <= years <= 2023:
                break
            else:
                print("Invalid Years. please input range between 1950 to 2023")
        except (ValueError, TypeError):
            print("Invalid Years. please input range between 1950 to 2023")
            pass


    response = requests.get(f"http://ergast.com/api/f1/{years}/driverStandings.json")
    data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
    driver_standings = []
    for standing in data:
        for driver in standing["DriverStandings"]:
            driver_info = {
                "Position": driver["position"],
                "Driver Name": f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}",
                "Constructor": driver["Constructors"][0]["name"],
                "Points": driver["points"],
            }
            driver_standings.append(driver_info)
    print("")
    print(f"{years} Driver Standing")

    print(tabulate(driver_standings, headers="keys", tablefmt="heavy_outline"))
    return True


def current_constructor_standing():
    response = requests.get(
        "https://ergast.com/api/f1/current/constructorStandings.json"
    )
    data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
    constructor_standings = []
    for standing in data:
        for constructor in standing["ConstructorStandings"]:
            constructor_info = {
                "Position": constructor["position"],
                "Constructor Name": constructor["Constructor"]["name"],
                "Points": constructor["points"],
            }
            constructor_standings.append(constructor_info)
    print("")
    print("Current Constructor Standing")
    print(tabulate(constructor_standings, headers="keys", tablefmt="heavy_outline"))


def constructor_standing():
    while True:
        try:
            years = int(input("Enter a year: "))
            if 1950 <= years <= 2023:
                break
            else:
                print("Invalid Years. please input range between 1950 to 2023")
        except (ValueError, TypeError):
            print("Invalid Years. please input range between 1950 to 2023")
            pass

    response = requests.get(
        f"https://ergast.com/api/f1/{years}/constructorStandings.json"
    )
    data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
    constructor_standings = []
    for standing in data:
        for constructor in standing["ConstructorStandings"]:
            constructor_info = {
                "Position": constructor["position"],
                "Constructor Name": constructor["Constructor"]["name"],
                "Points": constructor["points"],
            }
            constructor_standings.append(constructor_info)
    print("")
    print(f"{years} Constructor Standing")
    print(tabulate(constructor_standings, headers="keys", tablefmt="heavy_outline"))
    return True


def last_race_result():
    response = requests.get("https://ergast.com/api/f1/current/last/results.json")
    data = response.json()["MRData"]["RaceTable"]["Races"]
    information = data[0]
    race_result = []
    for result in data:
        for results in result["Results"]:
            race_info = {
                "Position": results["position"],
                "Driver Name": f"{results['Driver']['givenName']} {results['Driver']['familyName']}",
                "Constructor Name": results["Constructor"]["name"],
                "Status": results["status"],
                "Times": results.get("Time", {}).get("time", "-"),
                "Fastest Lap": results.get("FastestLap", {})
                .get("Time", {})
                .get("time", "-"),
                "Points": results["points"],
            }
            race_result.append(race_info)
    print("")
    print(f"{information['season']}, {information['raceName']}")
    print(f"{information['Circuit']['circuitName']}, {information['Circuit']['Location']['country']}")
    print(f"{information['date']}")
    print(tabulate(race_result, headers="keys", tablefmt="heavy_outline"))


if __name__ == "__main__":
    main()
