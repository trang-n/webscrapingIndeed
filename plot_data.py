import json
import re,csv
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt
from text_processing import *
import pandas as pd
import numpy as np



def load_file(filename):
    with open(filename, 'r') as f:
        job_dict = json.load(f)
        return job_dict

#extract string to make world cloud
def string_wc(list_titles):
    data = {}
    posting_data =[]

    #load posting values to 1 file
    for title in list_titles:
        file_name = '_'.join(title.split()) + '.json'
        data=load_file(file_name)
        for i in range(0,100):
            try:
                posting_data.append(data[str(i)]['posting'])
            except:
                continue
            
    #make it a list of string with lower case
    posting = ','.join(posting_data)
    posting
    posting =posting.lower()
    return posting

#make wordcloud
def make_wc(text, max_words = 200, list_stopw = [], save_file = False):
    wordcloud = WordCloud().generate(text)
    stopwords = set(STOPWORDS)
    stopwords.update(list_stopw)
    list_stopw

    wordcloud = WordCloud(background_color = 'white',
                      stopwords = stopwords,
                      max_words = max_words,
                      min_font_size = 6,
                      scale = 1,
                      width = 800, height = 800, random_state =8).generate(text)

    plt.figure(figsize =[15,10]) #create figure with width and height
    plt.imshow(wordcloud, interpolation = "bilinear") #display image on 2D
    plt.axis("off") #hide axis
    plt.show()


    if save_file:
        save_file = save_file + ".png"
        wordcloud.to_file(save_file)
        

#plot category of skills for both ds and da
def plot_skillcat(df1, df2, cat, save_figure = False):
    
    #set up variables
    categories = list(df1.skillset.unique())
    
    titles = ['data analyst', 'data scientist']
    
    if cat.title() not in categories: 
        print('category invalid')
        return None
    
    cat = cat.title() #capitalize first letters
    
    
    #subset dataframe to by skillset
    df1_cat = df1.query('skillset==@cat')
    df2_cat = df2.query('skillset==@cat')
    df = [df1_cat, df2_cat]
    
    ##ploting prep
    nrows = 2
    ncols = 1
    figsize = (18,15)
    
    #generate subplots
    fig, axes = plt.subplots(nrows = nrows, ncols = ncols, figsize = figsize)
    
    
    #loop through the axes of the figure, plotting each subplot
    for row in range(nrows):
        title = titles[row]
        df_plot = df[row].sort_values(by = 'frequency', ascending = False) #df_plot is df
        
        #decide twhich ax to plot
        ax = axes[row]
        df_plot = df_plot.plot(x = 'skill', y = 'frequency', kind ='bar', ax = ax, colormap = 'Dark2') #change df_plot to be a plot
        ax.set(title=title, xlabel = 'Languages', ylabel= 'Frequency')
        ax.get_legend().remove() #remove legend
        
        for tick in df_plot.get_xticklabels(): #rotate skillnames for reading
            tick.set_rotation(30)

    #add figure title
    fig_title = cat + ' Distribution'
    plt.suptitle(fig_title, horizontalalignment = 'center', fontsize = 25) #figure title as category
    plt.subplots_adjust(hspace = 0.40) #avoid overlapping between 2 plots
    plt.show()
    
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        