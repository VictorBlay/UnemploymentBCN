import base64

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{sel_gender}.csv">Download CSV File</a>'
    return href
des=st.markdown(filedownload(df), unsafe_allow_html=True)
col1.write(des)

#para poder descargar el dataFrame en un csv
#Funcionava pero despues petava la pagina con este error: StreamlitAPIException: _repr_html_() is not a valid Streamlit command.
