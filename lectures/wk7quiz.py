""" main.py

Code Challenge: Selecting observations in Pandas I

"""

import pandas as pd
import numpy as np

# IMPORTANT: please do not modify this import statement
# from placeholders import put_your_answer_here


# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)



# Q1: What expression for `sel_q1` below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-14 | 0.7281  |  NaN    |

# NOTE: replace `put_your_answer_here`
sel_q1 = ["2020-09-08","2020-09-14"]
q1 = df.loc[sel_q1]
print(q1)



# Q2: What expression for `start`, `stop` below will produce a DATA FRAME with
# following output?  (first two rows of `df`)
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |

(start_q2, stop_q2) = (0, 2)
q2 = df.iloc[start_q2:stop_q2]
print(q2)

# Q3: What expression for `start`, `stop` below will produce a DATA FRAME
# with following output?  (first two rows of `df`)
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |

(start_q3, stop_q3) = (0, 2)
q3 = df[start_q3:stop_q3]
# print(q3)

# Q4: What expression for row_sel, col_sel below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD |
# +------------+---------|
# | 2020-09-08 | 0.7280  |
# | 2020-09-09 | 0.7209  |

# row_sel_q4 = ['2020-09-08','2020-09-09']
# col_sel_q4 = ['AUD/USD']
# q4 = df.loc[row_sel_q4, col_sel_q4]
#
# print(q4)
#
# print(df.loc['0':'z'])
# new_df = df.copy()
# new_df.loc['1', :] = 1
# #

print(df.loc['AUD/USD'])