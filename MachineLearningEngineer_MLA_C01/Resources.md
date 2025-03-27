# Resources
* Videos
    * [AWS Power hour](https://pages.awscloud.com/GLOBAL-other-T2-Traincert-Power-Hour-ML-Assoc-2024-reg.html) - 6 hours of video, one of intro, one per domain, one review, with experts.

* Basic info
    * [AWS CLA-C01 Exam guide](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)
    * [Christian Greciano's notes](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0)
* Skill builder
    * [Skillbuilder practice question set](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/13266/exam-prep-official-practice-question-set-aws-certified-solutions-architect-associate-saa-c03-english) - Free
    * [Skillbuilder practice test](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/13593/exam-prep-official-practice-exam-aws-certified-solutions-architect-associate-saa-c03-english) - Subscription required
    * [Skillbuilder basic plan](https://explore.skillbuilder.aws/learn/learning_plan/view/2198/plan) - Free
    * [Skillbuilder enhanced plan](https://explore.skillbuilder.aws/learn/learning_plan/view/2197/plan) - Subscription required
* Whitepapers
    * [Overview of AWS Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html?did=wp_card&trk=wp_card)
    * Decision guides
        * [Choosing an AWS Database service](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html)

## Sagemaker
* [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
* [Model metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-metrics.html)
    * Regression
        * MAE - Mean Absolute Error
        * MSE - Mean Squared Error
        * RMSE - Root Mean Squared Error
        * R<sup>2</sup> - R squared, Measures the proportion of variance in the dependent variable that is explained by the model. Ranges from 0-1
        * (not?) Adjusted R<sup>2</sup> - Adds penalty for extra predictors
    * Binary Classification
        * Confusion Matrix
        * Recall
        * Precision
        * Accuracy
        * Precision, Accuracy and Recall of the best constant classifier
        * True/false positive/negative rate
        * ROCC - Receiver Operating Characteristic Curve
        * Precision Recall Curve
        * AUC - Area under Curve
        * f0.5, f1, f2
        * f0.5, f1, f2 of the best constant classifier
    * Multiclass Classification
        * Confusion Matrix
        * Weighted Recall
        