import matplotlib.pyplot as plt
import pandas as pd

# Taakdata: startdag (relatief) en duur in dagen
tasks = [
    {"task": "Probleemdomein onderzoeken", "start": 0, "duration": 1},
    {"task": "Literatuurstudie", "start": 1, "duration": 2},
    {"task": "Data verzamelen en voorbereiden", "start": 3, "duration": 3},
    {"task": "Proof-of-Concept bouwen", "start": 6, "duration": 3},
    {"task": "Proof-of-Concept valideren", "start": 9, "duration": 3},
    {"task": "Conclusie", "start": 12, "duration": 2},
]

# DataFrame maken en eindtijd berekenen
df = pd.DataFrame(tasks)
df['end'] = df['start'] + df['duration']

# Taken sorteren op starttijd (laatste taak onderaan)
df_sorted = df.sort_values(by="start", ascending=False).reset_index(drop=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for i, row in df_sorted.iterrows():
    fase_label = f"Fase {len(df_sorted) - i}"  # Aftellend van Fase 6 tot Fase 1
    ax.barh(y=row['task'], width=row['duration'], left=row['start'],
            height=0.8, color='forestgreen', edgecolor='black')
    ax.text(row['start'] + row['duration']/2, row['task'],
            fase_label, ha='center', va='center', color='white', fontweight='bold')

# As-instellingen
ax.set_xlabel("Week")
ax.set_ylabel("Fase")
ax.set_xlim(0, max(df['end']) + 2)
ax.set_title("Planning bachelorproef (14 weken)")
ax.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

# Opslaan
plt.savefig("gantt.png", dpi=300)
plt.show()
