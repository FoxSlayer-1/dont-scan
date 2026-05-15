name: Update Wordle

on:
  schedule:
    - cron: '0 5 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install libraries
        run: pip install requests beautifulsoup4

      - name: Run updater
        run: python update.py

      - name: Commit changes
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add .
          git commit -m "Daily update" || echo "No changes"
          git push
