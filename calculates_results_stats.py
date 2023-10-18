#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:   Junior David Roche
# DATE CREATED: 10/17/2023                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    
    # Calculates various statistics using list comprehension
    num_images = len(results_dic)
    num_dogs_img = sum( results_dic[key][3] for key in results_dic if results_dic[key][3] == 1 )
    num_notdogs_img = num_images - num_dogs_img
    num_matches = sum( results_dic[key][2] for key in results_dic if results_dic[key][2] == 1 )
    num_correct_dogs =  sum( results_dic[key][3] and results_dic[key][4] for key in results_dic )
    num_correct_notdogs =  sum( not results_dic[key][3] and not results_dic[key][4] for key in results_dic )
    num_correct_breed =  sum( results_dic[key][2] == 1 and results_dic[key][3] and results_dic[key][4] for key in results_dic )


    # Calculate percentages using dictionary comprehension
    pct_match = (num_matches / num_images) * 100 if num_images > 0 else 0
    pct_correct_dogs = (num_correct_dogs / num_dogs_img)  * 100 if num_dogs_img > 0 else 0
    pct_correct_notdogs = (num_correct_notdogs / num_dogs_img)  * 100 if num_notdogs_img > 0 else 0
    pct_correct_breed = (num_correct_breed / num_dogs_img)  * 100 if num_dogs_img > 0 else 0

    # Create and return results_stats_dic dictionary
    results_stats_dic = {
        'n_images': num_images,
        'n_dogs_img': num_dogs_img,
        'n_notdogs_img': num_notdogs_img,
        'n_match': num_matches,
        'n_correct_dogs': num_correct_dogs,
        'n_correct_notdogs': num_correct_notdogs,
        'n_correct_breed': num_correct_breed,
        'pct_match': pct_match,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_notdogs,
        'pct_correct_breed': pct_correct_breed
    }

    # Print acknowledgment info
    print("Results Statistics:")
    for key, value in results_stats_dic.items():
        print(f"{key}: {value}")
    
    return results_stats_dic
