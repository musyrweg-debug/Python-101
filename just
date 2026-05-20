# Step 1: Create the drug database with 4 drugs
drug_db = {
    "Amoxicillin":  {"class": "Antibiotic",    "max_dose_mg": 3000, "unit": "mg"},
    "Metformin":    {"class": "Antidiabetic",  "max_dose_mg": 2550, "unit": "mg"},
    "Lisinopril":   {"class": "ACE Inhibitor", "max_dose_mg": 40,   "unit": "mg"},
    "Atorvastatin": {"class": "Statin",        "max_dose_mg": 80,   "unit": "mg"},
}

def print_database(db):
    """Print all drugs and their maximum doses."""
    for drug, info in db.items():
        print(f"{drug:<12} | Class: {info['class']:<14} | Max dose: {info['max_dose_mg']} {info['unit']}")

print_database("Metformin")
# Step 2: Lookup function
# def lookup_drug(name):
#     """Return drug details or a not-found message."""
#     return drug_db.get(name, f"{name} not found in database.")

# # Print initial database
# print("=== Drug Database ===")
# print_database(drug_db)

# # Test the lookup function
# print("\nLooking up Metformin...")
# print(lookup_drug("Metformin"))

# print("\nLooking up Warfarin...")
# print(lookup_drug("Warfarin"))

# # Step 3: Add a new drug
# drug_db["Omeprazole"] = {"class": "PPI", "max_dose_mg": 40, "unit": "mg"}
# print("\nAfter adding Omeprazole:")
# print_database(drug_db)

# # Step 4: Update max dose for an existing drug
# drug_db["Lisinopril"]["max_dose_mg"] = 80
# print(f"\nAfter updating Lisinopril max dose to 80 mg:")
# print(f"Lisinopril max dose is now {drug_db['Lisinopril']['max_dose_mg']} mg")
