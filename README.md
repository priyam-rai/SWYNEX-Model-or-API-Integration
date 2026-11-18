# SWYNEX Model or API Integration: Customer Support Email Classifier

This is the Task 2 prototype for the SWYNEX AI Internship. It builds on the problem defined in Task 1 (AI Problem Design): sorting customer support emails into categories so support teams can respond faster.

## What it does

The prototype reads a customer email and predicts one of four categories:

- Billing
- Technical Issue
- Refund / Cancellation
- General Inquiry

## How it works

The project uses the **scikit-learn** library:

1. **TF-IDF** turns the email text into numbers (it gives more weight to important words).
2. A **Multinomial Naive Bayes** model learns from labelled sample emails and predicts the category.
3. The model also gives a confidence score for its prediction.

No external AI API is used, so **no API keys are needed** and no secret keys are stored in this repository.

## Files

- `email_classifier.py`: the full prototype (data, model and demo)
- `requirements.txt`: the library needed to run it
- `README.md`: this file

## How to run

```
pip install -r requirements.txt
python email_classifier.py
```

To classify your own email:

```
python email_classifier.py "I cannot reset my password"
```

## Example inputs and outputs

These results come from running the script.

| Input email | Predicted category | Confidence |
|---|---|---|
| Hi, I was charged twice this month. Please check my payment. | Billing | 45% |
| The app crashes whenever I try to open my profile. | Technical Issue | 41% |
| I want to cancel my order and get a refund. | Refund / Cancellation | 57% |
| Do you offer any discount for new customers? | General Inquiry | 47% |
| I cannot reset my password | Technical Issue | 33% |

On the 12 held-out test emails, the model got all of them right (100% accuracy).

## Limitations

- The dataset is **very small** (40 training emails and 12 test emails, written by hand for this demo), so 100% accuracy on 12 emails does not prove the model is reliable on real emails.
- Confidence scores are low because there is little training data.
- Emails that mention two issues at once (for example billing and refund) can be misclassified.
- It only supports English.

## Next steps

- Train on a larger real dataset (300 to 500 emails or more) to reach the Task 1 goal of 85%+ accuracy.
- Compare with an AI API or a language model.
- Add a simple web page where a user can paste an email and see the result.
