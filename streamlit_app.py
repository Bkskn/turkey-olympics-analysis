import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🇹🇷 Turkey Olympics Analysis",
    page_icon="🏅",
    layout="wide"
)

# ── Load Data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data/athlete_events.csv")
    df["Medal"] = df["Medal"].fillna("None")
    for m in ["Gold", "Silver", "Bronze"]:
        df[m] = (df["Medal"] == m).astype(int)
    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]
    return df

df = load_data()
df_turkey = df[(df["Team"] == "Turkey") & (df["Season"] == "Summer")].copy()

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏅 Turkey at the Olympics")
st.markdown("Deep-dive analysis of Turkey's Summer Olympic performance (1936–2016)")
st.divider()

# ── Sidebar Filters ───────────────────────────────────────────────────────────
st.sidebar.header("🔎 Filters")

year_range = st.sidebar.slider(
    "Year Range",
    min_value=int(df_turkey["Year"].min()),
    max_value=int(df_turkey["Year"].max()),
    value=(1936, 2016),
    step=4
)

sport_list = ["All"] + sorted(df_turkey["Sport"].unique().tolist())
selected_sport = st.sidebar.selectbox("Sport", sport_list)

# Apply filters
df_f = df_turkey[
    (df_turkey["Year"] >= year_range[0]) &
    (df_turkey["Year"] <= year_range[1])
]
if selected_sport != "All":
    df_f = df_f[df_f["Sport"] == selected_sport]

# ── KPI Cards ─────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("🥇 Gold",   int(df_f["Gold"].sum()))
col2.metric("🥈 Silver", int(df_f["Silver"].sum()))
col3.metric("🥉 Bronze", int(df_f["Bronze"].sum()))
col4.metric("🏅 Total",  int(df_f["Total"].sum()))

st.divider()

# ── Section 1: Medal Bar Chart ────────────────────────────────────────────────
st.subheader("📊 Medals by Year")

yearly = df_f.groupby("Year")[["Gold", "Silver", "Bronze"]].sum().reset_index()

fig_bar = px.bar(
    yearly, x="Year", y=["Gold", "Silver", "Bronze"],
    color_discrete_map={"Gold": "#FFD700", "Silver": "#C0C0C0", "Bronze": "#CD7F32"},
    barmode="stack",
    labels={"value": "Medal Count", "variable": "Medal Type"},
    title=f"Turkey Olympic Medals by Year ({year_range[0]}–{year_range[1]})"
)
fig_bar.update_layout(xaxis=dict(tickmode="linear", dtick=4))
st.plotly_chart(fig_bar, use_container_width=True)

# ── Section 2: Medals by Sport ────────────────────────────────────────────────
st.subheader("🤼 Medals by Sport")

sport_medals = (
    df_f.groupby("Sport")[["Gold", "Silver", "Bronze", "Total"]]
    .sum()
    .sort_values("Total", ascending=False)
    .reset_index()
)
sport_medals = sport_medals[sport_medals["Total"] > 0]

fig_sport = px.bar(
    sport_medals, x="Total", y="Sport",
    orientation="h",
    color="Gold",
    color_continuous_scale="YlOrRd",
    title="Medal Count by Sport"
)
fig_sport.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig_sport, use_container_width=True)

st.divider()

# ── Section 3: Correlation Heatmap ───────────────────────────────────────────
st.subheader("🔥 Correlation Heatmap")
st.markdown("Correlation between numeric features for Turkish athletes.")

numeric_cols = ["Age", "Height", "Weight", "Year", "Gold", "Silver", "Bronze", "Total"]
df_numeric = df_f[numeric_cols].dropna()

fig_heat, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(
    df_numeric.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    linewidths=0.5,
    ax=ax
)
ax.set_title("Feature Correlation Matrix — Turkish Athletes", fontsize=13)
plt.tight_layout()
st.pyplot(fig_heat)

st.divider()

# ── Section 4: Raw Data ───────────────────────────────────────────────────────
with st.expander("📋 Show Raw Data"):
    st.dataframe(
        df_f[df_f["Total"] > 0][["Name", "Sport", "Year", "Age", "Gold", "Silver", "Bronze"]]
        .sort_values("Year", ascending=False)
        .reset_index(drop=True),
        use_container_width=True
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("📁 [GitHub Repository](https://github.com/Bkskn/turkey-olympics-analysis)")
