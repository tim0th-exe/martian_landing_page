import random
import time

no_of_tracks = 3
selected_player_name = ""
selected_car = None


def slow_print(message, delay=0.01, end='\n', flush=False):
    for char in message:
        print(char, end='', flush=flush)
        time.sleep(delay)
    print(end, end='', flush=flush)


class Car:
    def __init__(self, name, speed, durability, handling, ai=None, flavor_message=""):
        self.name = name
        self.speed = speed
        self.durability = durability
        self.handling = handling
        self.ai = ai
        self.flavor_message = flavor_message

    def print_flavor_message(self):
        slow_print(self.flavor_message)


class EnemyCar(Car):
    def __init__(self, owner_name, car_name, speed, durability, handling, ai):
        super().__init__(car_name, speed, durability, handling)
        self.owner_name = owner_name
        self.ai = ai

    def apply_ai_effects(self):
        self.ai.apply_ai_effects(self)

    def apply_demand_effects(self):
        pass


class CarSelector:
    def __init__(self):
        self.cars = [
            Car("Nebula Mirage", 9, 3, 8,
                flavor_message="The Nebula Mirage, a futuristic marvel, combines speed and handling to dominate the race."),
            Car("Obsidian Regalia", 6, 7, 6,
                flavor_message="Obsidian Regalia, a symbol of brute force, is built for durability in the unforgiving cyberpunk race circuits."),
            Car("Zenith Nomad", 4, 8, 8,
                flavor_message="Zenith Nomad, an agile masterpiece, is designed for handling, perfect for navigating the cybernetic urban sprawl.")
        ]

    def prompt_car(self):
        slow_print("Choose your car:")
        for i, car in enumerate(self.cars, start=1):
            slow_print(
                f"\n{i}. | {car.name} | Speed: {car.speed} | Durability: {car.durability} | Handling: {car.handling} |")

        while True:
            try:
                choice = int(input("\nPick your ride (Enter the number): "))
                slow_print("-" * 80)

                if 1 <= choice <= len(self.cars):
                    return self.cars[choice - 1]
                else:
                    slow_print("Invalid choice enter one of the numbers listed.")
            except ValueError:
                slow_print("Invalid choice enter one of the numbers listed.")


class AI:
    def __init__(self, name, style):
        self.name = name
        self.style = style

    def apply_ai_effects(self, car):
        pass

    def get_flavor_message(self):
        return None

    def print_flavor_message(self):
        flavor_message = self.get_flavor_message()
        slow_print(flavor_message)


class AggressiveRiskyAI(AI):
    def apply_ai_effects(self, car):
        car.speed += 2
        car.durability -= 1
        car.handling += 0
        apply_random_variability(car)

    def get_flavor_message(self):
        return "This AI, known as Havoc Blitz, lives up to its name. It's all about aggressive and risky maneuvers, pushing the car to its limits."


class DefensiveCruisingAI(AI):
    def apply_ai_effects(self, car):
        car.speed -= 1
        car.durability += 2
        car.handling += 0
        apply_random_variability(car)

    def get_flavor_message(self):
        return "This AI, known as Guardian System, prioritizes durability over speed. A defensive and cruising style that aims for a steady race."


class PrecisionTechAI(AI):
    def apply_ai_effects(self, car):
        car.speed -= 1
        car.durability += 0
        car.handling += 2
        apply_random_variability(car)

    def get_flavor_message(self):
        return "Quantum Harmony AI, the epitome of precision tech driving. With unparalleled handling, it elegantly weaves through the most intricate racing paths."


class AISelector:
    def __init__(self):
        self.ais = [
            AggressiveRiskyAI('Havoc Blitz AI', 'Aggressive and Risky'),
            DefensiveCruisingAI('Guardian System AI', 'Durability over Speed'),
            PrecisionTechAI('Quantum Harmony AI', 'Precision Tech Driving')
        ]

    def prompt_ai(self):
        slow_print("Choose your AI driver:")
        for i, ai in enumerate(self.ais, start=1):
            slow_print(f"\n{i}. | {ai.name} | Style: {ai.style} |")

        while True:
            try:
                choice = int(input("\nSelect your AI (Enter the number): "))
                slow_print("-" * 80)

                if 1 <= choice <= len(self.ais):
                    return self.ais[choice - 1]
                else:
                    slow_print("Invalid choice. Enter one of the numbers listed.")
            except ValueError:
                slow_print("Invalid input. Enter a number.")


class EnemyCarSelector(CarSelector):
    def generate_enemy_cars(self, num_enemy_cars, chosen_track=None):
        elite_names = [
            "Zephyr Frost",
            "Aurelia Shadow",
            "Silas Vortex",
            "Luna Nova",
            "Orion Cipher",
            "Ivy Eclipse",
            "Rex Quantum",
            "Seraphina Neon",
            "Axel Blitz"
        ]

        available_names = elite_names.copy()
        random.shuffle(available_names)

        enemy_cars = []

        for _ in range(num_enemy_cars):
            if not available_names:
                slow_print("Warning: Out of unique names for enemy racers. Reusing names.")
                available_names = elite_names.copy()

            random_owner_name = available_names.pop()
            random_car = random.choice(self.cars)
            random_ai = random.choice(AISelector().ais)  # Choose AI randomly for enemy cars

            enemy_car = EnemyCar(random_owner_name, random_car.name, random_car.speed, random_car.durability,
                                 random_car.handling, random_ai)

            # Apply AI effects to the enemy car ### Not entirely sure if this in fact works?
            random_ai.apply_ai_effects(enemy_car)

            # Apply track demand effects to the enemy car
            chosen_track.apply_demand_effects(enemy_car)

            enemy_cars.append(enemy_car)

        return enemy_cars


class Track:
    def __init__(self, name, surface, durability_demand, complexity, speed_demand, conditions, handling_demand):
        self.name = name
        self.surface = surface
        self.durability_demand = durability_demand
        self.complexity = complexity
        self.speed_demand = speed_demand
        self.conditions = conditions
        self.handling_demand = handling_demand

    def apply_demand_effects(self, car):
        # Dictionary to map demand levels to corresponding stat adjustments
        demand_levels = {'Very Low': 2, 'Low': 1, 'Moderate': 0, 'High': -1, 'Very High': -2}

        # Adjust car stats based on track demands
        car.speed += demand_levels[self.speed_demand]
        car.durability += demand_levels[self.durability_demand]
        car.handling += demand_levels[self.handling_demand]

        # Add some randomness for variability (applied after adjusting stats)
        car.speed += round(random.uniform(-0.2, 0.2), 2)
        car.durability += round(random.uniform(-0.2, 0.2), 2)
        car.handling += round(random.uniform(-0.2, 0.2), 2)


class TrackSelector:
    def __init__(self):
        self.tracks = [
            Track("Neon Boulevard Circuit", "Smooth", "Very Low", "Challenging", "Very High", "Rain", "Moderate"),
            Track("Cyberpunk Junkyard Rally", "Uneven Terrain", "Very High", "Dynamic Layout", "Moderate", "Dusty",
                  "Moderate"),
            Track("Virtual Reality Skyline Challenge", "Holographic Platforms", "Moderate", "Intricate Maze",
                  "Very High", "Digital Rain", "Very High"),
            Track("Megacity Expressway", "Straight Stretches", "Very Low", "Straightforward", "Very High", "Normal",
                  "Low"),
            Track("Underground Tech Tunnels", "High-tech Tunnels", "Moderate", "Tactical Path", "Very High",
                  "Artificial Light Grid", "High"),
            Track("Quantum Overpass Dash", "Holographic Bridges", "Moderate", "Twisting Skyways", "Very High",
                  "Acidic Rain", "High"),
            Track("Cybernetic Alley Sprints", "Narrow Urban Corridors", "Moderate", "Tight Turns", "Very High", "Smog",
                  "Very High"),
            Track("Nanotech Labyrinth", "Nano-Infused Grid", "Very Low", "Molecular Maze", "Very High", "Nano Storm",
                  "Very High"),
            Track("Skyport Skyscraper Climb", "Glass Skybridges", "Low", "Vertical Ascension", "Very High",
                  "Lightning Storm", "Moderate"),
            Track("Synthetic Jungle Rally", "Bio-Engineered Terrain", "Very High", "Organic Trails", "Moderate",
                  "Bioluminescent Mist", "Moderate"),
            Track("Datastream Dash", "Digital Highways", "Very Low", "Data Streams", "Very High",
                  "Virtual Thunderstorm", "Very High"),
            Track("Nuclear Wasteland Sprint", "Radioactive Ground", "Very High", "Hazardous Ruins", "Moderate",
                  "Toxic Fallout", "Low"),
            Track("Megacorp Testing Grounds", "Electromagnetic Tracks", "Moderate", "Magnetic Fields", "Very High",
                  "EMP Surges", "High"),
            Track("Subterranean Cyber Maze", "Electro-Luminescent Tunnels", "Very High", "Networked Tunnels",
                  "Very High", "Dark Web Interference", "Very High"),
            Track("Quantum Gravity Loop", "Null-G Zone", "Very Low", "Gravity-Defying Loops", "Very High",
                  "Quantum Flux", "Very High")
        ]
        # generated track names and properties from chatGPT
        self.displayed_tracks = random.sample(self.tracks,
                                              min(no_of_tracks, len(self.tracks)))  # Randomly select tracks for display

    def choose_track(self):
        slow_print("Choose a track:")
        for i, track in enumerate(self.displayed_tracks, start=1):
            slow_print(
                f"\n{i}. | {track.name} | Surface: {track.surface} | Route Complexity: {track.complexity} "
                f"| Conditions: {track.conditions} |")
            slow_print("-" * 80)

        while True:
            try:
                choice = int(input("\nEnter the number of your chosen track: "))
                slow_print("-" * 80)
                if 1 <= choice <= len(self.displayed_tracks):
                    chosen_track = self.displayed_tracks[choice - 1]
                    chosen_track.apply_demand_effects(selected_car)  # Apply demand effects to the selected car
                    return chosen_track
                else:
                    slow_print(f"Invalid choice. Please enter a number between 1 and {len(self.displayed_tracks)}.")
            except ValueError:
                slow_print("Invalid input. Please enter a number.")


class Race:
    def __init__(self, player_car, enemy_cars, track):
        self.player_car = player_car
        self.enemy_cars = enemy_cars
        self.track = track

    def calculate_time(self, car):
        # Calculate the base time based on car attributes
        base_time = 30.0 - (car.speed * 0.3 + car.durability * 0.3 + car.handling * 0.3)

        # Map demand levels to time adjustments
        demand_levels = {'Very Low': 1.0, 'Low': 0.5, 'Moderate': 0.0, 'High': -0.5, 'Very High': -1.0}

        # Apply track demand effects
        time_adjustment = (
                demand_levels[self.track.speed_demand] +
                demand_levels[self.track.durability_demand] +
                demand_levels[self.track.handling_demand]
        )

        # Ensure the final time is non-negative
        final_time = max(0.0, base_time + time_adjustment)
        return final_time

    def race(self):
        slow_print("Race is starting!\n")

        all_cars = [self.player_car] + self.enemy_cars

        slow_print("GO!")

        # Calculate and collect race times for all cars
        lap_times = {car: self.calculate_time(car) for car in all_cars}

        # Find the maximum width of lap times
        max_time_width = max(len(f"{lap_times[car]:.2f}") for car in all_cars)

        # Display lap times for each car
        sorted_cars = sorted(all_cars, key=lambda car: lap_times[car])

        for i, car in enumerate(sorted_cars):
            if isinstance(car, EnemyCar):
                slow_print(
                    f"{car.owner_name}'s {car.name} finished the lap in {lap_times[car]:>{max_time_width}.2f} seconds")
            else:
                slow_print(
                    f"{selected_player_name}, you finished the lap in {lap_times[car]:>{max_time_width}.2f} seconds")

        return sorted_cars, lap_times, max_time_width


def print_welcome_messages():
    messages = [
        '\033[1;96mWelcome to \033[1;95mAUTO PRISTINE\033[0m',
        '\033[1;93mA cyberpunk racing dystopia for the elite.\033[0m',
        '\033[1;94mCustomize your ride, choose surreal tracks,\033[0m',
        '\033[1;92mand let bizarre driving styles unfold.\033[0m',
        '\033[1;95mVictory is pursued from the detached luxury of the uber-rich,\033[0m',
        '\033[1;91mWho neither get in the car\033[0m',
        '\033[1;96mNor bother to watch it race.\033[0m'
    ]

    for message in messages:
        slow_print(message)


def select_player_car():
    car_selector = CarSelector()
    selected_car = car_selector.prompt_car()
    slow_print(f"\n{selected_player_name}, you've chosen the {selected_car.name}")
    selected_car.print_flavor_message()
    return selected_car


def select_player_ai(selected_car):
    ai_selector = AISelector()
    selected_ai = ai_selector.prompt_ai()
    slow_print(f"\n{selected_player_name}, you've chosen the {selected_ai.name}")
    selected_ai.print_flavor_message()
    return selected_ai


def apply_random_variability(car):
    car.speed += round(random.uniform(-0.2, 0.2), 2)
    car.durability += round(random.uniform(-0.2, 0.2), 2)
    car.handling += round(random.uniform(-0.2, 0.2), 2)


def generate_enemy_cars(chosen_track):
    num_enemy_cars = random.randint(5, 9)
    enemy_car_selector = EnemyCarSelector()
    enemy_cars = enemy_car_selector.generate_enemy_cars(num_enemy_cars, chosen_track)
    slow_print("\nOpponents:")
    for i, enemy_car in enumerate(enemy_cars, start=1):
        slow_print(f"{i}. | Owner: {enemy_car.owner_name} | Car: {enemy_car.name} | AI: {enemy_car.ai.name}")
    slow_print("-" * 80)
    return enemy_cars


def select_race_track(selected_car):
    track_selector = TrackSelector()
    chosen_track = track_selector.choose_track()
    slow_print(f"\n{selected_player_name}, you've chosen the {chosen_track.name} track!")
    slow_print("-" * 80)
    chosen_track.apply_demand_effects(selected_car)  # Apply demand effects to the selected car
    return chosen_track


def race_results(sorted_cars, lap_times, max_time_width):
    for i, car in enumerate(sorted_cars):
        if isinstance(car, EnemyCar):
            slow_print(
                f"{car.owner_name}'s {car.name} finished the lap in {lap_times[car]:>{max_time_width}.2f} seconds")
        else:
            slow_print(f"{selected_player_name}, you finished the lap in {lap_times[car]:>{max_time_width}.2f} seconds")


def main():
    global selected_player_name
    global selected_car

    print_welcome_messages()
    selected_player_name = input("Enter your name: ")

    while True:
        selected_car = select_player_car()
        selected_ai = select_player_ai(selected_car)
        chosen_track = select_race_track(selected_car)

        enemy_cars = generate_enemy_cars(chosen_track)

        race = Race(selected_car, enemy_cars, chosen_track)
        result, lap_times, max_time_width = race.race()

        if selected_car in [car for car in result if lap_times[car] == min(lap_times.values())]:
            slow_print("\nCongratulations! You emerged victorious!")
            slow_print(
                "In this city, cred only lasts so long. Dare to go again and assert your dominance among the elite?")
        else:
            slow_print(
                "\nLooks like you shmucked out, kid. In this unforgiving city, defeat is just another curve "
                "in the track.")
            slow_print(
                "But remember, only the resilient thrive in AUTO PRISTINE. Dust off, recalibrate, "
                "and dare to reclaim your position among the best. The city awaits your comeback.")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            slow_print("Thank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
