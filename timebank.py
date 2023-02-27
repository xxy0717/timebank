import streamlit as st
import time
import threading

# Set page title
st.set_page_config(page_title="Time Bank")

# Define initial values
total_time = 0
time_unit = "seconds"
add_button_text = "Start Adding Time"
subtract_button_text = "Start Subtracting Time"

# Define helper function to convert seconds to specified time unit
def convert_time(seconds, time_unit):
    if time_unit == "seconds":
        return seconds
    elif time_unit == "minutes":
        return seconds / 60
    elif time_unit == "hours":
        return seconds / 3600
    elif time_unit == "days":
        return seconds / 86400

# Define function to update total time
def update_total_time(change):
    global total_time
    total_time += change

# Define function to run timer in background
def timer():
    while True:
        time.sleep(1)
        update_total_time(1)

# Define function to start and stop adding time
def add_time():
    global add_button_text
    if add_button_text == "Start Adding Time":
        add_button_text = "Stop Adding Time"
        timer_thread = st.experimental_thread(timer)
    else:
        add_button_text = "Start Adding Time"

# Define function to start and stop subtracting time
def subtract_time():
    global subtract_button_text
    if subtract_button_text == "Start Subtracting Time":
        subtract_button_text = "Stop Subtracting Time"
        timer_thread = st.experimental_background_thread(timer)
    else:
        subtract_button_text = "Start Subtracting Time"

# Define Streamlit app
def main():
    global total_time, time_unit, add_button_text, subtract_button_text

    # Add title and description
    st.title("Time Bank")
    st.write("This app allows you to add and subtract time.")

    # Add slider to select time unit
    time_unit = st.sidebar.selectbox("Select time unit:", ["seconds", "minutes", "hours", "days"])

    # Add total time display
    st.write(f"Total time: {convert_time(total_time, time_unit):,.2f} {time_unit}")

    # Add adding and subtracting buttons
    add_button = st.button(add_button_text)
    subtract_button = st.button(subtract_button_text)

    # Update total time and button text based on adding button click
    if add_button:
        add_time()
        if add_button_text == "Start Adding Time":
            update_total_time(1)
        st.experimental_rerun()

    # Update total time and button text based on subtracting button click
    if subtract_button:
        subtract_time()
        if subtract_button_text == "Start Subtracting Time":
            update_total_time(-1)
        st.experimental_rerun()

    # Add progress bar to represent total time
    st.progress(convert_time(total_time, time_unit) / 86400)

if __name__ == "__main__":
    main()
