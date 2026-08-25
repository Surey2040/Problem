import json
import os
import random

PROBLEMS_FILE = 'problems.json'
PUSHED_FILE = 'pushed_problems.txt'
OUTPUT_DIR = 'solutions'

def main():
    if not os.path.exists(PROBLEMS_FILE):
        print(f"Error: {PROBLEMS_FILE} not found.")
        return

    with open(PROBLEMS_FILE, 'r') as f:
        problems = json.load(f)

    pushed = set()
    if os.path.exists(PUSHED_FILE):
        with open(PUSHED_FILE, 'r') as f:
            pushed = set(line.strip() for line in f)

    available = [p for p in problems if p['title'] not in pushed]

    if not available:
        print("All problems have been pushed! Time to add more to problems.json")
        return

    selected = random.choice(available)
    title = selected['title']
    code = selected['code']

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = title.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '') + '.py'
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, 'w') as f:
        f.write(f'# Problem: {title}\n')
        f.write(f'# Difficulty: {selected.get("difficulty", "Unknown")}\n\n')
        f.write(code + '\n')

    with open(PUSHED_FILE, 'a') as f:
        f.write(title + '\n')

    print(f"Successfully generated solution for: {title}")

if __name__ == '__main__':
    main()
