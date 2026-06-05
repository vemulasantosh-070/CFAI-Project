import random
import time
from datetime import datetime


class SmartTrafficManagement:

    def __init__(self):
        self.roads = {
            "North": 0,
            "South": 0,
            "East": 0,
            "West": 0
        }

    def collect_sensor_data(self):
        """Simulate vehicle sensor readings"""
        for road in self.roads:
            self.roads[road] = random.randint(0, 100)

    def detect_emergency_vehicle(self):
        """Random emergency vehicle detection"""
        emergency = random.choice([True, False, False, False, False])
        if emergency:
            return random.choice(list(self.roads.keys()))
        return None

    def pedestrian_request(self):
        """Random pedestrian crossing request"""
        return random.choice([True, False, False])

    def is_peak_hour(self):
        """Peak hour simulation"""
        current_hour = datetime.now().hour

        if (8 <= current_hour <= 10) or (17 <= current_hour <= 20):
            return True
        return False

    def display_status(self):
        print("\n" + "=" * 50)
        print("CURRENT TRAFFIC STATUS")
        print("=" * 50)

        for road, vehicles in self.roads.items():
            print(f"{road:<10}: {vehicles} vehicles")

    def calculate_green_time(self, vehicles):

        # Rule 1: Heavy congestion
        if vehicles > 80:
            return 40

        # Rule 2: High traffic
        elif vehicles > 50:
            return 30

        # Rule 3: Medium traffic
        elif vehicles > 20:
            return 20

        # Rule 4: Low traffic
        elif vehicles > 0:
            return 10

        # Rule 5: Empty road
        return 5

    def select_signal(self):

        # Emergency Vehicle Priority
        emergency_road = self.detect_emergency_vehicle()

        if emergency_road:
            print("\n🚑 EMERGENCY VEHICLE DETECTED!")
            print(f"Priority given to {emergency_road}")
            return emergency_road, 45

        # Normal Rule-Based Decision
        selected_road = max(self.roads, key=self.roads.get)

        green_time = self.calculate_green_time(
            self.roads[selected_road]
        )

        # Peak Hour Adjustment
        if self.is_peak_hour():
            green_time += 10
            print("\n⏰ PEAK HOUR ACTIVE")

        return selected_road, green_time

    def handle_pedestrian_crossing(self):

        if self.pedestrian_request():
            print("\n🚶 Pedestrian Crossing Requested")
            print("Walk Signal ON for 10 seconds")
            time.sleep(2)

    def run(self):

        print("=" * 60)
        print(" SMART TRAFFIC MANAGEMENT SYSTEM ")
        print(" RULE-BASED ALGORITHM PROJECT ")
        print("=" * 60)

        while True:

            # Data Collection Layer
            self.collect_sensor_data()

            # Monitoring Dashboard
            self.display_status()

            # Pedestrian Safety Module
            self.handle_pedestrian_crossing()

            # Decision Engine
            road, green_time = self.select_signal()

            print("\nDECISION ENGINE OUTPUT")
            print("-" * 40)
            print(f"Green Signal Road : {road}")
            print(f"Vehicle Count     : {self.roads[road]}")
            print(f"Green Time        : {green_time} sec")

            print("\nSignal Running...")
            time.sleep(3)

            print("\nCycle Completed")

            choice = input(
                "\nRun Next Cycle? (Y/N): "
            ).strip().lower()

            if choice != "y":
                print("\nSystem Shutdown Successfully.")
                break


if __name__ == "__main__":
    traffic_system = SmartTrafficManagement()
    traffic_system.run()