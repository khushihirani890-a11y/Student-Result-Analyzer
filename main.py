import pandas as pd

# Load the CSV file
df = pd.read_csv("student_results.csv")

# Calculate Total Marks
df["Total"] = df[["Math", "Science", "English", "History"]].sum(axis=1)

# Calculate Percentage (out of 400)
df["Percentage"] = (df["Total"] / 400) * 100

# Assign Grades
def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(assign_grade)

# Display full results
print("===== Student Results =====")
print(df)

# Class Topper
topper = df.loc[df["Total"].idxmax()]

print("\n===== Class Topper =====")
print(f"Name: {topper['Name']}")
print(f"Total Marks: {topper['Total']}")
print(f"Percentage: {topper['Percentage']:.2f}%")
print(f"Grade: {topper['Grade']}")

# Subject-wise Average
print("\n===== Subject-wise Average =====")
print(df[["Math", "Science", "English", "History"]].mean())

# Class Average
print("\n===== Class Average =====")
print(f"Average Percentage: {df['Percentage'].mean():.2f}%")
