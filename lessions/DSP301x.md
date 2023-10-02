# Flowchart for Data Scientist by John Rollins from IBM
<!--TODO: fix markdown lsp...-->

## 10 questions to answers from John Rollins
### Business Understanding
1. What is the questions that we need to solve?
### analytic approach
2. Explain the relationship between the questions and how data-driven method can be used to solve it.
### Working with data
3. Which data should you use to answer the questions?
4. What is the required data source we need to obtain? How should we obtain it? 
5. Does the data we obtained solve the big problems/questions that we planned above?
6. What should we used to interact and work with the data we collected above?

### Follow up
7. What data visualization should we use?
8. The model we planning to use can answer the question? Is there any parameter should we used?
9. Can the model be used in practical / real life situation?
10. Does we have a good framework to receive feedback to optimize our answer more?

- This is the pseudo flowchart
Business Understanding -> analytic approach -> Data Requirement <-> Data Collection <-> Data Understanding -> Data preparation (loop back to Data Collection) <-> Modeling <-> Evaluation -> Deployment -> Feedback (loop back to Modeling)

## Business Understanding and analytic approach
- Clarity on the questions/problem. Typically it is to either improve the efficiency or increase the profit of a business. => We need to really understand the goal of the person asking the question
  - Case study: Best way to maximize usage in heart disease care. Mainly about Readmission in heart disease and the company need to use its own assets to cover -> Raising rate for all customer
  - Provide quality care without increasing costs -> identify the inefficiencies
  - Need to see the sponsor's involvement
- How can we use data to answer the question
  - The model should be predict outcome Y or N for each patient (re-admission) (risk)
  - What are the cause of the events that lead to the predicted/model outcome for each patients
  - Need to be easy to input and use the model to predict the readmission risk
  <!--TODO:-->
  - (Food for thought): This can apply the Logistic Regression model as well.

  ### analytic approach
  - Approaches:
  1. Descriptive: Describe the current status
  2. Diagnostic (Statistical Analysis): What happened? Why?
  3. Predictive (Forecasting): What if this trend continue, what will happen next
  4. Prescriptive: How do we solve it?

  - Types of questions:
    - Determine probabilities of an action: Use a predictive model
    - Show relationship: descriptive model
    - Yes/no answer: classification model
    - Human behavior: clustering association approaches

  - Machine learning: Incorporated new data without being explicitly programmed
  - Decision tree: categorical outcome, with explicit decision path and each nodes represent a feature
    - Leaf node is the final outcome
    - Root node is the initial
    - Split node in between

## Data Requirement and Data Collection
  ### Data Requirements
    - Define the data content
      - For example the inpatient, which can help us access information
    - Define the data formats
      - Table, which columns represent a feature and patient
    - Define the data sources

  ### Data Collection

  Kaggle
