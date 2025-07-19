

class DietPlannerAgent:
    def plan_diet(self, bmi_insight, diet_pref):
        print("\n🥗 [Diet Planner]: Creating your personalized meal plan.")
        category = bmi_insight['category']
        diet = diet_pref.lower()

        meal_plan = []
        if category == "Underweight":
            meal_plan = ["Breakfast: Oatmeal + nuts", "Lunch: Rice + lentils + veggies", 
                         "Snack: Smoothie", "Dinner: Pasta + protein"]
        elif category == "Normal":
            meal_plan = ["Breakfast: Eggs + wholegrain toast", 
                         "Lunch: Grilled chicken salad", "Snack: Fruit", "Dinner: Fish + veggies"]
        else:
            meal_plan = ["Breakfast: Protein shake + oats", 
                         "Lunch: Quinoa salad", "Snack: Greek yogurt", "Dinner: Mixed salad"]

        if diet == "vegan":
            meal_plan = [meal.replace("chicken", "tofu").replace("fish", "tofu") for meal in meal_plan]

        print("✅ [Diet Planner]: Here's your meal plan.")
        return meal_plan
