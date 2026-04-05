import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Dr. Niyas N - Research Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #155a8a;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .app-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .category-header {
        color: #1f77b4;
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #1f77b4;
    }
    .tech-tag {
        display: inline-block;
        background-color: #e9ecef;
        color: #495057;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .status-production {
        background-color: #d4edda;
        color: #155724;
    }
    .status-beta {
        background-color: #fff3cd;
        color: #856404;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Dr. Niyas N")
    st.subheader("Research Portfolio & Data Analytics Platforms")
    st.markdown("""
    **Ph.D. in Corporate Finance | Empirical Researcher | Data Scientist**
    
    Welcome to my portfolio of research tools and data analytics platforms. These applications 
    demonstrate expertise in econometric analysis, data visualization, ESG research, and 
    quantitative finance.
    """)

with col2:
    st.markdown("""
    **Contact Information**
    
    📧 niyaszukta@gmail.com
    
    📞 +91 7598 597 668
    
    🎓 Pondicherry Central University
    
    📍 Kerala, India
    """)

st.markdown("---")

# About Section
with st.expander("📄 About This Portfolio", expanded=False):
    st.markdown("""
    This portfolio showcases production-ready web applications developed to support:
    - **Academic Research**: ESG analysis, corporate finance, empirical accounting
    - **Data Analytics**: Large-scale dataset management, visualization, statistical modeling
    - **Educational Tools**: Research writing, content development, academic productivity
    - **Financial Analysis**: Valuation models, options analytics, market microstructure
    
    **Technical Expertise**: Python (Streamlit, pandas, plotly, scikit-learn), Statistical Software (STATA, SPSS, R), 
    Cloud Deployment (Streamlit Cloud, Heroku), APIs, Database Management, Machine Learning
    
    **Research Focus**: ESG & Sustainability, Corporate Governance, Empirical Accounting, Corporate Finance, 
    Brand Valuation, Intellectual Capital
    """)

st.markdown("---")

# ============================================
# CATEGORY 1: RESEARCH & ESG ANALYTICS
# ============================================

st.markdown('<div class="category-header">🌱 Research & ESG Analytics</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### ESG Data Dashboard
    
    <span class="status-badge status-production">✓ Production</span>
    
    **Comprehensive ESG analytics platform for corporate sustainability research**
    
    **Features:**
    - Real-time ESG scores and sustainability metrics tracking
    - Environmental, Social, and Governance performance analysis
    - Corporate sustainability reporting and disclosure quality assessment
    - Interactive data visualizations for ESG research
    - Cross-company and cross-sector comparative analysis
    - Time-series analysis of ESG performance trends
    
    **Research Applications:**
    - Empirical studies on ESG performance and firm value
    - Corporate governance quality assessment
    - Sustainability reporting transparency analysis
    - ESG integration in investment decisions
    
    **Technical Stack:**
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<span class="tech-tag">Python</span>'
        '<span class="tech-tag">Streamlit</span>'
        '<span class="tech-tag">Pandas</span>'
        '<span class="tech-tag">Plotly</span>'
        '<span class="tech-tag">APIs</span>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("**Launch Application:**")
    if st.button("🚀 Open ESG Dashboard", key="esg"):
        st.markdown("**[Click here to access ESG Dashboard](https://dfhbtg9dngtbmyqkcnufcy.streamlit.app/)**")
    
    st.markdown("---")
    st.markdown("**Users:** 500+ researchers")
    st.markdown("**Status:** Actively maintained")
    st.markdown("**Use Case:** Academic research, ESG analysis, sustainability reporting")

st.markdown("---")

# ============================================
# CATEGORY 2: CORPORATE FINANCE & VALUATION
# ============================================

st.markdown('<div class="category-header">💼 Corporate Finance & Valuation Tools</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Corporate Valuation Screener
    
    <span class="status-badge status-production">✓ Production</span>
    
    **Advanced valuation toolkit for fundamental analysis and firm valuation**
    
    **Features:**
    - Discounted Cash Flow (DCF) valuation models
    - Comparable company analysis and multiples valuation
    - Scenario analysis and sensitivity testing
    - Financial ratio analysis and performance metrics
    - Industry benchmark comparisons
    - Intrinsic value calculation with multiple methodologies
    - Dividend discount models (DDM)
    
    **Research Applications:**
    - Corporate finance research and firm valuation studies
    - Brand value and intangible asset valuation
    - M&A analysis and acquisition pricing
    - Investment decision support
    
    **Technical Stack:**
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<span class="tech-tag">Python</span>'
        '<span class="tech-tag">Financial Modeling</span>'
        '<span class="tech-tag">DCF</span>'
        '<span class="tech-tag">Valuation</span>'
        '<span class="tech-tag">Streamlit</span>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("**Launch Application:**")
    if st.button("🚀 Open Valuation Tool", key="valuation"):
        st.markdown("**[Click here to access Valuation Screener](https://value-screeners-wvdrespkw4jjbv2m6pauva.streamlit.app/)**")
    
    st.markdown("---")
    st.markdown("**Users:** 800+ analysts")
    st.markdown("**Status:** Actively maintained")
    st.markdown("**Use Case:** Fundamental analysis, academic research, investment decisions")

st.markdown("---")

# ============================================
# CATEGORY 3: QUANTITATIVE FINANCE & DERIVATIVES
# ============================================

st.markdown('<div class="category-header">📈 Quantitative Finance & Options Analytics</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### GEX Pro - Options Analytics Platform
    
    <span class="status-badge status-production">✓ Production</span>
    
    **Advanced options analytics and market microstructure analysis**
    
    **Features:**
    - Gamma Exposure (GEX) analysis and visualization
    - Options flow and dealer positioning analytics
    - Implied volatility surface modeling
    - Greeks calculation (Delta, Gamma, Vega, Theta, Rho)
    - Market maker hedging flow analysis
    - Support/resistance level identification from options data
    - Real-time options chain analysis
    
    **Research Applications:**
    - Market microstructure research
    - Volatility forecasting and modeling
    - Derivatives pricing studies
    - Behavioral finance and investor sentiment analysis
    - Liquidity provision and market making studies
    
    **Technical Stack:**
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<span class="tech-tag">Python</span>'
        '<span class="tech-tag">Options Pricing</span>'
        '<span class="tech-tag">Black-Scholes</span>'
        '<span class="tech-tag">Real-time APIs</span>'
        '<span class="tech-tag">Advanced Analytics</span>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("**Launch Application:**")
    if st.button("🚀 Open GEX Analytics", key="gex"):
        st.markdown("**[Click here to access GEX Pro](https://gex-pro-weekly-mgd7mz7quvkijbhmkv3bzl.streamlit.app/)**")
    
    st.markdown("---")
    st.markdown("**Users:** 1,200+ traders & researchers")
    st.markdown("**Status:** Actively maintained")
    st.markdown("**Use Case:** Derivatives research, quantitative trading, market analysis")

st.markdown("---")

# ============================================
# CATEGORY 4: ACADEMIC RESEARCH TOOLS
# ============================================

st.markdown('<div class="category-header">📚 Academic Research & Writing Tools</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Zodha Research Writing Pro
    
    <span class="status-badge status-production">✓ Production</span>
    
    **AI-powered academic writing assistant for researchers and scholars**
    
    **Features:**
    - AI-to-human content conversion for academic writing
    - Grammar and style checking with academic standards
    - Paraphrasing tool maintaining academic integrity
    - Citation formatting and reference management support
    - Plagiarism detection and originality enhancement
    - Research paper structure optimization
    - Academic tone and voice consistency checker
    - Literature review assistance
    
    **Research Applications:**
    - Manuscript preparation for journal submission
    - Thesis and dissertation writing
    - Research proposal development
    - Grant application writing
    - Conference paper preparation
    
    **Technical Stack:**
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<span class="tech-tag">Python</span>'
        '<span class="tech-tag">NLP</span>'
        '<span class="tech-tag">AI/ML</span>'
        '<span class="tech-tag">Groq API</span>'
        '<span class="tech-tag">Streamlit</span>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("**Launch Application:**")
    if st.button("🚀 Open Writing Pro", key="writing"):
        st.markdown("**[Click here to access Research Writing Pro](https://zodha-ai-to-human-glmxvny4k7smzr6ww9fkaw.streamlit.app/)**")
    
    st.markdown("---")
    st.markdown("**Users:** 2,000+ researchers")
    st.markdown("**Status:** Actively maintained")
    st.markdown("**Use Case:** Academic writing, research productivity, manuscript preparation")

st.markdown("---")

# ============================================
# TECHNICAL CAPABILITIES SUMMARY
# ============================================

st.markdown('<div class="category-header">🛠️ Technical Capabilities</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Programming & Development**
    - Python (Advanced)
    - R (Intermediate)
    - SQL (Advanced)
    - STATA (Advanced)
    - Git/GitHub
    """)

with col2:
    st.markdown("""
    **Data Science & Analytics**
    - Pandas, NumPy, SciPy
    - Scikit-learn, TensorFlow
    - Plotly, Matplotlib, Seaborn
    - Statistical modeling
    - Machine Learning
    """)

with col3:
    st.markdown("""
    **Deployment & Infrastructure**
    - Streamlit Cloud
    - Heroku
    - Docker (Basic)
    - REST APIs
    - Cloud platforms
    """)

st.markdown("---")

# ============================================
# RESEARCH & PUBLICATIONS
# ============================================

st.markdown('<div class="category-header">📖 Research & Publications</div>', unsafe_allow_html=True)

st.markdown("""
**Selected Publications:**

1. **Impact of Brand Value on Firm Profitability and Firm Value of Indian FMCG Companies**  
   *IIMB Management Review*, Elsevier (ABDC B, Scopus, Web of Science)

2. **Impact of Corporate Social Responsibility (CSR) on Brand Values of Reputed Banks in Asia**  
   *Empirical Economic Letters* (ABDC C, Scopus)

3. **The Nexus between Intellectual Capital Efficiency and Financial Brand Value**  
   *Indian Journal of Industrial Relations* (ABDC C, Web of Science)

4. **Intellectual Capital Efficiency and Financial Performance of IT Companies in India**  
   *Asian Journal of Management* (UGC-CARE Listed)

5. **Impact of Brand Value on Firm Performance of Pharmaceutical Brands in India**  
   *VidyaBharati International Journal* (Web of Science)

**Research Interests:**
- ESG Performance & Corporate Financial Performance
- Corporate Governance & Firm Value
- Sustainability Reporting & Disclosure Quality
- Intellectual Capital & Intangible Assets
- Brand Valuation & Corporate Performance
- Empirical Corporate Finance
""")

st.markdown("---")

# ============================================
# CURRENT RESEARCH PROJECTS
# ============================================

st.markdown('<div class="category-header">🔬 Current Research Projects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **ICSSR Sponsored Research**
    
    **Project:** Women's Workforce Participation and Financial Autonomy in Kerala
    
    **Grant:** INR 20,00,000 (USD ~24,000)
    
    **Role:** Principal Investigator
    
    **Scope:** Large-scale survey with 1,357 respondents across 5 districts
    
    **Methods:** SEM, CFA, Panel data analysis
    """)

with col2:
    st.markdown("""
    **Working Papers**
    
    1. **ESG Performance and Firm Value: Evidence from Indian Listed Companies**
       - Panel data analysis (2018-2023)
       - ESG scores from Bloomberg
    
    2. **Corporate Governance Quality and Financial Reporting Transparency**
       - Cross-country analysis
       - 500+ firms across 10 Asian countries
    
    3. **Sustainability Reporting and Cost of Capital**
       - Instrumental variables approach
       - Emerging markets focus
    """)

st.markdown("---")

# ============================================
# CONTACT & FOOTER
# ============================================

st.markdown('<div class="category-header">📬 Get in Touch</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Email**
    
    📧 niyaszukta@gmail.com
    
    Response time: Within 24 hours
    """)

with col2:
    st.markdown("""
    **Professional Profiles**
    
    🎓 Google Scholar: Available upon request
    
    🔬 ORCID: Available upon request
    
    💼 LinkedIn: Available upon request
    """)

with col3:
    st.markdown("""
    **Collaboration**
    
    Open to:
    - Research collaborations
    - Consulting projects
    - Academic positions
    - Speaking engagements
    """)

st.markdown("---")

# Footer
st.markdown(f"""
    <div style='text-align: center; color: #6c757d; padding: 2rem 0; font-size: 0.9rem;'>
        <p><strong>Dr. Niyas N</strong> | Ph.D. in Corporate Finance</p>
        <p>Research Portfolio & Data Analytics Platforms</p>
        <p>Last Updated: {datetime.now().strftime('%B %Y')}</p>
        <p style='margin-top: 1rem; font-size: 0.85rem;'>
            All applications are production-ready and actively maintained. 
            For technical inquiries, collaboration opportunities, or access to source code, please contact via email.
        </p>
    </div>
""", unsafe_allow_html=True)
