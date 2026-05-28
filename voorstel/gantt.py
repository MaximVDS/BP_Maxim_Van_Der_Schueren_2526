import matplotlib.pyplot as plt
import pandas as pd

# Taakdata: startdag (relatief) en duur in dagen
tasks = [
    {"task": "Probleemdomein onderzoeken", "start": 0, "duration": 1, "color": "#2196A6"},
    {"task": "Literatuurstudie", "start": 1, "duration": 2, "color": "#9C2C77"},
    {"task": "Data verzamelen en voorbereiden", "start": 3, "duration": 3, "color": "#E07B00"},
    {"task": "Proof-of-Concept bouwen", "start": 6, "duration": 3, "color": "#5A8A00"},
    {"task": "Proof-of-Concept valideren", "start": 9, "duration": 3, "color": "#6A4C9C"},
    {"task": "Conclusie", "start": 12, "duration": 2, "color": "#B22222"},
]

# DataFrame maken en eindtijd berekenen
df = pd.DataFrame(tasks)
df['end'] = df['start'] + df['duration']

# Taken sorteren op starttijd (laatste taak onderaan)
df_sorted = df.sort_values(by="start", ascending=False).reset_index(drop=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for i, row in df_sorted.iterrows():
    fase_label = f"Fase {len(df_sorted) - i}"
    ax.barh(y=row['task'], width=row['duration'], left=row['start'],
            height=0.8, color=row['color'], edgecolor='black')
    ax.text(row['start'] + row['duration']/2, row['task'],
            fase_label, ha='center', va='center', color='white', fontweight='bold')

    # Week label fix
    start_week = row['start'] + 1
    end_week = row['end']
    if start_week == end_week:
        week_label = f"Week {start_week}"
    else:
        week_label = f"Week {start_week}–{end_week}"
    ax.text(row['end'] + 0.1, row['task'],
            week_label, ha='left', va='center', fontsize=9)

# As-instellingen
ax.set_xlabel("Week")
ax.set_ylabel("Fase")
ax.set_xlim(0, max(df['end']) + 2)
ax.set_title("Planning bachelorproef (14 weken)")
ax.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

# Opslaan
plt.savefig("img/gantt.png", dpi=300)
plt.show()