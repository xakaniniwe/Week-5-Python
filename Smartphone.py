class Smartphone:
    """
    Represents a smartphone with attributes like brand, model, storage,
    and methods for common smartphone operations.
    """
    def __init__(self, brand, model, storage_gb, color, battery_capacity_mah):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone (e.g., Samsung, Apple).
            model (str): The model of the smartphone (e.g., Galaxy S21, iPhone 13).
            storage_gb (int): The storage capacity in gigabytes.
            color (str): The color of the smartphone.
            battery_capacity_mah (int): The battery capacity in mAh.
        """
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.color = color
        self.battery_capacity_mah = battery_capacity_mah
        self.is_on = False
        self.apps = []  # List to store installed apps
        self.current_app = None  # Keep track of currently running app

    def turn_on(self):
        """
        Turns the smartphone on.
        """
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is turning on...")
            print("Welcome!")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def turn_off(self):
        """
        Turns the smartphone off.
        """
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is turning off...")
            self.current_app = None  # Close any running app
        else:
            print(f"{self.brand} {self.model} is already off.")

    def install_app(self, app_name):
        """
        Installs an app on the smartphone.

        Args:
            app_name (str): The name of the app to install.
        """
        if self.is_on:
            if app_name not in self.apps:
                self.apps.append(app_name)
                print(f"{app_name} has been installed on {self.brand} {self.model}.")
            else:
                print(f"{app_name} is already installed on {self.brand} {self.model}.")
        else:
            print(f"Cannot install {app_name}. Please turn on the phone first.")

    def uninstall_app(self, app_name):
        """
        Uninstalls an app from the smartphone.

        Args:
            app_name (str): The name of the app to uninstall.
        """
        if self.is_on:
            if app_name in self.apps:
                self.apps.remove(app_name)
                print(f"{app_name} has been uninstalled from {self.brand} {self.model}.")
                if self.current_app == app_name:
                    self.current_app = None  # Close the uninstalled app
            else:
                print(f"{app_name} is not installed on {self.brand} {self.model}.")
        else:
            print(f"Cannot uninstall {app_name}. Please turn on the phone first.")

    def open_app(self, app_name):
        """Opens a specified app."""
        if self.is_on:
            if app_name in self.apps:
                if self.current_app:
                    print(f"Closing {self.current_app}...")
                self.current_app = app_name
                print(f"Opening {app_name} on {self.brand} {self.model}.")
            else:
                print(f"{app_name} is not installed. Please install it first.")
        else:
            print("Please turn on the phone to open apps.")

    def close_app(self, app_name):
        """Closes a specified app."""
        if self.is_on:
            if self.current_app == app_name:
                self.current_app = None
                print(f"Closing {app_name} on {self.brand} {self.model}.")
            else:
                print(f"{app_name} is not currently open.")
        else:
            print("Please turn on the phone to close apps.")

    def display_info(self):
        """
        Displays the smartphone's information.
        """
        print("--- Smartphone Information ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage_gb} GB")
        print(f"Color: {self.color}")
        print(f"Battery Capacity: {self.battery_capacity_mah} mAh")
        print(f"Status: {'On' if self.is_on else 'Off'}")
        print("Installed Apps:", ", ".join(self.apps) if self.apps else "None")
        if self.current_app:
            print(f"Current App: {self.current_app}")

    def make_call(self, number):
        """Simulates making a call."""
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}...")
            print("Call ended.")
        else:
            print("Please turn on the phone to make calls.")

    def send_message(self, number, message):
        """Simulates sending a text message."""
        if self.is_on:
            print(f"Sending message to {number} from {self.brand} {self.model}:")
            print(f"\"{message}\"")
            print("Message sent.")
        else:
            print("Please turn on the phone to send messages.")

    def play_music(self, song_name):
        """Simulates playing music."""
        if self.is_on:
            print(f"Playing \"{song_name}\" on {self.brand} {self.model}...")
        else:
            print("Please turn on the phone to play music.")

    def take_photo(self):
        """Simulates taking a photo."""
        if self.is_on:
            print(f"Taking a photo with {self.brand} {self.model}...")
            print("Photo saved.")
        else:
            print("Please turn on the phone to take photos.")


class GamingPhone(Smartphone):
    """
    Represents a gaming smartphone, inheriting from the Smartphone class.
    Adds attributes and methods specific to gaming phones.
    """
    def __init__(self, brand, model, storage_gb, color, battery_capacity_mah, cooling_system, refresh_rate_hz):
        """
        Constructor for the GamingPhone class.

        Args:
            brand (str): The brand of the gaming phone.
            model (str): The model of the gaming phone.
            storage_gb (int): The storage capacity in gigabytes.
            color (str): The color of the gaming phone.
            battery_capacity_mah (int): The battery capacity in mAh.
            cooling_system (str): The type of cooling system (e.g., liquid cooling).
            refresh_rate_hz (int): The screen refresh rate in Hz.
        """
        super().__init__(brand, model, storage_gb, color, battery_capacity_mah)
        self.cooling_system = cooling_system
        self.refresh_rate_hz = refresh_rate_hz
        self.game_mode = False

    def enable_game_mode(self):
        """
        Enables game mode, optimizing performance.
        """
        if self.is_on:
            self.game_mode = True
            print(f"Game mode enabled on {self.brand} {self.model}. Performance optimized!")
        else:
            print("Please turn on the phone to enable game mode.")

    def disable_game_mode(self):
        """
        Disables game mode, restoring normal performance.
        """
        if self.is_on:
            self.game_mode = False
            print(f"Game mode disabled on {self.brand} {self.model}.")
        else:
            print("Please turn on the phone to disable game mode.")

    def display_info(self):
        """
        Overrides the display_info method to include gaming-specific information.
        """
        super().display_info()
        print("--- Gaming Phone Information ---")
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate_hz} Hz")
        print(f"Game Mode: {'On' if self.game_mode else 'Off'}")

    def launch_game(self, game_name):
        """Simulates launching a game."""
        if self.is_on:
            if game_name in self.apps:
                print(f"Launching {game_name} on {self.brand} {self.model} in Game Mode...")
                self.open_app(game_name)  # Use the open_app method from the parent class
            else:
                print(f"{game_name} is not installed. Please install it first.")
        else:
            print("Please turn on the phone to launch games.")

# Example Usage
my_gaming_phone = GamingPhone("ROG", "Phone 7", 512, "Phantom Black", 6000, "Vapor Chamber", 165)

my_gaming_phone.turn_on()
my_gaming_phone.install_app("PUBG Mobile")
my_gaming_phone.install_app("Genshin Impact")
my_gaming_phone.display_info()

my_gaming_phone.enable_game_mode()
my_gaming_phone.display_info()
my_gaming_phone.launch_game("PUBG Mobile")
my_gaming_phone.close_app("PUBG Mobile")
my_gaming_phone.disable_game_mode()

my_gaming_phone.turn_off()
