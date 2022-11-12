
# coding: utf-8

# In[16]:


import chardet
with open("/home/tier1marketspace/ncua/csv/AcctDesc2018-12.csv", 'rb') as file:
    print(chardet.detect(file.read()))


# In[9]:


period = { 
"2018-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-12.zip",

}

csvFileName = ["AcctDesc",
"Acct-DescGrants",
"Acct-DescTradeNames",
"Credit Union Branch Information",
"FOICU",
"FOICUDES",
"FS220",
"FS220A",
"FS220B",
"FS220C",
"FS220D",
"FS220G",
"FS220H",
"FS220I",
"FS220J",
"FS220K",
"FS220L",
"FS220M",
"FS220N",
"FS220P",
"FS220Q",
"FS220R",
]

txtFileName= [
"AcctDesc.txt",
"Acct-DescGrants.txt",
"Acct-DescTradeNames.txt",
"Credit Union Branch Information.txt",
"FOICU.txt",
"FOICUDES.txt",
"FS220.txt",
"FS220A.txt",
"FS220B.txt",
"FS220C.txt",
"FS220D.txt",
"FS220G.txt",
"FS220H.txt",
"FS220I.txt",
"FS220J.txt",
"FS220K.txt",
"FS220L.txt",
"FS220M.txt",
"FS220N.txt",
"FS220P.txt",
"FS220Q.txt",
"FS220R.txt"
]


# In[17]:


import requests, zipfile, io
import pandas as pd
for x in period:
    try:
        zip_file_url = period[x]
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("/home/tier1marketspace/ncua/txt/")
        y=0
    except:
        pass
    for a in txtFileName:
        try:
            read_file = pd.read_csv (f'/home/tier1marketspace/ncua/txt/{a}', encoding = 'ascii' )
            read_file.to_csv (f'/home/tier1marketspace/ncua/csv/{csvFileName[y]+x+".csv"}', index=None )
            print(x)
            y=y+1
            with open as
        except:
            pass


# In[13]:





# In[25]:


import requests, zipfile, io
import pandas as pd
for x in period:
    zip_file_url = period[x]
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("/home/tier1marketspace/ncua/txt/")
    y=0

    for a in txtFileName:
        with open(f'/home/tier1marketspace/ncua/txt/{a}', 'rb') as file:
            print(chardet.detect(file.read()))
        read_file = pd.read_csv (f'/home/tier1marketspace/ncua/txt/{a}', encoding = 'Windows-1252' )
        read_file.to_csv (f'/home/tier1marketspace/ncua/csv/{csvFileName[y]+x+".csv"}', index=None )
        print({a})
        y=y+1


# In[24]:


#fs220L2018-12
#fs220L2019-9-6-3
#fs220M2018-3-6-12
#fs220N2022-6 OK
#fs220N2020-9-6-3


# In[ ]:


period = { 
    "2022-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-09.zip",
    "2022-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-06.zip",
    "2022-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-03.zip",
    "2021-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-12.zip",
    "2021-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-09.zip",
    "2021-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-06.zip",
    "2021-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-03.zip",
    "2020-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-12.zip",
    "2020-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-09.zip",
    "2020-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-06.zip",
    "2020-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-03.zip",
    "2019-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-12.zip",
    "2019-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-09.zip",
    "2019-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-06.zip",
    "2019-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-03.zip",
    "2018-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-12.zip",
    "2018-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-09.zip",
    "2018-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-06.zip",
    "2018-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-03.zip",
    "2017-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-12.zip",
    "2017-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-09.zip",
    "2017-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-06.zip",
    "2017-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-03.zip",
    "2016-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-12.zip",
    "2016-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-09.zip",
    "2016-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-06.zip",
    "2016-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-03.zip",
          }

