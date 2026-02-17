# Personal Visualization - Week 2
## Data Scientist Salaries Across Canada: Where Should Data Science Students Apply? (2025)

![Data Science Salaries Visualization](data_science_salaries_canada_2025.png)

---

## 1. Data

**What the data is:** 
This visualization uses current (2025) wage data for Data Scientists, Database Analysts, and Machine Learning Engineers across Canadian provinces. The data includes low, median, and high hourly wages, which I've converted to annual salaries for easier interpretation by students planning their co-op applications.

**Where it came from:**
- **Primary Sources:** 
  - Government of Canada - Job Bank (NOC 21211: Data Scientists, NOC 21223: Database Analysts)
  - LinkedIn Salary Insights (Canada 2025)
  - Glassdoor Canada Salary Reports
- **Data Updated:** November 2025 - January 2026
- **Data Accessed:** January 19, 2026
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
I chose Python with matplotlib because:
- Perfect for quantitative salary data comparison and analysis
- Can create multi-panel visualizations showing different perspectives
- Allows custom color coding to highlight key provinces (Alberta, BC)
- Easy data transformation (hourly wages → annual salaries)
- Reproducible - can update when new salary data releases
- Demonstrates practical data science and visualization skills needed for co-op positions
- Python is the #1 tool for data science roles - practicing what I'll use on the job

---

## 3. Encodings

**How to read the visualization:**

### Top Chart (Bar Chart):
- **X-axis (Horizontal):** Canadian provinces (abbreviated: AB=Alberta, BC=British Columbia, etc.)
- **Y-axis (Vertical):** Annual median salary in thousands of CAD
- **Bar Height:** Represents the median salary for data scientists in that province
- **Bar Color:** 
  - **Red (#E74C3C):** Alberta - my current province, strong energy+tech data science market
  - **Blue (#3498DB):** British Columbia - highest median salary, Vancouver tech hub
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
  - **BC tech companies** (highest pay, but factor in cost of living)
  - **Ontario AI firms** (second highest, Toronto AI corridor)

- **Skill Development Priority:** The $141k BC salary suggests ML/AI specialization pays significantly more than general analysis. I should deepen my ML skills (TensorFlow, PyTorch, deep learning).

- **Industry Targeting:** Alberta's strength in energy sector data science means I can combine local advantage with industry specialization. Oil & gas companies need ML for predictive maintenance, exploration analytics.

- **Financial Planning:** Understanding $79-83k entry range helps me:
  - Set realistic co-op salary expectations ($25-40/hour)
  - Negotiate confidently with data-backed benchmarks
  - Plan budgets if I need to relocate for co-op

- **Stay vs Relocate Decision:** Alberta's $114k median + lower cost of living might offer better quality of life than BC's $141k + high housing costs. This changes my post-graduation planning.

- **Long-term Career View:** Seeing $229k ceiling in Alberta validates staying here long-term. I don't need to move to Toronto/Vancouver to maximize earnings - can build great career in Calgary.

---

## 5. Reflection

**What I learned while creating it:**

### Technical Learning:
1. **Multi-source data integration:** First time combining government data (Job Bank) with industry sources (LinkedIn, Glassdoor) to create more complete picture. Learned to triangulate when official data is limited.

2. **Data validation:** Realized I need to verify salary data across multiple sources since ranges can vary significantly. Cross-referenced three sources to ensure accuracy.

3. **Advanced matplotlib customization:** Built on previous visualization experience - added arrow annotations (`arrowprops`), improved label placement, refined color hierarchy for emphasis.

4. **Salary data interpretation:** Learned that "Data Scientist" is broad category - includes junior analysts ($79k) to senior ML engineers ($229k). Need to segment by experience level for accurate comparison.

5. **Industry research:** Discovered Job Bank uses NOC codes (21211, 21223) - useful system for searching government labour statistics and immigration pathways.

### Domain Learning:
1. **Data Science market dynamics:** Shocked that data scientists earn 10-20% more than software engineers in tech hubs. The ML/statistics specialization commands premium - validates my interest in this field!

2. **Alberta's data scene:** Didn't realize Calgary has emerging ML scene focused on energy applications. Companies like Suncor, Cenovus, and tech startups doing predictive analytics for oil & gas.

3. **Geographic arbitrage:** BC's $141k sounds great until you factor in $2,500+/month rent in Vancouver vs $1,400 in Calgary. Real purchasing power might be similar - life planning insight!

4. **Entry-level reality check:** Junior data science roles ($79-83k) are still ~$15k higher than entry software roles. But they also typically require more education (Master's preferred) or specialized skills.

5. **Industry variations:** Data science in finance/tech pays more than energy, but Alberta's energy sector is stable and has unique problems (geological data, predictive maintenance) that are interesting.

### Career Planning Breakthroughs:
1. **Co-op targeting shift:** Before this, I was randomly applying everywhere. Now I have clear strategy: 
   - Primary: Calgary/Edmonton companies (local advantage, competitive pay)
   - Secondary: Vancouver tech firms (highest pay)
   - Tertiary: Toronto AI companies (cutting-edge work)

2. **Skill prioritization:** The salary premium for ML skills ($141k BC vs $94k MB) shows that deep learning, neural networks, and production ML systems are high-value skills. I should focus on these, not just basic Python/SQL.

3. **Negotiation confidence:** When co-op offers come, I now know:
   - Junior data analysts: ~$25-30/hour
   - Data scientists: ~$35-45/hour  
   - ML engineers: ~$40-55/hour
   - Can negotiate based on my skill level with data backing

4. **Long-term location strategy:** Initially thought I'd need to move to Toronto/Vancouver post-grad. Now I see Alberta's $114k + low cost of living might offer better lifestyle. Can stay near family and still have great career.

5. **Industry focus:** Alberta's $114k median in context of strong energy sector = opportunity to specialize in energy analytics. Unique niche that's geographically locked to AB/TX, reducing competition.

### Design & Visualization Learning:
1. **Storytelling with dual charts:** Using both median comparison (bar) AND full range (range plot) tells complete story. Median alone doesn't show growth potential; range alone doesn't show typical outcomes. Together = powerful.

2. **Annotation effectiveness:** Adding arrows and text boxes to highlight AB and BC makes key insights jump out. User doesn't need to decode the visualization - the story is clear.

3. **Color psychology in data viz:** Using red for "my location" (personal connection) and blue for "best option" (aspiration) creates emotional engagement. Grey for others keeps them visible but de-emphasized.

4. **Practical data transformation:** Converting hourly to annual salary makes data more relatable to students. People think in yearly salaries, not hourly rates - small change, big impact on usability.

5. **Visual hierarchy:** Learned that you can guide viewer's attention through: color (AB/BC bright, others muted), size (thicker lines), annotations (arrows to key points), and title (stating main finding).

### Challenges Overcome:
1. **Data availability:** Government data for "Data Scientist" as separate category is limited (relatively new field). Had to combine NOC codes and supplement with industry data - more research than expected.

2. **Defining "Data Scientist":** Role varies hugely - from Excel analysts to PhD-level ML engineers. Had to decide what range represents "typical" data scientist vs outliers.

3. **Balancing completeness and clarity:** Wanted to show all provinces for completeness, but highlighting AB/BC for relevance. Found right balance through color and annotation without hiding other data.

4. **Personal vs general insights:** Struggled with making it relevant to ME (co-op student in AB) while keeping it useful for broader audience. Annotations and reflection section solved this.

### Surprising Discoveries:
1. **BC's massive lead:** Expected BC to be higher, but $141k vs $114k AB (24% difference) is substantial. Vancouver's tech hub status really drives salaries.

2. **Alberta's strong showing:** Thought Alberta would be mid-tier, but $114k median places it 3rd nationally and competitive with Ontario. Energy sector data science is legit!

3. **Entry-level floor is high:** Even "low" end in major provinces ($79-83k) is higher than I expected for fresh graduates. Data science field pays well even at entry level.

4. **Range width varies:** BC and AB have huge ranges ($83k-$239k, $79k-$229k) while smaller provinces have compressed ranges. Suggests more diverse role types and seniority levels in major markets.

5. **Data science premium:** The 10-20% salary advantage over software engineering surprised me. I thought they'd be similar, but the ML specialization really commands higher pay.

### Personal Impact & Next Steps:
This exercise fundamentally changed my co-op application strategy:

**Immediate actions:**
- Update LinkedIn profile to highlight ML/Python skills (high-value skills)
- Target Calgary companies in energy sector (Suncor, Cenovus, Shell, AltaML)
- Also apply to Vancouver tech firms (Amazon, Microsoft, SAP) for highest pay
- Join UofC Data Science Club to network with local companies

**Skill development:**
- Deepen ML knowledge: finish Andrew Ng's course, build portfolio projects
- Learn production ML: MLOps, model deployment, A/B testing
- Focus on Python, SQL, TensorFlow - these are table stakes
- Add specialized domain knowledge: time series (energy), NLP (finance)

**Long-term thinking:**
- Staying in Calgary post-grad is now a serious option (not a compromise)
- Consider energy sector specialization - unique niche with good pay
- Master's degree might be worth it (many senior roles want advanced degree)

**Financial planning:**
- Co-op expectations: aim for $35-40/hour as data science intern
- Post-grad starting salary: realistic target $80-95k in Calgary
- 5-year goal: $120-140k (senior level)
- Understand cost of living matters as much as raw salary

### Future Improvements I'd Make:
- **Add cost-of-living adjustment:** Show "real" purchasing power, not just nominal salary. $141k in Vancouver might = $110k lifestyle.
- **Include job posting volume:** High salary × low opportunities isn't helpful. Add data on # of data science jobs by province.
- **Break down by specialization:** ML engineer vs data analyst vs business intelligence - very different roles and salaries.
- **Add required skills:** Which skills correlate with highest salaries? Python? Deep learning? Cloud platforms?
- **Time series view:** Are data science salaries growing faster than software engineering? Is the premium increasing?
- **Interactive version:** Let users filter by experience level, industry, specific cities within provinces.
- **Industry breakdown:** Finance vs tech vs energy vs healthcare - which industries in which provinces pay best?

### Meta-Learning (About Learning Itself):
1. **Relevant data = higher engagement:** When visualization directly affects MY decisions (where to apply for co-op), I'm way more engaged in creating it. Personal stakes drive quality.

2. **Research depth matters:** Easy to plot surface-level data, but digging deeper (why AB strong? what drives BC premium?) creates richer insights.

3. **Iterate on purpose:** First version focused on showing all data. Second version (this one) focuses on actionable insights for co-op students. Purpose refinement improved quality.

4. **Document while fresh:** Writing this reflection right after creating visualization captures thinking process. Waiting would lose details about decision-making and discoveries.

---

## References

1. Government of Canada. (2025). *Labour Market Information - Data Scientists*. Job Bank. NOC 21211/21223. Retrieved January 19, 2026, from https://www.jobbank.gc.ca/

2. LinkedIn. (2025). *Salary Insights: Data Scientist Salaries in Canada*. LinkedIn Economic Graph.

3. Glassdoor Canada. (2025). *Data Scientist Salaries by Location*. Glassdoor Salary Database.

4. Dataset License: Open Government Licence - Canada. https://open.canada.ca/en/open-government-licence-canada

---

*Created by: Ayman*  
*Date: January 19, 2026*  
*Course: CPSC 582 - University of Calgary*  
*Context: CS student actively seeking data science co-op placement*  
*Personal Interests: Data Science, Machine Learning, Co-op Opportunities, Canadian Job Market, Financial Planning*
