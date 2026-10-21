import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = sns.load_dataset('exercise')
df.head()

Running = df.loc[df['kind']=="running"]

#2 Creating Data frames
Pulse_Reading = Running.loc[
    Running['time']=="1 min",
    ['id','pulse']
]

Thirty_minutes = Running.loc[
    Running['time']=="30 min",
    ['id','pulse']
]

#3 Merging and sorting
Merging = Pulse_Reading.merge(Thirty_minutes,on='id',suffixes= ("_1_minute","_30_minutes"))
#Suffixes adds extended name to column name
print("Fitness Merge Data:",Merging)

Merging["pulse_progress"]= (Merging['pulse_30_minutes']-Merging['pulse_1_minute'])
print("Print Progress: ",Merging)

Merging = Merging.sort_values('pulse_progress',ascending=False)
print("Sorted Fitness Data: ",Merging)

#4 Creating dictionary
participant_names = [
    "Participant" + str(participant_id) 
     for participant_id in Merging['id']
]

fitness_data = {
    "Participant": participant_names,
    "pulse_1_minute": Merging["pulse_1_minute"].tolist(),
    "pulse_30_minutes": Merging ["pulse_30_minutes"].tolist()
}

chart_df = pd.DataFrame(fitness_data)
print("Chart Data: ",chart_df)

#5 Creating bar plot

positions = np.arange(len(chart_df["Participant"]))

bar_width = 0.35

plt.figure(figsize= (12,7))

one_minute_bar = plt.bar(
    positions  - bar_width / 2,
    chart_df["pulse_1_minute"],
    width= bar_width,
    label="After_1_min"
)

thirty_minutes_bar = plt.bar(
    positions  + bar_width / 2,
    chart_df["pulse_30_minutes"],
    width= bar_width,
    label="After_30_mins"
)

plt.title("Fitness charts")
plt.xlabel("Participant")
plt.ylabel("Pulse Rate")

plt.xticks(positions,chart_df["Participant"],rotation=45)
plt.legend()

#6 Label The bars

for bar in one_minute_bar:
    value = bar.get_height()
    plt.annotate(
        str(value),
        (bar.get_x() + bar.get_width() / 2, value),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center"
    )

for bar in thirty_minutes_bar:
    value = bar.get_height()
    plt.annotate(
        str(value),
        (bar.get_x() + bar.get_width() / 2, value),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center"
    )

plt.tight_layout()
plt.show()



