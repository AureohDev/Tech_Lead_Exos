import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

def file_selector(folder_path=os.path.dirname(os.path.realpath(__file__))+"/source"):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Choisissez un fichier",filenames)
    return os.path.join(folder_path,selected_filename)


# Title
st.title("Star Wars Planète & Véhicules Data App")

# File Selector
st.header("Séléction d'un fichier")
filename = file_selector()
st.info("Vous avez choisis le fichier {}".format(filename))

# Read Dataset
data = pd.read_csv(filename)
st.header("Affichage du dataset")

# Show Dataset rows
if st.checkbox("Afficher X lignes du dataset"):
    number_rows = st.number_input("Nombre de lignes à afficher",value=1)
    st.dataframe(data.head(number_rows))

# Show Dataset columns and their types
st.subheader("Affichage des colonnes et leurs données")
if st.checkbox("Afficher noms des colonnes"):
	st.write(data.columns)

selected_columns = st.multiselect("Choisissez une colonne",data.columns.tolist())
if len(selected_columns) != 0: 
    data_columns = data[selected_columns]
    st.dataframe(data_columns.dtypes)

# Show Dataset Shape
st.subheader("Affichage de la shape")
if st.checkbox("Afficher Shape"):
	data_dim = st.radio("Afficher la dimensions des",("Lignes","Colonnes"))
	if data_dim == 'Lignes':
		st.text("Nombres de lignes")
		st.write(data.shape[0])
	elif data_dim == 'Colonnes':
		st.text("Nombre de colonnes")
		st.write(data.shape[1])
	else:
		st.write(data.shape)

# Show Dataset Datatypes
st.subheader("Affichage des statistiques descriptives")
if st.checkbox("Afficher Datatypes"):
		st.write(data.dtypes)

# Show Dataset Graphs
st.subheader("Affichage Graphique des données")

if st.checkbox("HeatMap"):
    heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True)
    heatmap.set_title("Heatmap", fontdict={'fontsize':12}, pad=12)
    st.write(heatmap)
    st.pyplot()

if st.checkbox("Graphique en Barre"):
    
    selected_column = st.selectbox("Choisissez une colonne à visualiser",data.columns.tolist())
    if len(selected_column) != 0: 
        data_column = data[selected_column]
        displot = sns.displot(x=data_column)
        st.write(displot)
        st.pyplot()

if st.button("Thanks"):
    st.balloons()