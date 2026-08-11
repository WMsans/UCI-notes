## Research Question

To what extent does first-generation college graduate from UCI status (neither parent holds a 4‑year degree) affect the number of promotions received within five years of graduation?

## Variables

The independent variables is the status of being first gen student or not. It is determined by whether any of the parents has a four year college degree: if one does, are not first gen; otherwise, they are a first gen student. To measure this variable, the participants would self-report the status in a survey. 

The dependent variables is career advancement, measured as total promotions in a five year period following bachelor’s degree completion. To measure this variable, the participants would self‑report a numeric response in the survey under a well worded question (for instance, "How many times have you been promoted since graduating"). 

The control variables include industry type, economic standing, and undergraduate GPA. These are important because these each impact the dependent variables in measure. First, the career advancement speed varies a lot from each other in different industries.. A person working in tech company may get his first promotion in a few month while it may take years in education. To solve this, the participants would be sort into different industries when analyzing. Then, the economic standing, measured in parents’ income, would affect the participants behavior in their work, such as risk taking abilities and promotion-seeking behaviors. To reduce the bias, the participants would be ranked by their income level to low, mid and high when analyzing. Finally, the undergraduate GPA of the participants proxies for individual merit, which is what this research is not interested in instead of the isolated net effect of ascribed status (first gen). Thus, similar to financial, the participants are ranked by GPA as well when analyzing. 

## Data and Methods

To collect the data, an online self-report survey would be send out to the alumnus of UCI graduated five years ago. This is due to that more precise collection methods like in‑depth interviews produce sample sizes that are too small to generalize to the UCI undergraduate population, while direct methods including HR records are usually unavailable due to privacy barriers. As a result, despite the recall bias, self‑report surveys is most suitable to this research. In addition, the surveys are very short with only a few questions, and can be totally anonymous, which can greatly increase the respond rate. 

The content of the survey include a multiple choice of parental education, a number input question titled "In the 5 years since you graduated from UCI, how many times have you been promoted (excluding title changes without pay increase)?", and the control variable questions including industry (categorical list), current economic standing (e.g., self‑rated financial security + income bracket), and GPA (self‑reported on a 4.0 scale). 

First, the Alumni lists is fetched from the UCI website, restricted to graduates of a single cohort year (class of 2021). Then, instead of simple random sampling, the sample space is stratified so that the sample size for each major is around the same. Stratification ensures sufficient statistical power for group comparisons, avoiding a situation where one group in a certain industry is too small than the others. The sample size would be around 200 complete responses based on an a‑priori power analysis using $$G \cdot Power$$For an independent‑samples t‑test, with alpha = 0.05, power = 0.80, and a moderate effect size, the required total sample is roughly 102 per group (first gen or non first gen). Since I plan to run a multiple linear regression with four predictors, 100 per group ensures stable standard errors and sufficient power to detect a gap in promoteons. Restricting the sample to graduates of the UCI Class of 2021, surveyed in 2026, is critical because the dependent variable is a count of promotions. While I could add “years since graduation” as an additional control, that would still assume a linear relationship with promotions, which is unlikely (promotions cluster by times). Standardizing to exactly 5 years for every respondent removes this confound. 

## Analysis

After running descriptive statistics and a t‑test, I will estimate a linear regression where each of the variables gets an coefficient. Only the coefficient of the first gen status matters the most. In conflict‑theory terms, that coefficient captures the “net penalty” of ascribed background that cannot be explained by individual merit (GPA) or post‑graduate resources. In other words, If that coefficient is negative and statistically significant, it suggests that the stratification system continues to operate in the workplace.

### Conflict Theory

This design aligns with conflict theory because it treats the workplace promotion systems as class conflict battlefield where social capital are converted into promotions. Drawing on "Bourdieu", non‑first‑gen graduates typically enter the workforce with tacit knowledge of professional norms. First‑gen graduates, despite equal GPAs, often lack the abilities to networking properly. My design tests the core conflict proposition that ascribed status shapes life chances net of achieved status (GPA). 

## Ethical Considerations

If this research is real, it would be submitted to IRB review at UCI. All participants will view a consent form that explains the purpose, risks (minimal), and their right to skip any question or withdraw. The whole process would also be anonymous, with data safely stored in UCI servers.