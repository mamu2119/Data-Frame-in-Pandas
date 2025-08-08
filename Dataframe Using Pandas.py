import pandas as pd
import numpy as np
exam_data = {'name': ['Ansh', 'Krish', 'Krishnaraj', 'Saumayaraj', 'Shauryaraj', 'Rahil', 'Garg', 'Meet', 'Devarsh', 'Marmik'],
             'score': [18, np.nan, 18, 16, np.nan, 18.5, 16, 15, 17, 19],
             'attempts':[1, 2, 2, 3, 4, 2, 4, 3, 2, 1],
             'qualify':['yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df)
print(df.info())