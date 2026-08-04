import pandas as pd
import numpy as np

s = pd.Series([5,6,7,np.nan,8,5,6,7])
print(f"源s:{s}");

clears_s = s.dropna();
print(f"删除缺失值clears_s:{clears_s}");

fill_s = s.fillna(0);
print(f"填充缺失值fill_s:{fill_s}");

fill_s_forward = s.ffill();
print(f"前向填充缺失值fill_s_forward:{fill_s_forward}"); #na的前一个值

fill_s_backward = s.bfill();
print(f"反向填充缺失值fill_s_backward:{fill_s_backward}"); #na的后一个值

dup_s = s.drop_duplicates()
print(f"删除重复值\n{dup_s}")


#按键取值——安全取值
v = s.get('10',-1)
print(f"v:{v}")

