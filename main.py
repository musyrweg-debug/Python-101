9
#DATE DETAILS
# date = "04th May 2026"
# location = "SWISS RESTAURANT"
# time = "18:00"
# dresscode = "black dress"
# transport_means = "black volvo"

# float values
# weight_kg = 68.5               # patient weight in kilograms
# dose_per_kg = 2.5              # dose in mg per kg of body weight
# creatinine_clearance = 72.3    # ml/min - used for renal dose adjustment
# bmi = 24.8                     # body mass index

# #Calculate weight - based dose

# movie = "michael"
# duration = 2
# biopic = "michael jackson"
# actor ="jafaar jackson"
# number_of_shows = 4
# total_amount_of_time = duration * number_of_shows
# print(f"Today I watched a movie of {biopic} which was proudly played by {actor}")
# print(f"The total duration of the movie is {duration} hours")
# print(f"with the  number of shows available  the actual watch time is {total_amount_of_time}hours")

# is_allergic = True                 # patient has a known drug allergy
# requires_refrigeration = False     # medication does not need cold storage
# is_controlled_substance = True     # medication is a controlled drug
# is_generic_available = False       #no generic equivalent on formulary
# patient_consented = True           #patient has given informed consent   

# print(is_allergic)                 # True
# print (requires_refrigeration)     # False

# Checking the data type

# dose_mg = 500
# weight_kg = 68.5
# drug_name = "Metformin"
# is_allergic = True

# print(type(dose_mg))
# print (type(weight_kg))
# print(type(drug_name))
# print(type(is_allergic))

# user_input = "250"
# print(type(user_input))

# # Check type then convert
# print(f"Input type: {type(user_input)}")
# numeric_dose = int(user_input)
# print(f"After conversion : {type(numeric_dose)}")
# total_daily_dose = numeric_dose * 3
# print(f"Total daily dose: {total_daily_dose}mg")

# dose_input = "500"
# dose_mg = int(dose_input)

# total_daily_dose = dose_mg * 3
# print (f"Single dose: {dose_mg} mg")
# print(f"Total daily dose: {total_daily_dose} mg")

# # Floats

# weight_input = "68.5"
# weight_kg = float(weight_input)
# dose_per_kg = 2.5

# total_dose = weight_kg * dose_per_kg
# print(f"Patient weight: {weight_kg} kg")
# print(f"Dose per kg: {dose_per_kg} mg/kg")
# print(f" Total dose: {total_dose} mg")

# dose_mg = 500       # int
# dose_per_day = 3    # int

# dose_per_dose = dose_mg / dose_per_day
# print(dose_per_dose)
# print(type(dose_per_dose))

# dose_float = float(dose_mg)
# print(dose_float)
# print(type(dose_float))

# drug_name = "Metformin"
# dose_mg = 500
# quantity = 60

# label = drug_name + " " + str(dose_mg) + "mg - Qty:" + str(quantity)
# print(label)

# Personal practise
# dose_mg = 500
# total_dose = dose_mg * 3
# #print(total_dose)

# # Patient BMI to qualify for a bariatric surgery
# Patient_name = "Lana"
# Patient_age = 36

# # DATA FOR BMI
# weight_kg = float(input("Enter your weight:"))
# height = float(input("Enter your height in cm:"))
# print(weight_kg)
# print(height)
 
# # Calculation formula
# height_m = height / 100
# bmi = weight_kg / (height_m**2)

# # Judging criteria
# if bmi< 18.5:
#     print("underweight")

# if 18.5 < bmi < 24.9:
#     print("normal weight")

# if 24.9<bmi < 25.9:
#     print ("overweight")

# if 26< bmi <34.9:
#     print("Obese")

# if bmi> 35:
#     print("Very Obese")

# # TO CHECK IF PATIENT QUALIFIES FOR BARIATRIC SURGERY
# qualify =  (
#     Patient_age > 18 and bmi > 35
#     )    
# print(qualify)
# print (f"Patient named {Patient_name} and of age {Patient_age} has a bmi of {bmi:.2f}, thus her qualification status for a bariactric surgery are {qualify}")

# ------ STRING PRACTICE----------
# Instruction_single = "Patient's drug should be placed in a refrigerator"
# Instruction_double ='Dispense using "Medication Guide" attached'
# print(Instruction_single)
# print(Instruction_double)

# #     PRACTICE 2----------
# drug_label = '''
# Patient name: ANITHA
# Drug name : TETRACYCLINE

# Dosage: Take twice daily
# Precaution: Always take one hour before meals
# '''
# print(drug_label)

# ----------PRACTICE 2-----------
# label ="Omeprazole 2omg.\nTake one hour before meal.\nStore in a cool and dry place."
# print(label)

# #-------PRACTICE 3----------
# drug_name = "WATER RUNS DRY"
# print(drug_name[9])
# print(drug_name[7])
# print(drug_name[4])
# print(drug_name[-5])
# print(drug_name[-6])
# print(drug_name[4:7])
# print(drug_name[0:6])
# print(drug_name[:3])
# print(drug_name[6:])
# print(drug_name[ ::1])
# print(drug_name[:])

#--------PRACTICE 2
# drug_name = " prednisolone drug "
# label =drug_name.upper()
# title = label.lower()
# print(label)
# print(title)
# name = drug_name.rstrip()
# print(f"'{name}'")

# raw_input =  " high tides "
# clean = raw_input.strip()
# print(f"'{clean}'")
# print(f"'{raw_input}'")

# drug= ' Prednisolone '
# new_drug = drug.strip()
# print(f"'{drug}'")
# print(f"'{new_drug}'")

#---------REPLACE PRACTICE
# instruction = "Give DNS stat at arrival time"
# expanded = instruction.replace("DNS", "Dextrose Normal Saline").replace("stat","Immediatley!!")
# print(instruction)
# print(expanded)

# general_label = "Patient has diagnosis thus should be given this drug"
# specific = general_label. replace("Patient","Lana"). replace("diagnosis","Asthma"). replace("this drug","salbutamol inhaler")
# print(general_label)
# print(specific) 

# #-------SPRING LIST
# medicine_list = [90,"Ipratropium","Labetalol","Epinephrine"]
# medications = medicine_list.split("/")
#print(medicine_list)
# print(type(medicine_list))
# print(medications)
# meds = medicine_list.split()rff
# print(meds)
# list= medicine_list.split("/")
# print(list)

# #----------JOIN
# medicines_list = "amoxicillin", "ciprofloxacin","dexamethasone"
# summary=",".join(medicines_list)
# row = "\n -".join(medicines_list)
# new_one = ",".join(meds)
# new_two = "\n *".join(medicines_list)
# print(summary)
# print(row)
# print(new_one)
# print(new_two)

#--------FIND
# Instructions = "Drink while hot at 32 degrees"
# placement = Instructions.find("hot")
# if_present = Instructions.find("cold")
# print(placement)
# print(if_present)

# #-------STARTS WITH
# drug_code = "DOX"
# antibiotic_prefixes = ("AMOX","CIPRO","PEN")
# if drug_code.startswith(antibiotic_prefixes):
#     print("shown antibiotic resistance")
# else:
#     print("safe to give patient")

# #-------ENDS WITH
# file_type= "Muhimbili hospital.peg"
# if file_type.endswith(".jpg"):
#     print("correct file type")
# else:
#     print("not correct file type")


#----------------------LIST-----
# Medicine = ["ciprofloxacin","Amoxicillin","doxorubicin","Kanamycin","cefixime"]
# print(Medicine[0])
# print(Medicine[-2])
# print(Medicine[3:-1])
# medidata = ["eli", 6,  34.06, True]
# print(f"patients details: {medidata}")
# Medicine.append("Gentamycin")
# print(Medicine)
# Medicine.append("doxorubicin")
# print(Medicine)
# Medicine.remove("doxorubicin")
# print(Medicine)
# Medicine.remove("ciprofloxacin")
# print(Medicine)
# meds = Medicine.pop()
# print(meds)
# print(Medicine)
# meds1 = Medicine.pop(2)
# print(meds1)
# print(Medicine)
# Medicine.insert(2,"Kanamycin")
# print(Medicine)
# Medicine.replace("kanamycin", "Doxorubicin")
# print(Medicine)
# Medicine.insert(2, "Penicillin")
# print(Medicine)
# Medicine.remove("Kanamycin")
# print(Medicine)
# Medicine.sort()
# print(Medicine)
# Medicine.reverse()
# print(Medicine)
# print(len(Medicine))
# Medicine = ["ciprofloxacin","Amoxicillin","doxorubicin","Kanamycin","cefixime"]
# # Medicine.append("Penicillin")
# print(Medicine)
# Medicine.remove("doxorubicin")
# print(Medicine)
# Medicine.insert(-2, "ceftriaxone")
# print(Medicine)
# Meds1 = Medicine.pop(1)
# print(Medicine)
# print(Meds1)
# Medicine.sort()
# print(Medicine)
# Medicine.reverse()
# print(Medicine)
# 


#----------------ITERATION UNDERSTANDING--------
# band = "seventeen","ateez", "enhyphen","straykids"
# for k in band:
#     print(band)
# for index, k in enumerate(band):
#     print(f"{index+1} , {k}")
# for index, num in enumerate(band):
#     print(f"{index} / {num}")
# for index, us in enumerate(band):
#     print(f"{index + 1}, {us}")
# for n in band:
#     print(n[::-1])
# for b in band:
#     print(f"Buy ticket:{b}")
# for v in band:
#     print(f"V is not a member of {v}")
# for up in band:
#     print(f"Rewrite in bold:band.upper{up}")

#---------TUPLES--------
# songs = ("2022","2023","2024","2019") 
# astrounant,view,mixtape, redlights = songs
# # print(f"fav song: {astrounant}")
# print(f"most wins: {view}")
# print(f"top song:{mixtape}")
# print(f"most viewed:{redlights}")
# medicine_time=("09:00","15:00","21:00")
# morning, evening, night = medicine_time
# print(f"blue pill:{morning}")
# print(f"yellow pill:{evening}")
# print(f"pink pill:{night}")
# songs.remove(0)
# print(type(songs))

# name = "mine"
# for m in name:
#     m.upper()
#     print(m``))
# words = ["hello", "world", "python"]
# upper_words = [w.upper() for w in words]
# print(upper_words)


#-----------------------LIST COMPHRENSION-------
# doses_mg = [5, 10, 20, 25, 50]
# higher_dose= [dose//2 for dose in doses_mg if dose> 10]
# print(f"These should not be given{higher_dosennm;n}")
# print(doses_mg)
# print(higher_dose)

# # w
# Patient_name = ["han","lee","IN","bang"]
# confusing = [con.lower() for con in Patient_name]
# print(confusing)
# upps = [name.upper() for name in Patient_name]
# print(upps)
# print(input("Enter product name:"))
# print(input(float("Enter price of product:")))

#--------LIST COMPREHENSION
# numbers = [0,1,2 ,3,4]
# doubles = [num *2  for num in numbers] 
# print(doubles)

# names= ["lindana","irene","lisa"]
# uppercase = [m.upper() for m in names]
# print(uppercase)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = [num for num in numbers if num % 2 == 0]
# print(even)

# marks = [45, 67, 80, 32, 90]
# actual = [m for m in marks if m > 50]
# print(actual)

# doses = [50, 100, 250]
# dose_mg = [f" {do}mg "for do in doses]
# print(dose_mg)

# drugs = ["aspirin", "morphine", "ibuprofen"]
# length = [len(d) for d in drugs]
# print(length)

# values = [-3, 5, -1, 7, 9, -2]
# negatives = [v for v in values if v >= 0]
# print(negatives)

# numbers = [1, 2, 3, 4, 5]
# square = [n**2 for n in numbers if ((n % 2 == 1))]
# print(square)

# marks = [80, 45, 90, 30, 70]
# fail_remark = ["fail" if marks < 50 else "pass"]
# print(fail_remark)

# drugs = ["Paracetamol", "Ibuprofen", "Morphine"]
# first = [p[0] for p in drugs]
# print(first)

# numbers= [n**2 for n in range(1, 11)]
# print(numbers)

# words = ["tablet", "gel", "capsule", "pill"]
# keep = [w for w in words if len(w) > 5]
# print(keep)

# marks = [80, 45, 90, 30]
# picks = ["PASS" if m > 50 else "FAIL"for m in marks ]
# results = ["Pass" if mark >= 50 else "Fail" for mark in marks]

# print(picks)

# temps = [20, 35, 15, 40]
# right = ["HOT" if t > 25 else "cold" for t in temps]
# print(right)

# drugs = ["aspirin", "ibuprofen", "gel", "morphine", "pen"]
# conv = [a.upper() for a in drugs if len(a) > 5]
# print(conv)

# doses = [25, 50, 150, 200, 75]
# label = [ f"{d}mg"for d in doses if d > 50]
# print(label)

# numbers = [1, 2, 3, 4, 5, 6]
# odd = ["odd"if n % 2 == 1 else n for n in numbers ]
# print(odd)

# words = ["tablet", "gel", "capsule", "pill", "syringe"]
# new =[ n[0] for n in words]
# print(new)

# medications = ["Aspirin", "Ibuprofen", "Acetaminophen"]
# new = medications.pop()
# print(new)
# # medications.append("doxy")
# # medications.append("alu")
# print(medications)
# print(medications[0])

# doses = [100, 200, 50, 300]
# high_doses = [d for d in doses if d > 150]
# print(high_doses)

# medications = ["A", "B", "C"]
# length = len(medications)
# print(length)            

#-------USER STORIES-----------
# products = []

# num = int(input("How many products do you want to buy?"))
# print(num)
# for x in range(num):
#     name = input("Enter the name of the product:")
#     break

# product = float(input("Enter the number of products:"))
# while True:
#     try:
#         price = input ("Enter price of product:")
#         break
#     except:
#         print("Enter valid amount, example'23'....")

# while True:
#     try:
#         quantity = float(input("Enter quantity of product"))
#         break
#     except:
#         print("Enter valid amount....."
# print("stop")

#-----TRY 2
# num = int(input("How many products do you want to buy?:"))

# for x in range(num):

#     name = input("Enter name of the product:")
    
#     while True:
#         try:
#             price = float (input("Enter the price of your product:"))
#             break
#         except:
#             print("Enter valid amount...")
    
#     while True:
#         try:
#             quantity = float(input("Enter the quantity of product:"))
#             break
#         except:
#             print("Enter valid amount....")

# Patient_details = {
#     "Name": "Hudson",
#     "Age": 12,
#     "Disease": "Hunter Virus"
#     }
# print(Patient_details"the name of the patient["Name"]")

#-------DICTIONARIES-------
# Patient ={
#     "name":"Sarah Jackson",
#     "age":45,
#     "weight_kg": 68,
#     "medications":["Metformin", "Lisinopril","Atorastatin"],
#     "allergies":["Penicillin"]
# }
# Patient_3 ={
#     "name": "pretty",
#     "age": 53,
#     "weight_kg": 45
# }
# Patient.update(Patient_3)
# # Patient.update(Patient_2)
# print(Patient)
# print(Patient_3)
# print(Patient)
# print(Patient["age"])
# print(Patient["name"])
# print(Patient.get("weight_g"))
# print(Patient.get("allergy","None present"))
# print(Patient.get("weight_kg"))
# Patient["prescriber"]= "Dr Chen"
# Patient["movie"]= "King the Land"
# Patient["Genre"]="K-Drama"
# print(Patient["movie"])
# del Patient["movie"]
# del Patient["prescriber"]
# del Patient["Genre"]
# print(Patient)

# for j in Patient:
#     print(j)
# for v in Patient.values():
#     print(v)
# for j, v in Patient.items():
#     print(f"{j}:{v}")
# k = list(Patient.keys())
# print(k)
# v = list(Patient.values())
# print(v)
# things = (f"{k},{v}"for k, v in Patient.items())
# print("=== Patient Summary===")
# for kay,vee in Patient.items():
#     print( f"{kay.capitalize()}:{vee}")

# things = (f"{k.capitalize()}:{v}"for k,v in Patient.items())
# print(things)

# --- Pharmacy Example: Drug database with nested entries ---
# Context: Each drug maps to a sub-dictionary of clinical properties

# drug_db = {
#     "Amoxicillin": {"class": "Antibiotic",    "max_dose_mg": 3000, "unit": "mg"},
#     "Metformin":   {"class": "Antidiabetic",  "max_dose_mg": 2550, "unit": "mg"},
#     "Lisinopril":  {"class": "ACE Inhibitor", "max_dose_mg": 40,   "unit": "mg"},
# }
# print(f" the max dose for Metformin is {drug_db["Metformin"]["max_dose_mg"]}{drug_db['Metformin']["unit"]}")

# # Look up a specific drug
# drug = "Metformin"
# # print(f"{drug} max dose: {drug_db[drug]['max_dose_mg']} {drug_db[drug]['unit']}")

# songs = {
#     "human_nature":{"artist":"MJ", "mood":"deep"},
#     "view":{"artist":"straykids", "mood":"enlighten"},
#     "whisper":{"artist":"wham", "mood":"low"},
# }
# print({songs["human_nature"]["mood"]})
# print(f" the song {songs["whisper"]["artist"]} feels like {songs["whisper"]["mood"]}")
# print(f"My top artist are {songs["human_nature"]["artist"]} and {songs["whisper"]["artist"]}" )
# # print(for key in capitals.keys())
# print(help(songs))
# song = "view"
# for 
# print(f"{song}" mood: {songs[song]})

# drugs = {"paracetamol","aspirin","omeprazole"}
# diseases ={"headache","thrombosis","ulcers"}
# drugs.remove("aspirin")
# diseases.discard("ulcers")
# print(drugs)
# print(diseases)

# patient = {"name":"Jane","age":45,"gender":"female"}
# patient["weight"]=45
# print(len(patient))
# print(f"Her name is {patient["name"]}")

# meds_a = {"Metformin", "Lisinopril", "Aspirin"}
# meds_b = {"Lisinopril", "Atorvastatin", "Aspirin"}
# print(meds_a & meds_b)

# drug_db = {
#     "Amoxicillin": {"max_dose_mg": 3000},
#     "Metformin":   {"max_dose_mg": 2550},
# }
# for dru,dose  in drug_db.items():
#     print(dru,dose["max_dose_mg"])
# key = list(drug_db.keys())
# print(key)
# value = list(drug_db.values())
# print(value)
# for value in drug_db.values():
#     print(value)
# for key in drug_db.keys():
#     print(key)
# meds = {"Metformin", "Lisinopril", "Metformin", "Aspirin"}
# print(len(meds))

#======= FUNCTION-------------
# def song_list(artist, name):
#     artist = artist.capitalize()
#     name = name.capitalize()
#     print(artist + " " + "is very good"+" " +"artist"+" "+ "he made the song" + " "+ name)
# song_list("MJ","bad")
# song_list("Jason","give it")

# def total_dose(dose, frequency):
#     add = dose * frequency
#     print(f"the total dose is {add}")
#     return add

# print(total_dose(30,3))
# print(total_dose(500,2))

#---------DICTIONARY---------
# capital ={
#     "Tanzania": "Dodoma",
#     "china":"beijing",
#     "korea":"seoul"
# }

# #----retrieve one capital
# for value in capital.values():
#     print(value)

# print(capital["Tanzania"])
# capital["korea"]="busan"
# capital["denmark"]="copenhagen"
# del capital["china"]
# for x,y in capital.items():
#     print(f" the capitals \n {x}:{y}")

#--------DICTIONARY 2---------
students = {
    "student 1" : {"name":"chris", "age": 12, "grade": 6},
    "student 2" : {"name":"jack", "age": 13, "grade": 6},
    "student 3" : {"name":"jill", "age": 14, "grade": 7}
}
teachers = {
    "teacher 1" : {"name":"rick", "age": 34, "grade": 6},
    "teacher 2" : {"name":"hailey", "age": 23, "grade": 6},
    "teacher 3" : {"name":"caleb", "age": 44, "grade": 7}
}
teachers.update(students)
print(students["student 1"]["grade"])
students["student 2"]["grade"]= 8
print(teachers)

best_student = max(students, key=lambda x: x["average"])
    print(f"The best student is {best_student['name']} with an average score of {best_student['average']}")
