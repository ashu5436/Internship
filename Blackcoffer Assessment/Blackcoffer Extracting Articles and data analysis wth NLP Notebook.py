#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installing the selenium 
get_ipython().system('pip install selenium')


# In[2]:


#importing libraries for selenium
import selenium
from selenium import webdriver #webdriver needs to be of same version as that of chrome
from selenium.webdriver.common.by import By #'By' locates an elements by the exact text it displays.
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException #used for exceptions
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#Automating the Chrome
driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
#Now I'll be using all 115 url's one by one to extract the text information from the all the given url's articles
driver.get('https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/')
Text_37=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_37.append(i.text)
Text_37


# In[148]:


#saving the text articles in the form of txt file with the same url_id name as said in the problem statement
with open('37.txt', 'w') as file:
    for item in Text_37:
        file.write(str(item) + '\n')
    #The 'w' mode tells Python to open the file in write mode, which means that it will be overwritten if it already exists. 
    #The for loop writes each item in the list to a new line in the text file.


# ### Finding the text information for other 113 article's

# In[4]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/')
Text_38=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_38.append(i.text)
print(Text_38)


# In[6]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/')
Text_39=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_39.append(i.text)
print(Text_39)


# In[7]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/')
Text_40=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_40.append(i.text)
print(Text_40)


# In[8]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/')
Text_41=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_41.append(i.text)
print(Text_41)


# In[9]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/')
Text_42=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_42.append(i.text)
print(Text_42)


# In[10]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/')
Text_43=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_43.append(i.text)
print(Text_43)


# In[146]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/')
Text_44=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_44.append(i.text)
print(Text_44)


# ###### we didn't get any text from 44th article as the page is no more existing on the website.

# In[12]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/')
Text_45=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_45.append(i.text)
print(Text_45)


# In[13]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/')
Text_46=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_46.append(i.text)
print(Text_46)


# In[14]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/')
Text_47=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_47.append(i.text)
print(Text_47)


# In[15]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/')
Text_48=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_48.append(i.text)
print(Text_48)


# In[16]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/')
Text_49=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_49.append(i.text)
print(Text_49)


# In[17]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/')
Text_50=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_50.append(i.text)
print(Text_50)


# In[18]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/')
Text_51=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_51.append(i.text)
print(Text_51)


# In[19]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/')
Text_52=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_52.append(i.text)
print(Text_52)


# In[20]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/')
Text_53=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_53.append(i.text)
print(Text_53)


# In[21]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/')
Text_54=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_54.append(i.text)
print(Text_54)


# In[22]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/evolution-of-advertising-industry/')
Text_55=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_55.append(i.text)
print(Text_55)


# In[23]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/')
Text_56=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_56.append(i.text)
print(Text_56)


# In[150]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/')
Text_57=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_57.append(i.text)
print(Text_57)


# ###### we didn't get any text from 57th article as the page is no more existing on the website.

# In[25]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/')
Text_58=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_58.append(i.text)
print(Text_58)


# In[26]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/')
Text_59=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_59.append(i.text)
print(Text_59)


# In[27]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/')
Text_60=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_60.append(i.text)
print(Text_60)


# In[28]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/')
Text_61=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_61.append(i.text)
print(Text_61)


# In[29]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/')
Text_62=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_62.append(i.text)
print(Text_62)


# In[30]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/')
Text_63=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_63.append(i.text)
print(Text_63)


# In[33]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/')
Text_64=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_64.append(i.text)
print(Text_64)


# In[34]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/')
Text_65=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_65.append(i.text)
print(Text_65)


# In[35]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-we-forecast-future-technologies/')
Text_66=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_66.append(i.text)
print(Text_66)


# In[36]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/')
Text_67=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_67.append(i.text)
print(Text_67)


# In[37]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/')
Text_68=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_68.append(i.text)
print(Text_68)


# In[38]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/')
Text_69=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_69.append(i.text)
print(Text_69)


# In[39]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/')
Text_70=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_70.append(i.text)
print(Text_70)


# In[40]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/')
Text_71=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_71.append(i.text)
print(Text_71)


# In[41]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/')
Text_72=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_72.append(i.text)
print(Text_72)


# In[42]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/')
Text_73=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_73.append(i.text)
print(Text_73)


# In[57]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/')
Text_74=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_74.append(i.text)
print(Text_74)


# In[61]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/')
Text_75=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_75.append(i.text)
print(Text_75)


# In[62]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/')
Text_76=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_76.append(i.text)
print(Text_76)


# In[63]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/')
Text_77=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_77.append(i.text)
print(Text_77)


# In[64]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/')
Text_78=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_78.append(i.text)
print(Text_78)


# In[65]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/')
Text_79=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_79.append(i.text)
print(Text_79)


# In[67]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/')
Text_80=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_80.append(i.text)
print(Text_80)


# In[68]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/')
Text_81=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_81.append(i.text)
print(Text_81)


# In[69]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/')
Text_82=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_82.append(i.text)
print(Text_82)


# In[70]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/')
Text_83=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_83.append(i.text)
print(Text_83)


# In[71]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/')
Text_84=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_84.append(i.text)
print(Text_84)


# In[72]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/')
Text_85=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_85.append(i.text)
print(Text_85)


# In[74]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/')
Text_86=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_86.append(i.text)
print(Text_86)


# In[75]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/')
Text_87=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_87.append(i.text)
print(Text_87)


# In[76]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/')
Text_88=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_88.append(i.text)
print(Text_88)


# In[77]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/')
Text_89=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_89.append(i.text)
print(Text_89)


# In[78]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/')
Text_90=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_90.append(i.text)
print(Text_90)


# In[79]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/human-rights-outlook/')
Text_91=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_91.append(i.text)
print(Text_91)


# In[80]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/')
Text_92=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_92.append(i.text)
print(Text_92)


# In[81]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/')
Text_93=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_93.append(i.text)
print(Text_93)


# In[82]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/')
Text_94=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_94.append(i.text)
print(Text_94)


# In[83]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/')
Text_95=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_95.append(i.text)
print(Text_95)


# In[84]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/')
Text_96=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_96.append(i.text)
print(Text_96)


# In[85]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/')
Text_97=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_97.append(i.text)
print(Text_97)


# In[86]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/')
Text_98=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_98.append(i.text)
print(Text_98)


# In[87]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/')
Text_99=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_99.append(i.text)
print(Text_99)


# In[89]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/')
Text_100=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_100.append(i.text)
print(Text_100)


# In[90]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/travel-and-tourism-outlook/')
Text_101=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_101.append(i.text)
print(Text_101)


# In[91]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/')
Text_102=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_102.append(i.text)
print(Text_102)


# In[92]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/')
Text_103=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_103.append(i.text)
print(Text_103)


# In[93]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/')
Text_104=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_104.append(i.text)
print(Text_104)


# In[94]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/')
Text_105=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_105.append(i.text)
print(Text_105)


# In[95]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/')
Text_106=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_106.append(i.text)
print(Text_106)


# In[96]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/')
Text_107=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_107.append(i.text)
print(Text_107)


# In[97]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/')
Text_108=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_108.append(i.text)
print(Text_108)


# In[98]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/')
Text_109=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_109.append(i.text)
print(Text_109)


# In[100]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/')
Text_110=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_110.append(i.text)
print(Text_110)


# In[101]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/')
Text_111=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_111.append(i.text)
print(Text_111)


# In[102]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/')
Text_112=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_112.append(i.text)
print(Text_112)


# In[103]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/')
Text_113=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_113.append(i.text)
print(Text_113)


# In[105]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/')
Text_114=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_114.append(i.text)
print(Text_114)


# In[106]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/')
Text_115=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_115.append(i.text)
print(Text_115)


# In[107]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/')
Text_116=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_116.append(i.text)
print(Text_116)


# In[108]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/')
Text_117=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_117.append(i.text)
print(Text_117)


# In[109]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/')
Text_118=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_118.append(i.text)
print(Text_118)


# In[110]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/')
Text_119=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_119.append(i.text)
print(Text_119)


# In[111]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/')
Text_120=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_120.append(i.text)
print(Text_120)


# In[112]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/')
Text_121=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_121.append(i.text)
print(Text_121)


# In[113]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/')
Text_122=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_122.append(i.text)
print(Text_122)


# In[114]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/')
Text_123=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_123.append(i.text)
print(Text_123)


# In[115]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/')
Text_124=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_124.append(i.text)
print(Text_124)


# In[117]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/')
Text_125=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_125.append(i.text)
print(Text_125)


# In[118]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/')
Text_126=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_126.append(i.text)
print(Text_126)


# In[119]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/')
Text_127=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_127.append(i.text)
print(Text_127)


# In[120]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/')
Text_128=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_128.append(i.text)
print(Text_128)


# In[122]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/')
Text_129=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_129.append(i.text)
print(Text_129)


# In[123]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/')
Text_130=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_130.append(i.text)
print(Text_130)


# In[124]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/')
Text_131=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_131.append(i.text)
print(Text_131)


# In[125]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/')
Text_132=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_132.append(i.text)
print(Text_132)


# In[126]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/continued-demand-for-sustainability/')
Text_133=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_133.append(i.text)
print(Text_133)


# In[127]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/')
Text_134=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_134.append(i.text)
print(Text_134)


# In[128]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/')
Text_135=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_135.append(i.text)
print(Text_135)


# In[129]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/why-is-there-a-severe-immunological-and-inflammatory-explosion-in-those-affected-by-sarms-covid-19/')
Text_136=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_136.append(i.text)
print(Text_136)


# In[130]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/what-do-you-think-is-the-lesson-or-lessons-to-be-learned-with-covid-19/')
Text_137=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_137.append(i.text)
print(Text_137)


# In[131]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/coronavirus-the-unexpected-challenge-for-the-european-union/')
Text_138=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_138.append(i.text)
print(Text_138)


# In[132]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/industrial-revolution-4-0-pros-and-cons/')
Text_139=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_139.append(i.text)
print(Text_139)


# In[133]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy/')
Text_140=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_140.append(i.text)
print(Text_140)


# In[134]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-2/')
Text_141=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_141.append(i.text)
print(Text_141)


# In[135]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy/')
Text_142=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_142.append(i.text)
print(Text_142)


# In[136]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-global-economy/')
Text_143=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_143.append(i.text)
print(Text_143)


# In[139]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/ensuring-growth-through-insurance-technology/')
Text_144=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_144.append(i.text)
print(Text_144)


# ###### we didn't get any text from 144th article as the page is no more existing on the website.

# In[140]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/blockchain-in-fintech/')
Text_145=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_145.append(i.text)
print(Text_145)


# In[141]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/blockchain-for-payments/')
Text_146=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_146.append(i.text)
print(Text_146)


# In[142]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/the-future-of-investing/')
Text_147=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_147.append(i.text)
print(Text_147)


# In[143]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/big-data-analytics-in-healthcare/')
Text_148=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_148.append(i.text)
print(Text_148)


# In[144]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/business-analytics-in-the-healthcare-industry/')
Text_149=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_149.append(i.text)
print(Text_149)


# In[145]:


driver=webdriver.Chrome(r'C://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://insights.blackcoffer.com/challenges-and-opportunities-of-big-data-in-healthcare/')
Text_150=[]
for i in driver.find_elements(By.XPATH,'//div[@class="td-post-content"]//p'):
    Text_150.append(i.text)
print(Text_150)


# ### Saving all the 114 text articles in txt file having the same name as url_id of each

# In[159]:


with open('38.txt', 'w') as file:
    for item in Text_38[0:-1]:
        file.write(str(item) + '\n')
        
#The 'w' mode tells Python to open the file in write mode, which means that it will be overwritten if it already exists. 
#The for loop writes each item in the list to a new line in the text file.

with open('39.txt', 'w') as file:
    for item in Text_39:
        file.write(str(item) + '\n')
        
with open('40.txt', 'w') as file:
    for item in Text_40[0:-1]:
        file.write(str(item) + '\n')

with open('41.txt', 'w') as file:
    for item in Text_41:
        file.write(str(item) + '\n')

with open('42.txt', 'w') as file:
    for item in Text_42[0:-1]:
        file.write(str(item) + '\n')  

with open('43.txt', 'w') as file:
    for item in Text_43[0:-1]:
        file.write(str(item) + '\n')

with open('44.txt', 'w') as file:
    for item in Text_44:
        file.write(str(item) + '\n')   

with open('45.txt', 'w') as file:
    for item in Text_45:
        file.write(str(item) + '\n')
        
with open('46.txt', 'w') as file:
    for item in Text_46:
        file.write(str(item) + '\n')
        
with open('47.txt', 'w') as file:
    for item in Text_47:
        file.write(str(item) + '\n')
        
with open('48.txt', 'w') as file:
    for item in Text_48[0:-1]:
        file.write(str(item) + '\n')
        
with open('49.txt', 'w') as file:
    for item in Text_49:
        file.write(str(item) + '\n')
        
with open('50.txt', 'w') as file:
    for item in Text_50:
        file.write(str(item) + '\n')
        
with open('51.txt', 'w') as file:
    for item in Text_51[0:-1]:
        file.write(str(item) + '\n')
        
with open('52.txt', 'w') as file:
    for item in Text_52[0:-1]:
        file.write(str(item) + '\n')
        
with open('53.txt', 'w') as file:
    for item in Text_53[0:-1]:
        file.write(str(item) + '\n')
        
with open('54.txt', 'w') as file:
    for item in Text_54[3:-1]:
        file.write(str(item) + '\n')
        
with open('55.txt', 'w') as file:
    for item in Text_55[0:-1]:
        file.write(str(item) + '\n')
        
with open('56.txt', 'w') as file:
    for item in Text_56:
        file.write(str(item) + '\n')
        
with open('57.txt', 'w') as file:
    for item in Text_57:
        file.write(str(item) + '\n')
        
with open('58.txt', 'w') as file:
    for item in Text_58[0:-1]:
        file.write(str(item) + '\n')
        
with open('59.txt', 'w') as file:
    for item in Text_59:
        file.write(str(item) + '\n')
        
with open('60.txt', 'w') as file:
    for item in Text_60:
        file.write(str(item) + '\n')
        
with open('61.txt', 'w') as file:
    for item in Text_61:
        file.write(str(item) + '\n')
        
with open('62.txt', 'w') as file:
    for item in Text_62:
        file.write(str(item) + '\n')
        
with open('63.txt', 'w') as file:
    for item in Text_63:
        file.write(str(item) + '\n')
        
with open('64.txt', 'w') as file:
    for item in Text_64[0:-1]:
        file.write(str(item) + '\n')
        
with open('65.txt', 'w') as file:
    for item in Text_65:
        file.write(str(item) + '\n')
        
with open('66.txt', 'w') as file:
    for item in Text_66:
        file.write(str(item) + '\n')
        
with open('67.txt', 'w') as file:
    for item in Text_67:
        file.write(str(item) + '\n')
        
with open('68.txt', 'w') as file:
    for item in Text_68:
        file.write(str(item) + '\n')
        
with open('69.txt', 'w') as file:
    for item in Text_69:
        file.write(str(item) + '\n')
        
with open('70.txt', 'w') as file:
    for item in Text_70:
        file.write(str(item) + '\n')
        
with open('71.txt', 'w') as file:
    for item in Text_71[1:]:
        file.write(str(item) + '\n')
        
with open('72.txt', 'w') as file:
    for item in Text_72:
        file.write(str(item) + '\n')
        
with open('73.txt', 'w') as file:
    for item in Text_73:
        file.write(str(item) + '\n')
        
with open('74.txt', 'w') as file:
    for item in Text_74[0:-1]:
        file.write(str(item) + '\n')
        
with open('75.txt', 'w') as file:
    for item in Text_75:
        file.write(str(item) + '\n')
        
with open('76.txt', 'w') as file:
    for item in Text_76:
        file.write(str(item) + '\n')
        
with open('77.txt', 'w') as file:
    for item in Text_77:
        file.write(str(item) + '\n')
        
with open('78.txt', 'w') as file:
    for item in Text_78:
        file.write(str(item) + '\n')
        
with open('79.txt', 'w') as file:
    for item in Text_79:
        file.write(str(item) + '\n')
        
with open('80.txt', 'w') as file:
    for item in Text_80:
        file.write(str(item) + '\n')
        
with open('81.txt', 'w') as file:
    for item in Text_81:
        file.write(str(item) + '\n')
        
with open('82.txt', 'w') as file:
    for item in Text_82[0:-1]:
        file.write(str(item) + '\n')
        
with open('83.txt', 'w') as file:
    for item in Text_83[0:-1]:
        file.write(str(item) + '\n')
        
with open('84.txt', 'w', encoding="utf-8") as file:
    for item in Text_84:
        file.write(str(item) + '\n')
        
with open('85.txt', 'w') as file:
    for item in Text_85:
        file.write(str(item) + '\n')
        
with open('86.txt', 'w') as file:
    for item in Text_86:
        file.write(str(item) + '\n')
        
with open('87.txt', 'w',encoding="utf-8") as file:
    for item in Text_87:
        file.write(str(item) + '\n')

#UTF-8 is an encoding system for Unicode. It can translate any Unicode character to a matching unique binary string
        
with open('88.txt', 'w') as file:
    for item in Text_88[0:-1]:
        file.write(str(item) + '\n')
        
with open('89.txt', 'w') as file:
    for item in Text_89:
        file.write(str(item) + '\n')
        
with open('90.txt', 'w') as file:
    for item in Text_90:
        file.write(str(item) + '\n')
        
with open('91.txt', 'w') as file:
    for item in Text_91[0:-3]:
        file.write(str(item) + '\n')
        
with open('92.txt', 'w') as file:
    for item in Text_92:
        file.write(str(item) + '\n')
        
with open('93.txt', 'w') as file:
    for item in Text_93:
        file.write(str(item) + '\n')
        
with open('94.txt', 'w') as file:
    for item in Text_94:
        file.write(str(item) + '\n')
        
with open('95.txt', 'w') as file:
    for item in Text_95:
        file.write(str(item) + '\n')
        
with open('96.txt', 'w',encoding="utf-8") as file:
    for item in Text_96[0:-1]:
        file.write(str(item) + '\n')
        
with open('97.txt', 'w') as file:
    for item in Text_97:
        file.write(str(item) + '\n')
        
with open('98.txt', 'w') as file:
    for item in Text_98:
        file.write(str(item) + '\n')
        
with open('99.txt', 'w') as file:
    for item in Text_99:
        file.write(str(item) + '\n')
        
with open('100.txt', 'w') as file:
    for item in Text_100[2:]:
        file.write(str(item) + '\n')
        
with open('101.txt', 'w') as file:
    for item in Text_101[0:-2]:
        file.write(str(item) + '\n')
        
with open('102.txt', 'w') as file:
    for item in Text_102[0:-1]:
        file.write(str(item) + '\n')
        
with open('103.txt', 'w') as file:
    for item in Text_103:
        file.write(str(item) + '\n')
        
with open('104.txt', 'w') as file:
    for item in Text_104:
        file.write(str(item) + '\n')
        
with open('105.txt', 'w') as file:
    for item in Text_105:
        file.write(str(item) + '\n')
        
with open('106.txt', 'w') as file:
    for item in Text_106:
        file.write(str(item) + '\n')
        
with open('107.txt', 'w') as file:
    for item in Text_107:
        file.write(str(item) + '\n')
        
with open('108.txt', 'w') as file:
    for item in Text_108:
        file.write(str(item) + '\n')
        
with open('109.txt', 'w') as file:
    for item in Text_109:
        file.write(str(item) + '\n')
        
with open('110.txt', 'w') as file:
    for item in Text_110:
        file.write(str(item) + '\n')
        
with open('111.txt', 'w') as file:
    for item in Text_111[0:-1]:
        file.write(str(item) + '\n')
        
with open('112.txt', 'w') as file:
    for item in Text_112:
        file.write(str(item) + '\n')
        
with open('113.txt', 'w') as file:
    for item in Text_113:
        file.write(str(item) + '\n')
        
with open('114.txt', 'w') as file:
    for item in Text_114:
        file.write(str(item) + '\n')
        
with open('115.txt', 'w') as file:
    for item in Text_115:
        file.write(str(item) + '\n')
        
with open('116.txt', 'w') as file:
    for item in Text_116:
        file.write(str(item) + '\n')
        
with open('117.txt', 'w',encoding="utf-8") as file:
    for item in Text_117:
        file.write(str(item) + '\n')
        
with open('118.txt', 'w') as file:
    for item in Text_118[0:-1]:
        file.write(str(item) + '\n')
        
with open('119.txt', 'w') as file:
    for item in Text_119:
        file.write(str(item) + '\n')
        
with open('120.txt', 'w',encoding="utf-8") as file:
    for item in Text_120:
        file.write(str(item) + '\n')
        
with open('121.txt', 'w') as file:
    for item in Text_121[0:-1]:
        file.write(str(item) + '\n')
        
with open('122.txt', 'w') as file:
    for item in Text_122[0:-1]:
        file.write(str(item) + '\n')
        
with open('123.txt', 'w') as file:
    for item in Text_123:
        file.write(str(item) + '\n')
        
with open('124.txt', 'w') as file:
    for item in Text_124:
        file.write(str(item) + '\n')
        
with open('125.txt', 'w') as file:
    for item in Text_125:
        file.write(str(item) + '\n')
        
with open('126.txt', 'w') as file:
    for item in Text_126:
        file.write(str(item) + '\n')
        
with open('127.txt', 'w') as file:
    for item in Text_127:
        file.write(str(item) + '\n')
        
with open('128.txt', 'w') as file:
    for item in Text_128:
        file.write(str(item) + '\n')
        
with open('129.txt', 'w') as file:
    for item in Text_129:
        file.write(str(item) + '\n')
        
with open('130.txt', 'w') as file:
    for item in Text_130[0:-1]:
        file.write(str(item) + '\n')
        
with open('131.txt', 'w') as file:
    for item in Text_131:
        file.write(str(item) + '\n')
        
with open('132.txt', 'w') as file:
    for item in Text_132[0:-3]:
        file.write(str(item) + '\n')
        
with open('133.txt', 'w') as file:
    for item in Text_133[0:-1]:
        file.write(str(item) + '\n')
        
with open('134.txt', 'w') as file:
    for item in Text_134:
        file.write(str(item) + '\n')
        
with open('135.txt', 'w') as file:
    for item in Text_135:
        file.write(str(item) + '\n')
        
with open('136.txt', 'w') as file:
    for item in Text_136:
        file.write(str(item) + '\n')
        
with open('137.txt', 'w') as file:
    for item in Text_137:
        file.write(str(item) + '\n')
        
with open('138.txt', 'w') as file:
    for item in Text_138:
        file.write(str(item) + '\n')
        
with open('139.txt', 'w') as file:
    for item in Text_139[0:-1]:
        file.write(str(item) + '\n')
        
with open('140.txt', 'w',encoding="utf-8") as file:
    for item in Text_140:
        file.write(str(item) + '\n')
        
with open('141.txt', 'w') as file:
    for item in Text_141[0:-1]:
        file.write(str(item) + '\n')
        
with open('142.txt', 'w',encoding="utf-8") as file:
    for item in Text_142[0:-1]:
        file.write(str(item) + '\n')
        
with open('143.txt', 'w') as file:
    for item in Text_143[0:-1]:
        file.write(str(item) + '\n')
        
with open('144.txt', 'w') as file:
    for item in Text_144:
        file.write(str(item) + '\n')
        
with open('145.txt', 'w') as file:
    for item in Text_145[0:-1]:
        file.write(str(item) + '\n')
        
with open('146.txt', 'w') as file:
    for item in Text_146[0:-1]:
        file.write(str(item) + '\n')
        
with open('147.txt', 'w') as file:
    for item in Text_147:
        file.write(str(item) + '\n')
        
with open('148.txt', 'w') as file:
    for item in Text_148:
        file.write(str(item) + '\n')
        
with open('149.txt', 'w') as file:
    for item in Text_149:
        file.write(str(item) + '\n')
        
with open('150.txt', 'w') as file:
    for item in Text_150:
        file.write(str(item) + '\n')


# ### Data Analysis with the help of Natural Language Processing(NLP)

# In[160]:


import nltk #NLP libraries with respect to machine learning
import re   #Regular Expression
from nltk.corpus import stopwords
nltk.download('stopwords')


# ### 1.Sentimental Analysis
# Text Preprocessing

# In[182]:


from nltk.tokenize import word_tokenize

#loading stopwords by combining different txt files from stopwords folder
import os # provides the facility to establish the interaction between the user and the operating system
stopwords_list = []
stopwords_folder = "C://Users//Admin//Downloads//StopWords" #location of file
for file in os.listdir(stopwords_folder):
    if file.endswith(".txt"):
        with open(os.path.join(stopwords_folder, file)) as f:
            stopwords = set(f.read().splitlines()) # it reads the contents of the file, splits it into a list of lines and 
            #then creates a set of words from the list of lines. This creates a new set that contains all the stopwords 
            #from the file.It is important to note that, each line in the file should contain one word only, otherwise 
            #it will be treated as multiple stopwords
            stopwords_list.append(stopwords)
stop_words = set().union(*stopwords_list) # it is used to create a union of all the elements in the list of sets called 
                                          #stopwords_list.

# Loading positive and negative dictionaries from text files
with open("C://Users//Admin//Downloads//MasterDictionary//positive-words.txt", "r") as pos_file:
    positive_words = set(word.strip() for word in pos_file)

with open("C://Users//Admin//Downloads//MasterDictionary//negative-words.txt", "r") as neg_file:
    negative_words = set(word.strip() for word in neg_file)

# Function to clean the text and calculate the sentiment scores
def sentiment_scores(text):
    
    # converting the texts into lowercase
    text = text.lower() 
    text = ' '.join([word for word in text.split() if word not in stop_words]) # obtained text is free from stopwords
    
    # Tokenizing the text
    tokens = word_tokenize(text)
    
    # Initializing the scores
    positive_score = 0
    negative_score = 0
    
    # Calculating the positive and negative scores
    for token in tokens:
        if token in positive_words:
            positive_score += 1
        elif token in negative_words:
            negative_score += 1
    
    # Calculating the polarity and subjectivity scores
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(tokens) + 0.000001)
    #Total Words after cleaning=len(tokens)
    
    print("Positive Score:", positive_score)
    print("Negative Score:", negative_score)
    print("Polarity Score:", polarity_score)
    print("Subjectivity Score:", subjectivity_score)


# In[211]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Sentiment Analysis Results for " + file)
            sentiment_scores(text)
            print("\n")
#In this example, the loop iterates over each file in the directory text_folder, if the file ends with .txt, it opens the 
#file, reads the contents of the file, and calls the sentiment_scores function passing the text as an argument. 
#The result of the function call is printed along with the file name. The \n at the end of the print statement is used to 
#add a new line between the results of different files.


# ### 2.Analysis of Readability with Complex Word Count

# In[258]:


# function to get the syllables count
def count_syllables(text):
    text = text.lower()
    words = word_tokenize(text)
    vowels = "aeiou"
    total_syllables = 0
    for word in words:
        word = re.sub(r"([^aeiouy])", r"\1", word)
        word = re.sub(r"([aeiouy]){2,}", r"\1", word)
        word = re.sub(r"e$", "", word)
        total_syllables += len([c for c in word if c in vowels])
    return total_syllables

# function to check whether the word is complex or not
def is_complex_word(word):
    return count_syllables(word) > 2

#modify your Analysis_of_Readability function as follows

def Analysis_of_Readability(text):
    # Tokenizing the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    complex_words = []
    # Calculating the Average Sentence Length and Percentage of Complex Words
    average_sentence_length = len(words) / len(sentences)
    complex_words = [word for word in words if is_complex_word(word)]
    complex_word_count = len(complex_words)
    percentage_complex_words = complex_word_count / len(words)
# Calculating the Fog Index
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

# Printing the results
    print("Average Sentence Length: ", average_sentence_length)
    print("Complex Word Count: ", complex_word_count)
    print("Percentage of Complex Words: ", percentage_complex_words)
    print("Fog Index: ", fog_index)


# In[259]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Analysis of Readability for " + file)
            Analysis_of_Readability(text)
            print("\n")
# i didn't take the file 44,57 and 144 as there is no information inside it, otherwise it will give zero division error


# ### 3.Average Number of Words Per Sentence

# In[266]:


def anowps(text):
# Tokenizing the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

# Calculating the Average Number of Words Per Sentence
    average_number_of_words_per_sentence = len(words) / len(sentences)

# Print the results
    print("Average Number of Words Per Sentence: ", average_number_of_words_per_sentence)
    


# In[268]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Average Number of Words Per Sentence for " + file)
            anowps(text)
            print("\n")


# ### 4.Word Count and Average Word Length

# In[271]:


# Defining the Stop Words Lists using stopwords class of nltk package
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))

def wc_awl(text):
# Tokenizing the text into words
    words = word_tokenize(text)

# Removing stop words and punctuation
    cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in STOPWORDS]

# Calculating the Word Count
    word_count = len(cleaned_words)
    
# Calculating the Average Word Length
    average_word_length = sum(len(word) for word in cleaned_words) / word_count

# Printing the results
    print("Word Count: ", word_count)
    print("Average Word Length: ", average_word_length)


# In[272]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Word Count and Average Word Length for " + file)
            wc_awl(text)
            print("\n")
# i didn't take the file 44,57 and 144 as there is no information inside it, otherwise it will give zero division error


# ### 5.Syllable Count Per Word

# In[275]:


#importing the regular expression
import re
#defining the function
def count_syllables(text):
    text = text.lower()
    words = word_tokenize(text)
#defining the vowels
    vowels = "aeiou"
    total_syllables = 0
    for word in words:
        word = re.sub(r"([^aeiouy])", r"\1", word)
        word = re.sub(r"([aeiouy]){2,}", r"\1", word)
        word = re.sub(r"e$", "", word) 
        total_syllables += len([c for c in word if c in vowels])
    print(total_syllables)


# In[276]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Syllable Count Per Word for " + file)
            count_syllables(text)
            print("\n")


# ### 6.Personal Pronouns

# In[245]:


#defining the function
def count_personal_pronouns(text):
    text = text.lower()
#using given pronouns
    personal_pronouns = ["i", "we", "my", "ours", "us"]
    count = 0
    for pronoun in personal_pronouns:
        count += len(re.findall(r"\b" + pronoun + r"\b", text))
    print(count)


# In[246]:


import os
text_folder = "C://Users//Admin//Desktop//Micro Credit//FILEIMP"
for file in os.listdir(text_folder):
    if file.endswith(".txt"):
        with open(os.path.join(text_folder, file), 'r', encoding='latin-1') as f:
            text = f.read()
            print("Personal Pronouns for " + file)
            count_personal_pronouns(text)
            print("\n")


# In[ ]:




