import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.markdown("<h5 style='text-align: center; color: black;'>MF Financial Simulation</h5>", unsafe_allow_html=True)


df=pd.read_csv("SOPLatest29.csv")


df_month ={"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}

df_month=pd.DataFrame.from_dict(df_month)

with st.sidebar:
    start_mon_vol, end_mon_vol = st.select_slider('Month-VOL',
        options=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        value=('Jan', 'Dec'))
    col1,col2=st.sidebar.columns(2)
    with  col1:
        prd_vol = st.multiselect("Product Group-VOL",set(df['Product Sub-Group']))
    with col2:
        cust_vol = st.multiselect("Cust Group -VOL",set(df['Customer Group']))
    col1,col2,col3,col4=st.columns(4)
    with col1:
        vol_selectbox = st.slider('Volume',-100,100,0)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(vol_selectbox)+"</h3>", unsafe_allow_html=True)
    with col3:
        abs_vol_selectbox = st.slider('Abs_Volume',-100.0,100.0,0.0)
    with col4:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(abs_vol_selectbox)+"K"+"</h3>", unsafe_allow_html=True)

st.sidebar.markdown("----------------------------------")



with st.sidebar:

    start_mon_rrp, end_mon_rrp = st.select_slider('Month-RRP',
        options=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        value=('Jan', 'Dec'))
    col1,col2=st.sidebar.columns(2)
    with  col1:
        prd_rrp = st.multiselect("Product Group-RRP",set(df['Product Sub-Group']))
    with col2:
        cust_rrp = st.multiselect("Cust Group-RRP",set(df['Customer Group']))
    col1,col2,col3,col4=st.columns(4)
    with col1:
        rrp_selectbox = st.slider('RRP',-100,100,0)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(rrp_selectbox)+"</h3>", unsafe_allow_html=True)
    with col3:
        abs_rrp_selectbox = st.slider('Abs_RRP',-100.0,100.0,0.0)
    with col4:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(abs_rrp_selectbox)+"K"+"</h3>", unsafe_allow_html=True)

st.sidebar.markdown("----------------------------------")


with st.sidebar:
    start_mon_tm, end_mon_tm = st.select_slider('Month-TM',
        options=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        value=('Jan', 'Dec'))
    col1,col2=st.sidebar.columns(2)
    with  col1:
        prd_tm = st.multiselect("Product Group-TM",set(df['Product Sub-Group']))
    with col2:
        cust_tm = st.multiselect("Cust Group-TM",set(df['Customer Group']))
    col1,col2,col3,col4=st.columns(4)
    with col1:
        tm_selectbox = st.slider('TM',-100,100,0)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(tm_selectbox)+"</h3>", unsafe_allow_html=True)
    with col3:
        abs_tm_selectbox = st.slider('Abs_TM',-100.0,100.0,0.0)
    with col4:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(abs_tm_selectbox)+"K"+"</h3>", unsafe_allow_html=True)

st.sidebar.markdown("----------------------------------")


with st.sidebar:

    start_mon_cogs, end_mon_cogs = st.select_slider('Month-COGS',
        options=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        value=('Jan', 'Dec'))
    col1,col2=st.sidebar.columns(2)
    with  col1:
        prd_cogs = st.multiselect("Product Group-COGS",set(df['Product Sub-Group']))
    with col2:
        cust_cogs = st.multiselect("Cust Group-COGS",set(df['Customer Group']))
    col1,col2,col3,col4=st.columns(4)
    with col1:
        cogs_selectbox = st.slider('COGS',-100,100,0)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(cogs_selectbox)+"</h3>", unsafe_allow_html=True)
    with col3:
        abs_cogs_selectbox = st.slider('Abs_COGS',-100.0,100.0,0.0)
    with col4:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(abs_cogs_selectbox)+"K"+"</h3>", unsafe_allow_html=True)

st.sidebar.markdown("----------------------------------")



# volume calculations..........

dfvol=df.copy()
dfrrp=df.copy()
dfvol=dfvol[['index','Customer Group','Product Sub-Group','Scenario',
       'Month','Volumes','Currency','SOP','Year','Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj']]
dfrrp=dfrrp[['index','Customer Group','Product Sub-Group','Scenario',
       'Month','Recommended retail price -RRP','Currency','SOP','Year','Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj']]



dfvol=dfvol[(dfvol["Currency"]=="LC") &  (dfvol['SOP']=="SOP1") & (dfvol['Year']==2022) & (dfvol['Scenario']=="FCT")]

dfrrp=dfrrp[(dfrrp["Currency"]=="LC") &  (dfrrp['SOP']=="SOP1")  & (dfrrp['Year']==2022) & (dfvol['Scenario']=="FCT")]

dfrrp=dfrrp.drop(columns=["index"],axis=1)
dfvol=dfvol.drop(columns=["index"],axis=1)

dfvol['index'] = range(1, len(dfvol) + 1)
dfrrp['index'] = range(1, len(dfvol) + 1)

start_val_vol= df_month['Month'].to_list().index(start_mon_vol)
end_val_vol= df_month['Month'].to_list().index(end_mon_vol)

mon_list_vol=df_month['Month'].to_list()

mon_list_vol=mon_list_vol[start_val_vol:end_val_vol+1]



dfvol['New Volume'] = dfvol[(dfvol['Customer Group'].isin(cust_vol)) & (dfvol['Product Sub-Group'].isin(prd_vol)) & (dfvol['Month'].isin(mon_list_vol))]["Volumes"].apply(lambda x: x+(x*vol_selectbox/100))

dfvol['New Volume'].fillna(dfvol['Volumes'], inplace=True)


# RRP calculations..........

start_val_rrp= df_month['Month'].to_list().index(start_mon_rrp)
end_val_rrp= df_month['Month'].to_list().index(end_mon_rrp)

mon_list_rrp=df_month['Month'].to_list()

mon_list_rrp=mon_list_rrp[start_val_rrp:end_val_rrp+1]

dfrrp['New RRP'] = dfrrp[(dfrrp['Customer Group'].isin(cust_rrp)) & (dfrrp['Product Sub-Group'].isin(prd_rrp)) & (dfrrp['Month'].isin(mon_list_rrp))]["Recommended retail price -RRP"].apply(lambda x:x+(x*rrp_selectbox/100))
dfrrp['New RRP'].fillna(dfrrp['Recommended retail price -RRP'], inplace=True)

dfvol=dfvol[["index","New Volume",'Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj','Volumes','Month']]
dfrrp=dfrrp[["index","New RRP",'Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj','Recommended retail price -RRP','Month']]


# TM calculation
dftm=df.copy()
dftm=dftm[['index','Customer Group','Product Sub-Group','Scenario',
            'Month','Volumes','Currency','SOP','Year','Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj'
]]

dftm=dftm[(dftm["Currency"]=="LC") &  (dftm['SOP']=="SOP1")  & (dftm['Year']==2022) & (dftm['Scenario']=="FCT")]

dftm['index'] = range(1, len(dftm) + 1)



start_val_tm= df_month['Month'].to_list().index(start_mon_tm)
end_val_tm= df_month['Month'].to_list().index(end_mon_tm)

mon_list_tm=df_month['Month'].to_list()

mon_list_tm=mon_list_tm[start_val_tm:end_val_tm+1]


dftm['New TM'] = dftm[(dftm['Customer Group'].isin(cust_tm)) & (dftm['Product Sub-Group'].isin(prd_tm)) & (dftm['Month'].isin(mon_list_tm))]['Trade margin Rate'].apply(lambda x:x+(x*tm_selectbox/100))
dftm['New TM'].fillna(dftm['Trade margin Rate'], inplace=True)

dftm=dftm[['index','New TM','Month','MI in NTO_Adj']]

#APFO Calculations....


dfcogs=df.copy()
dfcogs=dfcogs[['index','Customer Group','Product Sub-Group','Scenario',
            'Month','Volumes','Currency','SOP','Year','Consumer discounting - CD','Distributor Margin','Trade margin Rate','MI in NTO', 'MI in NTO_Adj','OIE FX Admin OVH','MI',"COGS"
]]

dfcogs=dfcogs[(dfcogs["Currency"]=="LC") &  (dfcogs['SOP']=="SOP1")  & (dfcogs['Year']==2022) & (dfcogs['Scenario']=="FCT")]

dfcogs['index'] = range(1, len(dfcogs) + 1)


start_val_cogs= df_month['Month'].to_list().index(start_mon_cogs)
end_val_cogs= df_month['Month'].to_list().index(end_mon_cogs)

mon_list_cogs=df_month['Month'].to_list()

mon_list_cogs=mon_list_cogs[start_val_cogs:end_val_cogs+1]

print("COGS-mon--->",mon_list_cogs)
print("product---->",prd_cogs)
print("cust----->",cust_cogs)
print("volume",cogs_selectbox)

dfcogs['New COGS'] = dfcogs[(dfcogs['Customer Group'].isin(cust_cogs)) & (dfcogs['Product Sub-Group'].isin(prd_cogs)) & (dfcogs['Month'].isin(mon_list_cogs))]["COGS"].apply(lambda x:x+(x*cogs_selectbox/100))
dfcogs['New COGS'].fillna(dfcogs['COGS'], inplace=True)

dfcogs=dfcogs[['COGS','New COGS','OIE FX Admin OVH','MI','index']]



#------------------------------------------------------------------------------------------------------

df_merged = dfvol.set_index('index').combine_first(dfrrp.set_index('index')).reset_index()
df_merged = df_merged.set_index('index').combine_first(dftm.set_index('index')).reset_index()
df_merged = df_merged.set_index('index').combine_first(dfcogs.set_index('index')).reset_index()


# NEW NPTO

df_merged["CPTO-NEW"]=df_merged["New Volume"] * df_merged["New RRP"]


df_merged["VAT-NEW"]=df_merged["CPTO-NEW"] * (0.2/1.2) * -1 

df_merged["NA-NEW"]=df_merged["CPTO-NEW"] + df_merged["Consumer discounting - CD"] + df_merged["VAT-NEW"]

df_merged["FM-NEW"]=df_merged["NA-NEW"] * df_merged["New TM"] * -1

df_merged["NTO-PRE-NEW"]= df_merged["NA-NEW"] + df_merged["FM-NEW"] + df_merged["Distributor Margin"]

df_merged["NTO-POST-NEW"]= df_merged["NTO-PRE-NEW"] + df_merged['MI in NTO_Adj'] + df_merged['MI in NTO'] 

# OLD NPTO

df_merged["CPTO-OLD"]=df_merged["Volumes"] * df_merged["Recommended retail price -RRP"]


df_merged["VAT-OLD"]=df_merged["CPTO-OLD"] * (0.2/1.2) * -1 

df_merged["NA-OLD"]=df_merged["CPTO-OLD"] + df_merged["Consumer discounting - CD"] + df_merged["VAT-OLD"]

df_merged["FM-OLD"]=df_merged["NA-OLD"] * df_merged["Trade margin Rate"] * -1

df_merged["NTO-PRE-OLD"]= df_merged["NA-OLD"] + df_merged["FM-OLD"] + df_merged["Distributor Margin"]

df_merged["NTO-POST-OLD"]= df_merged["NTO-PRE-OLD"] + df_merged['MI in NTO_Adj'] + df_merged['MI in NTO'] 


# OLD APFO

df_merged['GM']=df_merged['NTO-POST-OLD'] + df_merged['COGS'] 

df_merged['APFO-OLD']=df_merged['GM']+df_merged['MI']+df_merged['OIE FX Admin OVH']

# NEW APFO

df_merged['NEW-GM']=df_merged['NTO-POST-NEW'] + df_merged['New COGS'] 

df_merged['APFO-NEW']=df_merged['NEW-GM']+df_merged['MI']+df_merged['OIE FX Admin OVH']



df_grouped=df_merged.groupby(['Month'],as_index=False).sum()

df_grouped=df_grouped[["Month","NTO-POST-OLD","NTO-POST-NEW","APFO-OLD","APFO-NEW"]]


df_month["Index"]= range(1, len(df_month) + 1)

df_grouped=df_grouped.merge(df_month, on='Month', how='inner')

df_grouped=df_grouped.sort_values(by="Index")

# st.dataframe(df_grouped)


#--------------------------------------------------------------------------------------------------------------------------

fig = go.Figure(data=[
    go.Bar(name='NTO old', x=df_grouped["Month"].to_list(), y=[round(item, 3) for item in df_grouped["NTO-POST-OLD"].to_list()]),
    go.Bar(name='NTO new', x=df_grouped["Month"].to_list(), y=[round(item, 3) for item in df_grouped["NTO-POST-NEW"].to_list()]),
])

# fig.update_layout(xaxis=dict(showgrid=False),
#             yaxis=dict(showgrid=False),
            
# )

fig.update_traces(texttemplate="%{y}")
fig.update_layout(plot_bgcolor="#FFFFFF")
st.plotly_chart(fig, use_container_width=True)

#-------------------------------------------------------------------------------------------------------------------------------

df_line=df_grouped.copy()
df_line=df_line[["APFO-OLD","APFO-NEW"]]
df_line=df_line.rename_axis('Index').reset_index().melt('Index').dropna()

df_line=df_line.sort_values(by="Index")
df_line=df_line.merge(df_month, on='Index', how='inner')
df_line=df_line.round(2)
fig = px.line(df_line, x="Month", y="value", color='variable',text="value").update_layout(
  xaxis_title="", yaxis_title=""
)
fig.update_layout(plot_bgcolor="#FFFFFF")
st.plotly_chart(fig, use_container_width=True)
# --------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------

# with col1:

#     st.write("NTO-POST-OLD")
#     st.write(str(df_merged["NTO-POST-OLD"].sum()))

# with col2:
#     st.write("NTO-POST-NEW")
#     st.write(str(df_merged["NTO-POST-NEW"].sum()))

# with col1:

#     st.write("APFO-OLD")
#     st.write(str(df_merged["APFO-OLD"].sum()))

# with col2:
#     st.write("APFO-NEW")
#     st.write(str(df_merged["APFO-NEW"].sum()))


#-----------------------------------------------------------------------------------------------------













# Index(['Unnamed: 0', 'index', 'Plant', 'Scenario', 'Forcast_Year',
#        'Forcast_Month', 'Year', 'Month', 'Semi', 'Quarter', 'Currency',
#        'Channel', 'Sub-Channel', 'Customer Group', 'CF Code',
#        'Product Segment', 'Product Group', 'Product Sub-Group',
#        'Product Brand', 'Volumes', 'Recommended retail price -RRP',
#        'Trade margin Rate', 'Consumer price turnover - CPTO',
#        'Consumer discounting - CD', 'VAT', 'Indirect VAT', 'External VAT',
#        'Net Available', 'Front Margin', 'Back Margin', 'Distributor Margin',
#        'NTO Pre-IFRS', 'MI in NTO', 'MI in NTO_Adj', 'NTO post IFRS', 'Excise',
#        'COGS-Calc', 'COGS-Adj', 'COGS', 'GM', 'Trade Margin', 'MI BE',
#        'MI NBE', 'MI', 'Market Contribution', 'OIE FX Admin OVH', 'APFO',
#        'CD % CPTO', 'MI % NTO', 'TM % NA', 'OM %', 'SOP', 'FY'],
#       dtype='object')

