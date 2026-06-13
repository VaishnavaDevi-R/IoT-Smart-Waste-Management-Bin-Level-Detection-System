import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

from analytics import load_data
from prediction_engine import predict_time_to_full


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Smart Waste Dashboard",
    page_icon="🗑",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)


# =====================================
# LOAD DATA
# =====================================

df = load_data()

st.write("Unique bins:", df["bin_id"].unique())
st.write("Count:", df["bin_id"].nunique())

latest = (
    df.sort_values("timestamp")
    .groupby("bin_id")
    .tail(1)
)

total_bins = len(latest)

critical_bins = len(
    latest[latest["fill_percentage"] >= 80]
)

avg_fill = round(
    latest["fill_percentage"].mean(),
    1
)

# =====================================
# WASTE INTELLIGENCE CENTER
# =====================================

with st.sidebar:

    st.title("🧠 Operations Briefing")

    highest_bin = latest.loc[
        latest["fill_percentage"].idxmax()
    ]

    predicted_hours = predict_time_to_full(
        highest_bin["fill_percentage"]
    )

    st.markdown("---")

    st.markdown(
        f"""
### 📋 Daily Brief

**Date:** 13 June 2026

The waste monitoring network is
operating normally.

**{highest_bin['location']}** is currently
the most active waste zone with a
fill level of **{highest_bin['fill_percentage']}%**.

No critical overflow events have
been detected across the network.

Current operational risk remains
within acceptable limits.
"""
    )

    st.markdown("---")

    st.markdown(
        f"""
### 🎯 Recommended Action

Monitor **{highest_bin['location']}**
closely and prepare collection
operations if fill levels continue
to increase.

**Priority:** Medium
"""
    )

    st.markdown("---")

    st.markdown(
        f"""
### ⏳ Forecast

Next expected capacity threshold:

📍 **{highest_bin['location']}**

Estimated Time:

**{predicted_hours} Hours**
"""
    )

    st.markdown("---")

    st.markdown(
        """
### 🟢 Network Status

System Health: Normal

Data Flow: Active

Monitoring: Online

Alert State: Stable
"""
    )

# =====================================
# TITLE
# =====================================

st.title("🗑 Smart Waste Management Dashboard")


# =====================================
# KPI CARDS
# =====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🗑 Total Bins",
        total_bins
    )

with col2:
    st.metric(
        "🚨 Critical Bins",
        critical_bins
    )

with col3:
    st.metric(
        "📊 Average Fill %",
        avg_fill
    )


# =====================================
# CRITICAL BINS
# =====================================

st.subheader("🚨 Critical Bins")

critical = latest[
    latest["fill_percentage"] >= 80
]

if len(critical) > 0:

    st.dataframe(
        critical[
            [
                "bin_id",
                "location",
                "fill_percentage",
                "alert"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "No Critical Bins Found"
    )

st.divider()


# =====================================
# LATEST BIN STATUS
# =====================================

st.subheader("📋 Latest Bin Status")

latest["status_icon"] = latest["status"].map({
    "FULL": "🔴",
    "WARNING": "🟡",
    "HALF FULL": "🟢"
})

st.dataframe(
    latest[
        [
            "status_icon",
            "bin_id",
            "location",
            "fill_percentage",
            "temperature",
            "humidity",
            "gas_level",
            "status",
            "alert"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🚛 Priority Collection Queue")

queue_df = latest.sort_values(
    by="fill_percentage",
    ascending=False
)[
    [
        "bin_id",
        "location",
        "fill_percentage",
        "status"
    ]
]

queue_df.insert(
    0,
    "Priority",
    range(1, len(queue_df) + 1)
)

st.dataframe(
    queue_df,
    use_container_width=True
)
st.divider()

st.subheader("📊 Overflow Risk Matrix")

for _, row in latest.sort_values(
    by="fill_percentage",
    ascending=False
).iterrows():

    fill = row["fill_percentage"]

    if fill >= 80:
        color = "🔴"
        risk = "HIGH"

    elif fill >= 60:
        color = "🟠"
        risk = "MEDIUM"

    else:
        color = "🟢"
        risk = "LOW"

    st.progress(fill / 100)

    st.write(
        f"{color} {row['bin_id']} ({row['location']}) | {fill}% | {risk}"
    )

    st.divider()

st.subheader(
    "🚛 Smart Collection Route Recommendation"
)

route_df = latest.sort_values(
    by="fill_percentage",
    ascending=False
)

route_text = " ➜ ".join(
    route_df["location"].tolist()
)

st.success(
    route_text
)

efficiency = round(
    (
        route_df["fill_percentage"]
        .mean()
    ),
    1
)

st.info(
    f"Estimated Route Efficiency: {efficiency}%"
)

# =====================================
# FILL LEVEL TREND
# =====================================

st.subheader(
    "📈 Waste Fill Level Trends"
)

fig = px.line(
    df,
    x="timestamp",
    y="fill_percentage",
    color="bin_id",
    markers=True,
    title="Real-Time Bin Fill Trends"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================
# FILL DISTRIBUTION
# =====================================

st.subheader(
    "📊 Current Fill Distribution"
)

fig2 = px.bar(
    latest,
    x="bin_id",
    y="fill_percentage",
    color="status",
    text="fill_percentage",
    title="Current Fill Percentage by Bin"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()


# =====================================
# TEMPERATURE ANALYSIS
# =====================================

st.subheader(
    "🌡 Temperature Analysis"
)

fig3 = px.bar(
    latest,
    x="bin_id",
    y="temperature",
    color="temperature",
    title="Current Temperature by Bin"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()


# =====================================
# GAS LEVEL ANALYSIS
# =====================================

st.subheader(
    "🧪 Gas Level Analysis"
)

fig4 = px.bar(
    latest,
    x="bin_id",
    y="gas_level",
    color="gas_level",
    title="Current Gas Levels"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()


# =====================================
# TIME TO FULL PREDICTION
# =====================================

st.subheader(
    "⏳ Time To Full Prediction"
)

for _, row in latest.iterrows():

    prediction = predict_time_to_full(
        row["fill_percentage"]
    )

    st.info(
        f"{row['bin_id']} → {prediction} hours remaining"
    )

st.divider()

st.subheader("📋 Executive Summary")

highest_bin = latest.loc[
    latest["fill_percentage"].idxmax()
]

st.success(
    f"""
    The waste monitoring network is operating normally.

    Highest priority location:
    {highest_bin['location']} ({highest_bin['fill_percentage']}%).

    Recommended action:
    Schedule collection for this location first.

    Overall network health:
    {100 - critical_bins * 20}%.
    """
)

# =====================================
# FOOTER
# =====================================

st.caption(
    "Developed using ESP32, MQTT, HiveMQ Cloud, Node-RED, SQLite, Streamlit and Python"
)