📊 CSV Analysis Project – Student Performance Insights

A Python-based project that cleans educational data, engineers new features, groups students by ethnic group and weekly study hours, computes performance metrics, and visualizes descriptive patterns using bar charts and a pie chart.

1. 🎯 Project Purpose

Work with a real-world educational dataset

Practice data cleaning and feature engineering

Explore how study hours relate to academic performance (descriptively)

Visualize patterns using clear statistical graphics

2. 🛠 What the Script Does

Removes rows with missing or invalid values

Computes per-student:

Total Score

Average Score

Highest and Lowest Subject Scores

Groups students by:

Ethnic Group (A–E)

Weekly Study Hours (<5, 5–10, >10)

Computes group-wise average scores

Exports enriched data to CSV (original logic preserved)

Generates 5 visualizations:

Students by study hours

Average score by study hours

Average score by ethnic group × study hours

Ethnic group distribution (pie chart)

Students by study hours for each ethnic group

3. 📈 Visualizations Included

Bar charts for comparisons

Pie chart for group proportions

Consistent color scheme:

<5 → Blue

5–10 → Orange

>10 → Green

Legends include student counts

All figures display together at the end of script execution

4. 🔍 Key Observations (From Graphs)

Students studying more than 10 hours per week generally show the highest average scores.

The 5–10 hour group shows moderate and stable performance.

Students studying less than 5 hours consistently show the lowest averages.

This pattern appears across all ethnic groups.

Most students fall into the 5–10 hour study category.

Differences between ethnic groups exist, but the effect of study hours is more consistent than ethnic-group differences.

Each ethnic group follows a similar internal pattern:

<5 → lowest

5–10 → middle

>10 → highest

These are descriptive patterns only. No causal or statistically significant claims are made.

5. ⚠️ Limitations

No inferential statistical tests were performed

No causal relationship is claimed

Other variables (family background, test prep, etc.) were not controlled

Results depend on the dataset after cleaning

6. ▶️ How to Run

Clone the repository

Run:

python Csv_analysis_project.py


Output:

Enriched CSV: New_Data_1.csv

5 figures displayed together

7. 📁 Tools & Libraries

Python 3

Libraries:

csv

collections

matplotlib

8. 📌 Future Scope

Save figures as PNG for README

Add inferential tests (correlation, ANOVA)

Extend analysis using regression models
