# Data Science Salary Visualizations - Canada 2025

A data visualization project analyzing salary trends across Canadian provinces for data science roles, helping students make informed co-op and career decisions.

---

## 📊 Visualization Projects

### 1. Data Science Salaries Across Canada (2025)

![Data Science Salaries](output/canada_data_science_salaries_2025.png)

**Key Question:** Where should data science students apply for co-op and entry-level positions to maximize salary potential?

**Key Findings:**
- 🥇 **BC leads** at $141k median salary (Vancouver tech hub)
- 🥈 **Ontario follows** at $129k (Toronto AI corridor - Vector Institute)
- 🥉 **Alberta competitive** at $114k (strong energy + tech data science market)
- 💰 **Entry to senior range:** $79k - $239k across Canada
- 📈 **Data science premium:** 10-20% higher pay vs software engineering

**What makes this useful for students:**
- Current 2025 data from Job Bank Canada, LinkedIn, and Glassdoor
- Compares median salaries AND complete salary ranges (entry-level to senior)
- Helps students set realistic salary expectations for co-op and negotiations
- Factors in cost of living considerations for relocation decisions
- Identifies geographic trade-offs for career planning

**📂 Full Documentation:** [View Detailed Methodology](docs/methodology.md)

---

## � Features

### 📊 Interactive Dashboard
- **Live filtering** by province and salary type
- **Cost-of-living adjustments** for accurate purchasing power comparison
- **Real-time visualizations** with matplotlib integration
- **Sortable data tables** with gradient highlighting
- **Student-focused insights** and recommendations

### 📓 Jupyter Notebook Analysis
- **Step-by-step data exploration** with explanations
- **Statistical analysis** and key metrics
- **Multiple visualizations** comparing different perspectives
- **Exportable results** for further analysis

### 📈 Static Visualizations
- Original dual-panel salary comparison
- Cost-of-living adjusted comparisons  
- Career growth potential analysis

---

## �🛠️ Technologies Used

- **Python 3.13** - Primary programming language
- **matplotlib & seaborn** - Data visualization libraries
- **pandas & numpy** - Data manipulation and analysis
- **Streamlit** - Interactive web dashboard
- **Jupyter** - Data exploration notebooks

---

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.13 or higher
python --version

# pip package manager
pip --version
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/aymanmomin/data-science-salaries-canada.git
cd data-science-salaries-canada
```

2. Create and activate virtual environment (recommended):
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project

**🎯 Option 1: Interactive Dashboard (Recommended)**
```bash
# Launch the Streamlit dashboard
streamlit run app.py
```
Open your browser to `http://localhost:8501` to explore the interactive dashboard.

**📓 Option 2: Jupyter Notebook Analysis**
```bash
# Launch Jupyter
jupyter notebook

# Open notebooks/data_exploration.ipynb
```

**Option 3: Generate Static Visualization**

```bash
# Run the visualization script
python src/salary_analysis.py
```

The visualization will be generated as a PNG image in the same directory.

---

## 📁 Project Structure

```
.
├── src/
│   └── salary_analysis.py                    # Python analysis script
├── notebooks/
│   └── data_exploration.ipynb                # Interactive data exploration
├── data/
│   └── salary_data.csv                       # Raw salary data
├── output/
│   ├── canada_data_science_salaries_2025.png # Original visualization
│   ├── salary_comparison_adjusted.png        # CoL-adjusted comparison
│   └── career_growth_analysis.png            # Growth potential chart
├── docs/
│   ├── index.md                              # GitHub Pages site
│   ├── methodology.md                        # Detailed methodology
│   └── _config.yml                           # Jekyll configuration
├── app.py                                    # Streamlit dashboard
├── requirements.txt                          # Python dependencies
├── .venv/                                    # Virtual environment (not in repo)
├── .gitignore                                # Git ignore rules
└── README.md                                 # This file
```

---

## 📈 Data Sources

All visualizations use credible, up-to-date sources:

- **Government of Canada Job Bank** - Official labour market wage data
- **LinkedIn Salary Insights** - Industry compensation trends
- **Glassdoor Canada** - Company-reported salary information

Data accessed: November 2025 - January 2026  
License: Open Government Licence - Canada (for Job Bank data)

---

## 🎯 Skills Demonstrated

- **Data Analysis:** Processing salary data from multiple sources with cost-of-living adjustments
- **Python Programming:** Clean, efficient, well-documented code
- **Data Visualization:** Multiple chart types (bar charts, range plots, adjusted comparisons)
- **Web Development:** Interactive Streamlit dashboard deployment
- **Statistical Analysis:** Comparative analysis and purchasing power calculations
- **Communication:** Translating data insights into actionable career advice

---

## 📝 License

This project is open source and available for educational and portfolio purposes.

Data sources maintain their original licenses (Open Government Licence - Canada for government data).

---

## 👤 Author

Created by Ayman - Data Science Portfolio Project

Demonstrating practical data analysis and visualization skills for real-world career planning.

---

## 🌐 Deployment Options

### Run Locally (Quick Start)
```bash
# After installing dependencies
streamlit run app.py
# Open http://localhost:8501
```

### Deploy to Streamlit Cloud (Free)
1. Push this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository and `app.py` as the main file
5. Click "Deploy"!
6. Get a free public URL to share on your resume

### View Documentation
**GitHub Pages:** [View Project Documentation →](https://aymanmomin.github.io/data-science-salaries-canada/)

---

*This is an independent project using publicly available data to demonstrate data science and Python visualization skills.*
