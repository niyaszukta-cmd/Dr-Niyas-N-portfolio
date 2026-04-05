import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Dr. Niyas N - Research Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with gradient backgrounds and modern styling
st.markdown("""
    <style>
    /* Main background gradient */
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
        padding: 0;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.95) 0%, rgba(126, 34, 206, 0.95) 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 1rem;
    }
    
    .hero-description {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.05rem;
        line-height: 1.6;
        max-width: 900px;
    }
    
    /* Stats cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        padding: 2rem 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.08) 100%);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #a78bfa;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.95rem;
        color: rgba(255, 255, 255, 0.8);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* App cards */
    .app-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(126, 34, 206, 0.4);
        border: 1px solid rgba(167, 139, 250, 0.4);
    }
    
    .app-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .app-title {
        color: white;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .app-description {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Feature tags */
    .feature-tag {
        display: inline-block;
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.3) 0%, rgba(126, 34, 206, 0.3) 100%);
        color: #e9d5ff;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid rgba(167, 139, 250, 0.3);
        font-weight: 500;
    }
    
    /* Status badge */
    .status-badge {
        display: inline-block;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #7e22ce 0%, #a78bfa 100%);
        color: white;
        border-radius: 15px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.05rem;
        border: none;
        box-shadow: 0 6px 20px rgba(126, 34, 206, 0.4);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #6b21a8 0%, #8b5cf6 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(126, 34, 206, 0.6);
    }
    
    /* Section headers */
    .section-header {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 3rem 0 2rem 0;
        padding-bottom: 1rem;
        border-bottom: 3px solid rgba(167, 139, 250, 0.5);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Contact section */
    .contact-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    
    .contact-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .contact-text {
        color: white;
        font-size: 1rem;
        margin-bottom: 0.3rem;
    }
    
    .contact-detail {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.95rem;
    }
    
    /* Publication card */
    .pub-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.04) 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #a78bfa;
        margin-bottom: 1rem;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Tech stack */
    .tech-stack {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #7e22ce 0%, #a78bfa 100%);
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================

st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🎓 Dr. Niyas N</div>
        <div class="hero-subtitle">Ph.D. in Corporate Finance | Empirical Researcher | Data Scientist</div>
        <div class="hero-description">
            Institutional-grade research platforms & data analytics tools for ESG analysis, 
            corporate finance, and quantitative research — built for academics, researchers, and financial professionals.
        </div>
        <div style="margin-top: 1.5rem; display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="https://www.linkedin.com/in/drniyas/" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #0077b5 0%, #005582 100%); color: white; padding: 0.6rem 1.5rem; border-radius: 10px; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 15px rgba(0, 119, 181, 0.3); transition: all 0.3s ease;">
                    💼 LinkedIn
                </div>
            </a>
            <a href="https://www.youtube.com/@NYZTrade" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%); color: white; padding: 0.6rem 1.5rem; border-radius: 10px; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3); transition: all 0.3s ease;">
                    ▶️ YouTube (10K+)
                </div>
            </a>
            <a href="https://www.instagram.com/nyztrade/" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #E1306C 0%, #C13584 100%); color: white; padding: 0.6rem 1.5rem; border-radius: 10px; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 15px rgba(225, 48, 108, 0.3); transition: all 0.3s ease;">
                    📸 Instagram
                </div>
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# STATS SECTION
# ============================================

st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Startups Founded</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">6</div>
            <div class="stat-label">Production Apps</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">12K+</div>
            <div class="stat-label">Active Users</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-label">Publications</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# STARTUPS & VENTURES
# ============================================

st.markdown("<div class='section-header'>🚀 Startups & Ventures</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">📊</div>
            <div class="app-title">NYZTrade Financial Solutions</div>
            <div style="color: #a78bfa; font-weight: 600; margin-bottom: 1rem;">Founder & CEO | 2020 - Present</div>
            <div class="app-description">
                DPIIT-registered startup specializing in options analytics, trading tools, and AI-powered 
                financial research platforms. Serving 10,000+ traders and researchers with institutional-grade 
                analytics for Indian FNO markets.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">GEX Analytics</span>
                <span class="feature-tag">Options Tools</span>
                <span class="feature-tag">AI Research</span>
                <span class="feature-tag">10K+ Users</span>
            </div>
            <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem; line-height: 1.6;">
                <strong>Products:</strong> Unified Dashboard, Premium Analytics, GEX Pro, VANNA Cascade<br>
                <strong>Market Focus:</strong> NSE/BSE FNO Markets<br>
                <strong>Revenue Model:</strong> Subscription-based SaaS Platform
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">🔬</div>
            <div class="app-title">Zodha Research Solutions</div>
            <div style="color: #a78bfa; font-weight: 600; margin-bottom: 1rem;">Director of Research | 2021 - Present</div>
            <div class="app-description">
                Research consultancy providing quantitative analysis, academic writing tools, and 
                data-driven insights for scholars, institutions, and businesses. Empowering 2,000+ 
                researchers with AI-powered academic productivity tools.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">Research Tools</span>
                <span class="feature-tag">AI Writing</span>
                <span class="feature-tag">Data Analytics</span>
                <span class="feature-tag">2K+ Users</span>
            </div>
            <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem; line-height: 1.6;">
                <strong>Services:</strong> Research Writing Pro, Statistical Consulting, Data Analysis<br>
                <strong>Clients:</strong> PhD Scholars, Academic Institutions, Research Organizations<br>
                <strong>Specialization:</strong> Quantitative Research & Academic Writing
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# CATEGORY 1: ESG & SUSTAINABILITY ANALYTICS
# ============================================

st.markdown("<div class='section-header'>🌱 ESG & Sustainability Analytics</div>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">🌍</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">ESG Data Dashboard</div>
            <div class="app-description">
                Comprehensive ESG analytics platform for corporate sustainability research. 
                Real-time ESG scores, sustainability metrics tracking, and interactive visualizations 
                for empirical studies on ESG performance and firm value.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">📊 ESG Metrics</span>
                <span class="feature-tag">🏢 Corporate Data</span>
                <span class="feature-tag">📈 Trend Analysis</span>
                <span class="feature-tag">🔄 Real-time</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch ESG Dashboard", key="esg"):
        st.markdown("### [Access ESG Dashboard →](https://dfhbtg9dngtbmyqkcnufcy.streamlit.app/)")

st.markdown("---")

# ============================================
# CATEGORY 2: QUANTITATIVE FINANCE & DERIVATIVES
# ============================================

st.markdown("<div class='section-header'>📈 Quantitative Finance & Derivatives</div>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">⚡</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">GEX Pro - Options Analytics Platform</div>
            <div class="app-description">
                Institutional-grade Gamma Exposure (GEX) analytics, VANNA cascade mathematics, 
                and dealer flow analysis. Advanced options analytics for market microstructure 
                research and quantitative trading strategies for NSE/BSE FNO markets.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">⚡ GEX Analysis</span>
                <span class="feature-tag">📊 Greeks</span>
                <span class="feature-tag">🎲 Vol Surface</span>
                <span class="feature-tag">🔄 Real-time</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch GEX Analytics", key="gex"):
        st.markdown("### [Access GEX Pro →](https://gex-pro-weekly-mgd7mz7quvkijbhmkv3bzl.streamlit.app/)")

st.markdown("---")

# ============================================
# CATEGORY 3: CORPORATE FINANCE & VALUATION
# ============================================

st.markdown("<div class='section-header'>💼 Corporate Finance & Valuation Tools</div>", unsafe_allow_html=True)

# App 1: Indian Markets Valuation
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">💰</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">Corporate Valuation Screener (Indian Markets)</div>
            <div class="app-description">
                Advanced valuation toolkit with DCF models, comparable analysis, and scenario testing 
                for Indian equity markets. Professional-grade fundamental analysis for NSE/BSE listed companies, 
                M&A analysis, and investment decisions.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">💵 DCF Models</span>
                <span class="feature-tag">📊 Multiples</span>
                <span class="feature-tag">🇮🇳 NSE/BSE</span>
                <span class="feature-tag">📈 Benchmarks</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch Indian Screener", key="valuation_india"):
        st.markdown("### [Access Valuation Tool →](https://value-screeners-wvdrespkw4jjbv2m6pauva.streamlit.app/)")

st.markdown("<br>", unsafe_allow_html=True)

# App 2: US Markets Valuation
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">🗽</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">US Stock Valuation Tool</div>
            <div class="app-description">
                Comprehensive valuation platform for US equity markets with real-time data integration. 
                DCF analysis, multiples valuation, and fundamental screening for NYSE, NASDAQ, and AMEX 
                listed companies with advanced financial modeling capabilities.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">🇺🇸 US Markets</span>
                <span class="feature-tag">📊 Real-time Data</span>
                <span class="feature-tag">💰 DCF Models</span>
                <span class="feature-tag">🎯 Screening</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch US Screener", key="valuation_us"):
        st.markdown("### [Access US Tool →](https://nyztradeusstocksvaluations-dcimvmugnxty8kqsprfedp.streamlit.app/)")

st.markdown("<br>", unsafe_allow_html=True)

# App 3: Sharia Compliant Stocks
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">☪️</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">Sharia-Compliant Value Stocks Screener</div>
            <div class="app-description">
                Islamic finance-focused stock screening platform with Sharia compliance verification 
                based on AAOIFI standards. Halal stock identification, Islamic finance ratios, 
                and value investing principles for ethical investment decisions.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">☪️ Halal Stocks</span>
                <span class="feature-tag">📊 AAOIFI Standards</span>
                <span class="feature-tag">💎 Value Investing</span>
                <span class="feature-tag">🕌 Islamic Finance</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch Sharia Screener", key="sharia"):
        st.markdown("### [Access Sharia Tool →](https://nyztrade-sharia-value-stocks-dz64ywzrizikua8ehg4gdf.streamlit.app/)")

st.markdown("---")

# ============================================
# CATEGORY 4: ACADEMIC RESEARCH TOOLS
# ============================================

st.markdown("<div class='section-header'>📚 Academic Research & Writing Tools</div>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div class="app-card">
            <div class="app-icon">✍️</div>
            <div class="status-badge">✓ Production</div>
            <div class="app-title">Zodha Research Writing Pro</div>
            <div class="app-description">
                AI-powered academic writing assistant with grammar checking, paraphrasing, 
                citation formatting, and plagiarism detection. Professional tool for manuscript 
                preparation, thesis writing, and research productivity enhancement.
            </div>
            <div style="margin-bottom: 1rem;">
                <span class="feature-tag">🤖 AI Assistant</span>
                <span class="feature-tag">✅ Grammar</span>
                <span class="feature-tag">📝 Paraphrase</span>
                <span class="feature-tag">📚 Citations</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Launch Writing Pro", key="writing"):
        st.markdown("### [Access Research Writing Pro →](https://zodha-ai-to-human-glmxvny4k7smzr6ww9fkaw.streamlit.app/)")

st.markdown("---")

# ============================================
# TECHNICAL STACK
# ============================================

st.markdown("<div class='section-header'>🛠️ Technical Capabilities</div>", unsafe_allow_html=True)

st.markdown("""
    <div class="tech-stack">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <div>
                <div style="color: #a78bfa; font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">
                    💻 Programming
                </div>
                <div style="color: rgba(255, 255, 255, 0.8); line-height: 1.8;">
                    Python (Advanced)<br>
                    R (Intermediate)<br>
                    SQL (Advanced)<br>
                    STATA (Advanced)<br>
                    Git/GitHub
                </div>
            </div>
            <div>
                <div style="color: #a78bfa; font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">
                    📊 Data Science
                </div>
                <div style="color: rgba(255, 255, 255, 0.8); line-height: 1.8;">
                    pandas, NumPy, SciPy<br>
                    Scikit-learn, TensorFlow<br>
                    Plotly, Seaborn<br>
                    Statistical Modeling<br>
                    Machine Learning
                </div>
            </div>
            <div>
                <div style="color: #a78bfa; font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">
                    ☁️ Deployment
                </div>
                <div style="color: rgba(255, 255, 255, 0.8); line-height: 1.8;">
                    Streamlit Cloud<br>
                    Heroku<br>
                    Docker (Basic)<br>
                    REST APIs<br>
                    Cloud Platforms
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# RESEARCH & PUBLICATIONS
# ============================================

st.markdown("<div class='section-header'>📖 Selected Publications</div>", unsafe_allow_html=True)

st.markdown("""
    <div class="pub-card">
        <strong>Impact of Brand Value on Firm Profitability and Firm Value of Indian FMCG Companies</strong><br>
        <em>IIMB Management Review</em>, Elsevier (ABDC B, Scopus, Web of Science)
    </div>
    <div class="pub-card">
        <strong>Impact of Corporate Social Responsibility on Brand Values of Reputed Banks in Asia</strong><br>
        <em>Empirical Economic Letters</em> (ABDC C, Scopus)
    </div>
    <div class="pub-card">
        <strong>The Nexus between Intellectual Capital Efficiency and Financial Brand Value</strong><br>
        <em>Indian Journal of Industrial Relations</em> (ABDC C, Web of Science)
    </div>
""", unsafe_allow_html=True)

# ============================================
# CONTACT SECTION
# ============================================

st.markdown("<div class='section-header'>📬 Get in Touch</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📧</div>
            <div class="contact-text">Email</div>
            <div class="contact-detail">niyaszukta@gmail.com</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📱</div>
            <div class="contact-text">Phone</div>
            <div class="contact-detail">+91 7598 597 668</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">💼</div>
            <div class="contact-text">LinkedIn</div>
            <div class="contact-detail"><a href="https://www.linkedin.com/in/drniyas/" target="_blank" style="color: #a78bfa; text-decoration: none;">@drniyas</a></div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">▶️</div>
            <div class="contact-text">YouTube</div>
            <div class="contact-detail"><a href="https://www.youtube.com/@NYZTrade" target="_blank" style="color: #a78bfa; text-decoration: none;">10K+ Subscribers</a></div>
        </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer content with proper escaping
footer_html = f"""
<div style='text-align: center; color: rgba(255, 255, 255, 0.6); padding: 2rem 0; font-size: 0.9rem; border-top: 1px solid rgba(255, 255, 255, 0.1);'>
    <p style='margin-bottom: 0.5rem;'><strong style='color: rgba(255, 255, 255, 0.9); font-size: 1.2rem;'>Dr. Niyas N</strong></p>
    <p style='margin-bottom: 0.5rem; color: rgba(255, 255, 255, 0.8);'>Ph.D. in Corporate Finance | Founder, NYZTrade & Zodha Research</p>
    <p style='margin-bottom: 1.5rem; color: rgba(255, 255, 255, 0.7);'>Pondicherry Central University, India</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)

# Social media buttons using Streamlit columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <a href="https://www.linkedin.com/in/drniyas/" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #0077b5 0%, #005582 100%); color: white; padding: 0.8rem 1rem; border-radius: 10px; font-weight: 600; text-align: center; box-shadow: 0 4px 15px rgba(0, 119, 181, 0.3);">
                💼 LinkedIn
            </div>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <a href="https://www.youtube.com/@NYZTrade" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%); color: white; padding: 0.8rem 1rem; border-radius: 10px; font-weight: 600; text-align: center; box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);">
                ▶️ YouTube
            </div>
        </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <a href="https://www.instagram.com/nyztrade/" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #E1306C 0%, #C13584 100%); color: white; padding: 0.8rem 1rem; border-radius: 10px; font-weight: 600; text-align: center; box-shadow: 0 4px 15px rgba(225, 48, 108, 0.3);">
                📸 Instagram
            </div>
        </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <a href="mailto:niyaszukta@gmail.com" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #7e22ce 0%, #a78bfa 100%); color: white; padding: 0.8rem 1rem; border-radius: 10px; font-weight: 600; text-align: center; box-shadow: 0 4px 15px rgba(126, 34, 206, 0.3);">
                📧 Email
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Final footer text
final_footer = f"""
<div style='text-align: center; color: rgba(255, 255, 255, 0.6); padding: 1rem 0; font-size: 0.9rem;'>
    <p style='margin-bottom: 0.5rem; font-size: 0.95rem; color: rgba(255, 255, 255, 0.7);'>Research Portfolio & Data Analytics Platforms</p>
    <p style='margin-bottom: 1rem; font-size: 0.85rem;'>Last Updated: {datetime.now().strftime('%B %Y')}</p>
    <p style='font-size: 0.85rem; color: rgba(255, 255, 255, 0.6);'>
        All applications are production-ready and actively maintained.<br>
        For technical inquiries, collaboration opportunities, or access to source code, please contact via email.
    </p>
</div>
"""

st.markdown(final_footer, unsafe_allow_html=True)
