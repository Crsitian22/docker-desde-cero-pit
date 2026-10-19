import openpyxl
import re
import csv

aiken_path = r"c:\Users\crist\Downloads\Docker\GUIAS_11VA_EDICION\moodle_aiken\Quiz_Sesiones_1_a_4_Aiken.txt"
excel_path = r"c:\Users\crist\Downloads\Docker\GUIAS_11VA_EDICION\moodle_aiken\Quiz_Sesiones_1_a_4_Quizizz.xlsx"
csv_path = r"c:\Users\crist\Downloads\Docker\GUIAS_11VA_EDICION\moodle_aiken\Quiz_Sesiones_1_a_4_Quizizz.csv"

with open(aiken_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

questions = []
cur_q = None

for line in lines:
    if not line:
        continue
    if line.startswith("ANSWER:"):
        ans_letter = line.replace("ANSWER:", "").strip().upper()
        mapping = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
        if cur_q:
            cur_q["correct_answer"] = mapping.get(ans_letter, 1)
            questions.append(cur_q)
            cur_q = None
    elif re.match(r"^[A-E]\.\s+", line):
        opt_text = re.sub(r"^[A-E]\.\s+", "", line).strip()
        if cur_q:
            cur_q["options"].append(opt_text)
    else:
        if cur_q is None:
            cur_q = {"question": line, "options": [], "correct_answer": 1}
        else:
            cur_q["question"] += " " + line

print(f"Total questions parsed: {len(questions)}")

# Create Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Quizizz"

headers = [
    "Question Text",
    "Question Type",
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    "Option 5",
    "Correct Answer",
    "Time in seconds",
    "Image Link"
]
ws.append(headers)

rows = []
for q in questions:
    opts = q["options"]
    opt1 = opts[0] if len(opts) > 0 else ""
    opt2 = opts[1] if len(opts) > 1 else ""
    opt3 = opts[2] if len(opts) > 2 else ""
    opt4 = opts[3] if len(opts) > 3 else ""
    opt5 = opts[4] if len(opts) > 4 else ""
    
    row = [
        q["question"],
        "Multiple Choice",
        opt1,
        opt2,
        opt3,
        opt4,
        opt5,
        q["correct_answer"],
        45,
        ""
    ]
    ws.append(row)
    rows.append(row)

wb.save(excel_path)
print(f"Saved Excel to {excel_path}")

with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
print(f"Saved CSV to {csv_path}")
