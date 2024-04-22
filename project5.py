#REQUIRED LIBRARIES
import streamlit as st
from streamlit_option_menu import option_menu
import re
import pickle
import numpy as np

# SETTING PAGE CONFIGURATIONS
st.set_page_config(page_title= "Industrial Copper Modelling Application| By Jameel",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This Application is created by *Jameel*!"""})
st.markdown("<h1 style='text-align: center; color: #00035E;'>INDUSTRIAL COPPER MODELLING APPLICATION</h1>", unsafe_allow_html=True)

# SETTING-UP BACKGROUND IMAGE
def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAsJCQcJCQcJCQkJCwkJCQkJCQsJCwsMCwsLDA0QDBEODQ4MEhkSJRodJR0ZHxwpKRYlNzU2GioyPi0pMBk7IRP/2wBDAQcICAsJCxULCxUsHRkdLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCz/wAARCADqARgDASIAAhEBAxEB/8QAFwABAQEBAAAAAAAAAAAAAAAAAAECA//EABsQAQEAAwEBAQAAAAAAAAAAAAAhARFhMQIy/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAEFB//EABURAQEAAAAAAAAAAAAAAAAAAAAR/9oADAMBAAIRAxEAPwDpnOd5SmfcjfcaKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKUAKABn3IZ9yAAoIAAKAgAAqAAoIKgAKCAACgIAAKgAKCCoACggAAAGfchn3JAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAhAAgBn3IZ9yAAoIAAKAgAAqAAoIKgAKCAACgIAAKgAKCCoACggAAAGfchn3IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABn3IZ9yAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZ9yGfckAVIQAIQFEhAAhAVCEAVIQFQhAFSEACEBRIQAIQFQhAFSEBUIQBUhAAhAAgC59yhn3IAqKCAAoAIACoqAKigIqAKiggAKACAAqKgCooCKgCooIAAABn3IZ9yAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZ9yGfcgCooIACgAgAKioAqKAioAqKCAAoAIACoqAKigIqAKiggAAAGfckM+5AIRQEhFQCEUBIQUEhFASEFBIRUAhFASEVAIRQEhBQSEUBIQUEhFQCEUBIRUAgoCZ9yGfcgAKCAACgIAAKgAKCCoACggAAoCAACoACggqAAoIAAABn3IZ9yAAoIAAKAgAAqAAoIKgAKCAACgIAAKgAKCCoACggAAAGfchn3IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABn3I39/rLIib4b40KVnfDfGgKzvhvjQFZ3w3xoCs74b40BWd8N8aArO+G+NAVnfDfGgKzvhvjQFZ3w3xoCs74b40BWd8N8aArO+G+NAVnfDfGgKzvhvjQFZ3w3xoCs74NAV//2Q==");
                        background-size: cover}}
                     </style>""",unsafe_allow_html=True)    
setting_bg()

# CREATING OPTION MENU
with st.sidebar:
    Option = option_menu('Menu', ["Home","Predictions"], 
                        icons=["house-door-fill","card-text"],
                        default_index=0,
                        styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", "--hover-color": "#00035E"},
                                "icon": {"font-size": "25px"},
                                "container" : {"max-width": "3000px"},
                                "nav-link-selected": {"background-color": "#0AFDDC"}})
    
#STREAMLIT PART
if Option=="Home":
    st.markdown("## <span style='color:#00035E'>**Technologies Used :**</span> Python, Streamlit, Pandas, Matplotlib.pyplot, Scikit-learn, Decision tree regressor and classifier , GridsearchCV, Evaluation metrics Pickling", unsafe_allow_html=True)
    st.markdown("## <span style='color:#00035E'>**Description :**</span> This application involves predicting the selling price of copper products and determining their status as either 'Won' or 'Lost'. The application is trained using copper data, which includes exploring dataset skewness and outliers, performing data transformation and cleaning, and implementing decision tree machine learning regression for predicting selling prices and classification for determining status.", unsafe_allow_html=True)

elif Option=="Predictions":
    tab1,tab2 = st.tabs(["$\huge SELLING PRICE $", "$\huge STATUS $"])
    with tab1:
        #Providing all the possible values for dropdown menus
        status_options = ['Won', 'Lost', 'Not lost for AM', 'Revised ', 'To be approved', 'Draft', 'Offered', 'Offerable', 'Wonderful']
        item_type_option = ['W', 'S', 'PL', 'Others', 'WI', 'IPL', 'SLAWR']
        country_options = [28.,  25.,  30.,  32.,  38.,  78.,  27.,  77., 113.,  79.,  26., 39.,  40.,  84.,  80., 107.,  89.]
        application_options = [10., 41., 28., 59., 15.,  4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79.,  3., 99.,  2.,  5., 39., 69., 70., 65., 58., 68.]
        product = ['611728', '611733', '611993', '628112', '628117', '628377', '640400', '640405', '640665', '164141591', '164336407', '164337175', '929423819', '1282007633', '1332077137', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

        #Taking inputs from user for selling price prediction
        with st.form("user_inputs"):
            col1,col2,col3 = st.columns([5,2,5])
            with col1:
                st.write(' ')
                status = st.selectbox("Status", status_options, key=1)
                item_type = st.selectbox("Item Type", item_type_option, key=2)
                country = st.selectbox("Country", sorted(country_options), key=3)
                application = st.selectbox("Application", sorted(application_options), key=4)
                product_ref = st.selectbox("Product Reference", product, key=5)
            with col3:
                st.write(f'<h5 style="color:#ee4647;">NOTE: Min & Max given for reference, you can enter any value</h5>', unsafe_allow_html=True)
                quantity_tons = st.text_input("Enter the Quantity in Tons (Min: 611728 & Max: 1722207579)")
                thickness = st.text_input("Enter Thickness (Min: 0.18 & Max: 400)")
                width = st.text_input("Enter Width (Min: 1, Max: 2990)")
                customer = st.text_input("Select Customer ID (Min: 12458, Max: 30408185)")
                submit_button = st.form_submit_button(label="PREDICT SELLING PRICE")
                
                #Prediction button
                st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #00035E;
                        color: white;
                        width: 100%;
                    }
                    </style>
                """, unsafe_allow_html=True)

            #Checking inputs as they are in correct format
            flag = 0
            pattern = "^(?:\d+|\d*\.\d+)$"
            for i in [quantity_tons, thickness, width, customer]:
                if re.match(pattern, i):
                    pass
                else:
                    flag = 1
                    break
        if submit_button and flag==1:
            if len(i)==0:
                st.write("please enter a valid numnber, spaces are not allowed")
            else:
                st.write("You have entered a invalid value:", i)

        #Importing all the required models for prediction
        if submit_button and flag==0:
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/selling_price_prediction.pkl", 'rb') as file:
                loaded_model = pickle.load(file)
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/scaler.pkl", 'rb') as f:
                scaler_loaded = pickle.load(f)
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/encoder_it.pkl", 'rb') as f:
                loaded_encoder_it = pickle.load(f)
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/encoder_s.pkl", 'rb') as f:
                loaded_encoder_s = pickle.load(f)

            #Encoding, correcting data types, scaling and predicting
            inputs = np.array([[np.log(float(quantity_tons)), application, np.log(float(thickness)), float(width), country, float(customer), int(product_ref), item_type, status]])
            Encoding_it = loaded_encoder_it.transform(inputs[:, [7]]).toarray()
            Encoding_status = loaded_encoder_s.transform(inputs[:, [8]]).toarray()
            Encoded_inputs = np.concatenate((inputs[:, [0,1,2,3,4,5,6]], Encoding_it, Encoding_status), axis=1)
            Transformed_inputs = scaler_loaded.transform(Encoded_inputs)
            Prediction = loaded_model.predict(Encoded_inputs)[0]
            st.write('<h2 style="color:#00035E; display: inline; font-size: 36px;">Predicted Selling Price: {:.2f}</h2>'.format(np.exp(Prediction)), unsafe_allow_html=True)

    #For Predicting Status
    with tab2:
        ##Taking inputs from user for status prediction
        with st.form("user_inputs_2"):
            col1,col2,col3 = st.columns([5, 2, 5])
            with col1:
                st.write(f'<h5 style="color:#ee4647;">NOTE: Min & Max given for reference, you can enter any value</h5>', unsafe_allow_html=True)
                quantity_tons_s = st.text_input("Enter Quantity Tons (Min: 611728 & Max: 1722207579)")
                thickness_s = st.text_input("Enter Thickness (Min: 0.18 & Max: 400)")
                width_s = st.text_input("Enter Width (Min: 1, & Max: 2990)")
                customer_s = st.text_input("Enter Customer ID (Min: 12458 & Max: 30408185)")
                selling_price_s = st.text_input("Enter Selling Price (Min: 1 & Max: 100001015)")

            with col3:
                st.write(' ')
                item_type_s = st.selectbox("Item Type", item_type_option, key=6)
                country_s = st.selectbox("Country", sorted(country_options), key=7)
                application_s = st.selectbox("Application", sorted(application_options), key=8)
                product_ref_s = st.selectbox("Product Reference", product, key=9)
                submit_button_s = st.form_submit_button(label="PREDICT STATUS")

            #Checking inputs as they are in correct format
            flag_s = 0
            pattern_s = "^(?:\d+|\d*\.\d+)$"
            for k in [quantity_tons_s, thickness_s, width_s, customer_s, selling_price_s]:
                if re.match(pattern, k):
                    pass
                else:
                    flag_s = 1
                    break

        if submit_button_s and flag_s==1:
            if len(k)==0:
                st.write("please enter a valid number, spaces are not allowed")
            else:
                st.write("You have entered an invalid value: ", k)

        #Importing all the required models for prediction
        if submit_button_s and flag_s==0:
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/status_prediction.pkl", 'rb') as file:
                loaded_model_s = pickle.load(file)
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/status_scaler.pkl", 'rb') as f:
                scaler_loaded_s = pickle.load(f)
            with open(r"C:/Users/Jameel Ahamed/OneDrive/Desktop/Python Pgm/s_encoder.pkl", 'rb') as f:
                encoder_s = pickle.load(f)

            #Encoding, correcting data types, scaling and predicting
            inputs_s = np.array([[np.log(float(quantity_tons_s)), np.log(float(selling_price_s)), application_s, np.log(float(thickness_s)), float(width_s), country_s, float(customer_s), int(product_ref_s), item_type_s]])
            encoding_it_s = encoder_s.transform(inputs_s[:, [8]]).toarray()
            encoded_inputs_s = np.concatenate((inputs_s[:, [0, 1, 2, 3, 4, 5, 6, 7]], encoding_it_s), axis=1)
            Transformed_inputs_s = scaler_loaded_s.transform(encoded_inputs_s)
            Prediction_s = loaded_model_s.predict(Transformed_inputs_s)
            if Prediction_s == 1:
                st.write('<h2 style="color:#225711;">The Status is Won</h2>', unsafe_allow_html=True)
            else:
                st.write('<h2 style="color:#F53526;">The Status is Lost</h2>', unsafe_allow_html=True)