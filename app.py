import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="IREOF | Renewable Energy Optimization",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# DEMONSTRATION DATA
# ---------------------------------------------------------
# NOTE:
# These values are demonstration values only.
# They will later be replaced with verified Kenyan energy data.

generation_data = pd.DataFrame({
    "Source": [
        "Geothermal",
        "Hydropower",
        "Wind",
        "Solar",
        "Bioenergy"
    ],
    "Generation_MW": [
        850,
        420,
        310,
        180,
        45
    ]
})

time_data = pd.DataFrame({
    "Hour": list(range(1, 25)),
    "Demand_MW": [
        1050, 1000, 970, 950, 960, 1020,
        1150, 1300, 1450, 1500, 1480, 1450,
        1420, 1400, 1380, 1420, 1500, 1650,
        1750, 1800, 1720, 1500, 1300, 1150
    ],
    "Renewable_MW": [
        1200, 1180, 1150, 1120, 1100, 1080,
        1150, 1250, 1350, 1450, 1520, 1580,
        1600, 1580, 1540, 1500, 1480, 1450,
        1420, 1380, 1350, 1300, 1250, 1220
    ]
})


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        # ⚡ IREOF

        **Integrated Renewable Energy  
        Optimization Framework**
        """
    )

    st.divider()

    st.markdown("### Navigation")

   st.markdown("🏠 **Dashboard**")
    st.page_link("pages/1_Generation.py", label="Generation", icon="⚡")
    st.page_link("pages/2_Storage.py", label="Energy Storage", icon="🔋")
    st.page_link("pages/3_Grid.py", label="Grid & Transmission", icon="🔌")
    st.page_link("pages/4_Optimization.py", label="Optimization", icon="🧠")
    st.page_link("pages/5_Scenarios.py", label="Scenario Analysis", icon="📊")
    st.page_link("pages/6_GIS_Map.py", label="GIS Map", icon="🗺️")
    st.page_link("pages/7_About.py", label="About IREOF", icon="ℹ️")

    st.divider()

    st.caption("IREOF Dashboard")
    st.caption("Demonstration Version")


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

st.title("⚡ IREOF Dashboard")

st.subheader(
    "Integrated Renewable Energy Optimization Framework"
)

st.markdown(
    """
    An interactive framework for exploring the coordination of
    **renewable generation, energy storage and grid infrastructure**
    to improve renewable-energy integration and system reliability.
    """
)

st.divider()


# ---------------------------------------------------------
# KEY PERFORMANCE INDICATORS
# ---------------------------------------------------------

total_generation = generation_data["Generation_MW"].sum()
peak_demand = time_data["Demand_MW"].max()
storage_capacity = 500
renewable_share = 92.0
curtailment = 4.2

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Renewable Generation",
        f"{total_generation:,.0f} MW"
    )

with col2:
    st.metric(
        "Peak Demand",
        f"{peak_demand:,.0f} MW"
    )

with col3:
    st.metric(
        "Storage Capacity",
        f"{storage_capacity:,.0f} MWh"
    )

with col4:
    st.metric(
        "Renewable Share",
        f"{renewable_share:.1f}%"
    )

with col5:
    st.metric(
        "Curtailment",
        f"{curtailment:.1f}%"
    )


st.divider()


# ---------------------------------------------------------
# GENERATION VS DEMAND
# ---------------------------------------------------------

st.subheader("Generation and Demand Profile")

fig = px.line(
    time_data,
    x="Hour",
    y=["Demand_MW", "Renewable_MW"],
    markers=True,
    labels={
        "value": "Power (MW)",
        "Hour": "Hour of Day",
        "variable": "Indicator"
    }
)

fig.update_layout(
    height=450,
    legend_title_text=""
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ---------------------------------------------------------
# GENERATION MIX
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Renewable Generation Mix")

    fig_generation = px.pie(
        generation_data,
        names="Source",
        values="Generation_MW",
        hole=0.45
    )

    fig_generation.update_layout(
        height=420,
        showlegend=True
    )

    st.plotly_chart(
        fig_generation,
        use_container_width=True
    )


with col2:

    st.subheader("IREOF System Status")

    st.markdown("### 🟢 Generation")
    st.progress(0.85)

    st.markdown("### 🟡 Energy Storage")
    st.progress(0.58)

    st.markdown("### 🟢 Transmission")
    st.progress(0.78)

    st.markdown("### 🟢 Renewable Integration")
    st.progress(0.91)


st.divider()


# ---------------------------------------------------------
# IREOF FRAMEWORK
# ---------------------------------------------------------

st.subheader("IREOF Framework")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### ⚡ Renewable Generation")

    st.write(
        """
        Evaluates the contribution and variability of
        geothermal, hydro, wind, solar and other renewable
        energy resources.
        """
    )


with col2:

    st.markdown("### 🔋 Energy Storage")

    st.write(
        """
        Examines how battery energy storage and other
        storage technologies can support renewable
        integration and system flexibility.
        """
    )


with col3:

    st.markdown("### 🔌 Grid Infrastructure")

    st.write(
        """
        Considers transmission and distribution constraints
        affecting the movement of renewable electricity
        across the system.
        """
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "IREOF | Integrated Renewable Energy Optimization Framework"
)

st.caption(
    "Demonstration dashboard — data will be replaced with "
    "verified sources during model development."
)
