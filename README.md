# Data Analytics Project: AI Job Market Insights

## Overview

This project explores a dataset containing insights into the AI job market. The objective is to analyze trends, salary distributions, skills in demand, and the impact of factors like industry, job title, and AI adoption levels on salaries and growth projections. The findings aim to guide stakeholders in making data-driven decisions.

The "AI-Powered Job Market Insights" dataset provides a synthetic but realistic snapshot of the modern job market, particularly focusing on the role of artificial intelligence (AI) and automation across various industries. This dataset includes 500 unique job listings, each characterized by different factors like industry, company size, AI adoption level, automation risk, required skills, and job growth projections. It is designed to be a valuable resource for researchers, data scientists, and policymakers exploring the impact of AI on employment, job market trends, and the future of work.

---

## Dataset

The dataset includes the following key columns:

- **Industry**: The industry where the job is categorized.
- **Job\_Title**: The title of the job position.
- **Salary\_USD**: The salary offered (in USD).
- **AI\_Adoption\_Level**: The extent of AI adoption in the company (Low, Medium, High).
- **Remote\_Friendly**: Indicates whether the job supports remote work.
- **Job\_Growth\_Projection**: The expected growth projection of the job (Growth, Decline, Stable).
- **Automation\_Risk**: The level of risk of automation for the job (Low, Medium, High).
- **Location**: Geographical location of the job.
- **Required\_Skills**: Skills necessary for the job role.

---

## Features and Objectives

### 1. **Data Exploration**

- Understand data structure and clean missing or inconsistent entries.
- Perform descriptive statistics to summarize key trends.

### 2. **Visualizations**

- Distribution and relationships between salary, industry, job title, and other attributes.
  - **Salary Distribution by Industry**: Analyze variations in salary across different industries.
  - **Salary by Job Title**: Insights into compensation trends for various roles.
  - **Impact of AI Adoption**: Study how AI adoption influences salaries.
  - **Remote-Friendly Jobs**: Examine the salary impact of remote work flexibility.
  - **Job Growth by Location**: Explore trends in job growth across geographical locations.

### 3. **Correlation Analysis**

- Explore relationships between:
  - Salary, AI adoption levels, and automation risk.
  - Job growth projections and required skills.

### 4. **Insights**

- Highlight key patterns in salary trends and growth opportunities.
- Identify the most in-demand skills for high-growth jobs.

---

## Tools and Libraries

- **Python**: Core programming language for analysis.
- **Pandas**: Data manipulation and analysis.
- **Seaborn**: Advanced visualization.
- **Matplotlib**: Plot customization and rendering.
- **Power BI**: Interactive dashboards and advanced visualizations.

---

## Code Snippets

### Salary Distribution by Industry

```python
plt.figure(figsize=(20, 10))
sns.boxplot(data=df, x='Industry', y='Salary_USD', palette='muted')
plt.xticks(rotation=45)
plt.title("Salary Distribution by Industry")
plt.xlabel("Industry")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.show()
```

### Correlation Analysis

```python
encoded_data = df.copy()
encoded_data['AI_Adoption_Level'] = encoded_data['AI_Adoption_Level'].map({'Low': 1, 'Medium': 2, 'High': 3})
encoded_data['Automation_Risk'] = encoded_data['Automation_Risk'].map({'Low': 1, 'Medium': 2, 'High': 3})

correlation_matrix = encoded_data[['Salary_USD', 'AI_Adoption_Level', 'Automation_Risk']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Salary, AI Adoption, and Automation Risk")
plt.tight_layout()
plt.show()
```

---

## Power BI Dashboard

### Overview
The Power BI dashboard complements the Python analysis with interactive visualizations and a user-friendly interface to explore the dataset. It includes the following components:

### Key Visualizations
1. **Salary Distribution by Industry**:
   - Interactive boxplots displaying salary ranges across various industries.
   - Filters to narrow down by AI adoption levels or job titles.

2. **AI Adoption and Salary Trends**:
   - Line charts showing the impact of AI adoption on salary distributions.

3. **Job Growth Projections by Location**:
   - Geographical heatmaps highlighting regions with high-growth opportunities.

4. **Skill Demand Analysis**:
   - Bar charts visualizing the most in-demand skills for AI jobs.

5. **Automation Risk**:
   - Risk analysis of job roles with respect to automation.

### Insights from Power BI
- **Industry Insights**: Technology and Healthcare consistently offer higher median salaries.
- **AI Adoption Levels**: High AI adoption correlates with better compensation packages.
- **Regional Trends**: Urban centers show a higher concentration of high-growth jobs.
- **Remote Work**: Jobs with remote flexibility are increasingly popular in certain industries.

---

## Insights and Recommendations

- **Salary Trends**: Industries like Technology and Manufacturing offer higher salaries, while Retail and Education lag behind.
- **High-Growth Skills**: Skills like Machine Learning, Data Analysis, and Cloud Computing are most in demand for high-growth jobs.
- **AI Adoption Impact**: Companies with high AI adoption levels offer significantly higher salaries.
- **Remote Work**: Remote-friendly jobs tend to have slightly higher salary medians.

---

## License

This project is open-source and can be used under the [MIT License](https://opensource.org/licenses/MIT).

