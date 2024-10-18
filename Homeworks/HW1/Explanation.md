I have two model: logistic regression and decision tree classifier. I trained classifier of recid in next two years based on a COMPAS dataset.

### Model Performance:
1. **Logistic Regression (Original)**:
   - **Accuracy**: 97.51%
   - **Precision**: 94.66%
   - **Recall**: 100%
   - **F1**: 97.26%

2. **Decision Tree**:
   - **Accuracy**: 94.41%
   - **Precision**: 95.05%
   - **Recall**: 92.17%
   - **F1**: 93.59%

3. **Logistic Regression (Mitigated with bonus)**:
   - **Accuracy**: 81.02%
   - **Precision**: 94.91%
   - **Recall**: 60.33%
   - **F1**: 73.77%

### Fairness Metrics:
1. **Logistic Regression (Original)**:
   - **Demographic Parity**: 1.44
   - **Equal Opportunity**: 1.53
   - **Predictive Parity**: 1.06

2. **Decision Tree**:
   - **Demographic Parity**: 1.50
   - **Equal Opportunity**: 1.59
   - **Predictive Parity**: 1.06

3. **Logistic Regression (Mitigated)**:
   - **Bonus 0.30**: Similar to the original linear model.
   - **Bonus 0.40**: 
     - **Demographic Parity**: 1.26
     - **Equal Opportunity**: 1.35
     - **Predictive Parity**: 1.07
   - **Bonus 0.45**: 
     - **Demographic Parity**: 0.49
     - **Equal Opportunity**: 0.53
     - **Predictive Parity**: 1.08

### Summary & Trade-offs:
- **Logistic Regression** provides the highest accuracy (97.51%) and recall (100%), but its fairness metrics show bias: high values for **Demographic Parity** (1.44) and **Equal Opportunity** (1.53).
- **Decision Tree** has lower accuracy and recall than the logistic regression but similar bias levels in fairness metrics.
- **Mitigated Logistic Regression**: After applying the bonus to mitigate bias, the **fairness metrics improved**. With a bonus of 0.45, **Demographic Parity** dropped significantly (0.49), and **Equal Opportunity** also dropped (0.53), indicating the model is more fair. However, this improvement in fairness comes with a **significant trade-off in performance**, as accuracy drops to 81%, and recall drops to 60.33%.

### Conclusion:
There is a clear **trade-off between fairness and performance**. As fairness improves through mitigation, accuracy and recall degrade, especially in the mitigated logistic regression model. This shows that improving fairness often leads to reduced predictive power, particularly in terms of recall.