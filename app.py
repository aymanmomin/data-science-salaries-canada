import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Canada Data Science Salaries",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2C3E50;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #ECF0F1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498DB;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🇨🇦 Data Science Salary Explorer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Interactive analysis for students planning co-op and career decisions</p>', unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/salary_data.csv')
    
    # Calculate adjusted salaries
    df['Adjusted_Median'] = (df['Median_Salary'] / df['Cost_of_Living_Index']) * 100
    df['Adjusted_Low'] = (df['Low_Salary'] / df['Cost_of_Living_Index']) * 100
    df['Adjusted_High'] = (df['High_Salary'] / df['Cost_of_Living_Index']) * 100
    df['Salary_Range'] = df['High_Salary'] - df['Low_Salary']
    df['Growth_Potential'] = ((df['High_Salary'] - df['Low_Salary']) / df['Low_Salary'] * 100).round(1)
    
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("🎯 Filters & Options")
st.sidebar.markdown("---")

# Salary type selector
salary_type = st.sidebar.radio(
    "Salary Type:",
    ["Nominal (Raw)", "Cost-of-Living Adjusted"],
    help="Adjusted salaries account for different living costs across provinces"
)

# Province selector
selected_provinces = st.sidebar.multiselect(
    "Select Provinces:",
    options=df['Province'].tolist(),
    default=df['Province'].tolist(),
    help="Compare specific provinces"
)

# Filter data
filtered_df = df[df['Province'].isin(selected_provinces)]

# Main content
if len(filtered_df) == 0:
    st.warning("⚠️ Please select at least one province to display data.")
else:
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    salary_col = 'Median_Salary' if salary_type == "Nominal (Raw)" else 'Adjusted_Median'
    
    with col1:
        st.metric(
            label="Highest Median",
            value=f"${filtered_df[salary_col].max():.0f}k",
            delta=f"{filtered_df.loc[filtered_df[salary_col].idxmax(), 'Province']}"
        )
    
    with col2:
        st.metric(
            label="Average Entry-Level",
            value=f"${filtered_df['Low_Salary'].mean():.0f}k",
            delta=f"${filtered_df['Low_Salary'].mean()*1000/2080:.0f}/hour"
        )
    
    with col3:
        st.metric(
            label="Average Senior",
            value=f"${filtered_df['High_Salary'].mean():.0f}k",
            delta=f"+{((filtered_df['High_Salary'].mean() - filtered_df['Low_Salary'].mean()) / filtered_df['Low_Salary'].mean() * 100):.0f}%"
        )
    
    with col4:
        st.metric(
            label="Salary Spread",
            value=f"${filtered_df[salary_col].max() - filtered_df[salary_col].min():.0f}k",
            delta="Difference"
        )
    
    st.markdown("---")
    
    # Two-column layout
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("📊 Median Salary Comparison")
        
        # Bar chart
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        
        colors = ['#3498DB' if p == 'BC' else '#E74C3C' if p == 'AB' else '#95A5A6' 
                  for p in filtered_df['Province']]
        
        bars = ax1.bar(filtered_df['Province'], filtered_df[salary_col], 
                       color=colors, edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for i, (p, v) in enumerate(zip(filtered_df['Province'], filtered_df[salary_col])):
            ax1.text(i, v + 2, f'${v:.0f}k', ha='center', fontsize=11, fontweight='bold')
        
        ax1.set_ylabel('Annual Salary ($k CAD)', fontsize=12)
        ax1.set_xlabel('Province', fontsize=12)
        ax1.set_title(f'{salary_type} Salaries', fontsize=14, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        st.pyplot(fig1)
        plt.close()
    
    with col_right:
        st.subheader("📈 Career Growth Potential")
        
        # Range plot
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        
        x_pos = np.arange(len(filtered_df))
        
        for i, row in enumerate(filtered_df.itertuples()):
            color = '#3498DB' if row.Province == 'BC' else '#E74C3C' if row.Province == 'AB' else '#95A5A6'
            linewidth = 4 if row.Province in ['BC', 'AB'] else 2
            
            ax2.plot([i, i], [row.Low_Salary, row.High_Salary], 
                    color=color, linewidth=linewidth, alpha=0.8)
            ax2.scatter(i, row.Median_Salary, color=color, s=150, 
                       zorder=5, edgecolor='black', linewidth=1.5)
        
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(filtered_df['Province'])
        ax2.set_ylabel('Annual Salary ($k CAD)', fontsize=12)
        ax2.set_xlabel('Province', fontsize=12)
        ax2.set_title('Entry-Level to Senior Range', fontsize=14, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)
        
        st.pyplot(fig2)
        plt.close()
    
    st.markdown("---")
    
    # Detailed data table
    st.subheader("📋 Detailed Salary Breakdown")
    
    # Prepare display dataframe
    display_df = filtered_df[['Province', 'Median_Salary', 'Low_Salary', 'High_Salary', 
                               'Adjusted_Median', 'Cost_of_Living_Index', 'Growth_Potential']].copy()
    
    display_df.columns = ['Province', 'Median ($k)', 'Entry ($k)', 'Senior ($k)', 
                          'Adjusted ($k)', 'CoL Index', 'Growth (%)']
    
    # Sort by selected metric
    sort_by = st.selectbox(
        "Sort by:",
        ['Median ($k)', 'Adjusted ($k)', 'Entry ($k)', 'Senior ($k)', 'Growth (%)'],
        index=1
    )
    
    display_df = display_df.sort_values(sort_by, ascending=False)
    
    st.dataframe(
        display_df.style.background_gradient(subset=['Median ($k)', 'Adjusted ($k)'], cmap='RdYlGn')
        .format({
            'Median ($k)': '{:.0f}',
            'Entry ($k)': '{:.0f}',
            'Senior ($k)': '{:.0f}',
            'Adjusted ($k)': '{:.0f}',
            'CoL Index': '{:.0f}',
            'Growth (%)': '{:.1f}%'
        }),
        use_container_width=True
    )
    
    # Insights section
    st.markdown("---")
    st.subheader("💡 Key Insights for Students")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏆 Best Value (Purchasing Power):**")
        best_value = filtered_df.loc[filtered_df['Adjusted_Median'].idxmax()]
        st.info(f"""
        **{best_value['Province']}**: ${best_value['Adjusted_Median']:.0f}k adjusted
        - Nominal salary: ${best_value['Median_Salary']}k
        - Cost of living: {best_value['Cost_of_Living_Index']}% of Vancouver
        - Best purchasing power for your money!
        """)
        
        st.markdown("**💰 Co-op Salary Guide:**")
        avg_entry = filtered_df['Low_Salary'].mean()
        st.success(f"""
        - Entry-level range: ${filtered_df['Low_Salary'].min()}k - ${filtered_df['Low_Salary'].max()}k/year
        - Hourly equivalent: ${filtered_df['Low_Salary'].min()*1000/2080:.0f} - ${filtered_df['Low_Salary'].max()*1000/2080:.0f}/hour
        - Target for data science co-ops: **$35-45/hour**
        """)
    
    with col2:
        st.markdown("**🎯 Highest Nominal Salary:**")
        highest_salary = filtered_df.loc[filtered_df['Median_Salary'].idxmax()]
        st.warning(f"""
        **{highest_salary['Province']}**: ${highest_salary['Median_Salary']}k
        - Entry to senior: ${highest_salary['Low_Salary']}k → ${highest_salary['High_Salary']}k
        - Growth potential: {highest_salary['Growth_Potential']}%
        - Best for major tech hub experience
        """)
        
        st.markdown("**📈 Best Growth Potential:**")
        best_growth = filtered_df.loc[filtered_df['Growth_Potential'].idxmax()]
        st.success(f"""
        **{best_growth['Province']}**: {best_growth['Growth_Potential']}% growth
        - From ${best_growth['Low_Salary']}k to ${best_growth['High_Salary']}k
        - Range: ${best_growth['Salary_Range']}k spread
        - Strong long-term career prospects
        """)

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 Data Sources")
st.sidebar.markdown("""
- Government of Canada Job Bank
- LinkedIn Salary Insights  
- Glassdoor Canada
- Numbeo Cost of Living Index

*Last updated: January 2026*
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.markdown("""
This interactive dashboard helps students explore data science salary trends across Canada to make informed co-op and career decisions.

**Created by:** Ayman  
**GitHub:** [View Project](https://github.com/aymanmomin/data-science-salaries-canada)
""")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #7F8C8D; font-size: 0.9rem;">'
    'Built with Python, Streamlit, and Canadian labour market data | '
    '<a href="https://github.com/aymanmomin/data-science-salaries-canada">View on GitHub</a>'
    '</p>',
    unsafe_allow_html=True
)
