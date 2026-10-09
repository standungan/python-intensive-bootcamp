import sys, os, importlib
sys.path.insert(0, os.path.dirname(__file__))
from lib import page
OUT = os.path.join(os.path.dirname(__file__), '..')
DECKS = [
    (0, 'd0', 'hari0-setup-lingkungan', 'Persiapan Lingkungan', '#fbbf24', '#b7791f'),
    (1, 'd1', 'hari1-python-fundamentals', 'Python Fundamentals', '#38bdf8', '#0b7bbd'),
    (2, 'd2', 'hari2-functions-modules-file-handling', 'Functions, Modules & File Handling', '#34d399', '#0f8f63'),
    (3, 'd3', 'hari3-oop', 'Object-Oriented Programming', '#a78bfa', '#6d4fd1'),
    (4, 'd4', 'hari4-numpy-pandas', 'NumPy & Pandas', '#fb923c', '#c2570c'),
    (5, 'd5', 'hari5-visualisasi-api-scraping', 'Visualisasi, API & Scraping', '#f472b6', '#b3306b'),
    (6, 'd6', 'hari6-capstone-project', 'Capstone Project', '#2dd4bf', '#0f8b7d'),
]
only = {int(a) for a in sys.argv[1:]} or None
for day, mod, fn, title, acc, accl in DECKS:
    if only and day not in only: continue
    try: m = importlib.import_module(mod)
    except ModuleNotFoundError: continue
    s = m.build()
    open(os.path.join(OUT, fn + '.html'), 'w', encoding='utf-8').write(page(day, title, s, acc, accl))
    print(f'Hari {day}: {len(s)} slide -> {fn}.html')
