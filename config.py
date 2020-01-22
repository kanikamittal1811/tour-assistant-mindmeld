# The namespace of the application. Used to prevent collisions in supporting services across
# applications. If not set here, the app's enclosing directory name is used.
# APP_NAMESPACE = 'app-name'

# An example decision tree model for intent classification
INTENT_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'dtree'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'max_features': ['log2', 'sqrt', 0.01, 0.1]
        },
    },
    "features": {
        "exact": {},
    }
}

DOMAIN_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'logreg'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'fit_intercept': [True, False],
            'C': [10, 100, 1000, 10000, 100000]
        },
    },
    'features': {
        "bag-of-words": {
            "lengths": [1, 2]
        },
        "edge-ngrams": {"lengths": [1, 2]},
        "in-gaz": {},
        "exact": {"scaling": 10},
        "gaz-freq": {},
        "freq": {"bins": 5}
    }
}






"""
# Fill in the other model configurations if necessary
# ENTITY_RECOGNIZER_CONFIG = {}
# ROLE_CLASSIFIER_CONFIG = {}
"""

# A example configuration for the parser
"""
# *** Note: these are place holder entity types ***
PARSER_CONFIG = {
    'grandparent': {
        'parent': {},
        'child': {'max_instances': 1}
    },
    'parent': {
        'child': {'max_instances': 1}
    }
}
"""
