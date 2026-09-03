import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sales & Inventory AI Copilot", layout="wide"
)

st.title("📈 Enterprise AI Sales & Inventory Forecasting Copilot")
st.write(
    "Real-time sales tracking, stock monitoring, and dynamic demand forecasting."
)


# Reload data without cache issues
def load_data():
    df = pd.read_csv("sales_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


try:
    df = load_data()

    # Sidebar Filter
    st.sidebar.header("Filter Options")
    product_list = df["Product"].unique().tolist()
    selected_product = st.sidebar.selectbox("Select Product", product_list)

    filtered_df = df[df["Product"] == selected_product].sort_values("Date")

    # Key Metrics
    col1, col2, col3 = st.columns(3)
    total_sales = filtered_df["Sales"].sum()
    avg_stock = int(filtered_df["Stock_Level"].mean())
    recent_sales = filtered_df["Sales"].iloc[-1]

    col1.metric("Total Units Sold", f"{total_sales} units")
    col2.metric("Avg Inventory Level", f"{avg_stock} units")
    col3.metric("Latest Daily Sales", f"{recent_sales} units")

    # Visualizations
    st.subheader(f"Sales Trend & Inventory for {selected_product}")

    fig_sales = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Historical Sales Trend",
        markers=True,
    )
    st.plotly_chart(fig_sales, use_container_width=True)

    fig_stock = px.bar(
        filtered_df,
        x="Date",
        y="Stock_Level",
        title="Stock Level Over Time",
        color="Stock_Level",
    )
    st.plotly_chart(fig_stock, use_container_width=True)

    # Simple AI Forecasting & Reorder Logic
    st.subheader("💡 AI Insights & Inventory Advice")
    avg_30day_sales = filtered_df["Sales"].tail(30).mean()
    current_stock = filtered_df["Stock_Level"].iloc[-1]

    if current_stock < (avg_30day_sales * 7):
        st.warning(
            f"⚠️ **Low Stock Alert!** Stock ({current_stock}) is below recommended 7-day threshold. Reorder soon."
        )
    else:
        st.success(
            f"✅ **Healthy Inventory!** Current stock level ({current_stock}) is sufficient."
        )

except Exception as e:
    st.error(
        f"Error loading data. Make sure `sales_data.csv` is generated first! Detail: {e}"
    )
        