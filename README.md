# M0BusinessDataAnalysis_SanchezItzel
## BUSINESS UNDERSTANDING
- We are a non- profit educational institute figuring out the way in which to help students pursue high education abroad. We are planning to help with the awareness of international schooling by bringing up the awareness of student costs for these international programs. Through our student surveys, the international programs throughout the cities of china and russia were more sought after,yet due to the school limitation on providing a direct link to these programs . We are tasked with figuring out which cities between china and russia offers the least educational expenses , in order to raise awareness of the cost for education abroad.

    
## DATA LIFECYCLE

 - Which cities between China an Russia offers the most affordable educational cost ?

### Collecting the data related to international cost for education 

- This data set is from [Kaggle Datasets](https://www.kaggle.com/datasets/adilshamim8/cost-of-international-education)

<img width="810" alt="CVS2" src="https://github.com/user-attachments/assets/d9ad1f14-58aa-4b02-b935-2fc923a1ad5a"/>

   The image demostrates a variety of different topics ranging from
   1. A variety of countries.
   2. A variety of cities.
   3. Variables consisting : Tuition, Visa Fees, Rent , Exchange Rate , Duration of years ,University names

### Filtering Data through Excel.

We start with navigating through the cvs file that we are using into a excel workbook.

Our Question is asking to specifically filter out the countries AND cities of China and Russia . ( Nothing more , Nothing less)

 - Creating a pivot table that specfically filters out the Countries , through advanced filter.
 - Our pivot table has to only contain the cities within these two countries.
 - Our pivot table has to containing information only related to the educational cost for each of these cities.

<img width="460" alt="Excel Out" src="https://github.com/user-attachments/assets/e64fcedc-bd18-4377-a17d-cdd8d0baf6b7" />

* This is an example of the china pivot table *
 - Sectioning out the vaules that don't hold much importance to solving the business question , different Cities , Universities , living cost , level , etc.
 - Using the Vaule Functions of excel to find the SUM of total cost for educational expenses.


 ### Filtering Data through PYTHON!

 Another way to easily acesses data for others to view would be through python.

 In order to view this data in a clean an concise way , we have to first import our cvs file. (Panda Library) 

<img width="589" alt="Beginning" src="https://github.com/user-attachments/assets/b3bf714c-7823-47c8-8f9c-52371cc7b95a" />

we recieved the output of :

<img width="694" alt="Beginning 2" src="https://github.com/user-attachments/assets/b65fc732-8528-4d3d-9422-296be7f58332" />

We then clean our data based on the colums we would like to keep , the rows that would stay, in order to help push 
the outputs our only viewing the total cost per city within their countries.


 

 




   

 



