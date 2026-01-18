📊 CSV Analysis Project – Student Performance Insights

A Python-based project that cleans educational data, engineers new features, groups students by ethnic group and weekly study hours, computes performance metrics, and visualizes descriptive patterns using bar charts and pie charts.

🚀 Project Purpose

Work with a real-world educational dataset

Practice data cleaning and feature engineering

Explore how study hours relate to academic performance (descriptively)

Visualize patterns using clear statistical graphics

🛠 What the Script Does

Removes rows with missing or invalid values

Computes per-student:

Total Score

Average Score

Highest and Lowest Subject Scores

Groups students by:

Ethnic Group (A–E)

Weekly Study Hours (<5, 5–10, >10)

Computes group-wise average scores

Exports enriched data to CSV (unchanged logic)

Generates 5 visualizations:

Students by study hours

Average score by study hours

Average score by ethnic group × study hours

Ethnic group distribution (pie chart)

Students by study hours for each ethnic group

📈 Visualizations Included

Bar charts for comparisons

Pie chart for group proportions

Consistent color scheme:

<5 → Blue

5–10 → Orange

>10 → Green

Legends include student counts

All figures display together at the end of script execution.

🔍 Key Observations (From Graphs)

Students studying more than 10 hours per week generally show the highest average scores.

The 5–10 hour group shows moderate and stable performance.

Students studying less than 5 hours consistently show the lowest averages.

This pattern is visible across all ethnic groups, suggesting study time has a strong descriptive association with performance.

Most students fall into the 5–10 hour study category.

Differences between ethnic groups exist, but the effect of study hours is more consistent than ethnic-group differences.

Each ethnic group shows a similar internal pattern:

<5 lowest

5–10 middle

>10 highest

These are descriptive patterns only. No causal or statistically significant claims are made.

⚠️ Limitations

No hypothesis testing or inferential statistics

No causality claimed

Other variables (family background, test prep, etc.) not controlled

Results depend on dataset quality after cleaning

▶️ How to Run
python Csv_analysis_project.py


Generates enriched CSV: New_Data_1.csv

Opens 5 figures together

📁 Tools & Libraries Used

Python 3

Libraries: csv, collections, matplotlib
