import csv 
import sys # for sys.exit()

class Vehicle:
    '''Models a Vehicle'''
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mpg = None
        self.matches = []  # store multiple matching trims

    def get_mpg(self):
        '''Finds matching vehicles and their mpg'''        
        for data in vehicle_data:
            if (self.brand == data['brand'] and self.year == data['year'] and self.model in data['model']):  # allow partial match
                self.matches.append({ "model": data['model'],"mpg": float(data['combined_mpg'])})
        if self.matches:
            return self.matches
        else:
         return None

    @staticmethod
    def mpg_to_kmpl_UK(mpg: float) -> float:
        """Convert mpg to km/l (UK gallon)."""
        return mpg * (1.60934 / 4.54609)

    @staticmethod
    def mpg_to_kmpl_US(mpg: float) -> float:
        """Convert mpg to km/l (US gallon)."""
        return mpg * (1.60934 / 3.78541)

    @staticmethod
    def mpg_to_l_per_100km(mpg: float) -> float:
        """Convert mpg (US) to L/100km."""
        return (100 * 3.78541) / (mpg * 1.60934)

# Extract the data 
vehicle_data = []
file = 'C:/Users/ThinkPad/Desktop/Python/VS Code/vehicle_mpg_cal/merged_mpg_data.csv'

try:
    with open(file, 'r') as file_obj:
        contents = csv.reader(file_obj)
        header_row = next(contents)  # skip header row

        for row in contents:
            try:
                data = {
                    'year': int(row[0]),
                    'brand': row[1].strip().lower(),   # normalize to lowercase
                    'model': row[4].strip().lower(),   # normalize to lowercase
                    'combined_mpg': row[45]
                }
                vehicle_data.append(data)
            except (ValueError, IndexError):
                continue

except FileNotFoundError:
    print('File does not exist or check the file path')
    sys.exit(1) # exit with status code 1 (error)

# __User Interaction__
while True:            
    try:
        brand = input('Enter the vehicle brand here: -> ').strip().lower()
        model = input('Enter vehicle model here: -> ').strip().lower()
        year = int(input('Enter year here: -> '))

        car = Vehicle(brand, model, year)
        matches = car.get_mpg()

        if matches:
            print("\nMultiple matches found:")
            for i, m in enumerate(matches, start=1):
                print(f"{i}. {year} {brand.title()} {m['model'].title()}")

            # Let user pick
            choice = int(input("\nSelect the trim number you want: -> "))
            if 1 <= choice <= len(matches):
                selected = matches[choice - 1]
                fuel_eff = selected["mpg"]

                fuel_eff_kmpl_UK = car.mpg_to_kmpl_UK(fuel_eff)
                fuel_eff_kmpl_US = car.mpg_to_kmpl_US(fuel_eff)
                fuel_eff_l_per_100km = car.mpg_to_l_per_100km(fuel_eff)

                print("\nYour vehicle's fuel efficiency:\n")

                # Table header
                print("--------------------------------------------------------------")
                print(f"{'Metric':^15} | {'Value':^15}")   # ^ = center alignment
                print("--------------------------------------------------------------")

                # Table rows with units
                print(f"{'Combined MPG':<15} | {fuel_eff:>10.2f} mpg")
                print(f"{'km/l (UK)':<15}   | {fuel_eff_kmpl_UK:>10.2f} km/l")
                print(f"{'km/l (US)':<15}   | {fuel_eff_kmpl_US:>10.2f} km/l")
                print(f"{'L/100km':<15}     | {fuel_eff_l_per_100km:>10.2f} L/100km")

                print("--------------------------------------------------------------")

            else:
                print("\nInvalid selection.")

        else:
            print('\nSorry vehicle not found.')

    except ValueError:
        print("\nInvalid input. Please enter numbers where required.")

    # Exit or continue     
    prompt = input('\nWould you like to check another vehicle? (Yes/No): -> ').lower().strip()
    if prompt == 'no':
        break
    elif prompt == 'yes':
        continue
    else:
        print('\nInvalid input.')
