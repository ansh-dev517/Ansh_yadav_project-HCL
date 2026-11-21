print("Patient Data Analysis")

'''1. Project introduction
Patient Data Analysis is a simple Python project that analyzes patient information such as age, gender, blood group and department.

The project uses basic Python concepts to calculate the total number of patients, average age, youngest and oldest patient, and department-wise distribution.

It helps beginners understand how Python can be used to organize data and generate useful information'''

'''2. Objectives
1. Store patient information using Python lists.
2. Display patient records.
3. Calculate total patients.
4. Calculate average patient age.
5. Find youngest and oldest patient.
6. Divide patients into age groups.
7. Analyze male and female patients.
8. Count patients in different departments.
9. Analyze blood groups.
10. Generate a final patient report.
3. Sample dataset
We will use the following 10 fictional patient records throughout the project.
Patient ID	Age	Gender	Blood Group	Department
1	25	Male	O+	Medicine
2	45	Female	B+	Cardiology
3	12	Male	A+	Pediatrics
4	60	Female	O+	Orthopedics
5	32	Male	AB+	Medicine
6	8	Female	B+	Pediatrics
7	70	Male	O-	Cardiology
8	22	Female	A+	Dermatology
9	55	Male	B-	Medicine
10	35	Female	O+	Orthopedics'''

print("Question 9: Count patients according to blood group")
print("Question: Write a Python program to count patients having different blood groups.")
blood_group = [
    "O+", "B+", "A+", "O+", "AB+",
    "B+", "O-", "A+", "B-", "O+"
]

o_positive = 0
b_positive = 0
a_positive = 0
ab_positive = 0
o_negative = 0
b_negative = 0

for blood in blood_group:

    if blood == "O+":
        o_positive = o_positive + 1

    elif blood == "B+":
        b_positive = b_positive + 1

    elif blood == "A+":
        a_positive = a_positive + 1

    elif blood == "AB+":
        ab_positive = ab_positive + 1

    elif blood == "O-":
        o_negative = o_negative + 1

    elif blood == "B-":
        b_negative = b_negative + 1

print("O+:", o_positive)
print("B+:", b_positive)
print("A+:", a_positive)
print("AB+:", ab_positive)
print("O-:", o_negative)
print("B-:", b_negative)



print("Display all Patient Detail")
print("Question: Write a Python program to store the ages of " \
"10 patients in a list and display all ages.")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

print("Patient Ages:")

for age in ages:
    print(age)

print("Question 2: Find the total number of patients")
print("Question2: Write a program to calculate the total number of patients.")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

total_patients = len(ages)

print("Total Patients:", total_patients)



print("Question 3: Calculate average patient age")
print("Question: Write a program to calculate the average age of patients.")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

total_age = sum(ages)
total_patients = len(ages)

average_age = total_age / total_patients

print("Average Age:", average_age)

print("Question 4: Find the youngest patient")
print("Question: Write a program to find the youngest patient from the dataset")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

youngest = min(ages)

print("Youngest Patient Age:", youngest)

print("Question 5: Find the oldest patient")
print("Question: Write a program to find the oldest patient.")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

oldest = max(ages)

print("Oldest Patient Age:", oldest)

print("Question 6: Count patients in different age groups")
print("Question: Divide patients into three age groups:")
print("- Children: below 18")
print("- Adults: 18 to 59")
print("- Senior citizens: 60 and above")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

children = 0
adults = 0
senior = 0

for age in ages:

    if age < 18:
        children = children + 1

    elif age < 60:
        adults = adults + 1

    else:
        senior = senior + 1

print("Children:", children)
print("Adults:", adults)
print("Senior Citizens:", senior)

print("Question 7: Count male and female patients")
print("Question: Write a Python program to count male and female patients.")
gender = [
    "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female"
]

male = 0
female = 0

for person in gender:

    if person == "Male":
        male = male + 1

    else:
        female = female + 1

print("Male Patients:", male)
print("Female Patients:", female)


print("Question 8: Count patients department-wise")
print("Question: Write a program to calculate the number of patients in each department.")
department = [
    "Medicine", "Cardiology", "Pediatrics",
    "Orthopedics", "Medicine", "Pediatrics",
    "Cardiology", "Dermatology", "Medicine",
    "Orthopedics"
]

medicine = 0
cardiology = 0
pediatrics = 0
orthopedics = 0
dermatology = 0

for dept in department:

    if dept == "Medicine":
        medicine = medicine + 1

    elif dept == "Cardiology":
        cardiology = cardiology + 1

    elif dept == "Pediatrics":
        pediatrics = pediatrics + 1

    elif dept == "Orthopedics":
        orthopedics = orthopedics + 1

    elif dept == "Dermatology":
        dermatology = dermatology + 1

print("Medicine:", medicine)
print("Cardiology:", cardiology)
print("Pediatrics:", pediatrics)
print("Orthopedics:", orthopedics)
print("Dermatology:", dermatology)

print("Question 10: Generate a complete patient analysis report")
print("Question: Write a Python program to display the total patients,/n")
print(" average age, youngest patient, oldest patient, age group analysis and gender analysis.")
# Patient Data Analysis Project

ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

gender = [
    "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female"
]

# Total patients
total_patients = len(ages)

# Average age
average_age = sum(ages) / total_patients

# Youngest and oldest
youngest = min(ages)
oldest = max(ages)

# Age groups
children = 0
adults = 0
senior = 0

for age in ages:

    if age < 18:
        children = children + 1

    elif age < 60:
        adults = adults + 1

    else:
        senior = senior + 1

# Gender count
male = 0
female = 0

for person in gender:

    if person == "Male":
        male = male + 1

    else:
        female = female + 1

# Final report
print("===== PATIENT DATA ANALYSIS =====")

print("Total Patients:", total_patients)
print("Average Age:", average_age)
print("Youngest Patient:", youngest)
print("Oldest Patient:", oldest)

print("\nAge Group Analysis")
print("Children:", children)
print("Adults:", adults)
print("Senior Citizens:", senior)

print("\nGender Analysis")
print("Male Patients:", male)
print("Female Patients:", female)