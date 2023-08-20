import psycopg2
import psycopg2-binary
from datetime import date
import streamlit as st 


try:
        conn = psycopg2.connect(
        database = data_base,
        user = user ,
        password = password,
        host = host ,
        port = port 
        )

except Exception as error:
    print("opsy:", error)

cursor = conn.cursor()








def main():
    st.title("Gym Progress Tracker")

    # Display Sidebar

    options = st.sidebar.selectbox("Select Type", ("Leg Day", "Chest Day", "Arms Day"))

    if options == "Leg Day":
          today = date.today()
          body_part = options
          event_date = st.date_input("When's your birthday", (today))
          type = st.selectbox("Select muscle", ("leg press", "leg extensions", "lying leg curl", "seated calf raises"))
          reps = st.number_input('Reps', min_value=1, max_value=20, value=8, step=1)
          sets = st.number_input('Sets', min_value=1, max_value=20, value=3, step=1)
          weight = st.number_input('weight', min_value=1, max_value=300, value=30, step=5)
          body_weight = st.number_input('Body Weight', min_value=40, max_value=100, value=80, step=1)

          if st.button("Submit"):
                sql = "insert into public.helath(type,body_part,event_date,reps,sets,weight,body_weight) values(%s,%s,%s,%s,%s,%s,%s)"
                val = (type,body_part,event_date,reps,sets,weight,body_weight)
                cursor.execute(sql, val)
                conn.commit()
                cursor.close()
                st.success("record has been created")

    elif options == "Arms Day":
          today = date.today()
          body_part = options
          event_date = st.date_input("When's your birthday", (today))
          type = st.selectbox("Select muscle", ("facepulls", "Hammer strength", "Underhand lat pulldown", "back extensions", "seated incline curls"))
          reps = st.number_input('Reps', min_value=1, max_value=20, value=8, step=1)
          sets = st.number_input('Sets', min_value=1, max_value=20, value=3, step=1)
          weight = st.number_input('weight', min_value=1, max_value=300, value=30, step=5)
          body_weight = st.number_input('Body Weight', min_value=40, max_value=100, value=80, step=1)

          if st.button("Submit"):
                sql = "insert into public.helath(type,body_part,event_date,reps,sets,weight,body_weight) values(%s,%s,%s,%s,%s,%s,%s)"
                val = (type,body_part,event_date,reps,sets,weight,body_weight)
                cursor.execute(sql, val)
                conn.commit()
                cursor.close()
                st.success("record has been created")

    elif options == "Chest Day":
          today = date.today()
          body_part = options
          event_date = st.date_input("When's your birthday", (today))
          type = st.selectbox("Select muscle", ("lateral raises", "flat machine press", "decline machine press", "incline machine chest press", "Rope Pushdown", "close grip pushdown"))
          reps = st.number_input('Reps', min_value=1, max_value=20, value=8, step=1)
          sets = st.number_input('Sets', min_value=1, max_value=20, value=3, step=1)
          weight = st.number_input('weight', min_value=1, max_value=300, value=30, step=5)
          body_weight = st.number_input('Body Weight', min_value=40, max_value=100, value=80, step=1)

          if st.button("Submit"):
                sql = "insert into public.helath(type,body_part,event_date,reps,sets,weight,body_weight) values(%s,%s,%s,%s,%s,%s,%s)"
                val = (type,body_part,event_date,reps,sets,weight,body_weight)
                cursor.execute(sql, val)
                conn.commit()
                cursor.close()
                st.success("record has been created")





if __name__ == "__main__":
      main()