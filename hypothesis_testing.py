from scipy import stats

def hypothesis_test(df):
    binary_variables = ['Diabetes','BloodPressureProblems','AnyTransplants','AnyChronicDiseases',
                        'KnownAllergies','HistoryOfCancerInFamily']
    # Significance level
    alpha = 0.05

    for var in binary_variables:
        # Separate the data into two groups
        group_0 = df[df[var] == 0]['PremiumPrice']
        group_1 = df[df[var] == 1]['PremiumPrice']
        
        # Perform the t-test
        t_stat, p_value = stats.ttest_ind(group_0, group_1)
        
        # Print the hypotheses and results
        print(f"\033[1mTesting the effect of {var} on insurance price\033[0m")
        print(f"\033[1mNull Hypothesis (H0)\033[0m: {var} has no effect on the insurance price.")
        print(f"\033[1mAlternative Hypothesis (H1)\033[0m: {var} has a significant effect on the insurance price.")
        print(f"\033[1mP-value\033[0m: {p_value}")
        
        if p_value < alpha:
            print("\033[1mReject the null hypothesis\033[0m: There is a significant effect of {} on insurance price.".format(var))
        else:
            print("\033[1mFail to reject the null hypothesis\033[0m: There is no significant effect of {} on insurance price.".format(var))
        
        # Print a delimiter
        return print("\033[1m-\033[0m" * 100)