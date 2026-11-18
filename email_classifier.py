"""
SWYNEX Internship - Task 2: Model or API Integration
Customer Support Email Classifier (prototype)

This prototype uses the scikit-learn library (TF-IDF + Naive Bayes model)
to sort customer support emails into 4 categories:
Billing, Technical Issue, Refund / Cancellation, General Inquiry.

No API key is needed, so no secret keys are included in this project.

How to run:
    pip install -r requirements.txt
    python email_classifier.py                      (runs the demo)
    python email_classifier.py "Your email text"    (classifies your own email)
"""

import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# ---------------------------------------------------------------------------
# 1. Small sample dataset (written by hand for this
