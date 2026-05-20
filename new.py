# name = "musi"
# bestfriend = "faith"
# university = "muhas"
# her_university = "sauti"
# label = name + " " + bestfriend + " "+ university + " " + her_university
# print(label)

# # the operators
# a,b = 3,7
# exact = a!=b
# print((exact))

# patient_age = 23
# is_an_adult = patient_age > 18
# print(is_an_adult)

#qualifications for adult dose
# patient_age = 12
# patient_weight = 80
# eligible = patient_age >= 16 or patient_weight> 55
# print(eligible)

# # the not value
# patient_is_allergic = False
# patient_state = not patient_is_allergic
# print(patient_state)

# Checking the eligibility of the patient
# Context: prescribe this drug only if:
#  -patient is an adult (age >=18)
#  -patient is not pregnant
#  -patient has adequate renal function (Crcl >= 60) OR is on reduced dose protocol

# patient_age = 36
# is_pregnant = False
# creatinine_clearance = 55.0
# on_reduced_dose_protocol = True

# eligible = (
#     patient_age >= 18
#     and not is_pregnant
#     and (creatinine_clearance >= 60 or on_reduced_dose_protocol)
# )
# print(eligible)

# check eligibility for pessaries
# patient age > 14
# patient sex = female
# diagnosis = candidiasis and visible rashes 

# patient_age = 12
# patient_female = True
# diagnosis_candidiasis = True
# visible_rashes = False

# eligible = (
#     patient_age>14 
#     and patient_female
#     and(diagnosis_candidiasis or visible_rashes) 
# )
# print(eligible)
#  ----Pharmacy example: Multi-step
# Context : Amoxicillin 500 mg capsules, 3 times daily for 7 days
# Step 1: total_daily-dose = dose_mg * doses_per_day
# Step 2: total course dose = total_daily_dose * days
# Step 3: number of tablets = total course dose / dose_mg  (should equal doses_per_day  * days)
#  

# 
# daily safe aspirin dose
# dose_mg = 45
# days = 5
# total_dose = dose_mg * days
# max_tolerable_dose = 450
# its_safe = total_dose< max_tolerable_dose
# print(its_safe)
# print(total_dose)
# print(type(total_dose))
# print(dose_mg//days)
# print(float(dose_mg%days))
# print(max_tolerable_dose + dose_mg * 3)
# print((max_tolerable_dose+ dose_mg) * 3)

# Input trial
# novel_name = "King of Envy" 
# author_name = "Ana Huang"
# print(input(novel_name))
# print(input(author_name))

# TRIAL 2
# title = input("Enter the title:")
# author = input("Enter the name of the author:")
# print(title)
# print(author)

# #TRIAL 2
# song_name =input("name of the song:")
# artist = input ("name of the artist")
# print(song_name)
# print(artist)

#TRial 3 
# arrival_time =input ("Time of arrival:")
# age = input ("Age:")
# person_name = input ("What is your name?:")
# print(arrival_time)
# print(age)
# print(person_name)

# PRACTICE TUE
# name = input ("Enter your name:")
# course = input ("Enter your course:")
# email = input("Enter your email:")
# print(name)
# print(course)
# print(email)

#  BMI RANGE CLASSIFICATION
weight_kg = int(input("Enter your weight:"))
height_cm = int(input("Enter your height:"))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

if bmi< 18.5:
    print("Underweight")

if 18.5<bmi< 24.9:
    print("normal weight")

if 25<bmi<29.9:
    print("Overweight")

if 30<bmi<34.9:
    print("Obese")

