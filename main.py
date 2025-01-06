import streamlit as st
from PIL import Image

def main():
    # Inject custom CSS with necessary <link> tags for fonts
    st.markdown(
        """
        <style>

        .large-title {
            font-family: cursive;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }

        .e1nzilvr1{
        
            font-family: cursive;
            font-weight: bold;
        }

        .e1nzilvr5{
            font-family: cursive;
            font-weight: bold;
        }

        .spaced-section {
            margin-bottom: 30px;
        }

        .centered-text {
            text-align: center;
        }
        .st-emotion-cache-1v0mbdj img{
            width: 130px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    # Sidebar Navigation
    menu = ["Home", "Products", "About"]
    choice = st.sidebar.radio("", menu)

    if choice == "Home":
        home_page()
    elif choice == "Products":
        products_page()
    elif choice == "About":
        about_page()

# def home_page():
#     st.markdown('<div class="large-title">WILLWIN ENTERPRISES</div>', unsafe_allow_html=True)
#     st.markdown('<div class="centered-text spaced-section">QUALITY, PERFECTION & RELIABILITY DELIVERED</div>', unsafe_allow_html=True)

#     st.write("""
#     In an industry that demands highly competitive and precision-based products, WILLWIN ENTERPRISES is committed to excellent service, up-to-date technological upgradation, state-of-the-art infrastructure, and highly qualified human resources. We supply machined parts ready to assemble components for various industries.
#     """)

#     st.write("""
#     #### VISION:
#     TO SUPPLY QUALITY PRODUCTS BY INCORPORATING THE NEEDS AND REQUIREMENTS OF CUSTOMERS
#     """)

#     st.write("""
#     #### MISSION:
#     TO ACHIEVE HIGHEST CUSTOMER SATISFACTION BY CONTINUAL IMPROVEMENT OF THE PROCESSES AND INCREASING EFFECTIVENESS OF QUALITY MANAGEMENT SYSTEM BY EMPLOYEE INVOLVEMENT
#     """)

#     st.write("""
#     #### CULTURE:
#     CUSTOMER SATISFACTION QUALITY EXCELLENCE
#     """)

#     st.write("""
#     #### QUALITY POLICY:
#     WE AT WILLWIN ENTERPRISES ARE COMMITTED TO SUPPLY PRECISION MACHINED COMPONENTS AND SUB-ASSEMBLIES WITH HIGH QUALITY TO MEET CUSTOMERS' DESIRED REQUIREMENTS.
#     """)

#     st.write("""
#     #### PRODUCT RANGE:
#     - MATERIAL HANDLING EQUIPMENT
#     - CRANES SPARES
#     - HOISTS SPARES
#     - ELEVATOR PARTS
#     - AUTOMOBILE PARTS
#     - ACTUATOR GEARBOXES
#     - ALL TYPES OF VALVES
#     - PUMPS COMPONENTS
#     - ALL TYPES OF COMPRESSOR SPARES
#     - AGRICULTURAL IMPLEMENTS
#     - FOOD INDUSTRY SPARES
#     - TRACTOR PARTS
#     - CEMENT PLANTS PARTS
#     - SUGAR PLANTS PARTS
#     - FLOUR & RICE MILL MACHINERY SPARES
#     """)
def home_page():
    # Create two columns for the title and the logo
    col1, col2 = st.columns([3, 1])  # Adjust the proportions as needed
    
    with col1:
        # Add the title in the first column
        st.markdown('<div class="large-title">WILLWIN ENTERPRISES</div>', unsafe_allow_html=True)
    
    with col2:
        # Add the logo in the second column
        logo_path = "images/logo.png"  # Update with the correct path to your logo
        try:
            logo_image = Image.open(logo_path)
            st.image(logo_image, use_container_width =True)
        except FileNotFoundError:
            st.error("Logo image not found. Please ensure the logo path is correct.")

    # Centered subtitle below the title and logo
    st.markdown('<div class="centered-text spaced-section">QUALITY, PERFECTION & RELIABILITY DELIVERED</div>', unsafe_allow_html=True)

    # Remaining content
    st.write("""
    In an industry that demands highly competitive and precision-based products, WILLWIN ENTERPRISES is committed to excellent service, up-to-date technological upgradation, state-of-the-art infrastructure, and highly qualified human resources. We supply machined parts ready to assemble components for various industries.
    """)
    st.write("""
    #### VISION:
    TO SUPPLY QUALITY PRODUCTS BY INCORPORATING THE NEEDS AND REQUIREMENTS OF CUSTOMERS
    """)
    st.write("""
    #### MISSION:
    TO ACHIEVE HIGHEST CUSTOMER SATISFACTION BY CONTINUAL IMPROVEMENT OF THE PROCESSES AND INCREASING EFFECTIVENESS OF QUALITY MANAGEMENT SYSTEM BY EMPLOYEE INVOLVEMENT
    """)
    st.write("""
    #### CULTURE:
    CUSTOMER SATISFACTION QUALITY EXCELLENCE
    """)
    st.write("""
    #### QUALITY POLICY:
    WE AT WILLWIN ENTERPRISES ARE COMMITTED TO SUPPLY PRECISION MACHINED COMPONENTS AND SUB-ASSEMBLIES WITH HIGH QUALITY TO MEET CUSTOMERS' DESIRED REQUIREMENTS.
    """)
    st.write("""
    #### PRODUCT RANGE:
    - MATERIAL HANDLING EQUIPMENT
    - CRANES SPARES
    - HOISTS SPARES
    - ELEVATOR PARTS
    - AUTOMOBILE PARTS
    - ACTUATOR GEARBOXES
    - ALL TYPES OF VALVES
    - PUMPS COMPONENTS
    - ALL TYPES OF COMPRESSOR SPARES
    - AGRICULTURAL IMPLEMENTS
    - FOOD INDUSTRY SPARES
    - TRACTOR PARTS
    - CEMENT PLANTS PARTS
    - SUGAR PLANTS PARTS
    - FLOUR & RICE MILL MACHINERY SPARES
    """)



def products_page():
    st.title("Products Gallery")

    # Grid for product images
    image_paths = ["pic1.png", "pic2.png", "pic3.png", "pic4.png", "pic5.png", 
                   "pic6.png", "pic7.png", "pic8.png", "pic9.png", "pic10.png", "pic11.png", "pic12.png"]

    for i in range(0, len(image_paths), 2):
        cols = st.columns(2)
        for col, img_path in zip(cols, image_paths[i:i+2]):
            with col:
                image = Image.open(f"images/{img_path}")
                resized_image = image.resize((250, 250))
                st.image(resized_image, use_container_width =True)

def about_page():
    st.title("About Us")
    st.write("""
    WILLWIN ENTERPRISES IS A PROPRIETORSHIP ESTABLISHED IN 2018, MANAGED BY MR. ABDULHAMID SHAIKH AND HAS A GOOD REPUTATION IN THE FIELD OF FOUNDRY AS WELL AS MACHINING OF PRECISION MACHINED PARTS READY TO ASSEMBLY COMPONENTS FOR VALVES & PUMPS INDUSTRY, TRACTOR INDUSTRY, FOOD INDUSTRY & MATERIAL HANDLING INDUSTRY, CRANE'S, HOIST’S, ELEVATOR PART’S, ALL TYPES OF COMPRESSOR SPARES, AGRICULTURE IMPLEMENTS, CEMENT & SUGAR INDUSTRY, FLOUR & RICE MILL MACHINERY SPARES IN GRADED CAST IRON, S.G. IRON, ALLOY STEEL CASTINGS, FERROUS & NON FERROUS MACHINED COMPONENTS, SPECIALISED IN “V” GROOVE MOTOR PULLEY’S & FLYWHEELS.

    LOCATION: SMART CITY BELGAUM, KARNATAKA STATE, INDIA. BELGAUM IS ONE OF THE MOST PROMISING INDUSTRIAL CENTERS OF KARNATAKA, 150 KMS. (90 MILES) FROM GOA AND ABOUT 500 KMS. (300 MILES) FROM MUMBAI PORT. IT IS WELL CONNECTED BY AIR, RAIL & ROAD.

    TEAM: THE COMPANY HAS WELL-QUALIFIED AND MOTIVATED TEAM OF ENGINEERS AND SKILLED PROFESSIONALS EXPERIENCED IN THE FIELD OF ENGINEERING WITH THE LATEST FACILITIES REQUIRED TO ACHIEVE AND SET GOALS. THE COMPANY TEAM FORCE OF 10-15 PEOPLE.
    """)

if __name__ == "__main__":
    main()
