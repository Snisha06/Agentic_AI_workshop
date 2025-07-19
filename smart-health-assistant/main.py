

from agents.user_proxy_agent import UserProxyAgent
from agents.bmi_agent import BMIAgent
from agents.diet_planner_agent import DietPlannerAgent
from agents.workout_scheduler_agent import WorkoutSchedulerAgent

def main():
    print("\n💬 Welcome to Smart Health Assistant\n")
    user_agent = UserProxyAgent()
    data = user_agent.collect_user_data()

    bmi_agent = BMIAgent()
    bmi_info = bmi_agent.evaluate_bmi(data['weight'], data['height'])

    diet_agent = DietPlannerAgent()
    meal_plan = diet_agent.plan_diet(bmi_info, data['diet_pref'])

    workout_agent = WorkoutSchedulerAgent()
    workout_schedule = workout_agent.schedule_workout(data['age'], data['gender'], meal_plan)

    print("\n📋 Final Health Plan Summary:")
    print(f"- BMI: {bmi_info['bmi']} ({bmi_info['category']})")
    print(f"- Health Advice: {bmi_info['recommendation']}")
    print("- Meal Plan:")
    for meal in meal_plan:
        print(f"  • {meal}")
    print("- Weekly Workout Routine:")
    for session in workout_schedule:
        print(f"  • {session}")

if __name__ == "__main__":
    main()
