# Piscine Python

Exercices d’introduction à Python (structures de données, I/O, CLI, packaging, et utilitaires).

## Prérequis

- Python ≥ 3.10
- Linux
- (Optionnel) Environnement virtuel :
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  ```

## Structure et usage

### ex00 — Hello.py
- Manipulation de listes, tuples, sets, dictionnaires.
- Exécution :
  ```bash
  python3 ex00/Hello.py
  ```

### ex01 — format_ft_time.py
- Affiche les secondes depuis l’époque Unix et la date courante, avec formatage.
- Exécution :
  ```bash
  python3 ex01/format_ft_time.py
  ```

### ex02 — find_ft_type.py
- Détection du type d’un objet et affichage personnalisé, retourne toujours 42.
- Exemple d’utilisation dans un REPL :
  ```python
  from ex02.find_ft_type import all_thing_is_obj
  all_thing_is_obj([1, 2])
  ```

### ex03 — NULL_not_found.py
- Classification des « valeurs nulles »: None, NaN, False, 0, '' avec message dédié.
- Exemple :
  ```python
  from ex03.NULL_not_found import NULL_not_found
  NULL_not_found(None)
  ```

### ex04 — Whatis.py
- Script CLI qui vérifie qu’un argument est un entier et affiche pair/impair.
- Exécution :
  ```bash
  python3 ex04/Whatis.py 42
  ```

### ex05 — building.py
- Compte des catégories de caractères dans un texte (upper, lower, digits, spaces, punctuation).
- Exécution avec argument :
  ```bash
  python3 ex05/building.py "Hello, World! 42"
  ```
- Ou en mode prompt (argument "None" ou sans argument) :
  ```bash
  python3 ex05/building.py None
  ```

### ex06 — ft_filter.py, filterstring.py
- ft_filter: réimplémentation simple de filter en compréhension de liste.
- filterstring.py: filtre les mots d’une chaîne selon une longueur minimale.
- Exécution :
  ```bash
  python3 ex06/filterstring.py "un deux trois quatre" 4
  ```

### ex07 — sos.py
- Encode une chaîne en code Morse via un dictionnaire de correspondances.
- Exécution :
  ```bash
  python3 ex07/sos.py "SOS 42"
  ```

### ex08 — Loading.py (+ comparaison tqdm)
- ft_tqdm: barre de progression minimaliste en console.
- Test avec comparaison à la librairie tqdm :
  ```bash
  source .venv/bin/activate
  python -m pip install tqdm
  python3 ex08/test.py
  ```

### ex09 — ft_package (packaging)
- Petit package `ft_package` exposant `count_in_list`.
- Contenu :
  - `ft_package/count_in_list.py`
  - `ft_package/__init__.py`
  - `README.md`, `LICENSE`, `python.toml` (métadonnées projet)
- Construction (si vous utilisez pyproject/build) :
  ```bash
  cd ex09
  python -m pip install build
  python -m build
  ```
- Installation depuis l’archive (exemple) :
  ```bash
  pip install ./ex09/dist/ft_package-0.0.1.tar.gz
  ```
- Utilisation :
  ```python
  from ft_package import count_in_list
  print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
  ```

## Divers

- Les fichiers temporaires et tests sont ignorés via `.gitignore` (ex: `.venv`, `__pycache__`, `test.py`).
- Les scripts CLI gèrent les erreurs via `AssertionError` et messages explicites.
