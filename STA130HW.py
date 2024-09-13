#!/usr/bin/env python
# coding: utf-8

# # STA130 Week 01 Homework 
# 
# Please see the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) for the list of topics covered in this homework assignment, and a list of topics that might appear during ChatBot conversations which are "out of scope" for the purposes of this homework assignment (and hence can be safely ignored if encountered)
# 

# <details class="details-example"><summary style="color:blue"><u>Introduction</u></summary>
# 
# ### Introduction
#     
# A reasonable characterization of STA130 Homework is that it simply defines a weekly reading comprehension assignment. 
# Indeed, STA130 Homework essentially boils down to completing various understanding confirmation exercises oriented around coding and writing tasks.
# However, rather than reading a textbook, STA130 Homework is based on ChatBots so students can interactively follow up to clarify questions or confusion that they may still have regarding learning objective assignments.
# 
# > Communication is a fundamental skill underlying statistics and data science, so STA130 Homework based on ChatBots helps practice effective two-way communication as part of a "realistic" dialogue activity supporting underlying conceptual understanding building. 
# 
# It will likely become increasingly tempting to rely on ChatBots to "do the work for you". But when you find yourself frustrated with a ChatBots inability to give you the results you're looking for, this is a "hint" that you've become overreliant on the ChatBots. Your objective should not be to have ChatBots "do the work for you", but to use ChatBots to help you build your understanding so you can efficiently leverage ChatBots (and other resources) to help you work more efficiently.<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Instructions</u></summary>
# 
# ### Instructions
#     
# 1. Code and write all your answers (for both the "Prelecture" and "Postlecture" HW) in a python notebook (in code and markdown cells) 
#     
# > It is *suggested but not mandatory* that you complete the "Prelecture" HW prior to the Monday LEC since (a) all HW is due at the same time; but, (b) completing some of the HW early will mean better readiness for LEC and less of a "procrastentation cruch" towards the end of the week...
#     
# 2. Paste summaries of your ChatBot sessions (including link(s) to chat log histories if you're using ChatGPT) within your notebook
#     
# > Create summaries of your ChatBot sessions by using concluding prompts such as "Please provide a summary of our exchanges here so I can submit them as a record of our interactions as part of a homework assignment" or, "Please provide me with the final working verson of the code that we created together"
#     
# 3. Save your python jupyter notebook in your own account and "repo" on [github.com](github.com) and submit a link to that notebook though Quercus for assignment marking<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Prompt Engineering?</u></summary>
# 
# ### Prompt Engineering?    
#     
# The questions (as copy-pasted prompts) are designed to initialize appropriate ChatBot conversations which can be explored in the manner of an interactive and dynamic textbook; but, it is nonetheless **strongly recommendated** that your rephrase the questions in a way that you find natural to ensure a clear understanding of the question. Given sensible prompts the represent a question well, the two primary challenges observed to arise from ChatBots are 
# 
# 1. conversations going beyond the intended scope of the material addressed by the question; and, 
# 2. unrecoverable confusion as a result of sequential layers logial inquiry that cannot be resolved. 
# 
# In the case of the former (1), adding constraints specifying the limits of considerations of interest tends to be helpful; whereas, the latter (2) is often the result of initial prompting that leads to poor developments in navigating the material, which are likely just best resolve by a "hard reset" with a new initial approach to prompting.  Indeed, this is exactly the behavior [hardcoded into copilot](https://answers.microsoft.com/en-us/bing/forum/all/is-this-even-normal/0b6dcab3-7d6c-4373-8efe-d74158af3c00)...
# 
# </details>

# 
# ### Marking Rubric (which may award partial credit) 
# 
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.2 points]: Reasonable well-written general definitions for Question "2.2"
# - [0.3 points]: Demonstrated understanding regarding Question "4"
# <!-- - [0.2 points]: A sensible justification for the choice in Question "7.4" -->
# - [0.4 points]: Requested assessment of ChatBot versus google performance in Question "8.3"
# 

# ## "Pre-lecture" HW [*completion prior to next LEC is suggested but not mandatory*]

# #### 1. Pick one of the datasets from the ChatBot session(s) of the **TUT demo** (or from your own ChatBot session if you wish) and use the code produced through the ChatBot interactions to import the data and confirm that the dataset has missing values<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > If your TA has not shared a relevant ChatBot session from their **TUT demo** through a piazza post and a Quercus announcement, the **TUT notebook** has links to example ChatBot sessions that you can use; or, ...
# > 
# > ```python
# > # feel free to just use the following if you prefer...
# > import pandas as pd
# > url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
# > df = pd.read_csv(url)
# > df.isna().sum()
# > ```
#     
# </details>

# In[2]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# #### 2. Start a new ChatBot session with an initial prompt introducing the dataset you're using and request help to determine how many columns and rows of data a `pandas` DataFrame has, and then
# 
# 1. use code provided in your ChatBot session to print out the number of rows and columns of the dataset; and,  
# 2. write your own general definitions of the meaning of "observations" and "variables" based on asking the ChatBot to explain these terms in the context of your dataset<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > A good initial prompt to start would be be something like
# > - "I've downloaded a dataset about characters from animal crossings (from https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv), and I'd like to know what columns of information I have and how much data I have"
# > 
# > You can further reduce the scope of your inquiry with if needed with something like
# > - "I've already downloaded the data and want to understand the size (or dimensions) of the dataset to start with"
# > 
# > *Some ChatBots can upload your data and do this for you; but, extended usage of this feature [likely requires a paid subscription](https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk1/GPT/SLS/00006_gpt3p5_LoadDataPaywall.md); and, anyway, you need to run the code yourself rather than having a ChatBot do that for you; and, for STA130 we don't want a ChatBot to just do the analysis for us; rather, we instead want ChatBots to help us understand the steps we need to take to analyze the data; so,* **you DO NOT need to purchase an upgraded version of any ChatBots**
# > - Free-tier level ChatBots like [GPT4o-mini](https://chat.openai.com/) or [Copilot](https://copilot.microsoft.com/) (which is partially based on [ChatGPT4.0](https://chat.openai.com/), and which you have access to through your UofT account) are sufficiently sophisticated and perfectly appropriate for the STA130 course
#     
# </details>

# In[3]:


import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv'
df = pd.read_csv(url)

# Get the number of rows and columns
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")


#  "Observation" refers to individuals in the whole set. In this context, each row represents a villager, so the number of rows shows the number of villagers (observations) in the dataset. As for "vairables", they are different features in each villagers(observation). Number of columns show the number of features taken of the villagers.

# #### 3. Ask the ChatBot how you can provide simple summaries of the columns in the dataset and use the suggested code to provide these summaries for your dataset<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > Use your ChatBot session to help you create working examples of using  `df.describe()` and `df['column'].value_counts()` for your dataset (although note that the `.value_counts()` method is not really meant to be used for numeric variables, so if you dataset has only numeric variables, `.value_counts()` might not be particularly informative...)
# >
# > #### ChatBot Response Scope 
# >     
# > If prompts are not sufficiently focused you will likely get overly broad responses from the ChatBot, but you can always respond with subsequent refinement requests to appropriately limit the scope of the ChatBot responses to focus on addressing your actual content targets; so, 
# > - an initially very general inquiry like, "I need help analyzing my data" will likely result in a ChatBot response suggesting a wide variety of approaches and techniques for summarizing your dataset; but, re-prompting the ChatBot with something like, "What's the simplest form of summarization of this dataset that I could do and how do I do it in Python?" or suggesting guidance using the specific summarization methods requested above will helpfully re-orient the ChatBot to your specific interests and needs
# > 
# > #### Jupyter Notebook Hints
# > 
# > Jupyter notebook printouts usaully don't show all of the data (when there's too much to show, like if `df.describe()` includes results for many columns), but the printouts just show enough of the data to give an idea of what the results are which is all we're looking for at the moment
# > 
# > - Consider dividing the code that ChatBot provides you into different jupyter notebook cells so that each cell concludes with a key printed result; the last line of code in a jupyter notebook cell will automatically print out in a formatted manner, so replacing something like `print(df.head())` with `df.head()` as the last line of a cell provides a sensible way to organize your code
# > - The printout suggestions above are demonstrated in `STA130F24_CourseProject.ipynb` if looking at an example would be helpful to understand what they're getting at...
#     
# </details>

# There are some ways for me to provide simple summaries of the data set. For example, display basic information, describe numeric columns,describe categorical columns, find unique value, summarize missing value.

# In[1]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Basic information
print("Basic Information:")
print(df.info())
print()

# Summary statistics for numerical columns
print("Summary Statistics for Numerical Columns:")
print(df.describe())
print()

# Summary statistics for categorical columns
print("Summary Statistics for Categorical Columns:")
print(df.describe(include='object'))
print()

# Unique values for each column
print("Unique Values for Each Column:")
for column in df.columns:
    print(f"Column: {column}")
    print(df[column].value_counts(dropna=False))
    print()

# Missing values
print("Missing Values in Each Column:")
print(df.isna().sum())


# #### 4. If the dataset you're using has (a) non-numeric variables and (b) missing values in numeric variables, explain (perhaps using help from a ChatBot if needed) the discrepancies between size of the dataset given by `df.shape` and what is reported by `df.describe()` with respect to (a) the number of columns it analyzes and (b) the values it reports in the "count" column<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > If the dataset you're using does not have (a) non-numeric variables and (b) missing values in numeric variables (e.g., the `"villagers.csv"` example above has only a single numeric variable `row_n` which has no missing values), instead download and use the [https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)" data to answer this question  
# >
# > In (a) above, the "columns it analyzes" refers to the columns of the output of `df.describe()` which will only include "numeric" columns by default, but you can can see the names of all the columns in a dataset using `df.columns`; and, make sure `df.shape` is refering to the dataset you think it is... if you've loaded a different dataset it might not have been called `df`(!)
# >
# > **If you get any errors (for example related to column names), copy and paste them as a response to the ChatBot, and see if it can help you resove them by adding the suggested adjustments to your code and then reruning all your code to see if the changes have fixed the problem (and repeat this process as needed until the problems have been resolved).**
#     
# </details>

# Since the original dataset doesn't meet the terms. So I will use the Titanic dataset instead for this question. 

# (a) For number of columns analyzed. In the dataset, 'df.shape' represents the number of column and rows of the dataset, which is the whole size. In this case, it's 887 rows and 15 columns.In contrast, 'df.describe()' only represents the numeric columns (such as counts,mean, max,min) but not for the non-numerical columns.Therefore, df.describe() will show fewer columns than the total number of columns. For instance, the dataset has 15 columns but only 5 of them are numeric, df.describe() will only display those 5 numeric columns.

# (b) For the values it reports in the "count" column. The df.shape does not directly tell information about missing values; it only tells the total number of entries (rows and columns). In contrast, the "count" column in the output of df.describe() reflects the number of non-missing values in each numeric column. If a column has missing values, the count will be less than the total number of rows.In this data set numeric column originally has 887 rows but has 100 missing values, the "count" for that column will be 787.

# #### 5. Use your ChatBot session to help understand the difference between the following and then provide your own paraphrasing summarization of that difference
# 
# - an "attribute", such as `df.shape` which does not end with `()`
# - and a "method", such as `df.describe()` which does end with `()` 
#    
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > The fact that a "method" such as `df.describe()` ends with `()` suggests that "methods" are essentially something that we would call a "function" in programming language terminology; but, without getting too technical or "in the weeds", it might also be worth considering that we could also contrast what the difference is between a "function" in a programming language versus a "function" in mathematics...  
#     
# </details><br><br>
# 
# ***Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)!***<br><br>

# An attribute is a variable of an object. It shows one specific kind of data or info about the object. We don't need parentheses for the attributes to an object.df.shape is an attribute of a DataFrame object because it tells the number of rows and columns.Attributes are used to store and retrie information about the object, but they can't perform actions or operations. 
# 
# A method is a function of an object. They show the actions or operations that the object can perform.We need parentheses to call a method. In this case,df.describe() is a method. It computes and returns descriptive statistics of the numeric columns.

# Summary:
# Checking Missing Values: You provided code to load a dataset and check for missing values. The code reads the dataset from a URL and uses df.isna().sum() to count missing values in each column.
# 
# Summarizing the Dataset:
# 
# Basic Information: Use df.info() to get an overview of data types and non-null counts.
# Numerical Statistics: Use df.describe() to get summary statistics for numerical columns.
# Categorical Statistics: Use df.describe(include='object') to summarize categorical data.
# Unique Values: Use df[column].value_counts(dropna=False) to see unique values and their frequencies for each column.
# Missing Values: Use df.isna().sum() to check for missing data.
# This approach helps in understanding the dataset's structure, data distribution, and missing values, aiding in further analysis.
# 
# Dataset Discrepancies:
# 
# df.shape vs. df.describe():
# df.shape provides the total number of rows and columns in the DataFrame.
# df.describe() summarizes only numeric columns, so it shows fewer columns and reflects non-missing counts for numeric data.
# Attributes vs. Methods:
# 
# Attributes:
# Variables associated with an object that hold data (e.g., df.shape).
# Accessed directly without parentheses.
# Methods:
# Functions associated with an object that perform actions or computations (e.g., df.describe()).
# Accessed with parentheses.
# This distinction helps in understanding how to interact with pandas DataFrames and interpret their characteristics and behavior.
# 
# 
# 
# 
# 

# <details class="details-example"><summary style="color:blue"><u>Continue now...?</u></summary>
# 
# ### Prelecture VS Postlecture HW
#     
# Feel free to work on the "Postlecture" HW below if you're making good progress and want to continue: in this case this is particularly reasonable as questions "6" and "7" below directly follow up and extend the "Prelecture" HW questions
# 
# *The benefits of continue would are that (a) it might be fun to try to tackle the challenge of working through some problems without additional preparation or guidance; and (b) this is a very valable skill to be comfortable with; and (c) it will let you build experience interacting with ChatBots (and beginning to understand their strengths and limitations in this regard)... it's good to have sense of when using a ChatBot is the best way to figure something out, or if another approach (such as course provided resources or a plain old websearch for the right resourse) would be more effective*
#     
# </details>    
# 

# ## "Post-lecture" HW [*submission along with "Pre-lecture" HW is due prior to next TUT*]

# #### 6. The `df.describe()` method provides the 'count', 'mean', 'std', 'min', '25%', '50%', '75%', and 'max' summary statistics for each variable it analyzes. Give the definitions (perhaps using help from the ChatBot if needed) of each of these summary statistics<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > The answers here actually make it obvious why these can only be calculated for numeric variables in a dataset, which should help explain the answer to "4(a)" and "4(b)" above
# >   
# > Also notice that when `df.describe()` is used missing values are not explicitly removed, but `df.describe()`  provides answers anyway. Is it clear what `df.describe()` does with the data in each columns it analyzes if there is missing data in the column in question? 
# >
# > The next questions addresses removing rows or columns from a dataset in order to explicitly remove the presense of any missingness in the dataset (assuming we're not going to fill in any missing data values using any missing data imputation methods, which are beyond the scope of STA130); so, the behavior of `df.describe()` hints that explicitly removing missing may not always be necessary; but, the concern, though, is that not all methods may be able to handle missing data the way `df.describe()` does...
#     
# </details>

# Count: This shows the total number of entries in each column which aren't missing. It tells how many values are present in the dataset for a certain variable.
# 
# Mean: The mean(average) is calculated by adding up all the values in the column and dividing by the number of entries. It provides an average value around which the data tends to cluster.
# 
# Standard Deviation (std): This statistic measures how much the values in the column deviate from the mean. A higher standard deviation indicates that the values are spread out more widely, while a lower standard deviation suggests that they are closer to the mean.
# 
# Min: The minimum value is the smallest number in the column. 
# 
# 25% (First Quartile): Can be written as Q1, this value is the point below which 25% of the data falls. It provides data about the lower portion of the distribution.
# 
# 50% (Median): The median is the middle value of the dataset. It divides the dataset into two equal halves, one higher than this median and the other lower. 
# 
# 75% (Third Quartile): Can be written as Q3, this value is the point below which 75% of the data falls. It shows data of the upper range of the distribution.
# 
# Max: The maximum value is the largest number in the column. 

# #### 7. Missing data can be considered "across rows" or "down columns".  Consider how `df.dropna()` or `del df['col']` should be applied to most efficiently use the available non-missing data in your dataset and briefly answer the following questions in your own words
# 
# 1. Provide an example of a "use case" in which using `df.dropna()` might be peferred over using `del df['col']`<br><br>
#     
# 2. Provide an example of "the opposite use case" in which using `del df['col']` might be preferred over using `df.dropna()` <br><br>
#     
# 3. Discuss why applying `del df['col']` before `df.dropna()` when both are used together could be important<br><br>
#     
# 4. Remove all missing data from one of the datasets you're considering using some combination of `del df['col']` and/or `df.dropna()` and give a justification for your approach, including a "before and after" report of the results of your approach for your dataset.<br><br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > Start a new ChatBot session **[but remember to first ask your ChatBot for summaries of your current session and perhaps coding results (so you can supply these in the homework as requested)]**, since your last ChatBot session has likely gotten quite long and has covered a lot of material at this point 
# > - It can sometimes be helpful to reset ChatBot sessions to refocus them on the topics of inquiry without too much backlog history that might unintentionally bias things in certain directions and, of course, you can always re-introduce material from earlier conversations as it's relevant, such as for answering "D" based on reintroducing and updating code you made in a previous ChatBot session.  
# > 
# > #### ChatBot Scope Guidance
# > 
# > - This question is not interested in the general benefits of imputing missing data, or the general benefits of using `df.dropna()` and/or `del df['col']` to remove missing data, just how to most efficiently remove missing data if a user chooses to do so
# > 
# > - More sophisticated analyses for "filling in" rather than removing missing data (as considered here) are possible (based on making assumptions about missing data and using specific imputation methods or models) but these are "beyond the scope" of this homework assignment so this topics can be safely ignored for now
# > 
# > #### ChatBot Code Troubleshooting
# > 
# > A key issue to be aware of when asking ChatBots for help with something is that they are not running and checking code for correctess, and they often intertwine written instructions with code instructions; so, BEFORE YOU RUN ANY CODE provided by a ChatBot, you should check the following
# > 
# > 1. If this code changes an object or data, are you sure you want to run this code?
# > 2. Can you easily "undo" the results of running code (e.g., from a copy `df_saved=df.copy()` or reloading the data) if running the code doesn't do what you want?
# > 3. Is the state of the data what is expected by the code? Or have the objects been updated and changed so they're no longer what the code expects them to be? 
# > 
# > #### If you get any `Python` errors, copy and paste them into the ChatBot prompt and see if it can help you resove them; but, keep in mind the final point above becasue the ChatBot might not be aware of the state of your objects relative to the code it's producing...
# 
# </details><br>

# (1) For example,if there's a dataset in which row represent observation(customers), and column represent different feature(attributes of them such as age, income..). Some rows have missing values in different columns.if it's necessary to have all the complete data(maybe when the people need to be strictly selected to a jonb), we can use df.dropna() to remove any row with at least one missing value. This helps in maintaining a consistent dataset for analysis.
# (2) For example, if there's a dataset in which one specific column has missing data for many rows, but the column itself is not necessary for analysis(for instance, the attribute 'age' when hiring a cook), we can use del df['col'] to delete this column because it's not crutial and keeping it would result in serious error for the final work.
# (3)If I apply del df['col'] before df.dropna(), I can eliminate a big(maybe) proportion of the number of rows that need to be processed by df.dropna(). Removing columns with a high proportion of missing can make execution of df.dropna() more efficient. It also simplifies the dataset.
# (4)I use the dataset about villagers in the first problem.First I find out where the missing values are: id-1 missing value, song-11 missing values.Other columns have no missing values.Then I removed columns with high missing values which is the "song" column.Then I use df.dropna() to remove any rows that still have missing values. In this case, only the id column has a missing value, so I droppeed rows with missing values in the id column.
# 

# In[12]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Check the number of missing values per column before cleaning
missing_values = df.isna().sum()
print("Missing values per column before cleaning:\n", missing_values)

# Remove columns with high missing values
# Assuming 'song' is not essential and has a significant number of missing values
if 'song' in df.columns:
    del df['song']

# Drop rows with any remaining missing values
df_cleaned = df.dropna()

# Print the shape of the dataset before and after cleaning
print(f"Original dataset shape: {df.shape}")
print(f"Cleaned dataset shape: {df_cleaned.shape}")

# Check for missing values after cleaning
print("Missing values per column after cleaning:\n", df_cleaned.isna().sum())


# Justification
# Column Removal: The song column was removed because it had 11 missing values, which is a significant proportion of missing data relative to the overall dataset. Removing this column simplifies the dataset and avoids issues related to missing values in this column.
# 
# Row Removal: After removing the column, df.dropna() ensures that any remaining rows with missing values (such as the row with a missing id) are removed, resulting in a dataset where all remaining rows are complete.

# In[ ]:





# 

# 
# 
# 
# 
#     
# #### 8. Give brief explanations in your own words for any requested answers to the questions below
# 
# > This problem will guide you through exploring how to use a ChatBot to troubleshoot code using the "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" data set 
# > 
# > To initialially constrain the scope of the reponses from your ChatBot, start a new ChatBot session with the following slight variation on the initial prompting approach from "2" above
# > - "I am going to do some initial simple summary analyses on the titanic data set I've downloaded (https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv) which has some missing values, and I'd like to get your help understanding the code I'm using and the analysis it's performing"
#         
# 1. Use your ChatBot session to understand what `df.groupby("col1")["col2"].describe()` does and then demonstrate and explain this using a different example from the "titanic" data set other than what the ChatBot automatically provide for you
#     
# > If needed, you can help guide the ChatBot by showing it the code you've used to download the data **AND provide it with the names of the columns** using either a summary of the data with `df.describe()` or just `df.columns` as demonstrated [here](../CHATLOG/COP/00017_copilot_groupby.md)
#     
# 2. Assuming you've not yet removed missing values in the manner of question "7" above, `df.describe()` would have different values in the `count` value for different data columns depending on the missingness present in the original data.  Why do these capture something fundamentally different from the values in the `count` that result from doing something like `df.groupby("col1")["col2"].describe()`?
# 
# > Questions "4" and "6" above address how missing values are handled by `df.describe()` (which is reflected in the `count` output of this method); but, `count` in conjunction with `group_by` has another primary function that's more important than addressing missing values (although missing data could still play a role here).
# 
# 3. Intentionally introduce the following errors into your code and report your opinion as to whether it's easier to (a) work in a ChatBot session to fix the errors, or (b) use google to search for and fix errors: first share the errors you get in the ChatBot session and see if you can work with ChatBot to troubleshoot and fix the coding errors, and then see if you think a google search for the error provides the necessary toubleshooting help more quickly than ChatGPT<br><br>
#     
#     1. Forget to include `import pandas as pd` in your code 
#        <br> 
#        Use Kernel->Restart from the notebook menu to restart the jupyter notebook session unload imported libraries and start over so you can create this error
#        <br><br>
#        When python has an error, it sometimes provides a lot of "stack trace" output, but that's not usually very important for troubleshooting. For this problem for example, all you need to share with ChatGPT or search on google is `"NameError: name 'pd' is not defined"`<br><br>
# 
#     2. Mistype "titanic.csv" as "titanics.csv"
#        <br> 
#        If ChatBot troubleshooting is based on downloading the file, just replace the whole url with "titanics.csv" and try to troubleshoot the subsequent `FileNotFoundError: [Errno 2] No such file or directory: 'titanics.csv'` (assuming the file is indeed not present)
#        <br><br>
#        Explore introducing typos into a couple other parts of the url and note the slightly different errors this produces<br><br>
#       
#     3. Try to use a dataframe before it's been assigned into the variable
#        <br> 
#        You can simulate this by just misnaming the variable. For example, if you should write `df.groupby("col1")["col2"].describe()` based on how you loaded the data, then instead write `DF.groupby("col1")["col2"].describe()`
#        <br><br>
#        Make sure you've fixed your file name so that's not the error any more<br><br>
#         
#     4. Forget one of the parentheses somewhere the code
#        <br>
#        For example, if the code should be `pd.read_csv(url)` the change it to `pd.read_csv(url`<br><br>
#         
#     5. Mistype one of the names of the chained functions with the code 
#        <br>
#        For example, try something like `df.group_by("col1")["col2"].describe()` and `df.groupby("col1")["col2"].describle()`<br><br>
#         
#     6. Use a column name that's not in your data for the `groupby` and column selection 
#        <br>
#        For example, try capitalizing the columns for example replacing "sex" with "Sex" in `titanic_df.groupby("sex")["age"].describe()`, and then instead introducing the same error of "age"<br><br>
#         
#     7. Forget to put the column name as a string in quotes for the `groupby` and column selection, and see if the ChatBot and google are still as helpful as they were for the previous question
#        <br>
#        For example, something like `titanic_df.groupby(sex)["age"].describe()`, and then `titanic_df.groupby("sex")[age].describe()`
#         
# 

# (1)The df.groupby("col1")["col2"].describe() method in pandas is used to generate descriptive statistics for the col2 column, grouped by the unique values in col1. Essentially, it provides a summary of statistics for each group, such as count, mean, standard deviation, minimum, and the percentiles. To be more detailed, Group By: The groupby("col1") part groups the DataFrame df by the unique values in col1. Each group corresponds to one of these unique values. Select Column: The ["col2"] part selects the col2 column within each of these groups. Describe: The .describe() method then computes summary statistics for each group in the col2 column.

# In[6]:


#Using an example dataset:
import pandas as pd

# Create the DataFrame with employee data
data = {
    'department': ['Sales', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Engineering', 'Engineering', 'Engineering'],
    'salary': [50000, 55000, 60000, 48000, 51000, 70000, 75000, 80000],
    'years_experience': [5, 7, 8, 3, 4, 10, 12, 15]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

#Then perform the action:
import pandas as pd

# Create the DataFrame
data = {
    'department': ['Sales', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Engineering', 'Engineering', 'Engineering'],
    'salary': [50000, 55000, 60000, 48000, 51000, 70000, 75000, 80000],
    'years_experience': [5, 7, 8, 3, 4, 10, 12, 15]
}

df = pd.DataFrame(data)

# Group by 'department' and get descriptive statistics for 'salary'
result = df.groupby('department')['salary'].describe()

print(result)


# (2)Sorry, I dont quite understand this problem

# (3)I think it's more convenient to use the chat bot to fix errors since you can just tell the bot to automaticaly check the code and fix the error by itself. For example, in problem 7, firstly I forgot to define df_cleaned in the code, then I ask gpt bot to define it and put it in the code. It gives me a fixed version in very quick time which is correct and able to run.

# #### 9. Have you reviewed the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br>
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)
#     
# </details>
#     
# ***Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)!***

# Yes I did.

# Summary 1:Objective: You wanted to remove missing data from a dataset using del df['col'] and df.dropna(), and provide a justification along with a "before and after" report.
# 
# Dataset Inspection: We examined the dataset villagers.csv for missing values. The initial output indicated which columns had missing data.
# 
# Cleaning Approach:
# 
# Column Removal: Columns with a significant number of missing values (e.g., song) were removed. This simplifies the dataset by eliminating columns that could introduce complexity due to missing data.
# Row Removal: Rows with any remaining missing values were removed using df.dropna(), ensuring that the dataset is complete and clean.
# Implementation:
# 
# Before Cleaning: Displayed the shape of the dataset and the number of missing values per column before cleaning.
# After Cleaning: Printed the shape of the dataset and missing values per column after cleaning to confirm the dataset is now complete.
# Justification:
# 
# Removing Columns: Removes columns with high proportions of missing values that are not crucial to the analysis.
# Dropping Rows: Ensures that any remaining rows with missing values are removed, resulting in a dataset without missing data.
# The final code provided was a complete example, demonstrating how to properly clean the dataset and confirm that no missing values remain after the cleaning process.

# In[17]:


#Summary 2:
#Understanding df.groupby("col1")["col2"].describe():

#This method groups the DataFrame by unique values in col1 and then provides descriptive statistics (count, mean, std, min, 25%, 50%, 75%, max) for the col2 column within each group.
#Example with the Titanic Dataset:

#We discussed how to use this method to analyze the age column grouped by pclass in the Titanic dataset. This would give insights into how the ages of passengers vary across different classes.
#Alternative Example:

#We used a hypothetical dataset of employees with columns for department, salary, and years_experience. We created a DataFrame, grouped it by department, and computed descriptive statistics for the salary column.
#Code Correction:

#The code you provided to create the DataFrame and perform the grouping and descriptive statistics was correct and should work without errors. The code was:

import pandas as pd

# Create the DataFrame
data = {'department': ['Sales', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Engineering', 'Engineering', 'Engineering'], 'salary': [50000, 55000, 60000, 48000, 51000, 70000, 75000, 80000],'years_experience': [5, 7, 8, 3, 4, 10, 12, 15]}

df = pd.DataFrame(data)

# Group by 'department' and get descriptive statistics for 'salary'
result = df.groupby('department')['salary'].describe()

print(result)

#The provided code correctly initializes the DataFrame, groups by department, and calculates the descriptive statistics for salary. If there were any issues, they were not related to the correctness of this code.


# # Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course<br><br>
# 
# <details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
# 
# ## Ethical Professionalism Considerations
# 
# > If the observed data is "no events occured" does this mean the data is "missing" and [should be ignored](https://priceonomics.com/the-space-shuttle-challenger-explosion-and-the-o)?
# > 
# > - NASA: \<determines temperature doesn't affects "o-ring" by subseting data to just "o-ring" incidents\>
# > - Also NASA: \<launches the shuttle on a cold day\>
# 
# |No apparent "o-ring" failure and temperature relationship|Apparent between "o-ring" failure and temperature relationship|
# |:-|:-|
# if you just look at "o-ring" failure event data|if you instead look at ALL the data as you should|
# |![](https://etzq49yfnmd.exactdn.com/wp-content/uploads/2022/03/image06-14.png)|![](https://etzq49yfnmd.exactdn.com/wp-content/uploads/2022/03/image02-33.png)|
# |![](https://upload.wikimedia.org/wikipedia/commons/8/8b/Shuttle_Challenger_explosion.gif?20190203170223)|![](https://i.makeagif.com/media/10-04-2014/nT57xW.gif)|
# 
# <br>
#     
# </details>    
# 
# <details class="details-example"><summary style="color:blue"><u>Current Course Project Capability Level</u></summary>
# 
# ## Current Course Project Capability Level
# 
# > The data we'll use for the STA130 course project is based on the [Canadian Social Connection Survey](https://casch.org/cscs). Please see the [data use agreement](https://static1.squarespace.com/static/60283c2e174c122f8ebe0f39/t/6239c284d610f76fed5a2e69/1647952517436/Data+Use+Agreement+for+the+Canadian+Social+Connection+Survey.pdf) regarding the appropriate and ethical professional use of this data (available at the bottom of the [CSCS](https://casch.org/cscs) webpage).
# > 
# > 1. Have a very quick look at the list of available variables using the [link](https://drive.google.com/file/d/1ISVymGn-WR1lcRs4psIym2N3or5onNBi/view) (again at the bottom of the [CSCS](https://casch.org/cscs) webpage); then, 
# > 2. examine the code in the first thirteen code cells of [STA130F24_CourseProject.ipynb](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F24_CourseProject.ipynb) to get an initital understanding of how we might subset to different studies included in the [data](https://drive.google.com/file/d/1mbUQlMTrNYA7Ly5eImVRBn16Ehy9Lggo/view) (again accessible at the bottom of the [CSCS](https://casch.org/cscs) webpage); then,     
# > 3. review the fourteenth and fifteenth cells (with the comments "Here's a high level summary of the data" and "And here are some explanations about the columns in the data") a little more closely to get a better sense of which columns seem to be the most interesting and whether or not they seem to have a lot of missing data
#     
# </details>        

# ### Afterward
# 
# Here are few ideas of some other kinds of interactions you might consider exploring with a ChatBot...
# 
# > While these are likely to be extremely practically valuable, they are not a part of the homework assignment, so do not include anything related to these in your homework submission
# 
# - With respect to improving ones ability in statistics, coding, communication, and other key data science skills
#     - what is the ChatBots perception its own capabilities and uses as an AI-driven assistance tool 
#     - and does ChatBots assessment of itself influence or agree with your own evalution of the ChatBot? 
# 
# - ChatBots can introduce and explain the "World War 2 planes" problem and the "Monte Hall" problem... 
#     - how well does do they seem to do and introducing and explaining other "unintuitive surprising statistics paradoxes"?
# 
# - If you consider the process of writing about why you chose to take this course, and the skills you were hoping to build through this course with respect to your current ideas about what possible careers 
#     - and how do you think the exercise would be different if you framed it as a dialogue with a ChatBot
#     - and do you think the difference could be positive and productive, or potentially biasing and distracting?
#     
# - ChatBots sometimes immediately responds in simple helpful ways, but other times it gives a lot of extraneous information that can be overwheling... are you able to prompt and interact with ChatBots in manner that keeps its reponses helpful and focused on what you're interested in? 
# 
# - ChatBots tends to respond in a fairly empathetic and supportive tone...
#     - do you find it helpful to discuss concerns you might have about succeeding in the course (or entering university more generally) with a ChatBot?
#     
# - For what purposes and in what contexts do you think a ChatBot could provide suggestions or feedback about your experiences that might be useful? 
# 
