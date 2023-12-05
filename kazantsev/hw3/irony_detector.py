from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
from scipy.special import softmax

class IronyDetector:
    """Класс в котором инкапсулирована логика по настройке и использованию модели"""
    
    @classmethod
    def init(self):
        model_id = "cardiffnlp/twitter-roberta-base-irony"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id)

    @classmethod
    def analyze(self, text_to_detect: str):
        labels=["non-irony", "irony"]
        encoded_input = self.tokenizer(text_to_detect, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        rslt = []
        for i in range(scores.shape[0]):
            l = labels[ranking[i]]
            s = scores[ranking[i]]
            message = f"{l} {np.round(float(s), 3) * 100}%"
            rslt.append(message)
        return rslt