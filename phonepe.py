import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pymysql
import pymysql
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


db = pymysql.connect(
        host="localhost",
        user="root",
        password="123",
        database="project_2")
        

mycursor = db.cursor()
mycursor.execute("use project_2")


#streamlit setup
import streamlit as st


st.set_page_config (page_title= "Phonepe Pulse Data Visualization",
                   layout= "wide",
                   page_icon='📶',
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is cloned from Phonepe Pulse 
                               Github Repository"""})

with st.sidebar:
    st.image('ab.jpg')
    st.caption('Indians Digital Payment Wallet Phonepe')
    pdfFileObj = open('phonepe.pdf', 'rb')
    st.download_button('FACTSHEET', pdfFileObj, file_name='phonepe.pdf', mime='pdf')
 
st.subheader('About')
st.write("PhonePe started as a UPI (Unified Payments Interface) app in the year of 2016, allowing users to link their bank accounts and make seamless and instant fund transfers between banks. Over time, PhonePe has expanded its range of services to include - Money transfer, Investments, Online shopping, Digital Payments")
with st.sidebar:
    choice =  option_menu("Menu", ["Home","Top Charts","Data Survey"], 
                icons=["house","graph-up-arrow","bar-chart-line"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "15px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})

if choice == "Home":
    st.image("def.png")
    st.markdown("## :violet[Data Visualization and Exploration]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")
    col1,col2 = st.columns([4,2])
    with col1:
        st.write("Data Visualization")
        st.write("Data Analysis")
        st.markdown(":violet[Key Skills:] Github Cloning, Python, Pandas, MySQL, Streamlit, Plotly")
        st.markdown(":violet[Overview :] In Streamlit web app it is easy to visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Plotly's built-in Pie, Bar, Geo map functions are used to display the data on a charts and map and Streamlit is used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.")
    with col2:
        st.image("images.jpg")


# MENU 2 - TOP CHARTS
if choice == "Top Charts":
    st.markdown("# :violet[Graphs with manual adjustments of Year and Quarter]")
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with colum2:
        st.info('''#### My demo video of the PhonePe ''')
        video_file = open('phonepe.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    if Type == 'Transactions':
        select = st.selectbox("Select any one", ["State", "District", "Pincode"])

        # Consolidate the common condition
        if Year == 2023 and Quarter in [4]:
            st.markdown("No data to display for this selected Quarter yet")
        else:
            if select == "State":
                st.markdown("### :violet[State wise Transactions Pie-chart]")
                mycursor.execute(f"SELECT Year, Quarter, state, SUM(Transaction_count) as Total_Transactions_Count, SUM(Transaction_amount) as Total_Transaction_amount FROM agg_trans where Year = {Year} and Quarter = {Quarter} group by state order by Total_Transaction_amount desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'Quarter', 'State', 'Total_Transactions_Count', 'Total_Transaction_amount'])
                fig = px.pie(df, values='Total_Transactions_Count', names='State', title='Top Ten Total_Transaction_amount percentage of the State', color_discrete_sequence=px.colors.sequential.Purp, hover_data=['Total_Transaction_amount'])
                st.plotly_chart(fig, use_container_width=True, height=600, width=800)
                st.dataframe(df)


            if select == "District":
                st.markdown("### :violet[Transaction count according to District]")
                select_state = st.selectbox( "** Please select state to visualize**",
                                            ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                         'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat',
                                         'haryana','himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh',
                                         'lakshadweep','madhya-pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','puducherry',
                                         'punjab','rajasthan','sikkim','tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=22,key="state_to_selectbox")
                mycursor.execute(f"SELECT State, District, Year, Quarter, SUM(Transaction_count) as Total_Transactions_Count FROM map_trans WHERE Year = {Year} AND Quarter = {Quarter} AND State = '{select_state}' GROUP BY State, District, Year, Quarter ORDER BY Total_Transactions_Count desc limit 10;")
                df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Year','Quarter','Total_Transactions_Count'])
                fig=px.bar(df1,
                       title="Transaction Count According To District",
                       x="District",
                       y="Total_Transactions_Count",
                       color="Total_Transactions_Count",
                       hover_name= "State",
                       color_discrete_sequence= px.colors.sequential.Plasma_r)            
                st.plotly_chart(fig,use_container_width=True)
                st.dataframe(df1)

            if select == "Pincode":
                st.markdown("### :violet[Pincode-wise Transaction count]")
                mycursor.execute(f"SELECT State, Pincode, SUM(Transaction_count) as Total_Transactions_Count, SUM(Transaction_amount) as Total_transaction_amount FROM top_trans where Year = {Year} and Quarter = {Quarter} GROUP BY State, Pincode ORDER BY Total_transaction_amount DESC limit 10;")
                df2 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Pincode', 'Total_Transactions_Count', 'Total_transaction_amount'])
                fig=px.bar(df2,
                       title="Transaction Count According To Pincode",
                       x="State",
                       y="Total_Transactions_Count",
                       color="Pincode",
                       hover_name= "State",
                       color_discrete_sequence= px.colors.sequential.Plasma_r)            
                st.plotly_chart(fig,use_container_width=True)
                st.dataframe(df2)
                    
    if Type == 'Users':
            select = st.selectbox("Select any one", ["State", "District", "Pincode"])
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("No data to display for this selected Quarter of 2022")
            elif Year == 2023 and Quarter in [1,2,3,4]:
                st.markdown("No data to display for this selected Quarter of 2023 yet")
            else:
                if select == "State":
                    st.markdown("### :violet[Statewise average device users data]")
                    mycursor.execute(f"SELECT State, Device, SUM(User_count) as User_count, AVG(Device_share_percent)*100 as Avg_Percent FROM agg_user WHERE year = {Year} and quarter = {Quarter} GROUP BY State, Device ORDER BY User_count DESC LIMIT 10;")
                    df3 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Device', 'User_count', 'Avg_Percent'])
                    fig = px.bar(df3,
                                title='Top 10 State wise Device Share count',
                                x="User_count",
                                y="State",
                                orientation='h',
                                hover_data=['Device', 'Avg_Percent'],
                                color='Avg_Percent', 
                                color_continuous_scale=px.colors.sequential.Agsunset)
                    st.plotly_chart(fig,use_container_width=True)   
                    st.dataframe(df3)

                if select == "District":
                    st.markdown("### :violet[Districtwise Registered total users]")
                    mycursor.execute(f"select State, District, sum(Reg_users) as Total_users from map_user where year = {Year} and quarter = {Quarter} group by State, District order by Total_users desc limit 10;")
                    df4 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'District', 'Total_users'])
                    df4.Total_users = df4.Total_users.astype(float)
                    fig = px.bar(df4,
                                title='Top 10 District wise app users',
                                x="Total_users",
                                y="District",
                                orientation='h',
                                color='Total_users',
                                hover_data= 'State',
                                #hover_data= 'Total_App_opens', #removed since all are mostly 0 
                                color_continuous_scale=px.colors.sequential.Teal)
                    st.plotly_chart(fig,use_container_width=True)
                    st.dataframe(df4)
                    
                if select == "Pincode":
                    st.markdown("### :violet[Pincodewise-users]")
                    mycursor.execute(f"select State, Pincode, sum(Reg_users) as Total_Users from top_user where year = {Year} and quarter = {Quarter} group by State, Pincode order by Total_Users desc limit 10;")
                    df5 = pd.DataFrame(mycursor.fetchall(), columns=['State','Pincode','Total_Users'])
                    fig = px.pie(df5,
                                values='Pincode',
                                names='Total_Users',
                                title='Top 10 Pincode wise app users percentage',
                                color_discrete_sequence=px.colors.sequential.RdBu,
                                hover_data=['State'])
                    fig.update_traces(textposition='inside', textinfo='percent')
                    st.plotly_chart(fig,use_container_width=True)
                    st.dataframe(df5)
                
if choice == "Data Survey":
    Year = st.slider("**Year**", min_value=2018, max_value=2023)
    Quarter = st.slider("Quarter", min_value=1, max_value=4)
    Type = st.selectbox("**Type**", ("Transactions", "Users"))

    if Type == "Transactions":  
            st.markdown(":violet[This Geographical India map is used to visualize state-based data according to Transcation_count and Transcation_amount over the selected Year and Quarter]")
            mycursor.execute(f"SELECT state, SUM(Transaction_count) AS  All_Transaction, SUM(Total_amount) AS Total_Payment_value FROM map_trans WHERE year = {Year} AND Quarter = {Quarter} GROUP BY state ORDER BY state;")
            df6 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'All_Transaction', 'Total_Payment_value'])
            # Read state names from CSV
            df7 = pd.read_csv('State.csv')
            df6.State = df7
            fig = px.choropleth(df6, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locationmode='geojson-id',  
                                    locations='State',
                                    color='Total_Payment_value',
                                    hover_data='All_Transaction',
                                    color_continuous_scale='dense')
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(":violet[All time top 10 transaction details]")
            mycursor.execute(f"SELECT state, Year, Quarter, SUM(Transaction_count) AS  All_Transaction,  CONCAT(' ₹', SUM(Total_amount)) AS Total_Payment_value FROM map_trans WHERE year = {Year} AND Quarter =  {Quarter} GROUP BY state ORDER BY Total_Payment_value desc limit 10;")
            result = mycursor.fetchall()
            df = pd.DataFrame(result, columns=['State','Year', 'Quarter', 'All_Transaction', 'Total_Payment_value'])
            st.dataframe(df)
    if Type == "Users":
        st.markdown(":violet[This Geographical India map is used to visualize state-based Phonepe users with count over the selected Year and Quarter]")
        mycursor.execute(f"select State, sum(Reg_users) as Total_users, sum(App_opens) as Total_AppOpen from map_user where year = {Year} and quarter = {Quarter} group by State order by State;")
        df8 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_users', 'Total_AppOpen'])
        df9 = pd.read_csv('State.csv')
        df8.Total_AppOpen = df8.Total_AppOpen.astype(float)
        df8.State = df9
        fig = px.choropleth(df8, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Total_AppOpen',
                                hover_data= 'Total_users',
                                color_continuous_scale='sunset')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(":violet[All time top 10 transaction details]")
        mycursor.execute(f"select State, Year, Quarter, sum(Reg_users) as Total_users, sum(App_opens) as Total_AppOpen from map_user where year = {Year} and quarter = {Quarter} group by State order by Total_AppOpen desc limit 10;")
        result = mycursor.fetchall()
        df10 = pd.DataFrame(result, columns=['State','Year', 'Quarter', 'Total_users', 'Total_AppOpen'])
        st.dataframe(df10)