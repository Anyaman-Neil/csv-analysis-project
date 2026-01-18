📊 CSV Analysis Project – Student Performance Insights

A Python-based project that cleans educational data, engineers new features, groups students by ethnic group and weekly study hours, computes performance metrics, and visualizes descriptive patterns using bar charts and a pie chart.

1. 🎯 Project Purpose

   1. Work with a real-world educational dataset
   2. Practice data cleaning and feature engineering
   3. Explore how study hours relate to academic performance (descriptively)
   4. Visualize patterns using clear statistical graphics

2. 🛠 What the Script Does

   1. Removes rows with missing or invalid values
   2. Computes per-student:

      * Total Score
      * Average Score
      * Highest and Lowest Subject Scores
   3. Groups students by:

      * Ethnic Group (A–E)
      * Weekly Study Hours (<5, 5–10, >10)
   4. Computes group-wise average scores
   5. Exports enriched data to CSV 
   6. Generates 5 visualizations:

      1. Students by study hours
      2. Average score by study hours
      3. Average score by ethnic group × study hours
      4. Ethnic group distribution (pie chart)
      5. Students by study hours for each ethnic group

3. 📈 Visualizations Included

   1. Bar charts for comparisons
   2. Pie chart for group proportions
   3. Consistent color scheme:

      * "<5" → Blue
      * "5–10" → Orange
      * ">10" → Green
   4. Legends include student counts
   5. All figures are displayed together at the end of script execution

4. 🔍 Key Observations (From Graphs)

   1. Students studying more than 10 hours per week generally show the highest average scores.
   2. The 5–10 hour group shows moderate and stable performance.
   3. Students studying less than 5 hours consistently show the lowest averages.
   4. This pattern appears across all ethnic groups.
   5. Most students fall into the 5–10 hour study category.
   6. Differences between ethnic groups exist, but the effect of study hours is more consistent than ethnic-group differences.
   7. Each ethnic group follows a similar internal pattern:

      * "<5" → lowest
      * "5–10" → middle
      * ">10" → highest

   These are descriptive patterns only. No causal or statistically significant claims are made.

5. ⚠️ Limitations

   1. No inferential statistical tests were performed
   2. No causal relationship is claimed
   3. Other variables (family background, test prep, etc.) were not controlled
   4. Results depend on the dataset after cleaning

6. ▶️ How to Run

   1. Clone the repository

   2. Run:

      python Csv_analysis_project.py

   3. Output:

      * Enriched CSV: New_Data_1.csv
      * 5 figures displayed together

7. 📁 Tools & Libraries

   1. Python 3
   2. Libraries:

      * csv
      * collections
      * matplotlib

8. 📌 Future Scope

   1. Save figures as PNG for README
   2. Add inferential tests (correlation, ANOVA)
   3. Extend analysis using regression models
