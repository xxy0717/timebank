import streamlit as st
import time

def main():
    st.set_page_config(page_title="Time Bank")
    st.title("Time Bank")

    add_time = 0
    sub_time = 0
    total_time = 0
    start_time = None

    # Display the total time
    col1, col2 = st.beta_columns(2)
    with col1:
        st.subheader("Total Time")
        total_time_text = st.empty()
    with col2:
        st.subheader("Total Time Chart")
        total_time_chart = st.empty()

    # Add and Subtract buttons
    add_button, sub_button = st.beta_columns(2)
    add_pressed = add_button.button("Start Adding Time")
    sub_pressed = sub_button.button("Start Subtracting Time")

    # Update the total time when adding or subtracting
    while add_pressed or sub_pressed:
        # Adding
        if add_pressed:
            add_button.button("Stop Adding Time")
            if start_time is None:
                start_time = time.time()
            else:
                add_time += time.time() - start_time
                start_time = None
                add_pressed = False
        # Subtracting
        if sub_pressed:
            sub_button.button("Stop Subtracting Time")
            if start_time is None:
                start_time = time.time()
            else:
                sub_time += time.time() - start_time
                start_time = None
                sub_pressed = False

        total_time = add_time - sub_time
        total_time_text.markdown(f"{total_time:.2f} seconds")
        total_time_chart.bar_chart([total_time])

    # Show the final total time when not adding or subtracting
    total_time_text.markdown(f"{total_time:.2f} seconds")
    total_time_chart.bar_chart([total_time])

if __name__ == "__main__":
    main()
