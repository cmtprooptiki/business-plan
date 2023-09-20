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
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import plotly.io as pio

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

def run_query(conn,query):
    with conn.cursor() as cur:
        cur.execute(query)
        columnsnames=cur.column_names
        return cur.fetchall(),columnsnames
    

def create_record1(id,title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio):
    conn = init_connection()
    mycursor = conn.cursor()
    st.write("inside record1")
    st.write(id)
    # q="test"
    # age="testage"
    sql = "INSERT INTO forms (koispe_id, creation_date,title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio) VALUES (%s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (str(id),title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio)
    mycursor.execute(sql, val)
    conn.commit()
    return mycursor


def create_record_form2(id, title, q6_text, q6_1_ans_num, q6_1_calc, q7_text, q7_1_ans_num, q7_1_calc,
                        q8_text, q8_1_ans_num, q8_1_calc, q9_text, q9_1_ans_num, q9_1_calc,
                        q10_text, q10_1_ans_num, q10_1_calc, q11_text, q11_1_ans_num, q11_1_calc,
                        q12_text, q12_1_ans_num, q12_1_calc, q13_text, q13_1_ans_num, q13_1_calc,
                        q14_text,q14_1_ans_num,q15_text,q15_1_ans_num,q16_text,q16_1_ans_num,q17_text,q17_1_ans_num):
    conn = init_connection()
    mycursor = conn.cursor()
    st.write("inside record1 φορμ2")
    st.write(id)
    # q="test"
    # age="testage"
    sql = """
    INSERT INTO forms2 (
        koispe_id,
        creation_date,
        title,
        q6_text,
        q6_1_ans_num,
        q6_1_calc,
        q7_text,
        q7_1_ans_num,
        q7_1_calc,
        q8_text,
        q8_1_ans_num,
        q8_1_calc,
        q9_text,
        q9_1_ans_num,
        q9_1_calc,
        q10_text,
        q10_1_ans_num,
        q10_1_calc,
        q11_text,
        q11_1_ans_num,
        q11_1_calc,
        q12_text,
        q12_1_ans_num,
        q12_1_calc,
        q13_text,
        q13_1_ans_num,
        q13_1_calc,
        q14_text,
        q14_1_ans_num,
        q15_text,
        q15_1_ans_num,
        q16_text,
        q16_1_ans_num,
        q17_text,
        q17_1_ans_num
    ) VALUES (%s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
    """

    val = (
        str(id),
        title,
        q6_text,
        q6_1_ans_num,
        q6_1_calc,
        q7_text,
        q7_1_ans_num,
        q7_1_calc,
        q8_text,
        q8_1_ans_num,
        q8_1_calc,
        q9_text,
        q9_1_ans_num,
        q9_1_calc,
        q10_text,
        q10_1_ans_num,
        q10_1_calc,
        q11_text,
        q11_1_ans_num,
        q11_1_calc,
        q12_text,
        q12_1_ans_num,
        q12_1_calc,
        q13_text,
        q13_1_ans_num,
        q13_1_calc,
        q14_text,
        q14_1_ans_num,
        q15_text,
        q15_1_ans_num,
        q16_text,
        q16_1_ans_num,
        q17_text,
        q17_1_ans_num
    )




    # sql = "INSERT INTO forms2 (koispe_id, creation_date, title, q6_text ,q6_1_ans_num, q6_1_calc,q7_text,q7_1_ans_num,q7_1_calc) VALUES (%s, NOW(), %s, %s, %s,%s,%s,%s,%s)"
    # val = (str(id),title,q6_text,q6_1_ans_num,q6_1_calc,q7_text,q7_1_ans_num,q7_1_calc)
    mycursor.execute(sql, val)
    conn.commit()
    return mycursor




def form1(id,kpdf):
    # st.title("FORM1")
    st.subheader("Δημιουργία Νέου Business Plan")
        
    # Encapsulate the form using st.form
    with st.form(key="create_form",clear_on_submit=True):
        

        # ###QUESTION 1
        # st.write("Selected Year", year)
        st.title("Τίτλος επιχειρηματικής ιδέας")
        title=st.text_area("Συμπληρώστε εδώ:",key="title")

        st.title("Διαχρονική αποτύπωση λειτουργίας ΚοιΣΠΕ")

        st.markdown("<h3 style='text-align: center; color: grey;'>Διαχρονική Κατανομή Εργαζομένων ΚοιΣΠΕ</h3>", unsafe_allow_html=True)

# year = st.selectbox("Select year", ["2021", "2022", "2023", "2024"])
        colors = ['#618abb','#00235e','#F0894F']

        columns = ['D9', 'D10', 'D11']
        # kpdf_selected = kpdf[columns]
        # Create the stacked bar plot using Plotly
        legend_labels = ['Γενικού Πληθυσμού', 'ΛΥΨΥ', 'ΕΚΟ']
        fig=stackedChart(columns,kpdf,legend_labels,'Έτος','% επί του Συνόλου',colors)
        # Show the plot
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<h3 style='text-align: center; color: grey;'>Διαχρονική Κατανομή Κύκλου Εργασιών ανά Κατηγορία</h3>", unsafe_allow_html=True)

        colors2 = ['#00235e','#F0894F','#618abb']

        columns2 = ['D26', 'D27', 'D28']
        legend_labels = ['Κτηρια & Εξ.Χώροι ','Εστίαση','Λοιπές Δραστηριότητες']
        # kpdf_selected = kpdf[columns2]
        # Create the stacked bar plot using Plotly
        fig=stackedChart2(columns2,kpdf,legend_labels,'Έτος','Συχνότητα',colors2)
        st.plotly_chart(fig,use_container_width=True)

        st.markdown("<h3 style='text-align: center; color: grey;'>% Ετήσια Μεταβολή Κύκλου Εργασιών</h3>", unsafe_allow_html=True)

        categories=kpdf['year'].tolist()
        # Sample data
        # categories = ['Category A', 'Category B', 'Category C', 'Category D']
        values =kpdf['D24'].astype(float).tolist()
        line_labels=kpdf['D29'].tolist()
        fig=pctChangeV2(categories,values,line_labels,'Κύκλοι Εργασιών','Κυκλ.Εργασιών')
        # fig=pctChangeChart(values,categories,'Values','Ποσοστιαία μεταβολή','Percentage Change','Values')
        st.plotly_chart(fig,use_container_width=True)


        #Ερωτηση 1
        st.title("Παρουσίαση του ΚοιΣΠΕ (εσωτερικό περιβάλλον)")
        st.markdown("""<h4>Εξηγήστε το ιστορικό ίδρυσης του ΚοιΣΠΕ και την νομική οντότητα του Συνεταιρισμού. 
        Περιγράψτε: <br>
        •	την αποστολή, τις αξίες και τους κοινωνικούς στόχους σας. <br>
        •	τις έως τώρα επιχειρηματικές δράσεις, σχολιάζοντας τα διαχρονικά στοιχεία απασχόλησης και κύκλου εργασιών που προκύπτουν από τα παραπάνω διαγράμματα.  
        </h4>""",unsafe_allow_html=True)

        q1_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q1text",height=300)
        st.subheader("Η απάντησή σας εξηγεί επαρκώς το ιστορικό της ίδρυσης του ΚοιΣΠΕ;")
        q1_1_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q1_1_ans_radio")
        st.subheader("Έχει αναφερθεί ξεκάθαρα η νομική οντότητα του ΚοιΣΠΕ;")
        q1_2_ans_radio = st.radio("",["ΟΧΙ","ΝΑΙ"],horizontal=True,key="q1_2_ans_radio")
        st.subheader("Η απάντησή σας περιγράφει επαρκώς την αποστολή, τις αξίες και τους κοινωνικούς στόχους του ΚοιΣΠΕ;")
        q1_3_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q1_3_ans_radio")
        st.subheader("Η απάντησή σας περιγράφει επαρκώς τις έως τώρα επιχειρηματικές δράσεις;")
        q1_4_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q1_4_ans_radio")
        st.subheader("Παρατίθενται διαχρονικά στοιχεία απασχόλησης και κύκλου εργασιών;")
        q1_5_ans_radio = st.radio("",["ΟΧΙ","ΝΑΙ"],horizontal=True,key="q1_5_ans_radio")
        # ###QUESTION 2
        st.title("Ανάλυση της αγοράς (εξωτερικό περιβάλλον & οικοσύστημα των ΚοιΣΠΕ)")

        st.markdown("""<h4>Αναλύστε την αγορά-στόχο και το μέγεθός της.<br>
        Προσδιορίστε το κοινό-στόχο και τις ανάγκες του. <br>
        Αναφερθείτε σε τυχόν αντίστοιχη εμπειρία άλλων Συνεταιρισμών στον ίδιο τομέα.<br>
        Αξιολογήστε το ανταγωνιστικό τοπίο και τις τάσεις της τοπικής αγοράς.</h4>
        """,unsafe_allow_html=True)
        q2_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q2text",height=300)

        st.subheader("Η απάντησή σας αναλύει επαρκώς την αγορά-στόχο και το μέγεθός της;")
        q2_1_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q2_1_ans_radio")
        st.write('You selected ', q2_1_ans_radio)
        st.subheader("Η απάντησή σας προσδιορίζει επαρκώς το κοινό-στόχο και τις ανάγκες του;")
        q2_2_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q2_2_ans_radio")
        st.write('You selected ', q2_2_ans_radio)
        st.subheader("Στην απάντησή σας αναφέρετε εάν υπάρχουν ή όχι άλλοι Συνεταιρισμοί με αντίστοιχη εμπειρία;")
        q2_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q2_3_ans_radio")
        st.write('You selected ', q2_3_ans_radio)
        st.subheader("Έχετε αξιολογήσει το ανταγωνιστικό τοπίο και τις τάσεις της τοπικής αγοράς;")
        q2_4_ans_radio = st.radio("",  ["ΟΧΙ","ΝΑΙ"], horizontal=True,key="q2_4_ans_radio")
        st.write('You selected ', q2_4_ans_radio)
        # ###QUESTION 3
        st.title("Προϊόντα ή υπηρεσίες")
        st.markdown("""<h4>Αναφέρατε τα νέα προϊόντα ή τις νέες υπηρεσίες που θα προσφέρει ο συνεταιρισμός.<br>
        Εξηγήστε πώς οι προσφορές αυτές (προϊόντα ή υπηρεσίες) ανταποκρίνονται στις ανάγκες της αγοράς.<br>
        Επισημάνετε τυχόν μοναδικά σημεία πώλησης ή ανταγωνιστικά πλεονεκτήματα που διαθέτετε.</h4>
        """,unsafe_allow_html=True)
        q3_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q3text",height=300)
        st.subheader("Έχετε αναφέρει τα νέα προϊόντα ή τις νέες υπηρεσίες που θα προσφέρει ο Συνεταιρισμός σας;")
        q3_1_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"], horizontal=True,key="q3_1_ans_radio")
        st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς πώς οι προσφορές αυτές ανταποκρίνονται στις ανάγκες της αγοράς;")
        q3_2_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q3_2_ans_radio")
        st.subheader("Στην απάντησή σας επισημαίνονται επαρκώς τυχόν μοναδικά σημεία πώλησης ή ανταγωνιστικά πλεονεκτήματα που διαθέτετε;")
        q3_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q3_3_ans_radio")
        
        
        # ###QUESTION 4
        st.title("Ανάλυση επιχειρηματικής ιδέας")
        st.markdown("""<h4>Περιγράψτε τη διαδικασία παραγωγής και τις τυχόν αναγκαίες εγκαταστάσεις ή εξοπλισμό.Σχολιάστε την αλυσίδα εφοδιασμού και τα logistics της επιχειρηματικής ιδέας.</h4>
        """,unsafe_allow_html=True)
        q4_text=st.text_area("Γράψε ελεύθερο κείμενο", key="q4text",height=300)
        st.subheader("Στην απάντησή σας έχετε περιγράψει επαρκώς  τη διαδικασία παραγωγής και τις τυχόν αναγκαίες εγκαταστάσεις ή εξοπλισμό;")
        q4_1_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q4_1_ans_radio")
        st.subheader("Έχετε σχολιάσει την αλυσίδα εφοδιασμού και τα logistics της επιχειρηματικής ιδέας σας;")
        q4_2_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"], horizontal=True,key="q4_2_ans_radio")
        # ###QUESTION 5
        st.title("Διοίκηση και ομάδα")
        st.markdown("""<h4>Παρουσιάστε τα βασικά μέλη του συνεταιρισμού και τους ρόλους τους στην νέα επιχειρηματική ιδέα.
        Επισημάνετε τη σχετική εμπειρία και τα προσόντα τους (επόπτες, επαγγελματίες, ΛΥΨΥ). 
        Εξηγήστε την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες.</h4> 
        """,unsafe_allow_html=True)
        q5_text=st.text_area("Γράψε ελεύθερο κείμενο", key="q5text",height=300)
        st.subheader("Έχετε παρουσιάσει τα βασικά μέλη του συνεταιρισμού και τους ρόλους τους στην νέα επιχειρηματική ιδέα;")
        q5_1_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"], horizontal=True,key="q5_1_ans_radio")
        st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες ;")
        q5_2_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"], horizontal=True,key="q5_2_ans_radio")
        st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες ;")
        q5_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q5_3_ans_radio")
        # q=""
        # age=""
        # Submit button inside the form
        submit_button = st.form_submit_button("Submit")
    # Check if the submit button is clicked
    if submit_button:
        # Call the create_record function to insert the data into the database
        #create_record(id, year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio)
        # Calculate and display the result
        st.title("Βαθμός ικανοποίησης από την επάρκεια των απαντήσεων")
        st.text("Ποσοστό Ετοιμότητας")
        #metraopi nai oxi apanstise se 10 kai 0 antistoixa
        if q1_2_ans_radio=='ΝΑΙ':
            q1_2_ans_radio='10'
        else:
            q1_2_ans_radio='0'

        if q1_5_ans_radio=='ΝΑΙ':
            q1_5_ans_radio='10'
        else:
            q1_5_ans_radio='0'

        if q2_4_ans_radio=='ΝΑΙ':
            q2_4_ans_radio='10'
        else:
            q2_4_ans_radio='0'

        if q3_1_ans_radio=='ΝΑΙ':
            q3_1_ans_radio='10'
        else:
            q3_1_ans_radio='0'

        if q4_2_ans_radio=='ΝΑΙ':
            q4_2_ans_radio='10'
        else:
            q4_2_ans_radio='0'
        
        if q5_1_ans_radio=='ΝΑΙ':
            q5_1_ans_radio='10'
        else:
            q5_1_ans_radio='0'
        
        if q5_2_ans_radio=='ΝΑΙ':
            q5_2_ans_radio='10'
        else:
            q5_2_ans_radio='0'



        st.write(q1_2_ans_radio)    
        result_val = ( ( int(q1_1_ans_radio) + int(q1_2_ans_radio) + int(q1_3_ans_radio) + int(q1_4_ans_radio) 
                       + int(q1_5_ans_radio) +int(q2_1_ans_radio)  +int(q2_2_ans_radio) +int(q2_3_ans_radio)+int(q2_4_ans_radio)+int(q3_1_ans_radio)
                       +int(q3_2_ans_radio)+int(q3_3_ans_radio) +int(q4_1_ans_radio)+int(q4_2_ans_radio) +int(q5_1_ans_radio)
                       +int(q5_2_ans_radio)+int(q5_3_ans_radio)  ) / (17*10)) * 100
        st.write(result_val)

        fig = donut_pct_Chart(result_val, '#618abb', 'rgb(240,240,240)', ['% Ποσοστό Ετοιμότητας', ' '])
        st.plotly_chart(fig, use_container_width=True)
        # st.write("until here is working")

        mycursor=create_record1(id,title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,
                                q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,
                                q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,
                                q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,
                                q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio)
        # Display a success message
        
        st.success("Record Created Successfully!!!")
        if int(result_val) >= 80:
            st.write("Φαίνεται πως είστε ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Διερευνήστε τυχόν σημεία βελτίωσης και προχωρήστε στην συμπλήρωση των οικονομικών στοιχείων.")
            # return title
        elif (int(result_val) >= 50) and (int(result_val)<80):
            st.write("Φαίνεται πως είστε αρκετά ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Θα ήταν χρήσιμο να αναλύσετε περισσότερο την ιδέα σας στα πεδία που δεν νιώθετε σιγουριά, πριν προχωρήσετε στα οικονομικά στοιχεία.")
            # return title
        else:
            st.write("Φαίνεται πως δεν είστε ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Καλύτερα να αναλύσετε περισσότερο την ιδέα σας, πριν προχωρήσετε στα οικονομικά στοιχεία.")
            # return title



def form2(id):

    with st.form(key="rest_form2"):
        st.title("Τίτλος επιχειρηματικής ιδέας")
        title=st.text_area("Συμπληρώστε τον τίτλο που συμπληρώσατε και στη φόρμα 'Περιγραφή Επιχειρηματικής Ιδέας'",key="title")

        # title=st.text_area("Τίτλος Φορμας Οικονομικών στοιχείων",key="title")

        st.title("Κόστος Εκκίνησης")

        st.markdown("""<h4>Σε κάθε μία από τις παρακάτω κατηγορίες, καταγράψτε τον εξοπλισμό και τις υπηρεσίες που κρίνονται απαραίτητες για την έναρξη λειτουργίας της επιχείρησης.
                Έπειτα προσδιορίστε το κόστος για την κάθε κατηγορία (τάξη μεγέθους).</h4>""", unsafe_allow_html= True)
        # st.write(id)

        #QUESTION 6
        st.subheader("Κτίρια & Υποδομές")
        st.markdown("<h4>Σε αυτή την κατηγορία συμπεριλαμβάνεται η πάγια αγορά χώρου για την εγκατάσταση της επιχείρησης</h4>",unsafe_allow_html=True)

        q6_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q6text",height=300)
        
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)

        q6_1_ans_num=st.number_input('Συμπληρώστε νούμερο:',key="q6_1_ans_num")
        # st.write('The current number is ',q6_1_ans_num)
        q6_1_calc=q6_1_ans_num*0.04

        # st.write('Ετήσια απόσβεση:',q6_1_calc)

        # #QUESTION 7
        # st.title("Εξοπλισμός & Έπιπλα")
        # st.subheader("Σε αυτή την κατηγορία συμπεριλαμβάνεται το σύνολο του απαραίτητου εξοπλισμού και τα έπιπλα για τον χώρο της νέας επιχείρησης")

        # q7_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q7text",height=300)
        
        # q7_1_ans_num=st.number_input('Kόστος:',key="q7_1_ans_num")
        # st.write('To Κόστος ειναι:', q7_1_ans_num)
        # q7_1_calc=q7_1_ans_num*0.1

        # st.write('Ετήσια απόσβεση:',q7_1_calc)


        questions = [
            {"number": 7, "title": "Εξοπλισμός & Έπιπλα", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνεται το σύνολο του απαραίτητου εξοπλισμού και τα έπιπλα για τον χώρο της νέας επιχείρησης", "calc_coefficient": 0.1},
            {"number": 8, "title": "Εργασίες διαμόρφωσης, εγκατάστασης κλπ", "text": "Συμπεριλαμβάνονται τα έξοδα για τις εργασίες που απαιτούνται στον χώρο για την έναρξη λειτουργίας της επιχείρησης", "calc_coefficient": 0},
            {"number": 9, "title": "Μηχανήματα, εξοπλισμός εκτός Η/Υ και λογισμικού", "text": "Η κατηγορία συμπεριλαμβάνει την αγορά μηχανημάτων π.χ εκτυπωτές κλπ.", "calc_coefficient": 0.1},
            {"number": 10, "title": "Εξοπλισμός Η/Υ, κύριος και περιφερειακός & λογισμικό", "text": "Η κατηγορία συμπεριλαμβάνει την αγορά μηχανημάτων π.χ πρόγραμμα παραγγελιοληψίας, λογιστικά /εμπορικά προγράμματα κλπ.", "calc_coefficient": 0.2},
            {"number": 11, "title": "Λοιπές υπηρεσίες", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνονται υπηρεσίες τρίτων π.χ. πολιτικού μηχανικού για σχέδια – κατόψεις αλλά και την έκδοση άδειας λειτουργίας, υγειονολόγου ΤΕ για τη σύνταξη της μελέτης λειτουργίας της επιχείρησης, μηχανολόγου μηχανικού για μελέτη πυροπροστασίας κλπ.", "calc_coefficient": 0.2},
            {"number": 12, "title": "Αρχικό απόθεμα σε πρώτες και βοηθητικές ύλες", "text": "Συμπεριλαμβάνεται κάθε υλικό αγαθό που ανήκει στην επιχείρηση και προορίζεται για να πωληθεί στην κατάσταση που βρίσκεται ή να επεξεργαστεί για τους σκοπούς της παραγωγής", "calc_coefficient": 0},
            {"number": 13, "title": "Λοιπά έξοδα εκκίνησης", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνονται τα έξοδα που προκύπτουν κατά τη διαδικασία δημιουργίας μιας νέας επιχείρησης και δεν συμπεριλαμβάνονται στις ανωτέρω ενότητες", "calc_coefficient": 0},
            
        ]

        # QUESTION 7
        st.subheader(questions[0]["title"])
        #st.subheader(questions[0]["text"])
        st.markdown("""<h4>Σε αυτή την κατηγορία συμπεριλαμβάνεται το σύνολο του απαραίτητου εξοπλισμού και τα έπιπλα για τον χώρο της νέας επιχείρησης</h4>
        """,unsafe_allow_html=True)
        q7_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q7text", height=300)

        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q7_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q71ansnum")
        q7_1_calc = q7_1_ans_num * questions[0]["calc_coefficient"]


        # QUESTION 8
        st.subheader(questions[1]["title"])
        #st.subheader(questions[1]["text"])
        st.markdown("""<h4>Κείμενο Επεξήγησης	Συμπεριλαμβάνονται τα έξοδα για τις εργασίες που απαιτούνται στον χώρο για την έναρξη λειτουργίας της νέας επένδυσης.</h4>
        """,unsafe_allow_html=True)
        q8_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q8text", height=300)
        
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q8_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q81ansnum")
        q8_1_calc = q8_1_ans_num * questions[1]["calc_coefficient"]

        # QUESTION 9
        st.subheader(questions[2]["title"])
        st.markdown("""<h4>Η κατηγορία συμπεριλαμβάνει την αγορά μηχανημάτων π.χ οχήματα κλπ.</h4>
        """,unsafe_allow_html=True)

        q9_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q9text", height=300)
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q9_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q91ansnum")
        q9_1_calc = q9_1_ans_num * questions[2]["calc_coefficient"]

        # QUESTION 10
        st.subheader(questions[3]["title"])
        st.markdown("""<h4>Η κατηγορία συμπεριλαμβάνει την αγορά εξοπλισμού π.χ πρόγραμμα παραγγελιοληψίας, λογιστικά /εμπορικά προγράμματα κλπ.</h4>
        """,unsafe_allow_html=True)

        q10_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q10text", height=300)
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q10_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q101ansnum")
        q10_1_calc = q10_1_ans_num * questions[3]["calc_coefficient"]

        # QUESTION 11
        st.subheader(questions[4]["title"])
        st.markdown("""<h4>Σε αυτή την κατηγορία συμπεριλαμβάνονται υπηρεσίες τρίτων π.χ. πολιτικού μηχανικού για σχέδια – κατόψεις, αλλά και την έκδοση άδειας λειτουργίας, μηχανολόγου μηχανικού για μελέτη πυροπροστασίας κλπ.</h4>
        """,unsafe_allow_html=True)

        q11_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q11text", height=300)
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q11_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q111ansnum")
        q11_1_calc = q11_1_ans_num * questions[4]["calc_coefficient"]

        # QUESTION 12
        st.subheader(questions[5]["title"])
        st.markdown("""<h4>Συμπεριλαμβάνεται κάθε υλικό αγαθό που ανήκει στην επιχείρηση και προορίζεται για να πωληθεί στην κατάσταση που βρίσκεται ή να επεξεργαστεί για τους σκοπούς της παραγωγής.</h4>
        """,unsafe_allow_html=True)

        q12_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q12text", height=300)
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q12_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q121ansnum")
        q12_1_calc = q12_1_ans_num * questions[5]["calc_coefficient"]

        # QUESTION 13
        st.subheader(questions[6]["title"])
        st.markdown("""<h4>Σε αυτή την κατηγορία συμπεριλαμβάνονται τα έξοδα που προκύπτουν κατά τη διαδικασία της νέας επένδυσης και δεν συμπεριλαμβάνονται στις ανωτέρω ενότητες.</h4>
        """,unsafe_allow_html=True)

        q13_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q13text", height=300)
        st.markdown("<h4>Kόστος</h4>",unsafe_allow_html=True)
        q13_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q131ansnum")
        q13_1_calc = q13_1_ans_num * questions[6]["calc_coefficient"]


        # QUESTION 14
        st.title("Λειτουργικό Κόστος")
        st.markdown("<p>*για ένα έτος λειτουργίας</p>",unsafe_allow_html=True)
        st.subheader("Ενοικίαση χώρων")

        st.markdown("""<h4>Σε αυτή την κατηγορία, καταγράψτε τους χώρους που θα χρειαστούν για τη στέγαση της επιχειρηματικής δραστηριότητας και τυχόν άλλων χώρων που θα εξυπηρετούν τις ανάγκες της επιχείρησης λ.χ αποθήκη.
        Έπειτα υπολογίστε το ετήσιο κόστος για την ενοικίαση χώρου/ ων.
        Αν το μηνιαίο κόστος ενοικίασης χώρου είναι π.χ. 100€, υπολογίστε το ετήσιο κόστος πολλαπλασιάζοντας επί 12 (100*12=1200€). Εάν υπάρχουν περισσότεροι του ενός χώροι, προσθέστε τα ποσά που προκύπτουν.
        </h4>""",unsafe_allow_html=True)

        q14_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q14text", height=300)

        st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος για την ενοικίαση χώρου/ων;</h4>",unsafe_allow_html=True)
        # st.text("Πόσο υπολογίζετε το συνολικό ετήσιο κόστος για την ενοικίαση χώρου/ων;")

        
        q14_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q141ansnum")
        # st.write('To Κόστος είναι:', q14_1_ans_num)

        # QUESTION 15
        st.subheader("Δαπάνες μισθοδοσίας")
        st.markdown("""<h4>Καταγράψτε το σύνολο των εργαζομένων που θα απασχοληθούν στην επιχείρηση. Έπειτα υπολογίστε το ετήσιο κόστος μισθοδοσίας του συνόλου των εργαζομένων, λαμβάνοντας υπόψη το μισθολογικό κλιμάκιο που ανήκουν και τον χρόνο απασχόλησης. 
        Το κόστος είναι το άθροισμα των μικτών αποδοχών και εργοδοτικών εισφορών κάθε μήνα, ενώ επιπλέον, για κάθε ημερολογιακό έτος, προστίθεται δώρο Πάσχα & Χριστουγέννων, οι αποδοχές άδειας και η αποζημίωση της άδειας, αν προκύπτει.
        </h4>""",unsafe_allow_html=True)

        q15_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q15text", height=300)
        st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος μισθοδοσίας;</h4>",unsafe_allow_html=True)
        q15_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q151ansnum")
        
        # QUESTION 16
        st.subheader("Παροχές υπηρεσιών τρίτων")
        st.markdown("""<h4>Καταγράψτε τις παροχές υπηρεσιών από τρίτους, που θα χρειαστούν για ένα έτος λειτουργίας της επιχειρηματικής δραστηριότητας. Σε αυτή την κατηγορία συμπεριλαμβάνονται οι λογαριασμοί ΔΕΚΟ, έξοδα επαγγελματιών (δικηγόρος, λογιστής, τεχνικός ασφαλείας), έξοδα διαφήμισης κλπ.
        Έπειτα υπολογίστε το ετήσιο κόστος της κάθε υπηρεσίας, πολλαπλασιάζοντας επί 12 σε περιπτώσεις μηνιαίων χρεώσεων, π.χ. λογαριασμοί ΔΕΚΟ.
        </h4>""",unsafe_allow_html=True)

        q16_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q16text", height=300)
        st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος παροχής υπηρεσιών από τρίτους;</h4>",unsafe_allow_html=True)
        q16_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q161ansnum")

        # QUESTION 17
        st.subheader("Λοιπά έκτακτα έξοδα")
        st.markdown("""<h4>Καταγράψτε τυχόν έκτακτα έξοδα που μπορεί να προκύψουν σε ένα έτος λειτουργίας της επιχειρηματικής δράσης (π.χ. βλάβη μηχανημάτων, οχημάτων, κλπ.).
        Έπειτα υπολογίστε το συνολικό ετήσιο κόστος έκτακτων εξόδων.
        .</h4>""",unsafe_allow_html=True)

        q17_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q17text", height=300)
        st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος έκτακτων εξόδων;</h4>",unsafe_allow_html=True)
        q17_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q171ansnum")











        # Add input fields for Form 2
        # For example:
        # q = st.text_input("Enter your address")
        # age = st.text_input("Enter your phone number")
        st.write(id)
        submit_button2 = st.form_submit_button("Submit Form 2")

    if submit_button2:
        # Process Form 2 data here and save it to the same database table
        st.write('aposvesi ypologismo gia erotisi 6')
        st.write(q6_1_calc)
        st.write(q6_text)
        st.write(q6_1_ans_num)

        st.write('aposvesi ypologismo gia erotisi 7')
        st.write(q7_1_calc)
        st.write(q7_text)
        st.write(q7_1_ans_num)

        st.write('aposvesi ypologismo gia erotisi 8')
        st.write(q8_1_calc)
        st.write(q8_text)
        st.write(q8_1_ans_num)
        
        st.write('aposvesi ypologismo gia erotisi 9')
        st.write(q9_1_calc)
        st.write(q9_text)
        st.write(q9_1_ans_num)

        st.write('aposvesi ypologismo gia erotisi 10')
        st.write(q10_1_calc)
        st.write(q10_text)
        st.write(q10_1_ans_num)

        st.write('aposvesi ypologismo gia erotisi 11')
        st.write(q11_1_calc)
        st.write(q11_text)
        st.write(q11_1_ans_num)

        
        st.write('aposvesi ypologismo gia erotisi 12')
        st.write(q12_1_calc)
        st.write(q12_text)
        st.write(q12_1_ans_num)

        st.write('aposvesi ypologismo gia erotisi 13')
        st.write(q13_1_calc)
        st.write(q13_text)
        st.write(q13_1_ans_num)

        st.write('ypologismo gia erotisi 14')
        st.write(q14_text)
        st.write(q14_1_ans_num)

        st.write('ypologismo gia erotisi 15')
        st.write(q15_text)
        st.write(q15_1_ans_num)

        st.write('ypologismo gia erotisi 16')
        st.write(q16_text)
        st.write(q16_1_ans_num)

        st.write('ypologismo gia erotisi 17')
        st.write(q17_text)
        st.write(q17_1_ans_num)




        # create_record_form2(id,title,q6_text,q6_1_ans_num,q6_1_calc,q7_text,q7_1_ans_num,q7_1_calc)
        create_record_form2(id, title, q6_text, q6_1_ans_num, q6_1_calc, q7_text, q7_1_ans_num, q7_1_calc,
                        q8_text, q8_1_ans_num, q8_1_calc, q9_text, q9_1_ans_num, q9_1_calc,
                        q10_text, q10_1_ans_num, q10_1_calc, q11_text, q11_1_ans_num, q11_1_calc,
                        q12_text, q12_1_ans_num, q12_1_calc, q13_text, q13_1_ans_num, q13_1_calc,q14_text,q14_1_ans_num,q15_text,q15_1_ans_num,q16_text,q16_1_ans_num,q17_text,q17_1_ans_num)
        # mycursor=update_record(title,q6_text,q6_1_ans_num,q6_1_calc)
        # st.title("Αποτελέσματα")
        # st.write("Λειτουργικά έξοδα:",(q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num))
        # st.write("Αποσβέσεις:",(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc))
        # st.write("Άθροισμα εξόδων:",(q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num)+(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc)  )
        # st.write("Μinumum εσόδων επιχειρηματικής δραστηριότητας",((q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num)+(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc)))

        SUM_ek=q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc
        SUM_leit=q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num

        st.write("Το κόστος εκκίνησης, δηλαδή το κεφάλαιο που χρειάζεται για την έναρξης της επιχειρηματικής ιδέας σας, είναι:"+str(SUM_ek))
        st.write("Το Λειτουργικό κόστος, δηλαδή κόστος για τη λειτουργία της επιχειρηματικής ιδέας σας, για ένα έτος είναι:"+str(SUM_leit))
        st.markdown(""" <table>
                            <tr>
                                <th>Κατηγορία</th>
                                <th>Ετήσια απόσβεση</th>
                            </tr>
                            <tr>
                                <td>Κτίρια & Υποδομές</td>
                                <td>"""+str(round(q6_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Εξοπλισμός & Έπιπλα</td>
                                <td>"""+str(round(q7_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Εργασίες διαμόρφωσης, εγκατάστασης κλπ</td>
                                <td>"""+str(round(q8_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Μηχανήματα, εξοπλισμός εκτός Η/Υ και λογισμικού</td>
                                <td>"""+str(round(q8_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Εξοπλισμός Η/Υ, κύριος και περιφερειακός & λογισμικό</td>
                                <td>"""+str(round(q10_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Λοιπές υπηρεσίες</td>
                                <td>"""+str(round(q11_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Αρχικό απόθεμα σε πρώτες και βοηθητικές ύλες</td>
                                <td>"""+str(round(q12_1_calc,2))+"""</td>
                            </tr>
                            <tr>
                                <td>Λοιπά έξοδα εκκίνησης</td>
                                <td>"""+str(round(q13_1_calc,2))+"""</td>
                            </tr>
                        </table>
        """,unsafe_allow_html=True)
        st.write("Συνεπώς, για να είναι βιώσιμη η επιχειρηματική ιδέα σας, κρίνεται απαραίτητο, το ελάχιστο των ετήσιων εσόδων να είναι: "+str(SUM_leit))
        st.warning("Για κάθε επόμενο έτος λειτουργίας της επιχειρηματικής ιδέας σας, θα πρέπει να λάβετε υπόψιν τυχόν αύξηση του λειτουργικού κόστους (π.χ αυξήσεις μισθών, ανατιμήσεις αγαθών, κλπ.) και τις αποσβέσεις.")
        
        
        # st.success("Form 2 submitted successfully!")

def main():
 
    
    
    #st.write(home())
    st.set_page_config(
        page_title="Business Plan",
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

            selected_option1 = option_menu("Μενού", ["Επιχειρηματική Ιδέα","Οικονομικά Στοιχεία"],
                                icons=['table','table'],
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
    if selected_option1=="Επιχειρηματική Ιδέα":
        e_button9(id,kpdf)
    elif selected_option1=="Οικονομικά Στοιχεία":
        e_button10(id,kpdf)

def e_button9(id,kpdf):
    conn = init_connection()
    # id = st.number_input("Enter ID", userid)
    # total_days = st.number_input("Enter total days off", min_value=0, value=total_daysoff)
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete","export"))
    mycursor = conn.cursor()

    if option == "Create":
        form1(id,kpdf)


           
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
        st.subheader("Επεξεργασία καταχωρημένων Business Plan")
        st.write("Επέλεξε το Business Plan που θέλεις να επεξεργαστείς:")
        mycursor.execute("select * from forms where koispe_id="+str(id)+" ORDER BY creation_date DESC")
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
        # st.write(f"Selected Date: {selected_id}")
        # st.write(f"Corresponding ID: {selected_id_value}")
        st.subheader("EDIT FORM")
        #show form fields for editing
        with st.form(key="edit_form"):

            if selected_id:
                mycursor.execute("select * from forms where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
                result = mycursor.fetchall()
                for row in result:
                    # st.write(row)
                    pass
                # st.write("FIXING YES NO PROBLEM")
                # st.write(default_option_indexq1_2)
                # st.write(row[6])
              
                
                
    
                options = ["0","1", "2", "3", "4", "5","6","7","8","9","10"]
                option2=["ΟΧΙ","ΝΑΙ"]

                
                st.title("Τίτλος επιχειρηματικής ιδέας")
                title=st.text_area("",key="title",value=row[3])
                st.title("Διαχρονική αποτύπωση λειτουργίας ΚοιΣΠΕ")

                st.markdown("<h3 style='text-align: center; color: grey;'>Διαχρονική Κατανομή Εργαζομένων ΚοιΣΠΕ</h3>", unsafe_allow_html=True)

        # year = st.selectbox("Select year", ["2021", "2022", "2023", "2024"])
                colors = ['#618abb','#00235e','#F0894F']

                columns = ['D9', 'D10', 'D11']
                # kpdf_selected = kpdf[columns]
                # Create the stacked bar plot using Plotly
                legend_labels = ['Γενικού Πληθυσμού', 'ΛΥΨΥ', 'ΕΚΟ']
                fig=stackedChart(columns,kpdf,legend_labels,'Έτος','% επί του Συνόλου',colors)
                # Show the plot
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("<h3 style='text-align: center; color: grey;'>Διαχρονική Κατανομή Κύκλου Εργασιών ανά Κατηγορία</h3>", unsafe_allow_html=True)

                colors2 = ['#00235e','#F0894F','#618abb']

                columns2 = ['D26', 'D27', 'D28']
                legend_labels = ['Κτηρια & Εξ.Χώροι ','Εστίαση','Λοιπές Δραστηριότητες']
                # kpdf_selected = kpdf[columns2]
                # Create the stacked bar plot using Plotly
                fig=stackedChart2(columns2,kpdf,legend_labels,'Έτος','Συχνότητα',colors2)
                st.plotly_chart(fig,use_container_width=True)

                st.markdown("<h3 style='text-align: center; color: grey;'>% Ετήσια Μεταβολή Κύκλου Εργασιών</h3>", unsafe_allow_html=True)

                categories=kpdf['year'].tolist()
                # Sample data
                # categories = ['Category A', 'Category B', 'Category C', 'Category D']
                values =kpdf['D24'].astype(float).tolist()
                line_labels=kpdf['D29'].tolist()
                fig=pctChangeV2(categories,values,line_labels,'Κύκλοι Εργασιών','Κυκλ.Εργασιών')
                # fig=pctChangeChart(values,categories,'Values','Ποσοστιαία μεταβολή','Percentage Change','Values')
                st.plotly_chart(fig,use_container_width=True)


                st.title("Παρουσίαση του ΚοιΣΠΕ (εσωτερικό περιβάλλον)")
                st.markdown("""<h4>Εξηγήστε το ιστορικό ίδρυσης του ΚοιΣΠΕ και την νομική οντότητα του Συνεταιρισμού. <br>
                Περιγράψτε: <br>
                •	την αποστολή, τις αξίες και τους κοινωνικούς στόχους σας. <br>
                •	τις έως τώρα επιχειρηματικές δράσεις, σχολιάζοντας τα διαχρονικά στοιχεία απασχόλησης και κύκλου εργασιών που προκύπτουν από τα παραπάνω διαγράμματα.  
                </h4>""",unsafe_allow_html=True)
                q1_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q1text",height=300,value=row[4])
                st.subheader("Η απάντησή σας εξηγεί επαρκώς το ιστορικό της ίδρυσης του ΚοιΣΠΕ;")
                default_option_indexq1_1 = options.index(str(row[5]))
                q1_1_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq1_1 ,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q1_1_ans_radio")
                
                st.subheader("Έχει αναφερθεί ξεκάθαρα η νομική οντότητα του ΚοιΣΠΕ;")

                if row[6]=='0':
                    default_option_indexq1_2 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq1_2 = option2.index('ΝΑΙ')


                # default_option_indexq1_2 = option2.index(str(row[6]))
                #st.write("FIXING YES NO PROBLEM")
                #st.write(default_option_indexq1_2)
                #st.write(row[6])
                q1_2_ans_radio = st.radio("",["ΟΧΙ","ΝΑΙ"],default_option_indexq1_2,horizontal=True,key="q1_2_ans_radio")
                st.subheader("Η απάντησή σας περιγράφει επαρκώς την αποστολή, τις αξίες και τους κοινωνικούς στόχους του ΚοιΣΠΕ;")
                default_option_indexq1_3 = options.index(str(row[7]))
                q1_3_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq1_3 ,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q1_3_ans_radio")
                st.subheader("Η απάντησή σας περιγράφει επαρκώς τις έως τώρα επιχειρηματικές δράσεις;")
                default_option_indexq1_4 = options.index(str(row[8]))
                q1_4_ans_radio = st.radio("", ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq1_4 ,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q1_4_ans_radio")
                st.subheader("Παρατίθενται διαχρονικά στοιχεία απασχόλησης και κύκλου εργασιών;")
                
                if row[9]=='0':
                    default_option_indexq1_5 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq1_5 = option2.index('ΝΑΙ')

                
                
                # default_option_indexq1_5 = option2.index(str(row[9]))
                q1_5_ans_radio = st.radio("",["ΟΧΙ","ΝΑΙ"],default_option_indexq1_5,horizontal=True,key="q1_5_ans_radio")
                ###QUESTION 2
                st.title("Ανάλυση της αγοράς (εξωτερικό περιβάλλον & οικοσύστημα των ΚοιΣΠΕ)")

                st.markdown("""<h4>Αναλύστε την αγορά-στόχο και το μέγεθός της.<br>
                Προσδιορίστε το κοινό-στόχο και τις ανάγκες του. <br>
                Αναφερθείτε σε τυχόν αντίστοιχη εμπειρία άλλων Συνεταιρισμών στον ίδιο τομέα.<br>
                Αξιολογήστε το ανταγωνιστικό τοπίο και τις τάσεις της τοπικής αγοράς.
                </h4>""",unsafe_allow_html=True)
                q2_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q2text",value=row[10],height=300)

                st.subheader("Η απάντησή σας αναλύει επαρκώς την αγορά-στόχο και το μέγεθός της;")
                default_option_indexq2_1 = options.index(str(row[11]))
                q2_1_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq2_1,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q2_1_ans_radio")

                st.subheader("Η απάντησή σας προσδιορίζει επαρκώς το κοινό-στόχο και τις ανάγκες του;")
                default_option_indexq2_2 = options.index(str(row[12]))
                q2_2_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq2_2,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q2_2_ans_radio")

                st.subheader("Στην απάντησή σας αναφέρετε εάν υπάρχουν ή όχι άλλοι Συνεταιρισμοί με αντίστοιχη εμπειρία;")
                default_option_indexq2_3 = options.index(str(row[13]))
                q2_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq2_3,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q2_3_ans_radio")

                st.subheader("Έχετε αξιολογήσει το ανταγωνιστικό τοπίο και τις τάσεις της τοπικής αγοράς;")

                if row[14]=='0':
                    default_option_indexq2_4 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq2_4 = option2.index('ΝΑΙ')

                # default_option_indexq2_4 = option2.index(str(row[14]))
                q2_4_ans_radio = st.radio("",  ["ΟΧΙ","ΝΑΙ"],default_option_indexq2_4, horizontal=True,key="q2_4_ans_radio")

                ###QUESTION 3
                st.title("Προϊόντα ή υπηρεσίες")
                st.markdown("""<h4>Αναφέρατε τα νέα προϊόντα ή τις νέες υπηρεσίες που θα προσφέρει ο συνεταιρισμός.<br>
                Εξηγήστε πώς οι προσφορές αυτές (προϊόντα ή υπηρεσίες) ανταποκρίνονται στις ανάγκες της αγοράς.<br>
                Επισημάνετε τυχόν μοναδικά σημεία πώλησης ή ανταγωνιστικά πλεονεκτήματα που διαθέτετε.
                </h4>""",unsafe_allow_html=True)
                q3_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q3text",value=row[15],height=300)
                st.subheader("Έχετε αναφέρει τα νέα προϊόντα ή τις νέες υπηρεσίες που θα προσφέρει ο Συνεταιρισμός σας;")
                
                
                if row[16]=='0':
                    default_option_indexq3_1 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq3_1 = option2.index('ΝΑΙ')
                
                
                # default_option_indexq3_1 = option2.index(str(row[16]))
                q3_1_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"],default_option_indexq3_1, horizontal=True,key="q3_1_ans_radio")
                st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς πώς οι προσφορές αυτές ανταποκρίνονται στις ανάγκες της αγοράς;")
                default_option_indexq3_2 = options.index(str(row[17]))
                q3_2_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq3_2,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q3_2_ans_radio")
                st.subheader("Στην απάντησή σας επισημαίνονται επαρκώς τυχόν μοναδικά σημεία πώλησης ή ανταγωνιστικά πλεονεκτήματα που διαθέτετε;")
                default_option_indexq3_3 = options.index(str(row[18]))
                q3_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq3_3,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"],horizontal=True,key="q3_3_ans_radio")
                
                
                ###QUESTION 4
                st.title("Ανάλυση επιχειρηματικής ιδέας")
                st.markdown("""<h4>Περιγράψτε τη διαδικασία παραγωγής και τις τυχόν αναγκαίες εγκαταστάσεις ή εξοπλισμό.<br>
                Σχολιάστε την αλυσίδα εφοδιασμού και τα logistics της επιχειρηματικής ιδέας.</h4>
                """,unsafe_allow_html=True)
                q4_text=st.text_area("Γράψε ελεύθερο κείμενο", key="q4text",value=row[19],height=300)
                st.subheader("Στην απάντησή σας έχετε περιγράψει επαρκώς  τη διαδικασία παραγωγής και τις τυχόν αναγκαίες εγκαταστάσεις ή εξοπλισμό;")
                default_option_indexq4_1 = options.index(str(row[20]))
                q4_1_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq4_1,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q4_1_ans_radio")
                st.subheader("Έχετε σχολιάσει την αλυσίδα εφοδιασμού και τα logistics της επιχειρηματικής ιδέας σας;")

                if row[21]=='0':
                    default_option_indexq4_2 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq4_2 = option2.index('ΝΑΙ')

                # default_option_indexq4_2 = option2.index(str(row[21]))
                q4_2_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"],default_option_indexq4_2, horizontal=True,key="q4_2_ans_radio")
                ###QUESTION 5
                st.title("Διοίκηση και ομάδα")
                st.markdown("""<h4>Παρουσιάστε τα βασικά μέλη του συνεταιρισμού και τους ρόλους τους στη νέα επιχειρηματική ιδέα.<br>
                Επισημάνετε τη σχετική εμπειρία και τα προσόντα τους (επόπτες, επαγγελματίες, ΛΥΨΥ). <br>
                Εξηγήστε την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες.</h4> 
                """,unsafe_allow_html=True)
                q5_text=st.text_area("Γράψε ελεύθερο κείμενο", key="q5text",value=row[22],height=300)
                st.subheader("Έχετε παρουσιάσει τα βασικά μέλη του συνεταιρισμού και τους ρόλους τους στη νέα επιχειρηματική ιδέα;")

                if row[23]=='0':
                    default_option_indexq5_1 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq5_1 = option2.index('ΝΑΙ')

                # default_option_indexq5_1 = option2.index(str(row[23]))
                q5_1_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"],default_option_indexq5_1, horizontal=True,key="q5_1_ans_radio")
                st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες ;")

                if row[24]=='0':
                    default_option_indexq5_2 = option2.index('ΟΧΙ')
                else:
                    default_option_indexq5_2 = option2.index('ΝΑΙ')

                # default_option_indexq5_2 = option2.index(str(row[24]))
                q5_2_ans_radio = st.radio("", ["ΟΧΙ","ΝΑΙ"],default_option_indexq5_2, horizontal=True,key="q5_2_ans_radio")
                st.subheader("Στην απάντησή σας έχετε εξηγήσει επαρκώς την οργανωτική δομή και τυχόν συμβουλευτικές επιτροπές ή συνεργασίες ;")
                default_option_indexq5_3 = options.index(str(row[25]))
                q5_3_ans_radio = st.radio("",  ["0","1", "2", "3", "4", "5","6","7","8","9","10"],default_option_indexq5_3,captions = ["καθολου","","","","","","","","","", "Πάρα πολύ"], horizontal=True,key="q5_3_ans_radio")

                # Submit button inside the form
                # submit_button = st.form_submit_button("Submit")
                # Check if the submit button is clicked
                # if submit_button:
                #     # Call the create_record function to insert the data into the database
                #     #create_record(id, year, q1_text, q1_ans_radio, q2_text, q2_1_ans_radio, q2_2_ans_radio, q3_text, q3_ans_radio)
                #     create_record1(id,title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio)
                #     # Display a success message
                #     st.success("Record Created Successfully!!!")
                    
                #     # Calculate and display the result
                #     st.title("Result")
                #     st.text("Ποσοστό Ετοιμότητας")
                #     result_val = ((int(q1_ans_radio) + int(q2_1_ans_radio) + int(q2_2_ans_radio) + int(q3_ans_radio)) / 4) * 10
                #     st.write(result_val)
                #     fig = donut_pct_Chart(result_val, '#618abb', 'rgb(240,240,240)', ['% Ποσοστό Ετοιμότητας', ' '])
                #     st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("Choose Form for editing")

            submit_button_edit = st.form_submit_button("Update")

       

        if submit_button_edit:
            st.title("Βαθμός ικανοποίησης από την επάρκεια των απαντήσεων")
            st.text("Ποσοστό Ετοιμότητας")
            if q1_2_ans_radio=='ΝΑΙ':
                q1_2_ans_radio='10'
            else:
                q1_2_ans_radio='0'

            if q1_5_ans_radio=='ΝΑΙ':
                q1_5_ans_radio='10'
            else:
                q1_5_ans_radio='0'

            if q2_4_ans_radio=='ΝΑΙ':
                q2_4_ans_radio='10'
            else:
                q2_4_ans_radio='0'

            if q3_1_ans_radio=='ΝΑΙ':
                q3_1_ans_radio='10'
            else:
                q3_1_ans_radio='0'

            if q4_2_ans_radio=='ΝΑΙ':
                q4_2_ans_radio='10'
            else:
                q4_2_ans_radio='0'
            
            if q5_1_ans_radio=='ΝΑΙ':
                q5_1_ans_radio='10'
            else:
                q5_1_ans_radio='0'
            
            if q5_2_ans_radio=='ΝΑΙ':
                q5_2_ans_radio='10'
            else:
                q5_2_ans_radio='0'

            result_val = ( ( int(q1_1_ans_radio) + int(q1_2_ans_radio) + int(q1_3_ans_radio) + int(q1_4_ans_radio) 
                        + int(q1_5_ans_radio) +int(q2_1_ans_radio)  +int(q2_2_ans_radio) +int(q2_3_ans_radio)+int(q2_4_ans_radio)+int(q3_1_ans_radio)
                        +int(q3_2_ans_radio)+int(q3_3_ans_radio) +int(q4_1_ans_radio)+int(q4_2_ans_radio) +int(q5_1_ans_radio)
                        +int(q5_2_ans_radio)+int(q5_3_ans_radio)  ) / (17*10)) * 100
            st.write(result_val)

            fig = donut_pct_Chart(round(result_val,2), '#618abb', 'rgb(240,240,240)', ['% Ποσοστό Ετοιμότητας', ' '])
            st.plotly_chart(fig, use_container_width=True)

            sql="update forms set title=%s,q1_text=%s,q1_1_ans_radio=%s,q1_2_ans_radio=%s,q1_3_ans_radio=%s,q1_4_ans_radio=%s,q1_5_ans_radio=%s,q2_text=%s,q2_1_ans_radio=%s,q2_2_ans_radio=%s,q2_3_ans_radio=%s,q2_4_ans_radio=%s,q3_text=%s,q3_1_ans_radio=%s,q3_2_ans_radio=%s,q3_3_ans_radio=%s,q4_text=%s,q4_1_ans_radio=%s,q4_2_ans_radio=%s,q5_text=%s,q5_1_ans_radio=%s,q5_2_ans_radio=%s,q5_3_ans_radio=%s where id=%s"
            val=(title,q1_text,q1_1_ans_radio,q1_2_ans_radio,q1_3_ans_radio,q1_4_ans_radio,q1_5_ans_radio,q2_text,q2_1_ans_radio,q2_2_ans_radio,q2_3_ans_radio,q2_4_ans_radio,q3_text,q3_1_ans_radio,q3_2_ans_radio,q3_3_ans_radio,q4_text,q4_1_ans_radio,q4_2_ans_radio,q5_text,q5_1_ans_radio,q5_2_ans_radio,q5_3_ans_radio,str(selected_id_value))
            mycursor.execute(sql,val)
            conn.commit()
            # Display a success message
            
            st.success("Η φόρμα σας ενημερώθηκε με τις τελευταίες αλλαγές!")
            if int(result_val) >= 80:
                st.write("Φαίνεται πως είστε ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Διερευνήστε τυχόν σημεία βελτίωσης και προχωρήστε στην συμπλήρωση των οικονομικών στοιχείων.")
                # return title
            elif (int(result_val) >= 50) and (int(result_val)<80):
                st.write("Φαίνεται πως είστε αρκετά ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Θα ήταν χρήσιμο να αναλύσετε περισσότερο την ιδέα σας στα πεδία που δεν νιώθετε σιγουριά, πριν προχωρήσετε στα οικονομικά στοιχεία.")
                # return title
            else:
                st.write("Φαίνεται πως δεν είστε ικανοποιημένος/η από την περιγραφή της επιχειρηματικής ιδέας σας. Καλύτερα να αναλύσετε περισσότερο την ιδέα σας, πριν προχωρήσετε στα οικονομικά στοιχεία.")
            # return title
            # result_val=((int(q1_1_ans_radio)+int(q2_1_ans_radio)+int(q2_2_ans_radio)+int(q3_ans_radio))/4)*10
            # st.write(result_val)
            # fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
            # st.plotly_chart(fig,use_container_width=True)



    if(option=="Delete"):
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


        if selected_id:
            mycursor.execute("select * from forms where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

            st.write(row[1],row[2],row[3])

            if st.button("Remove"):
                try:
                    sql = "DELETE FROM forms WHERE id=%s AND koispe_id=%s"
                    val = (selected_id_value, id)
                    mycursor.execute(sql, val)

                    # Commit the transaction
                    conn.commit()

                    st.success("Record Deleted Successfully")
                    # st.experimental_rerun()

                except Exception as e:
                    st.error(f"Error deleting record: {str(e)}")
    
            # if st.button("remove"):
            #     st.write(str(selected_id_value))
            #     st.write(str(id))

            #     # mycursor.execute("delete from forms where id="+str(selected_id_value)+" and koispe_id="+str(id)+" ")
            #     sql="DELETE FROM forms WHERE id=%s and koispe_id=%s"
            #     val=(selected_id_value,id)
            #     mycursor.execute(sql,val)
            #     st.success("Record Deleted Succesfully")
                # st.error("are you sure?")
                # # mycursor.execute("delete from forms where id="+str(row[0])+"and koispe_id="+str(row[1])+" and creation_date="+str(row[2])+"")
                # if(st.button("yes")):
                #     st.write("Done")
                #     mycursor.execute("delete from forms where id="+str(selected_id_value)+" and koispe_id="+str(id)+" ")
                #     st.success("Record Deleted Succesfully")
                # elif(st.button("No")):
                #     pass
    if(option=="export"):

        mycursor.execute("select * from forms where koispe_id="+str(id)+"")
        result = mycursor.fetchall()
        # for row in result:
        #     st.write(row)
        # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]
        return_creation_date=[row[2] for row in result]
        return_year=[row[3] for row in result]
        return_identifierform=["Title:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
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
        # st.write(f"Selected Date: {selected_id}")
        # st.write(f"Corresponding ID: {selected_id_value}")

        if selected_id:
                mycursor.execute("select * from forms where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
                result = mycursor.fetchall()
                for row in result:
                    pass
                    # st.write(row)
                
                title=row[3]
                q1_text=row[4]
                q1_1_ans_radio=row[5]
                q1_2_ans_radio=row[6]
                q1_3_ans_radio=row[7]
                q1_4_ans_radio=row[8]
                q1_5_ans_radio=row[9]
                q2_text=row[10]
                q2_1_ans_radio=row[11]
                q2_2_ans_radio=row[12]
                q2_3_ans_radio=row[13]
                q2_4_ans_radio=row[14]
                q3_text=row[15]
                q3_1_ans_radio=row[16]
                q3_2_ans_radio=row[17]
                q3_3_ans_radio=row[18]
                q4_text=row[19]
                q4_1_ans_radio=row[20]
                q4_2_ans_radio=row[21]
                q5_text=row[22]
                q5_1_ans_radio=row[23]
                q5_2_ans_radio=row[24]
                q5_3_ans_radio=row[25]


                result_val =round(( ( int(q1_1_ans_radio) + int(q1_2_ans_radio) + int(q1_3_ans_radio) + int(q1_4_ans_radio) 
                            + int(q1_5_ans_radio) +int(q2_1_ans_radio)  +int(q2_2_ans_radio) +int(q2_3_ans_radio)+int(q2_4_ans_radio)+int(q3_1_ans_radio)
                            +int(q3_2_ans_radio)+int(q3_3_ans_radio) +int(q4_1_ans_radio)+int(q4_2_ans_radio) +int(q5_1_ans_radio)
                            +int(q5_2_ans_radio)+int(q5_3_ans_radio)  ) / (17*10)) * 100,2) 
                ##########################
                # st.write(result_val)                #st.write(result_val)
                fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
                #st.plotly_chart(fig,use_container_width=True)

                # Render the figure as an image (e.g., PNG)
                img_bytes = pio.to_image(fig, format="png")

                # Store the image binary data in a variable
                image_variable = io.BytesIO(img_bytes)
                image_base64 = base64.b64encode(image_variable.getvalue()).decode()
                ########################
                colors = ['#618abb','#00235e','#F0894F']

                columns = ['D9', 'D10', 'D11']
                # kpdf_selected = kpdf[columns]
                # Create the stacked bar plot using Plotly
                legend_labels = ['Γενικού Πληθυσμού', 'ΛΥΨΥ', 'ΕΚΟ']
                fig1=stackedChart(columns,kpdf,legend_labels,'Έτος','% επί του Συνόλου',colors)

                img_bytes = pio.to_image(fig1, format="png")

                # Store the image binary data in a variable
                image_variable = io.BytesIO(img_bytes)

                # Encode the image data as base64
                image_base64_1 = base64.b64encode(image_variable.getvalue()).decode()
                #######################
                colors2 = ['#00235e','#F0894F','#618abb']

                columns2 = ['D26', 'D27', 'D28']
                legend_labels = ['Κτηρια & Εξ.Χώροι ','Εστίαση','Λοιπές Δραστηριότητες']
                # kpdf_selected = kpdf[columns2]
                # Create the stacked bar plot using Plotly
                fig2=stackedChart2(columns2,kpdf,legend_labels,'Έτος','Συχνότητα',colors2)
                # st.plotly_chart(fig,use_container_width=True)

                img_bytes = pio.to_image(fig2, format="png")

                # Store the image binary data in a variable
                image_variable = io.BytesIO(img_bytes)

                # Encode the image data as base64
                image_base64_2 = base64.b64encode(image_variable.getvalue()).decode()
                #######################
                categories=kpdf['year'].tolist()
                # Sample data
                # categories = ['Category A', 'Category B', 'Category C', 'Category D']
                values =kpdf['D24'].astype(float).tolist()
                line_labels=kpdf['D29'].tolist()
                fig3=pctChangeV2(categories,values,line_labels,'Κύκλοι Εργασιών','Κυκλ.Εργασιών')
                # fig=pctChangeChart(values,categories,'Values','Ποσοστιαία μεταβολή','Percentage Change','Values')
                #st.plotly_chart(fig,use_container_width=True)

                img_bytes = pio.to_image(fig3, format="png")

                # Store the image binary data in a variable
                image_variable = io.BytesIO(img_bytes)

                # Encode the image data as base64
                image_base64_3 = base64.b64encode(image_variable.getvalue()).decode()
                #######################
                env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
                template = env.get_template("template.html")

                #desc=row[6]
                #desc2=" sdas  dasf 22222"
                # period=perds
                # submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

                html = template.render(
                    title=row[3],
                    q1_text=row[4],
                    q1_1_ans_radio=row[5],
                    q1_2_ans_radio=row[6],
                    q1_3_ans_radio=row[7],
                    q1_4_ans_radio=row[8],
                    q1_5_ans_radio=row[9],
                    q2_text=row[10],
                    q2_1_ans_radio=row[11],
                    q2_2_ans_radio=row[12],
                    q2_3_ans_radio=row[13],
                    q2_4_ans_radio=row[14],
                    q3_text=row[15],
                    q3_1_ans_radio=row[16],
                    q3_2_ans_radio=row[17],
                    q3_3_ans_radio=row[18],
                    q4_text=row[19],
                    q4_1_ans_radio=row[20],
                    q4_2_ans_radio=row[21],
                    q5_text=row[22],
                    q5_1_ans_radio=row[23],
                    q5_2_ans_radio=row[24],
                    q5_3_ans_radio=row[25],




                    # title=row[3],
                    # q1_text=row[4],
                    # q1_ans_radio=row[5],
                    # q2_text=row[6],
                    # q2_1_ans_radio=row[7],
                    # q2_2_ans_radio=row[8],
                    # q3_text=row[9],
                    # q3_ans_radio=row[10],
                    image_base64=image_base64,
                    image_base64_1=image_base64_1,
                    image_base64_2=image_base64_2,
                    image_base64_3=image_base64_3
                )

                pdf = pdfkit.from_string(html, False)
                st.download_button(
                        "⬇️ Λήψη Business Plan Report",
                        data=pdf,
                        file_name="diploma.pdf",
                        mime="application/octet-stream",
                    )
########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# FORM 2
########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     
def e_button10(id,kpdf):
    st.title("Οικονομικά Στοιχεία")
    conn = init_connection()
    # id = st.number_input("Enter ID", userid)
    # total_days = st.number_input("Enter total days off", min_value=0, value=total_daysoff)
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete","export"))
    mycursor = conn.cursor()
    
    if option == "Create":
        form2(id)
    if option == "Read":
        st.subheader("Read all Submitted Forms")
        mycursor.execute("select * from forms2 where koispe_id="+str(id)+"")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)
            # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]

        # Display the list of return_ids
        st.write(return_ids)
        st.write(str(return_ids))

    if option =="Update":
        st.subheader("Επεξεργασία καταχωρημένων Οικονομικών Στοιχείων")
        st.write("Επέλεξε την φόρμα Οικονομικών Στοιχείων που θέλεις να επεξεργαστείς:")
        mycursor.execute("select * from forms2 where koispe_id="+str(id)+" ORDER BY creation_date DESC")
        result = mycursor.fetchall()
        # for row in result:
        #     st.write(row)
            # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]
        return_creation_date=[row[2] for row in result]
        return_year=[row[3] for row in result]
        return_identifierform=["Τίτλος:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
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
        # st.write(f"Selected Date: {selected_id}")
        # st.write(f"Corresponding ID: {selected_id_value}")

        with st.form(key="edit_form"):
            if selected_id:
                mycursor.execute("select * from forms2 where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
                result = mycursor.fetchall()
                for row in result:
                    # st.write(row)
                    pass

                # options = ["0","1", "2", "3", "4", "5","6","7","8","9","10"]
                # option2=["ΟΧΙ","ΝΑΙ"]
                st.title("Τίτλος επιχειρηματικής ιδέας")
                title=st.text_area("",key="title",value=row[3])

                #QUESTION 6
                st.subheader("Κτίρια & Υποδομές")
                st.markdown("<h4>Σε αυτή την κατηγορία συμπεριλαμβάνεται η πάγια αγορά χώρου για την εγκατάσταση της επιχείρησης</h4>",unsafe_allow_html=True)

                q6_text = st.text_area("Γράψε ελεύθερο κείμενο", key="q6text",value=row[4], height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q6_1_ans_num=st.number_input('Συμπληρώστε νούμερο:',key="q6_1_ans_num", value=row[5])
                q6_1_calc=q6_1_ans_num*0.04


                #QUESTION 7
                # st.title("Εξοπλισμός & Έπιπλα")
                # st.subheader("Σε αυτή την κατηγορία συμπεριλαμβάνεται το σύνολο του απαραίτητου εξοπλισμού και τα έπιπλα για τον χώρο της νέας επιχείρησης")

                # q7_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[7] ,key="q7text",height=300)
                
                # q7_1_ans_num=st.number_input('Kόστος:',key="q7_1_ans_num",value=row[8])
                # st.write('To Κόστος ειναι:', q7_1_ans_num)
                # q7_1_calc=q7_1_ans_num*0.1

                # st.write('Ετήσια απόσβεση:',q7_1_calc)


                questions = [
                            {"number": 7, "title": "Εξοπλισμός & Έπιπλα", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνεται το σύνολο του απαραίτητου εξοπλισμού και τα έπιπλα για τον χώρο της νέας επιχείρησης", "calc_coefficient": 0.1},
                            {"number": 8, "title": "Εργασίες διαμόρφωσης, εγκατάστασης κλπ", "text": "Συμπεριλαμβάνονται τα έξοδα για τις εργασίες που απαιτούνται στον χώρο για την έναρξη λειτουργίας της επιχείρησης", "calc_coefficient": 0},
                            {"number": 9, "title": "Μηχανήματα, εξοπλισμός εκτός Η/Υ και λογισμικού", "text": "Η κατηγορία συμπεριλαμβάνει την αγορά μηχανημάτων π.χ εκτυπωτές κλπ.", "calc_coefficient": 0.1},
                            {"number": 10, "title": "Εξοπλισμός Η/Υ, κύριος και περιφερειακός & λογισμικό", "text": "Η κατηγορία συμπεριλαμβάνει την αγορά μηχανημάτων π.χ πρόγραμμα παραγγελιοληψίας, λογιστικά /εμπορικά προγράμματα κλπ.", "calc_coefficient": 0.2},
                            {"number": 11, "title": "Λοιπές υπηρεσίες", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνονται υπηρεσίες τρίτων π.χ. πολιτικού μηχανικού για σχέδια – κατόψεις αλλά και την έκδοση άδειας λειτουργίας, υγειονολόγου ΤΕ για τη σύνταξη της μελέτης λειτουργίας της επιχείρησης, μηχανολόγου μηχανικού για μελέτη πυροπροστασίας κλπ.", "calc_coefficient": 0.2},
                            {"number": 12, "title": "Αρχικό απόθεμα σε πρώτες και βοηθητικές ύλες", "text": "Συμπεριλαμβάνεται κάθε υλικό αγαθό που ανήκει στην επιχείρηση και προορίζεται για να πωληθεί στην κατάσταση που βρίσκεται ή να επεξεργαστεί για τους σκοπούς της παραγωγής", "calc_coefficient": 0},
                            {"number": 13, "title": "Λοιπά έξοδα εκκίνησης", "text": "Σε αυτή την κατηγορία συμπεριλαμβάνονται τα έξοδα που προκύπτουν κατά τη διαδικασία δημιουργίας μιας νέας επιχείρησης και δεν συμπεριλαμβάνονται στις ανωτέρω ενότητες", "calc_coefficient": 0}
                        ]
                # QUESTION 7
                st.subheader(questions[0]["title"])
                st.markdown("<h4>"+questions[0]["text"]+"</h4>",unsafe_allow_html=True)

                q7_text = st.text_area("Γράψε ελεύθερο κείμενο", value=row[7], key="q7text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q7_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q71ansnum",value=row[8])
                q7_1_calc = q7_1_ans_num * questions[0]["calc_coefficient"]

                # QUESTION 8
                st.title("")
                st.subheader(questions[1]["title"])
                st.markdown("<h4>"+questions[1]["text"]+"</h4>",unsafe_allow_html=True)

                q8_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[10], key="q8text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q8_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q81ansnum",value=row[11])
                q8_1_calc = q8_1_ans_num * questions[1]["calc_coefficient"]

                # QUESTION 9
                st.subheader(questions[2]["title"])
                st.markdown("<h4>"+questions[2]["text"]+"</h4>",unsafe_allow_html=True)

                q9_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[13] ,key="q9text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q9_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q91ansnum",value=row[14])
                q9_1_calc = q9_1_ans_num * questions[2]["calc_coefficient"]

                # QUESTION 10
                st.subheader(questions[3]["title"])
                st.markdown("<h4>"+questions[3]["text"]+"</h4>",unsafe_allow_html=True)

                q10_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[16] ,key="q10text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q10_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q101ansnum",value=row[17])
                q10_1_calc = q10_1_ans_num * questions[3]["calc_coefficient"]


                # QUESTION 11
                st.subheader(questions[4]["title"])
                st.markdown("<h4>"+questions[4]["text"]+"</h4>",unsafe_allow_html=True)

                q11_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[19], key="q11text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q11_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q111ansnum",value=row[20])
                q11_1_calc = q11_1_ans_num * questions[4]["calc_coefficient"]

                # QUESTION 12
                st.subheader(questions[5]["title"])
                st.markdown("<h4>"+questions[5]["text"]+"</h4>",unsafe_allow_html=True)

                q12_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[22], key="q12text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q12_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', value=row[23],key="q121ansnum")
                q12_1_calc = q12_1_ans_num * questions[5]["calc_coefficient"]


                # QUESTION 13
                st.subheader(questions[6]["title"])
                st.markdown("<h4>"+questions[6]["text"]+"</h4>",unsafe_allow_html=True)

                q13_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[25], key="q13text", height=300)
                st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q13_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q131ansnum",value=row[26])
                q13_1_calc = q13_1_ans_num * questions[6]["calc_coefficient"]


                # QUESTION 14
                st.subheader("Ενοικίαση χώρων")
                st.markdown("""<h4>Σε αυτή την κατηγορία, καταγράψτε τους χώρους που θα χρειαστούν για τη στέγαση της επιχειρηματικής δραστηριότητας και τυχόν άλλων χώρων που θα εξυπηρετούν τις ανάγκες της επιχείρησης λ.χ αποθήκη.
                Έπειτα υπολογίστε το ετήσιο κόστος για την ενοικίαση χώρου/ ων.
                Αν το μηνιαίο κόστος ενοικίασης χώρου είναι π.χ. 100€, υπολογίστε το ετήσιο κόστος πολλαπλασιάζοντας επί 12 (100*12=1200€). Εάν υπάρχουν περισσότεροι του ενός χώροι, προσθέστε τα ποσά που προκύπτουν.
                </h4>""",unsafe_allow_html=True)
                q14_text = st.text_area("Γράψε ελεύθερο κείμενο", value=row[28], key="q14text", height=300)
                st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος για την ενοικίαση χώρου/ων;</h4>",unsafe_allow_html=True)
                # st.markdown("<h4>Κόστος</h4>",unsafe_allow_html=True)
                q14_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q141ansnum",value=row[29])

                
                # QUESTION 15
                st.subheader("Δαπάνες μισθοδοσίας")
                st.markdown("""<h4>Καταγράψτε το σύνολο των εργαζομένων που θα απασχοληθούν στην επιχείρηση. Έπειτα υπολογίστε το ετήσιο κόστος μισθοδοσίας του συνόλου των εργαζομένων, λαμβάνοντας υπόψη το μισθολογικό κλιμάκιο που ανήκουν και τον χρόνο απασχόλησης. 
                Το κόστος είναι το άθροισμα των μικτών αποδοχών και εργοδοτικών εισφορών κάθε μήνα, ενώ επιπλέον, για κάθε ημερολογιακό έτος, προστίθεται δώρο Πάσχα & Χριστουγέννων, οι αποδοχές άδειας και η αποζημίωση της άδειας, αν προκύπτει.
                </h4>""",unsafe_allow_html=True)

                q15_text = st.text_area("Γράψε ελεύθερο κείμενο", value=row[30],key="q15text", height=300)
                st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος μισθοδοσίας;</h4>",unsafe_allow_html=True)
                q15_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q151ansnum",value=row[31])

                # QUESTION 16
                st.subheader("Παροχές υπηρεσιών τρίτων")
                st.markdown("""<h4>Καταγράψτε τις παροχές υπηρεσιών από τρίτους, που θα χρειαστούν κατά το πρώτο έτος λειτουργίας της επιχειρηματικής δραστηριότητας. Σε αυτή την κατηγορία συμπεριλαμβάνονται οι λογαριασμοί ΔΕΚΟ, έξοδα επαγγελματιών (δικηγόρος, λογιστής, τεχνικός ασφαλείας), έξοδα διαφήμισης κλπ.
                Έπειτα υπολογίστε το ετήσιο κόστος της κάθε υπηρεσίας, πολλαπλασιάζοντας επί 12 σε περιπτώσεις μηνιαίων χρεώσεων, π.χ. λογαριασμοί ΔΕΚΟ.
                </h4>""",unsafe_allow_html=True)

                q16_text = st.text_area("Γράψε ελεύθερο κείμενο", value=row[32],key="q16text", height=300)
                st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος παροχής υπηρεσιών από τρίτους;</h4>",unsafe_allow_html=True)
                q16_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q161ansnum",value=row[33])

                # QUESTION 17
                st.subheader("Λοιπά έκτακτα έξοδα")
                st.markdown("""<h4>Καταγράψτε τυχόν έκτακτα έξοδα που μπορεί να προκύψουν κατά τον πρώτο χρόνο λειτουργία της επιχειρηματικής δράσης (π.χ. βλάβη μηχανημάτων, οχημάτων, κλπ.).
                Έπειτα υπολογίστε το συνολικό ετήσιο κόστος έκτακτων εξόδων.</h4>""",unsafe_allow_html=True)

                q17_text = st.text_area("Γράψε ελεύθερο κείμενο",value=row[34], key="q17text", height=300)
                st.markdown("<h4>Πόσο υπολογίζετε το συνολικό ετήσιο κόστος έκτακτων εξόδων;<h4>",unsafe_allow_html=True)
                q17_1_ans_num = st.number_input('Συμπληρώστε νούμερο:', key="q171ansnum",value=row[35])


   









                submit_button_edit = st.form_submit_button("Update")



        if submit_button_edit:

            # st.write("Button click update")
            sql = """
                UPDATE forms2 
                SET 
                    title = %s,
                    q6_text = %s,
                    q6_1_ans_num = %s,
                    q6_1_calc = %s,
                    q7_text = %s,
                    q7_1_ans_num = %s,
                    q7_1_calc = %s,
                    q8_text = %s,
                    q8_1_ans_num = %s,
                    q8_1_calc = %s,
                    q9_text = %s,
                    q9_1_ans_num = %s,
                    q9_1_calc = %s,
                    q10_text = %s,
                    q10_1_ans_num = %s,
                    q10_1_calc = %s,
                    q11_text = %s,
                    q11_1_ans_num = %s,
                    q11_1_calc = %s,
                    q12_text = %s,
                    q12_1_ans_num = %s,
                    q12_1_calc = %s,
                    q13_text = %s,
                    q13_1_ans_num = %s,
                    q13_1_calc = %s,
                    q14_text=%s,
                    q14_1_ans_num=%s,
                    q15_text=%s,
                    q15_1_ans_num=%s,
                    q16_text=%s,
                    q16_1_ans_num=%s,
                    q17_text=%s,
                    q17_1_ans_num=%s
                WHERE id = %s
            """

            val = (
                title,
                q6_text,
                q6_1_ans_num,
                q6_1_calc,
                q7_text,
                q7_1_ans_num,
                q7_1_calc,
                q8_text,
                q8_1_ans_num,
                q8_1_calc,
                q9_text,
                q9_1_ans_num,
                q9_1_calc,
                q10_text,
                q10_1_ans_num,
                q10_1_calc,
                q11_text,
                q11_1_ans_num,
                q11_1_calc,
                q12_text,
                q12_1_ans_num,
                q12_1_calc,
                q13_text,
                q13_1_ans_num,
                q13_1_calc,
                q14_text,
                q14_1_ans_num,
                q15_text,
                q15_1_ans_num,
                q16_text,
                q16_1_ans_num,
                q17_text,
                q17_1_ans_num,
                str(selected_id_value)
            )

            mycursor.execute(sql, val)
            conn.commit()
            # st.success("Record Updated Successfully!!!")
            # st.title("Αποτελέσματα")
            # st.write("Λειτουργικά έξοδα:",(q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num))
            # st.write("Αποσβέσεις:",(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc))
            # st.write("Άθροισμα εξόδων:",(q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num)+(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc)  )
            # st.write("Μinumum εσόδων επιχειρηματικής δραστηριότητας",((q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num)+(q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc)))
            # # st.write("button click update")
            # sql="update forms2 set title=%s,q6_text=%s,q6_1_ans_num=%s,q6_1_calc=%s,q7_text=%s,q7_1_ans_num=%s, q7_1_calc=%s where id=%s"
            # val=(title,q6_text,q6_1_ans_num,q6_1_calc,q7_text,q7_1_ans_num,q7_1_calc,str(selected_id_value))
            # mycursor.execute(sql,val)
            # conn.commit()
            # st.success("Record Update Successfully!!!")

            SUM_ek=q6_1_calc+q7_1_calc+q8_1_calc+q9_1_calc+q10_1_calc+q11_1_calc+q12_1_calc+q13_1_calc
            SUM_leit=q14_1_ans_num+q15_1_ans_num+q16_1_ans_num+q17_1_ans_num

            st.write("Το κόστος εκκίνησης, δηλαδή το κεφάλαιο που χρειάζεται για την έναρξης της επιχειρηματικής ιδέας σας, είναι:"+str(SUM_ek))
            st.write("Το Λειτουργικό κόστος, δηλαδή κόστος για τη λειτουργία της επιχειρηματικής ιδέας σας, για ένα έτος είναι:"+str(SUM_leit))
            st.markdown(""" <table>
                                <tr>
                                    <th>Κατηγορία</th>
                                    <th>Ετήσια απόσβεση</th>
                                </tr>
                                <tr>
                                    <td>Κτίρια & Υποδομές</td>
                                    <td>"""+str(round(q6_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Εξοπλισμός & Έπιπλα</td>
                                    <td>"""+str(round(q7_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Εργασίες διαμόρφωσης, εγκατάστασης κλπ</td>
                                    <td>"""+str(round(q8_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Μηχανήματα, εξοπλισμός εκτός Η/Υ και λογισμικού</td>
                                    <td>"""+str(round(q8_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Εξοπλισμός Η/Υ, κύριος και περιφερειακός & λογισμικό</td>
                                    <td>"""+str(round(q10_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Λοιπές υπηρεσίες</td>
                                    <td>"""+str(round(q11_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Αρχικό απόθεμα σε πρώτες και βοηθητικές ύλες</td>
                                    <td>"""+str(round(q12_1_calc,2))+"""</td>
                                </tr>
                                <tr>
                                    <td>Λοιπά έξοδα εκκίνησης</td>
                                    <td>"""+str(round(q13_1_calc,2))+"""</td>
                                </tr>
                            </table>
            """,unsafe_allow_html=True)

            st.write("Συνεπώς, για να είναι βιώσιμη η επιχειρηματική ιδέα σας, κρίνεται απαραίτητο, το ελάχιστο των ετήσιων εσόδων να είναι: "+str(SUM_leit))
            st.warning("Για κάθε επόμενο έτος λειτουργίας της επιχειρηματικής ιδέας σας, θα πρέπει να λάβετε υπόψιν τυχόν αύξηση του λειτουργικού κόστους (π.χ αυξήσεις μισθών, ανατιμήσεις αγαθών, κλπ.) και τις αποσβέσεις.")
    if option=="Delete":
        mycursor.execute("select * from forms2 where koispe_id="+str(id)+"")
        result = mycursor.fetchall()
        if mycursor.rowcount!=0:
            pass
            # for row in result:
            #     st.write(row)
            # Extract values from the "return_id" column and store them in a list
            return_ids = [row[0] for row in result]
            return_creation_date=[row[2] for row in result]
            return_year=[row[3] for row in result]
            return_identifierform=["Title:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
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
            # st.write(f"Selected Date: {selected_id}")
            # st.write(f"Corresponding ID: {selected_id_value}")


            if selected_id:
                mycursor.execute("select * from forms2 where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
                result = mycursor.fetchall()
                for row in result:
                    # st.write(row)
                    pass

                # st.write(row[1],row[2],row[3])

                if st.button("Remove"):
                    try:
                        sql = "DELETE FROM forms2 WHERE id=%s AND koispe_id=%s"
                        val = (selected_id_value, id)
                        mycursor.execute(sql, val)

                        # Commit the transaction
                        conn.commit()

                        st.success("Record Deleted Successfully")
                        # st.experimental_rerun()

                    except Exception as e:
                        st.error(f"Error deleting record: {str(e)}")
        
                # if st.button("remove"):
                #     st.write(str(selected_id_value))
                #     st.write(str(id))

                #     # mycursor.execute("delete from forms where id="+str(selected_id_value)+" and koispe_id="+str(id)+" ")
                #     sql="DELETE FROM forms WHERE id=%s and koispe_id=%s"
                #     val=(selected_id_value,id)
                #     mycursor.execute(sql,val)
                #     st.success("Record Deleted Succesfully")
                    # st.error("are you sure?")
                    # # mycursor.execute("delete from forms where id="+str(row[0])+"and koispe_id="+str(row[1])+" and creation_date="+str(row[2])+"")
                    # if(st.button("yes")):
                    #     st.write("Done")
                    #     mycursor.execute("delete from forms where id="+str(selected_id_value)+" and koispe_id="+str(id)+" ")
                    #     st.success("Record Deleted Succesfully")
                    # elif(st.button("No")):
                    #     pass
        else:
            st.write("No records found to delete")    
    
    if option =="export":
        st.write("hello")
        # mycursor.execute("select * from forms where koispe_id="+str(id)+"")
        # result = mycursor.fetchall()
        # # for row in result:
        # #     st.write(row)
        # # Extract values from the "return_id" column and store them in a list
        # return_ids = [row[0] for row in result]
        # return_creation_date=[row[2] for row in result]
        # return_year=[row[3] for row in result]
        # return_identifierform=["Title:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
        # # st.write(return_identifierform)
        #  #getAllformsId
        # # st.write(str(return_ids))
        # # st.write(str(return_creation_date))
        # # Convert the list of datetime objects to a list of strings
        # date_str_list = [return_creation_date.strftime("%Y-%m-%d %H:%M:%S") for return_creation_date in return_creation_date]

        # # st.write(date_str_list)
        # # st.write(str(return_year))

        # #option=st.selectbox("Select an Form",date_str_list)

        # #st.write("You choose",str(option))

        # selected_id = st.selectbox("Select a Form", options=return_identifierform, index=0)
        # selected_id_index = return_identifierform.index(selected_id)
        # selected_id_value = return_ids[selected_id_index]

        # # Display the selected date and its corresponding ID
        # # st.write(f"Selected Date: {selected_id}")
        # # st.write(f"Corresponding ID: {selected_id_value}")
        mycursor.execute("select * from forms2 where koispe_id="+str(id)+" ORDER BY creation_date DESC")
        result = mycursor.fetchall()
        # for row in result:
        #     st.write(row)
            # Extract values from the "return_id" column and store them in a list
        return_ids = [row[0] for row in result]
        return_creation_date=[row[2] for row in result]
        return_year=[row[3] for row in result]
        return_identifierform=["Τίτλος:"+row[3]+" Creation Date:"+row[2].strftime("%Y-%m-%d %H:%M:%S")+" ID FORM:"+str(row[0]) for row in result]
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
        if selected_id:
            mycursor.execute("select * from forms2 where koispe_id="+str(id)+" and id="+str(selected_id_value)+"")
            result = mycursor.fetchall()
            for row in result:
                pass
                # st.write(row)
            
            title=row[3],
            q6_text=row[4],
            q6_1_ans_num=row[5],
            q6_1_calc=row[6],
            q7_text=row[7],
            q7_1_ans_num=row[8],
            q7_1_calc=row[9],
            q8_text=row[10],
            q8_1_ans_num=row[11],
            q8_1_calc=row[12],
            q9_text=row[13],
            q9_1_ans_num=row[14],
            q9_1_calc=row[15],
            q10_text=row[16],
            q10_1_ans_num=row[17],
            q10_1_calc=row[18],
            q11_text=row[19],
            q11_1_ans_num=row[20],
            q11_1_calc=row[21],
            q12_text=row[22],
            q12_1_ans_num=row[23],
            q12_1_calc=row[24],
            q13_text=row[25],
            q13_1_ans_num=row[26],
            q13_1_calc=row[27],
            q14_text=row[28],
            q14_1_ans_num=row[29],
            q15_text=row[30],
            q15_1_ans_num=row[31],
            q16_text=row[32],
            q16_1_ans_num=row[33],
            q17_text=row[34],
            q17_1_ans_num=row[35]


            # result_val =round(( ( int(q1_1_ans_radio) + int(q1_2_ans_radio) + int(q1_3_ans_radio) + int(q1_4_ans_radio) 
            #             + int(q1_5_ans_radio) +int(q2_1_ans_radio)  +int(q2_2_ans_radio) +int(q2_3_ans_radio)+int(q2_4_ans_radio)+int(q3_1_ans_radio)
            #             +int(q3_2_ans_radio)+int(q3_3_ans_radio) +int(q4_1_ans_radio)+int(q4_2_ans_radio) +int(q5_1_ans_radio)
            #             +int(q5_2_ans_radio)+int(q5_3_ans_radio)  ) / (17*10)) * 100,2) 
            
            # # st.write(result_val)                #st.write(result_val)
            # fig=donut_pct_Chart(result_val,'#618abb', 'rgb(240,240,240)',['% Ποσοστό Ετοιμότητας', ' '])
            # #st.plotly_chart(fig,use_container_width=True)

            # # Render the figure as an image (e.g., PNG)
            # img_bytes = pio.to_image(fig, format="png")

            # # Store the image binary data in a variable
            # image_variable = io.BytesIO(img_bytes)
            # image_base64 = base64.b64encode(image_variable.getvalue()).decode()
            #####

            env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
            template = env.get_template("template2.html")

            #desc=row[6]
            #desc2=" sdas  dasf 22222"
            # period=perds
            # submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

            html = template.render(
                title=row[3],
                q6_text=row[4],
                q6_1_ans_num=row[5],
                q6_1_calc=row[6],
                q7_text=row[7],
                q7_1_ans_num=row[8],
                q7_1_calc=row[9],
                q8_text=row[10],
                q8_1_ans_num=row[11],
                q8_1_calc=row[12],
                q9_text=row[13],
                q9_1_ans_num=row[14],
                q9_1_calc=row[15],
                q10_text=row[16],
                q10_1_ans_num=row[17],
                q10_1_calc=row[18],
                q11_text=row[19],
                q11_1_ans_num=row[20],
                q11_1_calc=row[21],
                q12_text=row[22],
                q12_1_ans_num=row[23],
                q12_1_calc=row[24],
                q13_text=row[25],
                q13_1_ans_num=row[26],
                q13_1_calc=row[27],
                q14_text=row[28],
                q14_1_ans_num=row[29],
                q15_text=row[30],
                q15_1_ans_num=row[31],
                q16_text=row[32],
                q16_1_ans_num=row[33],
                q17_text=row[34],
                q17_1_ans_num=row[35]
                # title=row[3],
                # q1_text=row[4],
                # q1_ans_radio=row[5],
                # q2_text=row[6],
                # q2_1_ans_radio=row[7],
                # q2_2_ans_radio=row[8],
                # q3_text=row[9],
                # q3_ans_radio=row[10],
                #image_base64=image_base64
            )

            pdf = pdfkit.from_string(html, False)
            st.download_button(
                    "⬇️ Λήψη Business Plan Report",
                    data=pdf,
                    file_name="diploma.pdf",
                    mime="application/octet-stream",
                )

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