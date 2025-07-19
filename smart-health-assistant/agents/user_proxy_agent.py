

class UserProxyAgent:
    def __init__(self):
        self.data = {}

    def collect_user_data(self):
        print("👤 [User Proxy]: Please enter your details.")
        self.data['weight'] = float(input("Weight (kg): "))
        self.data['height'] = float(input("Height (cm): "))
        self.data['age'] = int(input("Age: "))
        self.data['gender'] = input("Gender (M/F/O): ")
        self.data['diet_pref'] = input("Diet (Veg/Non-Veg/Vegan): ")
        return self.data
