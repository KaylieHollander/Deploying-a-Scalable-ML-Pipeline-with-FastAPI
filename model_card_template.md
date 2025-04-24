# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- **Model Name**: XGBoost
- **Model Version**: 3.0.0
- **Model Type**: Gradient Boosting Model
- **Framework**: XGBoost
- **Date**: This model was trained on 04/23/25

## Intended Use
- **Use Case**: This model performs a binary classification on the U.S. Census data in order to predict whether someone earns more or less than $50,000 annually.
- **Target Audience**: The target audience for this project are business analysts who may use the income classification trends and insights for decision-making or to make informed business strategies.

## Training Data
- **Dataset**: The model was trained on a publicly available U.S. Census dataset that was split with 80% of the data being used to train the model and 20% being used to test it.
- **Size**: The total number of samples within the training subset is 26,048.
- **Features**: The features used to train the dataset are workclass, education, marital-status, occupation, relationship, race, sex, and native-country. 

## Evaluation Data
- **Dataset**: The model was evaluated on the remaining 20% of the data from the U.S. Census dataset that was not used to train the model as stated above.
- **Size**: The total number of samples within the evaluation subset is 6,512.
- **Features**: The features used to evaluate the model are workclass, education, marital-status, occupation, relationship, race, sex, and native-country.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
- **Precision**: 79.01%
- **Recall**: 68.05%
- **F1 Score**:73.12%

## Ethical Considerations
- **Bias**: While no biases were introduced to the model, it may still inherit biases from the training dataset. For example, if the dataset does not equally represent every demographic the results may unintentionally become lower for those underrepresented groups. Additionally, features such as "occupation" or "education" could introduce bias if certain demographic groups are overrepresented in specific job categories or education levels.
- **Fairness**: This model aims to for equal accuracy accross all groups presented in order to maintain fairness.
- **Impact**: The model has the potential to provide insights into income distribution patterns across various demographic groups through analyzing model performance on different slices of the population which can support fairer and more accountable use of machine learning. However, care must still be taken to ensure that the model is not used for decisions that could negatively impact individuals without human oversight. 

## Caveats and Recommendations
- **Limitations**: The main limitation of this model is its feature dependence since it relies heavily on the features within the dataset being relevant and related to making predictions. If features that are not relevant or related are introduced it would diminish the model's accuracy.
- **Recommendations for Use**: Given the potential for biases within the predictions produced it is highly recommended that any decision made with the findings be paired with human judgment and thorough review to ensure fairness.
- **Future Work**: One feature that I would like to implement in a future version would be a user feedback loop. This loop will allow users to report inaccuracies or concerns about the model's predictions. With this feedback, it will be possible to spot any biases that may be present which will lead to more accurate and fair predictions.





