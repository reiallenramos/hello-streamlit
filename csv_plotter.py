import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(file_obj):
    return pd.read_csv(file_obj)

st.title("CSV Quick Plotter")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if 'df' not in st.session_state:
    st.session_state.df = None
if 'data_source_name' not in st.session_state:
    st.session_state.data_source_name = None

if uploaded_file is not None:
    if st.session_state.data_source_name != uploaded_file.name:
        st.session_state.df = load_csv(uploaded_file)
        st.session_state.data_source_name = uploaded_file.name
    df = st.session_state.df

tab1, tab2 = st.tabs(["Chart", "DataFrame"])

columns = df.columns.tolist()
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("Select x-axis:", columns)
with col2:
    y_axis = st.selectbox("Select y-axis:", columns)
plot_type = st.radio("Select plot type:", ("Bar Chart", "Line Chart"), horizontal=True)

if plot_type == 'Bar Chart':
    if df[x_axis].dtype == 'object' and df[x_axis].nunique():
        tab1.bar_chart(df.groupby(x_axis)[y_axis].mean(), height=250)
elif plot_type == 'Line Chart':
    chart_data = df.sort_values(by=x_axis)
    tab1.line_chart(chart_data.set_index(x_axis)[y_axis], height=250)

tab2.dataframe(df, height=250, use_container_width=True)

with st.expander("view data summary"):
    st.write("**Shape**", df.shape)
