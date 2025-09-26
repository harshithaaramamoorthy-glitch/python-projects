#BMI calculator
print("BMI calculator:")
name=input("enter the name of the patient:")
bmi=int(input("enter bmi value:"))
patient_weight=int(input("patient {bmi}:"))
if patient_weight<=40:
    print("underweight:")
if patient_weight>=110:
    print("obesity:")
if patient_weight==60:
    print("normal:")
    
