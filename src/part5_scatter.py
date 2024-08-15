'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatterplot_felony_vs_nonfelony(pred_universe):
    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony', hue='has_felony_charge', fit_reg=False)
    plt.savefig('../data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')

    # Interpretation
    print("What can you say about the group of dots on the right side of the plot?")
    print("They represent individuals with high predicted probabilities for both felony and nonfelony")
    
# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatterplot_felony_vs_actual_rearrest(pred_universe):
    sns.lmplot(data=pred_universe, x='prediction_felony', y='rearrest_felony', fit_reg=False)
    plt.savefig('../data/part5_plots/scatter_felony_vs_actual_rearrest.png', bbox_inches='tight')
  
    # Interpretation
    print("What does this plot suggest about how well the model is calibrated?")
    print("The plot suggests that the model is well-calibrated")
