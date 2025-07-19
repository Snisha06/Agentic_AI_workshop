
from tools.bmi_tool import calculate_bmi

class BMIAgent:
    def evaluate_bmi(self, weight, height):
        bmi = calculate_bmi(weight, height)
        print(f"\n📏 [BMI Tool]: Your BMI is {bmi}")
        if bmi < 18.5:
            category = "Underweight"
            rec = "Consider a calorie-rich balanced diet."
        elif bmi < 25:
            category = "Normal"
            rec = "Maintain your current lifestyle."
        elif bmi < 30:
            category = "Overweight"
            rec = "Include moderate exercise and balanced diet."
        else:
            category = "Obese"
            rec = "Consult a professional; start weight management."
        insight = {"bmi": bmi, "category": category, "recommendation": rec}
        print(f"✅ [BMI Agent]: Category: {category}, Advice: {rec}")
        return insight
