<h1>Report Generator</h1>

- **Application**: folder with interface and configuration elements
    -> interface.py: contains the interface configuration.
- **Data**: folder to enter the elements to create the report. **Are mandatory**.
    >- 2g, 3g, 4g and 5g Querys 
    >- Babysitting excel 
- **Graph**: folder with the graphics created by the program for the report
- **Domain**: folder with program functions
    - checkNOK.py: check the NOK KPI that gets from the Babysitting excel. Returns a list with the cell Name, KPI NOK and if it is OK or NO OK 
        >       [[Cell Name, KPI name, OK?],...]
    - reportGenerator.py: call to the differents functions to create the report (checkNOK, graph.create, word.create)
    - modules: folder with auxiliary functions.
         >- getNOKreport.py: gets the NOK KPI from the Babysitting
         >- getQueryData.py: obtains the data to check the KPIs
         >- analyzeKPI.py: analyzes the NOK KPIs with the data obtained from Querys. Returns a list with the cell, KPI anda if it is OK o not:
         >>     [Cell Name, KPI name, OK?]
         >- graph.py: creates the graph with the data obtained from Querys
         >- word.py: creates the word.docx with the KPI, the cell and the data obtained from Querys

- **App.py**: the executable -> cmd/ python App.py to start the programme (if there is an exe, this is not necessary)
- Babysitting_XXX.docx: the created report


<h2>Version 0.1</h2>

- **NºSectores**: number of sectors the site has

- **NºBandas**: number of bands on the site 

- **Report type**: 

>- Consolidation report: 2G/3G/4G 
>- Expansion report: NOT in this version (coming soon)
