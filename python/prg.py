
# Exp 1 ###############################################################
from collections import Counter

value = input("Enter a value: ")

if value == value[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

counted_dict = Counter(value)
print(counted_dict)

for key in counted_dict.keys():
    print(f'{key} appears {counted_dict[key]} times')

# EXP 2a ###############################################################
def fn(n):
    if n <= 2:
        return n - 1
    else:
        return fn(n - 1) + fn(n - 2)

try:
    num = int(input("Enter a number: "))
    if num > 0:
        print(f'fn({num}) = {fn(num)}')
    else:
        print("Input should be greater than 0")
except ValueError:
    print("Try with a numeric value")

# EXP 2b ###############################################################
def bin2Dec(val):
    return int(val, 2)

def oct2Hex(val):
    return hex(int(val, 8))

try:
    num1 = input("Enter a binary number: ")
    print(bin2Dec(num1))
except ValueError:
    print("Invalid literal in input with base 2")

try:
    num2 = input("Enter an octal number: ")
    print(oct2Hex(num2))
except ValueError:
    print("Invalid literal in input with base 8")

# 3a ###############################################################
import string

sentence = input("Enter a sentence: ")
wordList = sentence.strip().split(" ")
print(f'This sentence has {len(wordList)} words', end='\n\n')

digit_count = uppercase_count = lowercase_count = 0

for ch in sentence:
    if '0' <= ch <= '9':
        digit_count += 1
    elif 'A' <= ch <= 'Z':
        uppercase_count += 1
    elif 'a' <= ch <= 'z':
        lowercase_count += 1

print(f'This sentence has {digit_count} digits\n{uppercase_count} uppercase letters\n{lowercase_count} lowercase letters')

# 3b ###############################################################
str1 = input("Enter String 1\n").lower()
str2 = input("Enter String 2\n").lower()

string_1_length = len(str1)
string_2_length = len(str2)

short_string_length, long_string_length = min(string_1_length, string_2_length), max(string_1_length, string_2_length)

match_count = 0

for i in range(short_string_length):
    if str1[i] == str2[i]:
        match_count += 1

print("Similarity between the two strings:")
print(match_count / long_string_length)

# 4a ###############################################################
import numpy as np
import matplotlib.pyplot as plt
data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize=(10, 5))
plt.bar(courses, values, color='maroon', width=0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# 4b ###############################################################
import matplotlib.pyplot as plt
x1 = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20]
y1 = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10]
plt.scatter(x1, y1, c="pink", linewidths=2, marker="s", edgecolor="green", s=50)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 5a ###############################################################
import matplotlib.pyplot as plt
import numpy as np
data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)
plt.hist([data1, data2], bins=30, stacked=True, color=['yellow', 'green'], edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')
plt.legend(['Dataset 1', 'Dataset 2'])
plt.show()

# 5b ###############################################################
from matplotlib import pyplot as plt
import numpy as np
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.show()

# 6a ###############################################################
import matplotlib.pyplot as plt
overs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
runs_scored = [0, 7, 12, 20, 39, 49, 61, 83, 86, 97, 113, 116, 123, 137, 145, 163, 172, 192, 198, 198, 203]
plt.plot(overs, runs_scored)
plt.xlabel('Overs')
plt.ylabel('Runs scored')
plt.title('Run scoring in a T20 Cricket Match')
plt.grid(True)
plt.show()

# 6b ###############################################################
import matplotlib.pyplot as plt
overs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
runs_scored = [0, 7, 12, 20, 39, 49, 61, 83, 86, 97, 113, 116, 123, 137, 145, 163, 172, 192, 198, 198, 203]
plt.plot(overs, runs_scored, marker='X', linestyle='dashed', color='red', linewidth=2, markerfacecolor='blue', markersize=8)
plt.xlabel('Overs', color='green')
plt.ylabel('Runs scored')
plt.title('Run scoring in a T20 Cricket Match')
plt.grid(True)
plt.show()

# 7 ###############################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sinplot(n=10):
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * 5) * (n + 2 - i))
sns.set_theme()
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sinplot()
plt.title('Seaborn plots with Aesthetic functions')
plt.show()

# 8 ###############################################################
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
TOOLS = "pan, wheel_zoom, box_zoom, reset, save, box_select"
p1 = figure(title="Example 1", tools=TOOLS)
p1.circle(x, y, legend_label="sin(x)")
p1.circle(x, 2*y, legend_label="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend_label="3*sin(x)", color="green")
p1.legend.title = 'Markers'
p2 = figure(title="Example 2", tools=TOOLS)
p2.circle(x, y, legend_label="sin(x)")
p2.line(x, y, legend_label="sin(x)")
p2.line(x, 2*y, legend_label="2*sin(x)", line_dash=(4, 4), line_color="orange", line_width=2)
p2.square(x, 3*y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p2.line(x, 3*y, legend_label="3*sin(x)", line_color="green")
p2.legend.title = 'Lines'
show(gridplot([[p1, p2]], ncols=2, width=400, height=400))

# 9 ###############################################################
import plotly.express as px

df = px.data.gapminder().query("continent=='Asia'")
fig = px.line_3d(df, x="gdpPercap", y="pop", z="year", color='country', title='Economic Evolution of Asian Countries Over Time')
fig.show()

# 10a ###############################################################
import pandas as pd
import plotly.express as px

dollar_conv = pd.read_csv('CUR_DLR_INR.csv')
fig = px.line(dollar_conv, x='DATE', y='RATE', title='Dollar vs Rupee')
fig.show()

# 10b ###############################################################
import plotly.express as px
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
fig = px.choropleth(data, locations='iso_alpha', color='gdpPercap', hover_name='country', projection='natural earth', title='GDP per Capita by Country')
fig.show()











