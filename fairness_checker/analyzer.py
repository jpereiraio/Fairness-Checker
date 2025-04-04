from aif360.datasets import StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric
from datetime import datetime

class FairnessAnalyzer:
    def __init__(self, protected_attrs):
        self.protected_attrs = protected_attrs

    def analyze(self, df, reference_df):
        df = df[reference_df.columns]
        dataset = StandardDataset(df, protected_attribute_names=self.protected_attrs,
                                   label_name="label", favorable_classes=[1])
        metric = BinaryLabelDatasetMetric(dataset, 
                    unprivileged_groups=[{attr: 0 for attr in self.protected_attrs}],
                    privileged_groups=[{attr: 1 for attr in self.protected_attrs}])

        return {
            'disparate_impact': metric.disparate_impact(),
            'mean_difference': metric.mean_difference(),
            'timestamp': datetime.utcnow().isoformat()
        }

