import streamlit as st
from investor_scraper import (
    scrape_infosys_investor, scrape_tcs_investor, scrape_wipro_investor,
    scrape_hcl_investor, scrape_techm_investor
)
from sites_scraper import (
    scrape_et_tech_rss, scrape_moneycontrol, scrape_business_standard,
    scrape_cnbc_tv18, scrape_livemint
)
from data_storage import save_to_csv

st.title("Financial News & Investor Reports Scraper")

site_scrapers = {
    "Economic Times Tech": scrape_et_tech_rss,
    "Moneycontrol": scrape_moneycontrol,
    "Business Standard": scrape_business_standard,
    "CNBC TV18": scrape_cnbc_tv18,
    "LiveMint": scrape_livemint
}

investor_scrapers = {
    "Infosys": scrape_infosys_investor,
    "TCS": scrape_tcs_investor,
    "Wipro": scrape_wipro_investor,
    "HCL": scrape_hcl_investor,
    "Tech Mahindra": scrape_techm_investor
}

selected_sites = st.multiselect("Select up to 3 News Sites", list(site_scrapers.keys()), max_selections=3)
selected_investors = st.multiselect("Select up to 3 Investor Pages", list(investor_scrapers.keys()), max_selections=3)

if st.button("Fetch Data"):
    data = []
    for site in selected_sites:
        data.extend(site_scrapers[site]())
    for inv in selected_investors:
        data.extend(investor_scrapers[inv]())
    
    if data:
        df = save_to_csv(data)
        st.success(f"Fetched {len(df)} records.")
        st.dataframe(df)
    else:
        st.warning("No data fetched.")
