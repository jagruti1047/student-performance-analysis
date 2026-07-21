import pandas as pd 
df = pd.read_csv("student-mat.csv",sep=";")
print("Are there any missing values?", df.isnull().values.any())
duplicates = df.duplicated().sum()
print("Number of duplicate rows before removal:", duplicates)
print("Dataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
average_grade = df ['G3'].mean()
print("average final grade:",average_grade)
count = (df['G3']>15).sum()
print("no. of students scored above 15:",count)
correlation = df["studytime"].corr(df["G3"])
print("Is study time correlated with performance?",correlation)
if correlation>0 :
 print("Students who study more tend to score higher (positive correlation)")
elif correlation<0:
 print("Students who study more tend to score lower (negative correlation).")
else: 
 print("There is little or no relationship")
gender_performance=df.groupby("sex")["G3"].mean()
print(gender_performance)
F=gender_performance["F"]
M=gender_performance["M"]
if F>M:
 print("Females perform better")
else:
 print(" Males perform better")
 import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
plt.hist(df["G3"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df["studytime"], df["G3"], color="green")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.show()
gender_avg = df.groupby("sex")["G3"].mean()

plt.figure(figsize=(5,4))
plt.bar(gender_avg.index, gender_avg.values, color=["pink", "lightblue"])
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.show()