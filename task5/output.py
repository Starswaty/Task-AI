import os

def save_summary_to_file(summary, filename="summary.txt", folder="summaries"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(summary)
        return path
    except Exception as e:
        print(f"Failed to save summary: {e}")
        return None
