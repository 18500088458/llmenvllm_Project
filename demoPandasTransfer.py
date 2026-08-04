import pandas as pd
import numpy as np

s = pd.Series([5,4,7,np.nan,8,5,6,7])
print(f"apply:{s.apply(lambda x: x**2)}")
print(f"map:{s.map({5:66, 7:99})}")
print(f"replace:{s.replace({5:66, 7:99})}")


