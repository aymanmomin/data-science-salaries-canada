# Data Science Salary Analysis - Methodology
## Analyzing Salary Trends Across Canadian Provinces (2025)

![Data Science Salaries Visualization](../output/canada_data_science_salaries_2025.png)

---

## 1. Data

**Dataset Description:** 
This visualization uses current (2025) wage data for Data Scientists, Database Analysts, and Machine Learning Engineers across Canadian provinces. The data includes low, median, and high hourly wages, converted to annual salaries for easier interpretation by students planning their co-op applications and career paths.

**Data Sources:**
- **Primary Sources:** 
  - Government of Canada - Job Bank (NOC 21211: Data Scientists, NOC 21223: Database Analysts)
  - LinkedIn Salary Insights (Canada 2025)
  - Glassdoor Canada Salary Reports
- **Data Updated:** November 2025 - January 2026
- **Data Accessed:** January 2026
- **License:** Open Government Licence - Canada (Job Bank data)

This represents actual labour market information for data science roles across Canada, combining official government data with industry salary reports to provide a comprehensive view of the market. Data Science roles typically command 10-20% premium over software engineering due to specialized ML/AI skills.

---

## 2. Tools

**Tool(s) and Approach:**
- **Programming Language:** Python 3.13
- **Libraries:**
  - `matplotlib` - for creating both bar charts and range visualizations
  - `numpy` - for data array manipulation and calculations
- **Development Environment:** VS Code with virtual environment
- **Visualization Type:** Compound visualization with two charts:
  - Top: Bar chart for median salary comparison across provinces
  - Bottom: Range plot showing complete salary spectrum (junior to senior roles)

**Why this approach:**
Python with matplotlib was chosen because:
- Ideal for quantitative salary data comparison and analysis
- Supports multi-panel visualizations showing different perspectives
- Allows custom color coding to highlight key provinces
- Easy data transformation (hourly wages → annual salaries)
- Reproducible - can update when new salary data releases
- Demonstrates practical data science and visualization skills
- Python is the primary tool for data science work

---

## 3. Encodings

**How to read the visualization:**

### Top Chart (Bar Chart):
- **X-axis (Horizontal):** Canadian provinces (abbreviated: AB=Alberta, BC=British Columbia, etc.)
- **Y-axis (Vertical):** Annual median salary in thousands of CAD
- **Bar Height:** Represents the median salary for data scientists in that province
- **Bar Color:** 
  - **Red (#E74C3C):** Alberta - strong energy+tech data science market
  - **Blue (#3498DB):** British Columbia - highest median salary, Vancouver tech hub
  - **Grey (#95A5A6):** All other provinces
  - **Grey (#95A5A6):** All other provinces
- **Text on bars:** Exact salary values in thousands (e.g., "$141k" = $141,000/year)

### Bottom Chart (Range Plot):
- **X-axis:** Same provinces as top chart
- **Y-axis:** Annual salary range in thousands of CAD
- **Vertical thick lines:** Show the complete salary range from junior analyst (bottom) to senior ML engineer (top)
- **Dots on lines:** Mark the median salary position within each province's range
- **Line color & thickness:** Same color scheme as top chart; thicker and brighter for AB and BC to emphasize key provinces
- **Annotations with arrows:** Text boxes with arrows highlight key insights for Alberta and BC

**Reading example:** Looking at Alberta (AB): the bottom of the red line starts at ~$79k (junior/entry-level positions), the dot marks $114k (median for typical data scientist), and the top reaches $229k (senior ML engineers, principal data scientists). This shows your complete career earning potential if you stay in Alberta.

---

## 4. Goal/Value

**What the visualization reveals:**

This visualization transforms raw wage data into actionable career intelligence for data science students:

1. **Geographic Salary Landscape:** BC's median ($141k) is 25% higher than Alberta ($114k) and 50% higher than Manitoba ($94k). Geography significantly impacts earning potential - knowing this helps prioritize where to apply for co-ops.

2. **Alberta's Competitive Position:** Despite being away from major tech hubs, Alberta offers $114k median - competitive due to strong energy, finance, and growing tech sectors. Calgary is emerging as an ML/AI hub, especially for energy applications.

3. **Career Growth Trajectory:** The range chart shows you could grow from $79k (junior) to $229k (senior) in Alberta - nearly 3x salary growth potential over your career. BC's range is even wider ($83k to $239k).

4. **BC Premium vs Cost of Living:** BC offers highest median ($141k) but Vancouver's cost of living is 40% higher than Calgary. The $27k salary difference might not translate to better quality of life - important for post-grad planning.

5. **Data Science Premium:** Comparing to software engineering salaries (previous dataset I considered), data scientists earn 10-20% more in tech hubs. In AB: Data Science $114k vs Software $108k - the ML/statistics specialization pays off!

6. **Entry-Level Optimism:** Even "junior" positions in major provinces start at $79-83k - well above Canada's median household income and competitive with mid-career salaries in many other fields.

7. **Ontario's AI Corridor:** Ontario's $129k median reflects Toronto's status as Canada's AI hub (Vector Institute, major tech companies). Strong option if you want cutting-edge ML work.

**Why this matters for me specifically:**

- **Immediate Co-op Strategy:** I should focus applications on:
  - **Alberta companies** (local advantage, no relocation, strong energy data sector)
**Why this matters for students:**

- **Co-op Application Strategy:** Focus applications on Alberta (local advantage, strong energy+tech data sector), BC (highest pay), and Ontario (AI corridor)
- **Skill Development:** The salary premium suggests ML/AI specialization pays significantly more - prioritize learning TensorFlow, PyTorch, deep learning
- **Salary Negotiation:** Understanding the $79-229k range helps set realistic co-op expectations ($25-55/hour depending on role and experience)
- **Financial Planning:** Know that entry-level positions start at $79-83k - you can plan relocation budgets confidently
- **Geographic Decisions:** Alberta's $114k median + lower cost of living may offer better quality of life than BC's $141k + high housing costs
- **Long-term Planning:** $229k ceiling in Alberta shows you don't need to move to Toronto/Vancouver to maximize earnings

---

## 5. Technical Implementation

### Data Processing Pipeline

1. **Data Collection:** Aggregated wage data from Job Bank, LinkedIn, and Glassdoor
2. **Data Transformation:** Converted hourly wages to annual salaries (hourly × 2,080 hours/year)
3. **Data Validation:** Cross-referenced across multiple sources to ensure accuracy
4. **Visualization Creation:** Python script generates dual-panel matplotlib visualization

### Key Design Decisions

**Dual-chart approach:**
- Top panel (bar chart): Quick median comparison for decision-making
- Bottom panel (range plot): Complete picture showing career growth potential

**Color strategy:**
- Red: Alberta (strong energy+tech data science market)
- Blue: British Columbia (highest median salary, Vancouver tech hub)
- Grey: Other provinces (visible but de-emphasized)

**Annotation strategy:**
- Arrow callouts highlight key insights for Alberta and BC
- Direct value labels on bars for quick reading
- Clear axis labels and title

### Reproducibility

The analysis is fully reproducible:
```python
# Run the visualization script
python src/salary_analysis.py
```

The script generates the visualization as a PNG file in the `output/` directory.

---

## 6. Key Insights

### Market Dynamics

1. **BC's tech hub premium:** Vancouver's established tech ecosystem drives 24% higher median than Alberta
2. **Alberta's competitive position:** Strong energy sector creates robust data science market at $114k median
3. **Data science premium:** Roles command 10-20% higher pay vs software engineering due to specialized ML/AI skills
4. **Entry-level strength:** Even junior positions start at $79-83k, well above national median income
5. **Wide salary ranges:** BC and Alberta show ranges from ~$80k (junior) to ~$230k+ (senior), indicating diverse role types and career progression

### Geographic Considerations

- **Cost of Living:** Higher salaries in BC/Ontario may be offset by significantly higher housing and living costs
- **Industry Specialization:** Alberta's energy sector offers unique opportunities for domain specialization in industrial analytics
- **AI Corridors:** Ontario (Toronto/Vector Institute) and Quebec (Montreal/MILA) represent cutting-edge AI research opportunities

---

## 7. Data Limitations & Future Enhancements

### Current Limitations

- **Role Definition:** "Data Scientist" encompasses broad range from analysts to ML engineers
- **Sample Size:** Government data for this emerging field category is still developing
- **Industry Variation:** Aggregated data doesn't separate finance vs tech vs energy sector salaries
- **Experience Levels:** Ranges mix entry-level through principal/staff positions

### Potential Enhancements

- Add cost-of-living adjustment to show real purchasing power
- Include job posting volume data (salary × opportunity = actual value)
- Break down by specialization (ML engineer vs data analyst vs BI developer)
- Add time series view showing salary growth trends
- Include correlation with specific skills (Python, deep learning, cloud platforms)
- Interactive filtering by experience level, industry, and city

---

## References

1. Government of Canada. (2025). *Labour Market Information - Data Scientists*. Job Bank. NOC 21211/21223. Retrieved January 2026, from https://www.jobbank.gc.ca/

2. LinkedIn. (2025). *Salary Insights: Data Scientist Salaries in Canada*. LinkedIn Economic Graph.

3. Glassdoor Canada. (2025). *Data Scientist Salaries by Location*. Glassdoor Salary Database.

4. Dataset License: Open Government Licence - Canada. https://open.canada.ca/en/open-government-licence-canada

---

*Analysis by: Ayman*  
*Date: January 2026*  
*Tools: Python 3.13, matplotlib, numpy*
