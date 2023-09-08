import streamlit as st
import requests
from streamlit_option_menu import option_menu
import json
import pandas as pd
import plotly.express as px
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit.components.v1 import html
import base64
import io
from packageKPS import *
from packageCharts import *
from html_shortcuts import *
from PIL import Image
import pdfkit
import mysql.connector
import tempfile
# Define the HTML template for the PDF report


# Define the HTML template for the PDF report
def generate_pdf_report(form_data):
    # Create an HTML string containing the form data
    html = f"<h1>Form Data</h1>"
    for key, value in form_data.items():
        html += f"<p><strong>{key}:</strong> {value}</p>"

    # Generate the PDF report from the HTML
    pdfkit.from_string(html, 'form_data_report.pdf')


# def generate_pdf_report(form_data):
#     st.write("inside function")
#     st.write(form_data)
#     # Create an HTML string containing the form data
#     html = f"<h1>Form Data</h1>"
#     for key, value in form_data.items():
#         html += f"<p><strong>{key}:</strong> {value}</p>"
#     st.markdown(html,unsafe_allow_html= True)

    
#     # Generate the PDF report from the HTML
#     pdf=pdfkit.from_string(html, 'form_data_report.pdf')
#     st.balloons()

    

#     st.download_button(
#         "⬇️ Download report",
#         data=pdf,
#         file_name="report.pdf",
#         mime="application/octet-stream",
#     )

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

def run_query(conn,query):
    with conn.cursor() as cur:
        cur.execute(query)
        columnsnames=cur.column_names
        return cur.fetchall(),columnsnames
    
# Function to create a new record
def create_record(id, year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio):
    conn = init_connection()
    mycursor = conn.cursor()
    sql = "INSERT INTO forms (koispe_id, creation_date, year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio) VALUES (%s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (str(id), year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio)
    mycursor.execute(sql, val)
    conn.commit()
    return mycursor

def main():
 
    
    
    #st.write(home())
    st.set_page_config(
        page_title="Koispe Dashboard",
        page_icon="✅",
        layout="wide",
    )    

    
 
  
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


    #st.markdown(css_style, unsafe_allow_html=True)

            # Load the JavaScript function code
    with open("animated_counter.js", "r") as file:
            js_code = file.read()

    with open("style2.css", "r") as file:
            css_code = file.read()
    st.sidebar.image("https://koispesupport.gr/wp-content/uploads/2023/06/Logo-Koispe-203x90.png", width=100)


    # st.sidebar.title("KPI's Dashboard")
    id=get_url_params()
    # st.write("URL ID FROM VIDAVO:",id)
    # st.write("ID from Flask application: ",id)


    # image = Image.open('https://dreamleague-soccerkits.com/wp-content/uploads/2021/07/Real-Madrid-Logo.png','rb')
    # with st.container():
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         pass
    #     with col2:
    #         st.image("https://cmtprooptiki.gr/api/profile_images/"+str(id)+".png", width=300)
    #     with col3:
    #         pass
    # https://app.koispesupport.gr/koispe/api/getkoispe?id=1128

    #VIDAVO API CALL SPEICIFIC KOISPE WITH ID


    kpdf=get_data_from_json(id)
    # kpdf=kpdf.fillna(0)
 

    # st.title("Πίνακας Δεικτών")
    # st.write(kpdf)

        # 1. as sidebar menu

    with st.sidebar:

            selected_option1 = option_menu("Μενού", ["Business Plan"],
                                icons=['table'],
                                menu_icon="cast", default_index=0,
                                
                                styles={
                                    "menu-title":{"display":"none"},
                                    "icon": {"font-size": "25px"}, 

                                    "container": {"padding": "0!important", "background-color": "#D3ECFA", "color": "#ffffff"},
                                    "nav-link": {"font-family": "Roboto","font-style": "normal","font-weight": "700","line-height": "220%" ,"background-color": "#D3ECFA", "color": "#004BCF", "text-align": "left", "margin": "0px", "--hover-color": "#004BCF"},
                                    "nav-link-selected": {"color": "#ffffff", "background-color": "#004BCF"},
                                }
                                )

   
    # Empty container for the right side content
    content_container = st.empty()
        

    # elif selected_option1=="Αναλυτικός Πίνακας Δεικτών":
    #     e_button8(id,kpdf,js_code,css_code) 
    if selected_option1=="Business Plan":
        e_button9(id)

def e_button9(id):
    conn = init_connection()
    st.write("work on MACOS")
    st.title("Edit Days MAC off")
    # id = st.number_input("Enter ID", userid)
    # total_days = st.number_input("Enter total days off", min_value=0, value=total_daysoff)
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))
    mycursor = conn.cursor()
    st.write("Connection Established")

    if option == "Create":
        st.subheader("Create a Record")
        
        # Encapsulate the form using st.form
        with st.form(key="create_form"):
            year = st.selectbox("Select year", ["2021", "2022", "2023", "2024"])
            st.write("Selected Year", year)
            st.subheader("Στόχοι")
            st.text('Περιγράψτε τους στόχους που ελπίζετε να επιτύχετε.')
            q1_text = st.text_input("Γράψε ελεύθερο κείμενο", key="q1text")

            q1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τους στόχους που ελπίζετε να πετύχετε;", ["1", "2", "3", "4", "5"], horizontal=True)
            
            st.title("Περιγραφή της Επιχείρησης")

            st.text("""Δώστε μια θετική, συνοπτική και βασισμένη στην πραγματικότητα περιγραφή της επιχείρησής σας: με τι ασχολείται και τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη. 
            Περιγράψτε ειδικές δυνατότητες που θα κάνουν την επιχείρησή σας ελκυστική για πιθανούς πελάτες και θα προσδιορίσουν τους κύριους στόχους της εταιρείας σας.""")
            
            q2_text = st.text_input("Γράψε ελεύθερο κείμενο", key="q2text")
            
            q2_1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς με τι ασχολείται η επιχείρησή σας;", ["1", "2", "3", "4", "5"], horizontal=True)
            st.write('You selected ', q2_1_ans_radio)
            q2_2_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη;", ["1", "2", "3", "4", "5"], horizontal=True)
            st.write('You selected ', q2_2_ans_radio)

            st.subheader("Nομική οντότητα")
            st.text("""Αναφέρετε αν η επιχείρησή σας είναι μια εταιρεία μεμονωμένης ιδιοκτησίας, εταιρεία (τύπου) ή συνεργασία. Εάν χρειάζεται, ορίστε τον τύπο επιχείρησης (όπως είναι η βιομηχανία, το εμπόριο ή οι υπηρεσίες). 
            Εάν απαιτούνται άδειες χρήσης, περιγράψτε τις απαιτήσεις για την απόκτηση τους και το πού βρίσκεστε σε αυτή τη διαδικασία.
            Εάν δεν έχετε ήδη δηλώσει εάν πρόκειται για μια νέα ανεξάρτητη επιχείρηση, μια εξαγορά, ένα franchise ή μια επέκταση πρώην επιχείρησης, συμπεριλάβετε το εδώ.""")
            
            q3_text = st.text_input("Γράψε ελεύθερο κείμενο", key="q3text")
            q3_ans_radio = st.radio("Έχετε ορίσει επαρκώς την νομική οντότητα της επιχείρησής σας;", ["1", "2", "3", "4", "5"], horizontal=True)
            st.write('You selected ', q3_ans_radio)

            # Submit button inside the form
            submit_button = st.form_submit_button("Submit")

        # Check if the submit button is clicked
        if submit_button:
            # Call the create_record function to insert the data into the database
            create_record(id, year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio)
            
            # Display a success message
            st.success("Record Created Successfully!!!")
            
            # Calculate and display the result
            st.title("Result")
            st.text("Ποσοστό Ετοιμότητας")
            result_val = ((int(q1_ans_radio) + int(q2_1_ans_radio) + int(q2_2_ans_radio) + int(q3_ans_radio)) / 4) * 10
            st.write(result_val)
            fig = donut_pct_Chart(result_val, '#618abb', 'rgb(240,240,240)', ['% Ποσοστό Ετοιμότητας', ' '])
            st.plotly_chart(fig, use_container_width=True)
    ####################################################################
    ############ADMINISTRATION PART EDIT ##############################
#     conn = init_connection()
#     st.write("work on MACOS")
#     st.title("Edit Days MAC off")
#     # id=st.number_input("Enter ID",userid)
#     # total_days=st.number_input("Enter total days off",min_value=0,value=total_daysoff)
#     option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
#     mycursor=conn.cursor()
#     st.write("Connection Established")
#     if option=="Create":
#         st.subheader("Create a Record")
        
#         year=st.selectbox("Select year",["2021","2022","2023","2024"])
#         st.write("Selected Year",year)
#         st.subheader("Στόχοι")
#         st.text('Περιγράψτε τους στόχους που ελπίζετε να επιτύχετε.')
#         q1_text=st.text_input("Γράψε ελεύθερο κείμενο",key="q1text")

#         q1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τους στόχους που ελπίζετε να πετύχετε;",
#         ["1", "2", "3","4","5"])
#         st.title("Περιγραφή της Επιχείρησης")

#         st.text("""Δώστε μια θετική, συνοπτική και βασισμένη στην πραγματικότητα περιγραφή της επιχείρησής σας: με τι ασχολείται και τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη. 
#         Περιγράψτε ειδικές δυνατότητες που θα κάνουν την επιχείρησή σας ελκυστική για πιθανούς πελάτες και θα προσδιορίσουν τους κύριους στόχους της εταιρείας σας.""")
        
#         q2_text=st.text_input("Γράψε ελεύθερο κείμενο",key="q2text")
        
#         q2_1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς με τι ασχολείται η επιχείρησή σας;",
#         ["1", "2", "3","4","5"])
#         st.write('You selected ',q2_1_ans_radio)
#         q2_2_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη;",
#         ["1", "2", "3","4","5"])
#         st.write('You selected ',q2_2_ans_radio)

#         st.subheader("Nομική οντότητα")
#         st.text("""Αναφέρετε αν η επιχείρησή σας είναι μια εταιρεία μεμονωμένης ιδιοκτησίας, εταιρεία (τύπου) ή συνεργασία. Εάν χρειάζεται, ορίστε τον τύπο επιχείρησης (όπως είναι η βιομηχανία, το εμπόριο ή οι υπηρεσίες). 
# Εάν απαιτούνται άδειες χρήσης, περιγράψτε τις απαιτήσεις για την απόκτηση τους και το πού βρίσκεστε σε αυτή τη διαδικασία.
# Εάν δεν έχετε ήδη δηλώσει εάν πρόκειται για μια νέα ανεξάρτητη επιχείρηση, μια εξαγορά, ένα franchise ή μια επέκταση πρώην επιχείρησης, συμπεριλάβετε το εδώ.""")
        
#         q3_text=st.text_input("Γράψε ελεύθερο κείμενο",key="q3text")
#         q3_ans_radio = st.radio("Έχετε ορίσει επαρκώς την νομική οντότητα της επιχείρησής σας;",
#         ["1", "2", "3","4","5"])
#         st.write('You selected ',q3_ans_radio)

   
#         # st.text('Έχετε περιγράψει επαρκώς τους στόχους που ελπίζετε να πετύχετε;')
#         # q1_answer=st.text_input("Enter Email")
#         if st.button("Create"):
#             sql= "insert into forms(koispe_id,creation_date,year,q1_text,q1_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q3_text,q3_ans_radio) values(%s,now(),%s,%s,%s,%s,%s,%s,%s,%s)"
#             val= (str(id),year,q1_text,q1_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q3_text,q3_ans_radio)
#             mycursor.execute(sql,val)
#             conn.commit()
#             st.success("Record Created Successfully!!!")
#             st.title("Result")
#             st.text("Ποσοστό Ετοιμότητας")
#             result_val=((int(q1_ans_radio)+int(q2_1_ans_radio)+int(q2_2_ans_radio)+int(q3_ans_radio))/4)*10
#             st.write(result_val)
#             fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
#             st.plotly_chart(fig,use_container_width=True)
#############################end old##################################################
           

    if option=="Read":
        st.subheader("Read all Submitted Forms")
        mycursor.execute("select * from forms where koispe_id="+str(id)+"")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)
            # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]

        # Display the list of return_ids
        st.write(return_ids)
        st.write(str(return_ids))

    if option=="Update":
        st.subheader("Edit Submitted Forms")
        st.write("Select Form for editing")
        mycursor.execute("select * from forms where koispe_id="+str(id)+"")
        result = mycursor.fetchall()
        # for row in result:
        #     st.write(row)
            # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]
        return_creation_date=[row[2] for row in result]
        return_year=[row[3] for row in result]
        return_identifierform=["Year:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
        # st.write(return_identifierform)
         #getAllformsId
        # st.write(str(return_ids))
        # st.write(str(return_creation_date))
        # Convert the list of datetime objects to a list of strings
        date_str_list = [return_creation_date.strftime("%Y-%m-%d %H:%M:%S") for return_creation_date in return_creation_date]

        # st.write(date_str_list)
        # st.write(str(return_year))

        #option=st.selectbox("Select an Form",date_str_list)

        #st.write("You choose",str(option))

        selected_id = st.selectbox("Select a Form", options=return_identifierform, index=0)
        selected_id_index = return_identifierform.index(selected_id)
        selected_id_value = return_ids[selected_id_index]

        # Display the selected date and its corresponding ID
        st.write(f"Selected Date: {selected_id}")
        st.write(f"Corresponding ID: {selected_id_value}")
#show form fields for editing
        with st.form(key="edit_form"):

            if selected_id:
                mycursor.execute("select * from forms where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

                st.subheader("EDIT FORM")
                st.write("Selected Year",row[3])
                st.subheader("Στόχοι")
                st.text('Περιγράψτε τους στόχους που ελπίζετε να επιτύχετε.')
                # q1_text=st.text_input(placeholder=row[4],key="q1edit_text")
                # default_value=row[4]
                # st.write(default_value)
                q1_text = st.text_input("Enter Text:", value=row[4], key="q1edit_text")
                st.write(row[5])
                options = ["1", "2", "3", "4", "5"]

                # Default option index (5 corresponds to the default value "5")
                default_option_indexq1 = options.index(str(row[5]))
                q1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τους στόχους που ελπίζετε να πετύχετε;",options, default_option_indexq1, horizontal=True)
                st.title("Περιγραφή της Επιχείρησης")
                
                st.text("""Δώστε μια θετική, συνοπτική και βασισμένη στην πραγματικότητα περιγραφή της επιχείρησής σας: με τι ασχολείται και τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη. 
                Περιγράψτε ειδικές δυνατότητες που θα κάνουν την επιχείρησή σας ελκυστική για πιθανούς πελάτες και θα προσδιορίσουν τους κύριους στόχους της εταιρείας σας.""")
                
                q2_text=st.text_input("Γράψε ελεύθερο κείμενο",value=row[6],key="q2edit_text")

                default_option_indexq2_1=options.index(str(row[7]))
                q2_1_ans_radio = st.radio("Έχετε περιγράψει επαρκώς με τι ασχολείται η επιχείρησή σας;",options, default_option_indexq2_1, horizontal=True)
                st.write('You selected ',q2_1_ans_radio)
                
                default_option_indexq2_2=options.index(str(row[8]))
                q2_2_ans_radio = st.radio("Έχετε περιγράψει επαρκώς τι θα την κάνει μοναδική, ανταγωνιστική και επιτυχημένη;",options, default_option_indexq2_2, horizontal=True)
                st.write('You selected ',q2_2_ans_radio)

                st.subheader("Nομική οντότητα")
                st.text("""Αναφέρετε αν η επιχείρησή σας είναι μια εταιρεία μεμονωμένης ιδιοκτησίας, εταιρεία (τύπου) ή συνεργασία. Εάν χρειάζεται, ορίστε τον τύπο επιχείρησης (όπως είναι η βιομηχανία, το εμπόριο ή οι υπηρεσίες). 
                Εάν απαιτούνται άδειες χρήσης, περιγράψτε τις απαιτήσεις για την απόκτηση τους και το πού βρίσκεστε σε αυτή τη διαδικασία.
                Εάν δεν έχετε ήδη δηλώσει εάν πρόκειται για μια νέα ανεξάρτητη επιχείρηση, μια εξαγορά, ένα franchise ή μια επέκταση πρώην επιχείρησης, συμπεριλάβετε το εδώ.""")
                
                q3_text=st.text_input("Γράψε ελεύθερο κείμενο",value=row[9],key="q3edit_text")
                
                default_option_indexq3=options.index(str(row[10]))

                q3_ans_radio = st.radio("Έχετε ορίσει επαρκώς την νομική οντότητα της επιχείρησής σας;",options,default_option_indexq3, horizontal=True)
                st.write('You selected ',q3_ans_radio)

                       # Create a dictionary to store form data
                form_data = {
                    'Στόχοι': q1_text,
                    'Περιγραφή της Επιχείρησης': q2_text,
                    'Nομική οντότητα': q3_text,
                }


 
            else:
                st.write("Choose Form for editing")

            submit_button_edit = st.form_submit_button("Update")



        if submit_button_edit:
                        ########PDF CREATE
            # Create a dictionary to store form data
            generate_pdf_report(form_data)
            st.markdown("[Download PDF Report](form_data_report.pdf)", unsafe_allow_html=True)


            st.write("button click update")
            sql="update forms set q1_text=%s,q1_ans_radio=%s,q2_text=%s,q2_1_ans_radio=%s,q2_2_ans_radio=%s,q3_text=%s,q3_ans_radio=%s where id=%s"
            val=(q1_text,q1_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q3_text,q3_ans_radio,str(selected_id_value))
            mycursor.execute(sql,val)
            conn.commit()
            st.success("Record Update Successfully!!!")
            st.title("Result")
            st.text("Ποσοστό Ετοιμότητας")
            result_val=((int(q1_ans_radio)+int(q2_1_ans_radio)+int(q2_2_ans_radio)+int(q3_ans_radio))/4)*10
            st.write(result_val)
            fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
            st.plotly_chart(fig,use_container_width=True)
        
 







        # if st.button("Update"):
        #     st.write("button click update")
        #     sql="update forms set q1_text=%s,q1_ans_radio=%s,q2_text=%s,q2_1_ans_radio=%s,q2_2_ans_radio=%s,q3_text=%s,q3_ans_radio=%s where id=%s"
        #     val=(q1_text,q1_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q3_text,q3_ans_radio,str(selected_id_value))
        #     mycursor.execute(sql,val)
        #     conn.commit()
        #     st.success("Record Update Successfully!!!")
        #     st.title("Result")
        #     st.text("Ποσοστό Ετοιμότητας")
        #     result_val=((int(q1_ans_radio)+int(q2_1_ans_radio)+int(q2_2_ans_radio)+int(q3_ans_radio))/4)*10
        #     st.write(result_val)
        #     fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
        #     st.plotly_chart(fig,use_container_width=True)
        
        # with conn.cursor() as cur:
        #     cur.execute(sql,val)
        #     conn.commit()
        #     st.success("Record Updated Successfully")
        #     st.experimental_rerun()



# def e_button8(id,kpdf,js_code,css_code):
#     st.subheader("Αναλυτικός Πίνακας Δεικτών")
#     kpdf_filtered=kpdf.loc[:, ~kpdf.columns.isin(['D36_overal', 'D18_lipsi','D18_eko','D18_general','D22_23_g','D40_metaboli'])]
#     # st.write(kpdf.loc[:, ~kpdf.columns.isin(['D36_overal', 'D18_lipsi','D18_eko','D18_general','D22_23_g','D40_metaboli'])])
#    # Get the current column names in a list
#     current_cols = kpdf_filtered.columns.tolist()

#     # Create a dictionary to map old column names to new column names
#     new_cols = {}
#     found_year = False

#     # Enumerate through the current column names and rename them accordingly
#     for old_col in current_cols:
#         if old_col == 'year':
#             found_year = True
#             new_cols[old_col] = old_col  # Keep 'year' column unchanged
#         elif found_year:
#             new_cols[old_col] = f'Δ{len(new_cols) - 1}'  # Start enumeration from 1 after 'year'
#         else:
#             new_cols[old_col] = old_col  # Keep columns before 'year' unchanged

#     # Rename the columns using the .rename() method
#     kpdf_filtered.rename(columns=new_cols, inplace=True)

#     st.write(kpdf_filtered)
#     csv = convert_df(kpdf_filtered)

#     st.download_button(
#     label="Λήψη Πίνακα Δεικτών",
#     data=csv,
#     file_name='kpis_table.csv',
#     mime='text/csv',
#     )


# def display_pinkas_submenu(id):
#     st.subheader("pinkas Submenu")
#     st.write("Content for pinkas submenu")
    
#     response = json.loads(requests.get("https://cmtprooptiki.gr/api/getemploymentcmt.json").text)
#     df=pd.json_normalize(response, max_level=2)
#     df['year'] = df['year'].apply(format_year)

#     df1=df.groupby(['koispe_id','year'])['profile.eko.sum'].sum()
#     dftest=pd.DataFrame(df1).reset_index()
    
#     st.write(df)
#     dffilter=dftest[dftest['koispe_id']==int(id)]
#     # dffilter['year'] = dffilter['year'].apply(format_year)
#     # dffilter
#     # data_canada = px.data.gapminder().query("country == 'Canada'")
#     fig = px.bar(dffilter, x=dffilter['year'].astype(str), y='profile.eko.sum',orientation='v')
#     st.plotly_chart(fig)
    
    
    # Add content for pinkas submenu here


def get_url_params():
    query_params = st.experimental_get_query_params()
    id_received = query_params.get("id", [""])[0]
    
    return id_received
    # id_input = st.text_input("Enter ID", value=id_received)
    # if id_input:
    #     display_contents(id_input)

def display_contents(id_received):
    # Retrieve the contents of the specific ID (replace with your own logic)
    contents = {'id': id_received, 'name': 'John eseaas', 'email': 'john@example.com'}

    st.write(f'# Contents of ID: {id_received}')
    st.write(f'Name: {contents["name"]}')
    st.write(f'Email: {contents["email"]}')



if __name__ == "__main__":
    main()
    
