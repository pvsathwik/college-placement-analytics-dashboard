import random
import pandas as pd

# -----------------------------
# Basic Data
# -----------------------------

branches = ["CSE", "ISE", "ECE", "EEE", "ME", "CIVIL"]

skills_list = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "JavaScript",
    "React",
    "Machine Learning",
    "Data Analysis",
    "AWS",
    "AutoCAD",
    "Excel"
]

companies = {
    "TCS": (4.0, 8.0),
    "Infosys": (4.0, 9.0),
    "Wipro": (4.0, 8.0),
    "Accenture": (5.0, 10.0),
    "Cognizant": (4.5, 9.0),
    "Capgemini": (4.0, 8.0),
    "Deloitte": (6.0, 14.0),
    "IBM": (5.0, 12.0),
    "Tech Mahindra": (4.0, 8.0),
    "Amazon": (10.0, 25.0),
    "Microsoft": (15.0, 35.0),
    "Oracle": (8.0, 18.0),
    "Google": (15.0, 35.0),
    "Bosch": (5.0, 12.0),
    "L&T": (4.0, 9.0)
}

years = [2022, 2023, 2024, 2025, 2026]

# -----------------------------
# Generate Student Data
# -----------------------------

students = []

for i in range(1, 1501):

    student_id = f"STU{i:04d}"
    student_name = f"Student {i:04d}"

    branch = random.choice(branches)

    # Generate CGPA between 5.5 and 10
    cgpa = round(random.uniform(5.5, 10.0), 2)

    # Select 1-4 skills
    num_skills = random.randint(1, 4)
    skills = random.sample(skills_list, num_skills)
    skills_string = ", ".join(skills)

    year = random.choice(years)

    # Higher CGPA = slightly higher chance of placement
    placement_probability = 0.35 + ((cgpa - 5.5) / 4.5) * 0.55

    is_placed = random.random() < placement_probability

    if is_placed:

        company = random.choice(list(companies.keys()))

        min_salary, max_salary = companies[company]

        # Slightly influence salary using CGPA
        salary = random.uniform(min_salary, max_salary)

        salary += (cgpa - 7.0) * 0.25

        salary = max(min_salary, salary)
        salary = round(salary, 2)

        status = "Placed"

    else:

        company = "Not Placed"
        salary = 0
        status = "Not Placed"

    students.append([
        student_id,
        student_name,
        branch,
        cgpa,
        skills_string,
        company,
        salary,
        status,
        year
    ])

# -----------------------------
# Create DataFrame
# -----------------------------

columns = [
    "Student_ID",
    "Student_Name",
    "Branch",
    "CGPA",
    "Skills",
    "Company",
    "Salary_LPA",
    "Placement_Status",
    "Year"
]

df = pd.DataFrame(students, columns=columns)

# -----------------------------
# Save CSV
# -----------------------------

df.to_csv("placement_data.csv", index=False)

print("======================================")
print(" COLLEGE PLACEMENT DATA GENERATED")
print("======================================")

print(f"Total Students : {len(df)}")
print(f"Placed Students: {(df['Placement_Status'] == 'Placed').sum()}")
print(f"Not Placed     : {(df['Placement_Status'] == 'Not Placed').sum()}")

placement_rate = (
    (df["Placement_Status"] == "Placed").mean() * 100
)

print(f"Placement Rate : {placement_rate:.2f}%")

print("\nDataset saved as:")
print("placement_data.csv")