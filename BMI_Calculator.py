def calculate_bmi(W,H):
    bmi=W/((H*0.3048)**2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight_in_kg=float(input("enter the weight in KG: "))
height_in_feet=float(input("enter the height in feet: "))

bmi=calculate_bmi(weight_in_kg,height_in_feet)
print("your bmi is:",bmi)

category=categorize_bmi(bmi)
print("You have "+ category)
