# pip install plotly
# streamlit run C:\김지은\파이썬_src\프로젝트1\streamlit_project_1.py
import streamlit as st
import pandas as pd
import pymysql
import os
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

# ------------------------- DB & LOADERS -------------------------
def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database='autoreg_kr',
        charset='utf8mb4'
    )

@st.cache_data(ttl=300)
def load_car_data():
    query = "SELECT year, gender, age_group, car_count FROM gender_age_car"
    with get_connection() as conn:
        return pd.read_sql(query, conn)

@st.cache_data(ttl=300)
def load_faq():
    query = "SELECT question, answer FROM faq"
    with get_connection() as conn:
        return pd.read_sql(query, conn)

# ------------------------- PAGE CONFIG -------------------------
st.set_page_config(
    page_title="자동차 등록 현황 대시보드",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# (선택) 기본 메뉴 숨김 유지 시 주석 해제
# hide_elements = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_elements, unsafe_allow_html=True)

# ------------------------- SIDEBAR NAV -------------------------
st.sidebar.title("📂 메뉴")
page = st.sidebar.radio("이동", ["🏠 성별/연령", "❓ FAQ"], index=0, label_visibility="collapsed")

# 공통 데이터 로드
df = load_car_data()
age_order = ["10대이하","20대","30대","40대","50대","60대","70대","80대","90대이상"]
df["age_group"] = pd.Categorical(df["age_group"], categories=age_order, ordered=True)
year_list = sorted(df["year"].unique())

# ------------------------- DASHBOARD -------------------------
if page == "🏠 성별/연령":
    st.title("🚘 성별 및 연령별 자동차 등록 현황")

    # # 타이틀 바로 아래 연도 선택 (원형 차트용)
    # selected_year = st.selectbox("연도 선택", year_list, index=len(year_list)-1)

    # ====== 필터 표시 토글 (방법 B) ======
    st.sidebar.divider()
    show_filters = st.sidebar.toggle("필터 표시", value=False)  # 기본: 숨김

    if show_filters:
        st.sidebar.subheader("필터")
        years_sel = st.sidebar.multiselect("연도 범위(추이용)", year_list, default=year_list)
        genders_sel = st.sidebar.multiselect("성별 선택(추이용)", ["여성","남성"], default=["여성","남성"])
    else:
        # 숨김 시 기본값 적용: 전체 연도 + 남/녀
        years_sel = year_list
        genders_sel = ["여성", "남성"]
    # ====================================

    filtered_df = df[df["year"].isin(years_sel) & df["gender"].isin(genders_sel)]

    # 탭: 연도별 추이 / 선택연도 성별·연령 분포 / 증감률
    tab1, tab2, tab3 = st.tabs(["📊 연도별 추이", "📎 선택 연도 성별·연령 비율", "📈 연도별 증감률"])

    # ---------- 탭1: 연도별 남/녀 등록 추이 ----------
    with tab1:
        trend = (
            filtered_df.groupby(["year", "gender"])["car_count"]
            .sum()
            .reset_index()
            .sort_values("year")
        )
        fig_mf = px.line(
            trend,
            x="year", y="car_count", color="gender",
            markers=True, template="plotly_white",
            labels={"year": "연도", "car_count": "등록 수", "gender": "성별"},
            title="연도별 자동차 등록 추이"
        )
        fig_mf.update_yaxes(tickformat=",.0f", ticksuffix="명")
        fig_mf.update_traces(hovertemplate="연도=%{x}<br>등록 수=%{y:,.0f}명")
        st.plotly_chart(fig_mf, use_container_width=True)

    # ---------- 탭2: 선택한 연도의 남/녀 원형(연령대 비율 %) ----------
    with tab2:
    # 이 탭에서만 연도 선택 드롭다운 표시
        selected_year = st.selectbox(
            "연도 선택",
            year_list,
            index=len(year_list)-1,
            key="year_for_pies"   # 탭별 상태 유지용 키 (선택)
        )

        age_colors = {
            "10대이하": "#FFD9D9", "20대": "#FFE0B2", "30대": "#FFF59D",
            "40대": "#B2FF59", "50대": "#80DEEA", "60대": "#B39DDB",
            "70대": "#FFCCBC", "80대": "#F8BBD0", "90대이상": "#CFD8DC"
        }
        year_df = df[df["year"] == selected_year]

        def pie_by_gender(g):
            gdf = (
                year_df[year_df["gender"] == g]
                .groupby("age_group")["car_count"].sum()
                .reindex(age_order).fillna(0).reset_index()
            )
            total = gdf["car_count"].sum()
            gdf["pct"] = (gdf["car_count"] / total * 100) if total > 0 else 0
            fig = px.pie(
                gdf, names="age_group", values="car_count",
                color="age_group", color_discrete_map=age_colors,
                hole=0.35, template="plotly_white",
                title=f"{selected_year}년 {g} 연령대 비율"
            )
            fig.update_traces(textposition="inside", textinfo="percent+label")
            return fig

        c1, c2 = st.columns(2)
        c1.plotly_chart(pie_by_gender("남성"), use_container_width=True)
        c2.plotly_chart(pie_by_gender("여성"), use_container_width=True)

    # ---------- 탭3: 증감률 라인 + 우측 표 ----------
    with tab3:
        yearly_total = (
            df.groupby("year")["car_count"]
            .sum()
            .reset_index()
            .sort_values("year")
        )
        display_df = yearly_total.copy()
        display_df["증감"] = display_df["car_count"].diff().fillna(0).astype(int)
        display_df["증감률(%)"] = display_df["car_count"].pct_change().fillna(0) * 100

        fig_growth = px.line(
            display_df, x="year", y="증감률(%)",
            markers=True, template="plotly_white",
            labels={"year": "연도", "증감률(%)": "증감률 (%)"},
            title="연도별 등록수 증감률"
        )
        fig_growth.update_yaxes(tickformat=",.2f", ticksuffix="%")
        fig_growth.update_traces(hovertemplate="연도=%{x}<br>증감률=%{y:,.2f}%")

        # 표 포맷팅
        table_df = display_df.copy()
        table_df["등록 수"] = table_df["car_count"].apply(lambda x: f"{x:,.0f}명")
        table_df["전년 대비 증감"] = table_df["증감"].apply(lambda x: f"{x:+,}명")
        table_df["전년 대비 증감률"] = table_df["증감률(%)"].apply(lambda x: f"{x:+.2f}%")
        table_df = table_df[["year", "등록 수", "전년 대비 증감", "전년 대비 증감률"]]
        table_df.columns = ["연도", "등록 수", "전년 대비 증감", "전년 대비 증감률"]

        g1, g2 = st.columns([2, 1])
        g1.plotly_chart(fig_growth, use_container_width=True)
        g2.dataframe(table_df, use_container_width=True, hide_index=True)

# ------------------------- FAQ -------------------------
else:  # page == "❓ FAQ"
    st.title("❓ FAQ")
    faq_df = load_faq()
    for _, row in faq_df.iterrows():
        with st.expander(row["question"]):
            st.write(row["answer"])