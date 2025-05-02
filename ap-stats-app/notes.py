NOTES = {
    "Unit 1: Exploring One-Variable Data": {
        "Types of Data": (
            "Quantitative data: numerical values (e.g., height, test scores)\n"
            "Discrete – listable sets (counts)"
            "Continuous – any value over an interval of values (measurements)"
            "- **Categorical data**: descriptive groups (e.g., gender, color)\n"
            "- Display Quantitative: dotplot, histogram, boxplot\n"
            "- Display Categorical: bar graph, pie chart"
        ),
        "SOCS (Shape, Outliers, Center, Spread)": (
            "- **Shape**: symmetric, skewed left/right\n"
            "- **Outliers**: unusually high/low values\n"
            "- **Center**: mean (use if symmetric), median (use if skewed)\n"
            "- **Spread**: range, IQR(use if skewed), standard deviation(use if symmetric)"
        ),
        "Comparing Distributions": (
            "- Use SOCS\n"
            "- Always describe in context (mention variables and units)"
        ),
        "Boxplots": (
            "- Shows 5-number summary: Min, Q1, Median, Q3, Max\n"
            "- Good for comparing groups"
        ),
        "Standard Deviation & Variability": (
            "- SD measures average distance from the mean\n"
            "- Greater SD = more spread\n"
            "- Not resistant to outliers"
        ),
    },

    "Unit 2: Exploring Two-Variable Data": {
        "Scatterplots": (
            "- Shows direction, form, and strength\n"
            "- Look for linearity, clusters, outliers"
        ),
        "Correlation (r)": (
            "- Measures linear relationship strength\n"
            "- Between -1 and 1\n"
            "- No units, not resistant to outliers"
        ),
        "Regression Line": (
            "- Form: y = a + bx\n"
            "- b = slope, a = y-intercept\n"
            "- Use line to predict y from x"
        ),
        "Residuals": (
            "- Residual = actual - predicted\n"
            "- Residual plot shows if linear model is appropriate\n"
            "- No pattern = good fit"
        ),
        "r^2 (Coefficient of Determination)": (
            "- Tells % of variability in y explained by model\n"
            "- Closer to 1 = better fit"
        )
    },

    "Unit 3: Collecting Data": {
        "Sampling Methods": (
            "- SRS: random, each group equally likely\n"
            "- Stratified: divide into groups, sample from each\n"
            "- Cluster: divide into groups, sample whole groups\n"
            "- Systematic: every nth person\n"
            "- Convenience: easiest to reach (bad)\n"
            "- Voluntary response: people choose to respond (bad)"
        ),
        "Bias & Experiments": (
            "- Bias types: undercoverage, nonresponse, response, wording\n"
            "- Experiment: imposes treatment\n"
            "- Observational study: no treatment imposed\n"
            "- Control, random assignment, replication = good experiment"
        ),
        "Experimental Design": (
            "- Control group, placebo\n"
            "- Double-blind\n"
            "- Block: group by similar traits\n"
            "- Matched pairs: subjects paired by similarity"
        )
    },

    "Unit 4: Probability": {
        "Probability Basics": (
            "- Probability measures likelihood of an event\n"
            "- Between 0 and 1 (0 = impossible, 1 = certain)\n"
            "- Addition Rule: P(A or B) = P(A) + P(B) - P(A and B)\n"
            "- Multiplication Rule: P(A and B) = P(A) * P(B) if independent"
        ),
        "Conditional Probability": (
            "- P(A|B) = P(A and B) / P(B)\n"
            "- Used to find the probability of one event given another"
        ),
        "Disjoint & Independent Events": (
            "- Disjoint events: cannot happen at the same time (P(A and B) = 0)\n"
            "- Independent events: occurrence of one does not affect the other (P(A and B) = P(A) * P(B))"
        ),
        "Law of Total Probability & Bayes' Theorem": (
            "- Law of Total Probability: Total probability is sum of conditional probabilities\n"
            "- Bayes' Theorem: P(A|B) = [P(B|A) * P(A)] / P(B)"
        )
    },

    "Unit 5: Discrete Probability Distributions": {
        "Binomial vs Geometric": (
            "- **Binomial**: Fixed number of trials, probability of success remains constant\n"
            "- **Geometric**: Trials continue until first success, probability of success also constant"
        )
    },

    "Unit 6: Sampling Distributions": {
        "Sampling Distribution": (
            "- Distribution of a statistic (e.g., sample mean) based on all possible samples\n"
            "- Central Limit Theorem: As sample size increases, sample means approach a normal distribution"
        ),
        "Central Limit Theorem": (
            "- The sampling distribution of the sample mean will be normal for large sample sizes, regardless of the population distribution\n"
            "- Conditions: n > 30 or population is normal"
        ),
        "Standard Error": (
            "- Standard deviation of the sampling distribution of a statistic\n"
            "- Formula for mean: \( \frac{\sigma}{\sqrt{n}} \)"
        )
    },

    "Unit 7: Estimation": {
        "Interpreting Confidence Intervals": (
            "We are 95% confident that the interval of ... will contain the true population parameter"
        )
    },

    "Unit 8: Hypothesis Testing": {
        "Hypothesis Testing Basics": (
            "- Null hypothesis: Statement we seek evidence against\n"
            "- Alternative hypothesis: Statement we want to prove\n"
            "- p-value: Probability of observing data given that the null hypothesis is true"
        ),
        "Steps in Hypothesis Testing": (
            "1. Conditions: "
            "2. State hypotheses - don’t forget to define parameter\n"
            "3. Calculations – find z or t test statistic & p-value"
            "4. Calculate test statistic\n"
            "5. Find p-value\n"
            "6. Since the p-value is < (>) α, I reject (fail to reject) the Ho. There is (is not) sufficient evidence to suggest that [Ha]."
        ),
    },

    "Unit 9: Inference for Regression": {
    }
}
