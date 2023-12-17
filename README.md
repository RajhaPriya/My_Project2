# My_Project2
***Data Visualization and Exploration
A User-Friendly Tool Using Streamlit and Plotly***

The Phonepe pulse Github repository contains a large amount of data related to
various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner.

**Libraries/Modules needed required**
1. Plotly - (To plot and visualize the data)
2. Pandas - (To Create a DataFrame with the scraped data)
3. sqlite3 server- (To store and retrieve the data)
4. Streamlit - (To Create Graphical user Interface)
5. json - (To load the json files)
6. git.repo.base - (To clone the GitHub repository
7. PIL - The Python Imaging Library, used for opening, manipulating, and saving many different image file formats.


**Approach**

**Step 1: Cloning Github Repository**

Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as JSON. Use the below link to clone the phonepe github repository into your local drive.
  
  "!git clone https://github.com/PhonePe/pulse.git  "
  
**Step 2: Importing the Libraries:**
    import pandas as pd
    import sqlite3 as sql
    import streamlit as st
    import plotly.express as px
    import os
    import json
    from PIL import Image

**Step 3:Data transformation:**
After cloning, in this step the JSON files that are available in the folders are converted into the readeable and understandable DataFrame format by using the for loop and iterating file by file and then finally the DataFrame is created. In order to perform this step used os, json and pandas packages. And finally converted the dataframe into CSV file and storing in the local drive.

**Step 4: Database insertion**
To insert the dataframe into sqlite3, created a new database and tables using "sqlite3" library in Python and inserted the transformed data using SQL commands.

**Step 5:Dashboard creation**
To create colourful and insightful dashboard I've used Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in Pie, Bar, Geo map functions are used to display the data on a charts and map and Streamlit is used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.

**Step 6: Deployment**
Once created the dashboard, we can test it thoroughly and deploy it, making it accessible to users.
