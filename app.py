import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==========================================
# JEEVANSETU - RURAL HEALTHCARE HUB
# ==========================================

st.set_page_config(
    page_title="JeevanSetu | Rural Healthcare Hub",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# DARK THEME - JEEVANSETU
# ==========================================

st.markdown("""
<style>

/* MAIN APP BACKGROUND */
.stApp {
    background-color: #101817 !important;
    color: #ffffff !important;
}

/* MAIN CONTENT AREA */
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: #101817 !important;
    color: #ffffff !important;
}

/* ALL TEXT WHITE */
.stApp p,
.stApp span,
.stApp label,
.stApp li,
.stApp div,
.stApp small {
    color: #ffffff;
}

/* HEADINGS */
h1, h2, h3, h4, h5 {
    color: #7ee6a5 !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #172522 !important;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* SIDEBAR RADIO OPTIONS */
[data-testid="stSidebar"] [role="radiogroup"] label {
    background-color: #243b34 !important;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 6px;
}

/* HERO SECTION */
.hero {
    background: linear-gradient(
        135deg,
        #163d30,
        #1c302a
    ) !important;

    padding: 30px;
    border-radius: 18px;
    border: 1px solid #367b58;
    border-left: 7px solid #4ade80;
    margin-bottom: 25px;
    color: #ffffff !important;
}

.hero h1,
.hero h2,
.hero h3,
.hero p {
    color: #ffffff !important;
}

/* GENERAL CARDS */
.card {
    background-color: #1c2b27 !important;
    border: 1px solid #365c4d;
    padding: 22px;
    border-radius: 15px;
    margin-bottom: 15px;
    color: #ffffff !important;
}

.card h3 {
    color: #7ee6a5 !important;
}

.card p {
    color: #ffffff !important;
}

/* METRIC CARDS */
.metric-card {
    background-color: #203a30 !important;
    border: 1px solid #4b8066;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.metric-number {
    font-size: 30px;
    font-weight: bold;
    color: #7ee6a5 !important;
}

/* BUTTONS */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #198754 !important;
    color: #ffffff !important;
    border: 1px solid #4ade80 !important;
    border-radius: 10px;
    font-weight: bold;
}

.stButton > button *,
.stFormSubmitButton > button * {
    color: #ffffff !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #146c43 !important;
    border: 1px solid #7ee6a5 !important;
}

/* INPUT BOXES */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background-color: #24332f !important;
    color: #ffffff !important;
    border: 1px solid #5a796c !important;
    border-radius: 8px;
}

/* PLACEHOLDER TEXT */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #c4d4cc !important;
    opacity: 1 !important;
}

/* DROPDOWN */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #24332f !important;
    color: #ffffff !important;
    border-color: #5a796c !important;
}

.stSelectbox div[data-baseweb="select"] * {
    color: #ffffff !important;
}

/* DROPDOWN POPUP */
[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"] {
    background-color: #24332f !important;
}

[role="option"] {
    background-color: #24332f !important;
    color: #ffffff !important;
}

[role="option"]:hover {
    background-color: #198754 !important;
}

/* CHECKBOX */
.stCheckbox label,
.stCheckbox p {
    color: #ffffff !important;
}

/* DATA TABLES */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background-color: #1c2b27 !important;
    border: 1px solid #365c4d;
    border-radius: 10px;
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background-color: #172522 !important;
}

.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
}

/* METRICS */
[data-testid="stMetric"] {
    background-color: #203a30 !important;
    border: 1px solid #365c4d;
    padding: 15px;
    border-radius: 12px;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {
    color: #ffffff !important;
}

/* ALERT BOXES */
[data-testid="stAlert"] {
    background-color: #24332f !important;
    color: #ffffff !important;
    border: 1px solid #527665;
    border-radius: 10px;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] span {
    color: #ffffff !important;
}

/* DOWNLOAD BUTTON */
.stDownloadButton > button {
    background-color: #244b3a !important;
    color: #ffffff !important;
    border: 1px solid #4ade80 !important;
    border-radius: 10px;
}

/* DIVIDER */
hr {
    border-color: #365c4d !important;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #cbd5d1 !important;
    font-size: 13px;
    padding: 20px;
}

/* CAPTIONS */
.stCaption,
[data-testid="stCaptionContainer"] {
    color: #cbd5d1 !important;
}

/* EXPANDER */
[data-testid="stExpander"] {
    background-color: #1c2b27 !important;
    border: 1px solid #365c4d;
    border-radius: 10px;
}

[data-testid="stExpander"] summary {
    color: #ffffff !important;
}

/* FORM */
[data-testid="stForm"] {
    background-color: #172522 !important;
    border: 1px solid #365c4d;
    border-radius: 15px;
    padding: 20px;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background-color: #1c2b27 !important;
    border: 1px solid #365c4d;
    border-radius: 10px;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #101817;
}

::-webkit-scrollbar-thumb {
    background: #367b58;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# SAMPLE DATA
# ==========================================

sample_data = pd.DataFrame([
    {
        "Village": "Demo Village A",
        "Facility": "Demo Primary Health Centre",
        "Type": "PHC",
        "Contact": "Not verified",
        "Ambulance": "Not verified",
        "Address": "Demo address",
        "Notes": "Sample data only"
    },
    {
        "Village": "Demo Village B",
        "Facility": "Demo Rural Hospital",
        "Type": "Rural Hospital",
        "Contact": "Not verified",
        "Ambulance": "Not verified",
        "Address": "Demo address",
        "Notes": "Sample data only"
    }
])

DATA_FOLDER = "jeevansetu_data"

os.makedirs(DATA_FOLDER, exist_ok=True)

VILLAGE_FILE = os.path.join(
    DATA_FOLDER,
    "village_directory.csv"
)

REQUEST_FILE = os.path.join(
    DATA_FOLDER,
    "assistance_requests.csv"
)

if not os.path.exists(VILLAGE_FILE):
    sample_data.to_csv(VILLAGE_FILE, index=False)


# ==========================================
# DATA FUNCTIONS
# ==========================================

def load_village_data():
    try:
        return pd.read_csv(VILLAGE_FILE)
    except Exception:
        return sample_data.copy()


def load_requests():
    if os.path.exists(REQUEST_FILE):
        try:
            return pd.read_csv(REQUEST_FILE)
        except Exception:
            return pd.DataFrame()

    return pd.DataFrame()


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.markdown("""
<div style="text-align:center;padding:15px;">
    <h1>🌿</h1>
    <h2 style="color:#18794e;">JeevanSetu</h2>
    <p>Rural Healthcare & Youth Employment Hub</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🏥 Village Directory",
        "📝 Assistance Request",
        "⚙️ Hub Operations",
        "📊 Impact Dashboard",
        "ℹ️ About & Safety"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Academic Prototype | Offline-first Healthcare Information"
)


# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌿 JeevanSetu</h1>
        <h3>Bridging Rural Communities with Healthcare Access</h3>
        <p>
        An offline-first rural healthcare information and
        coordination platform designed to connect communities
        with healthcare facilities and trained local support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Our Mission")

    st.write("""
    JeevanSetu aims to improve access to healthcare
    information in rural communities where hospitals,
    healthcare workers, transportation and reliable
    internet connectivity may be limited.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🏥 Healthcare Access</h3>
            <p>
            Find stored information about nearby health
            facilities, locations and contact details.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📱 Offline-First Design</h3>
            <p>
            Access previously saved directory information
            when internet connectivity is unavailable.
            </p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🤝 Local Youth Employment</h3>
            <p>
            Create potential paid roles for trained local
            youth in directory maintenance and coordination.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h3>🚑 Emergency Coordination</h3>
            <p>
            Display stored emergency contacts and support
            coordination with authorized providers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Our Objectives")

    objectives = [
        "Improve access to healthcare facility information.",
        "Maintain a locally stored healthcare directory.",
        "Support coordination with authorized providers.",
        "Explore sustainable local youth employment."
    ]

    for item in objectives:
        st.markdown(f"- {item}")

    st.warning(
        "Academic demo only. Sample information is not "
        "verified and this app does not dispatch ambulances "
        "or provide medical advice."
    )


# ==========================================
# VILLAGE DIRECTORY
# ==========================================

elif page == "🏥 Village Directory":

    st.title("🏥 Village Healthcare Directory")

    st.write(
        "Search healthcare facility information "
        "and add directory entries."
    )

    df = load_village_data()

    search_village = st.text_input(
        "Search by Village Name"
    )

    if search_village:
        df = df[
            df["Village"].astype(str).str.contains(
                search_village,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("➕ Add Healthcare Facility")

    with st.form("add_facility_form"):

        village = st.text_input("Village Name")

        facility = st.text_input(
            "Hospital / PHC Name"
        )

        facility_type = st.selectbox(
            "Facility Type",
            [
                "PHC",
                "Rural Hospital",
                "Government Hospital",
                "Private Hospital",
                "Other"
            ]
        )

        contact = st.text_input(
            "Verified Contact Number"
        )

        ambulance = st.text_input(
            "Authorized Ambulance Contact"
        )

        address = st.text_area("Facility Address")

        notes = st.text_area("Additional Information")

        submitted = st.form_submit_button(
            "Save Facility"
        )

        if submitted:

            if village.strip() and facility.strip():

                new_data = pd.DataFrame([{
                    "Village": village,
                    "Facility": facility,
                    "Type": facility_type,
                    "Contact": contact,
                    "Ambulance": ambulance,
                    "Address": address,
                    "Notes": notes
                }])

                updated_df = pd.concat(
                    [load_village_data(), new_data],
                    ignore_index=True
                )

                updated_df.to_csv(
                    VILLAGE_FILE,
                    index=False
                )

                st.success(
                    "Facility saved successfully!"
                )

                st.rerun()

            else:
                st.error(
                    "Please enter village and facility name."
                )

    st.info(
        "Verify facility and ambulance details with "
        "authorized providers before real-world use."
    )
# ==========================================
# ASSISTANCE REQUEST PAGE
# ==========================================

elif page == "📝 Assistance Request":

    st.title("📝 Community Assistance Request")

    st.write(
        "Record a demo request for local healthcare "
        "information and coordination."
    )

    st.warning(
        "This is an academic demo. It does not contact "
        "hospitals or dispatch ambulances."
    )

    with st.form("assistance_form"):

        name = st.text_input(
            "Requester Name (Optional)"
        )

        village = st.text_input(
            "Village Name"
        )

        assistance_type = st.selectbox(
            "Type of Assistance",
            [
                "Healthcare Facility Information",
                "Transport Coordination",
                "General Healthcare Support",
                "Other"
            ]
        )

        description = st.text_area(
            "Brief Request Details",
            max_chars=300
        )

        consent = st.checkbox(
            "I understand this is an academic demo "
            "and not a real emergency service."
        )

        submitted = st.form_submit_button(
            "Submit Demo Request"
        )

        if submitted:

            if not village.strip():

                st.error(
                    "Please enter village name."
                )

            elif not consent:

                st.error(
                    "Please confirm that this is a demo."
                )

            else:

                new_request = pd.DataFrame([{
                    "Request ID": datetime.now().strftime(
                        "%Y%m%d%H%M%S"
                    ),
                    "Date": datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                    "Requester": name,
                    "Village": village,
                    "Type": assistance_type,
                    "Description": description,
                    "Status": "Demo - Not Dispatched"
                }])

                if os.path.exists(REQUEST_FILE):

                    old_requests = load_requests()

                    updated_requests = pd.concat(
                        [old_requests, new_request],
                        ignore_index=True
                    )

                else:

                    updated_requests = new_request

                updated_requests.to_csv(
                    REQUEST_FILE,
                    index=False
                )

                st.success(
                    "Demo request recorded locally!"
                )

                st.info(
                    "No hospital or ambulance has been "
                    "contacted. This is only a demo record."
                )


# ==========================================
# HUB OPERATIONS PAGE
# ==========================================

elif page == "⚙️ Hub Operations":

    st.title("⚙️ Hub Operations")

    st.write(
        "Manage healthcare directory entries and "
        "review locally stored demo requests."
    )

    # DIRECTORY MANAGEMENT

    st.subheader(
        "🏥 Healthcare Directory Management"
    )

    directory = load_village_data()

    st.metric(
        "Total Directory Entries",
        len(directory)
    )

    st.dataframe(
        directory,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # REQUEST MANAGEMENT

    st.subheader(
        "📋 Recorded Demo Requests"
    )

    requests = load_requests()

    if requests.empty:

        st.info(
            "No demo requests have been recorded yet."
        )

    else:

        st.dataframe(
            requests,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            label="Download Demo Requests CSV",
            data=requests.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="jeevansetu_requests.csv",
            mime="text/csv"
        )

    st.divider()

    # YOUTH EMPLOYMENT

    st.subheader(
        "🤝 Proposed Local Youth Employment"
    )

    roles = [
        (
            "Directory Assistant",
            "Maintain facility information and verify updates."
        ),
        (
            "Community Support Assistant",
            "Help residents understand available resources."
        ),
        (
            "Data Entry Assistant",
            "Maintain records and prepare basic reports."
        ),
        (
            "Coordination Assistant",
            "Support communication with authorized providers."
        )
    ]

    for role, description in roles:

        st.markdown(
            f"""
            <div class="card">
                <h3>{role}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "These are proposed employment roles. Actual "
        "implementation requires funding, training "
        "and local partnerships."
    )
# ==========================================
# IMPACT DASHBOARD
# ==========================================

elif page == "📊 Impact Dashboard":

    st.title("📊 Impact Dashboard")

    st.write(
        "Overview of healthcare directory entries "
        "and demo requests stored in JeevanSetu."
    )

    directory = load_village_data()
    requests = load_requests()

    total_facilities = len(directory)

    total_villages = (
        directory["Village"].nunique()
        if not directory.empty
        else 0
    )

    total_requests = len(requests)

    # METRIC CARDS

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {total_facilities}
                </div>
                <div>Directory Entries</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {total_villages}
                </div>
                <div>Villages Listed</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {total_requests}
                </div>
                <div>Demo Requests Recorded</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # FACILITY DISTRIBUTION

    st.subheader("🏥 Facility Distribution")

    if not directory.empty:

        facility_counts = (
            directory["Type"]
            .value_counts()
            .reset_index()
        )

        facility_counts.columns = [
            "Facility Type",
            "Count"
        ]

        st.bar_chart(
            facility_counts.set_index("Facility Type")
        )

    else:
        st.info("No facility data available.")

    st.divider()

    # ASSISTANCE REQUEST ANALYSIS

    st.subheader("📋 Requests by Assistance Type")

    if (
        not requests.empty
        and "Type" in requests.columns
    ):

        request_counts = (
            requests["Type"]
            .value_counts()
            .reset_index()
        )

        request_counts.columns = [
            "Assistance Type",
            "Count"
        ]

        st.bar_chart(
            request_counts.set_index("Assistance Type")
        )

    else:
        st.info(
            "Request analytics will appear after "
            "demo requests are recorded."
        )

    st.caption(
        "Dashboard metrics represent local demo records "
        "only. They do not measure actual healthcare impact."
    )


# ==========================================
# ABOUT & SAFETY
# ==========================================

elif page == "ℹ️ About & Safety":

    st.title("ℹ️ About JeevanSetu")

    st.markdown("""
    <div class="hero">
        <h2>JeevanSetu</h2>
        <h3>Rural Emergency Healthcare Access through Offline Technology</h3>
        <p>
        A social entrepreneurship concept that aims to
        improve rural healthcare information access
        through offline-first technology and local
        community coordination.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # PROBLEM

    st.subheader("1. The Problem")

    st.write("""
    Some rural communities face challenges such as
    long distances to healthcare facilities, limited
    availability of healthcare workers and unreliable
    internet connectivity.

    These challenges can make it difficult to find
    healthcare information quickly.
    """)

    # SOLUTION

    st.subheader("2. Our Proposed Solution")

    st.write("""
    JeevanSetu proposes a locally accessible healthcare
    directory with stored facility information and
    coordination support through trained local youth.

    The concept focuses on healthcare information access,
    not diagnosis or medical treatment.
    """)

    # DESIGN THINKING

    st.subheader("3. Design Thinking Approach")

    steps = [
        (
            "Empathize",
            "Understand the challenges faced by rural residents."
        ),
        (
            "Define",
            "Identify difficulties in accessing healthcare information."
        ),
        (
            "Ideate",
            "Explore offline directories and local coordination."
        ),
        (
            "Prototype",
            "Build a Streamlit-based healthcare information hub."
        ),
        (
            "Test",
            "Gather feedback and improve the prototype."
        )
    ]

    for title, description in steps:

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # SAFETY

    st.subheader("4. Safety and Limitations")

    st.warning("""
    IMPORTANT:

    1. This application is an academic prototype.

    2. Sample healthcare facility information is fictional
       and is not verified.

    3. The app does not diagnose illnesses or recommend
       medical treatment.

    4. The app does not dispatch ambulances or automatically
       contact hospitals.

    5. Offline access is limited to information already
       stored on the device.

    6. During a communication blackout, the app cannot
       send remote notifications or requests.

    7. Real deployment requires verified contacts,
       authorized partnerships, privacy safeguards,
       training and appropriate permissions.
    """)

    # PROJECT INFORMATION

    st.subheader("5. Project Information")

    st.write("**Project Name:** JeevanSetu")

    st.write(
        "**Project Theme:** Social Entrepreneurship "
        "and Rural Healthcare Access"
    )

    st.write(
        "**Technology:** Python, Streamlit and Pandas"
    )

    st.write(
        "**Academic Year:** 2026–2027"
    )

    st.markdown("""
    <div class="footer">
        JeevanSetu | Rural Healthcare & Youth Employment Hub
        <br>
        Academic Prototype | 2026–2027
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# END OF APPLICATION
# ==========================================