import streamlit as st
import pickle

with open('questions_dict.pickle', 'rb') as file:
    questions_dict = pickle.load(file) 

with open('dependent_dropdown_dict.pickle', 'rb') as file:
    dropdown_dict = pickle.load(file)

# Extracting years, dates, and shifts from the loaded dictionary
years = [''] + list(dropdown_dict.keys())

selected_year = st.selectbox("Select a year", years, index=0)

dates = []

# Once the year is selected, populate the dates for that year
if selected_year in dropdown_dict:
    dates = [''] + list(dropdown_dict[selected_year].keys())

selected_date = st.selectbox("Select a date", dates, index=0)
    
shifts = []

# Once the date is selected, get the shifts for that date
if selected_year in questions_dict and selected_date in questions_dict[selected_year]:
    shifts = list(questions_dict[selected_year][selected_date].keys())

selected_shift = st.selectbox("Select a shift", shifts, index=0)
show_questions = st.button("Show Questions")

if show_questions:
    if not selected_year or not selected_date or not selected_shift:
        st.warning("Please select a year, date, and shift to show questions.")
    else:
        st.title(f"JEE MAINS {selected_date[:2]}-{selected_date[3:]}-{selected_year} {str.upper(selected_shift)} SHIFT")
        if selected_year in questions_dict and selected_date in questions_dict[selected_year] and selected_shift in questions_dict[selected_year][selected_date]:
            questions = questions_dict[selected_year][selected_date][selected_shift]
            if questions:
                counter = 1
                for question_key, question_value in questions.items():
                    st.write(f"Question {counter:02d}: {question_value['Question']}")
                    options = question_value.get("Option", [])
                    if options:
                        for idx, option in enumerate(options, start=1):
                            st.write(f"{chr(64 + idx)}. {option}")
                    st.markdown("---")
                    counter += 1
            else:
                st.write("No questions available for the selected year, date, and shift")
        else:
            st.write("No data available for the selected year, date, and shift")