# Project 2: Persuasive or Deceptive Visualization?

## Project Overview
This project explores the ethical boundaries between persuasive and deceptive data visualization using World Bank climate change data (CO2 emissions, 1960-2020).

**Proposition:** "Developed countries are leading the fight against climate change through significant reductions in CO2 emissions."

## Files Included
- `index.html` - Main project webpage
- `viz1_supporting.png` - Visualization supporting the proposition
- `viz2_supporting.png` - Visualization supporting the proposition
- `viz1_opposing.png` - Visualization opposing the proposition
- `viz2_opposing.png` - Visualization opposing the proposition
- `climate-change.csv` - Source data from World Bank
- `create_visualizations.py` - Script to generate checkpoint PDF
- `export_images.py` - Script to export visualization images

## Deployment Instructions (GitHub Pages)

### Option 1: Deploy to existing portfolio (recommended)
1. Copy these files to a subdirectory in your existing portfolio repo (e.g., `proj2/`)
2. Push to GitHub:
   ```bash
   git add .
   git commit -m "Add Project 2 submission"
   git push
   ```
3. Access at: `https://[username].github.io/[repo-name]/proj2/`

### Option 2: Create new repository
1. Create a new repository on GitHub (e.g., `data-viz-proj2`)
2. Initialize git in this directory:
   ```bash
   git init
   git add index.html viz*.png README.md
   git commit -m "Initial commit: Project 2"
   git branch -M main
   git remote add origin https://github.com/[username]/[repo-name].git
   git push -u origin main
   ```
3. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Under "Source", select "main" branch and "/" (root)
   - Click Save
4. Access at: `https://[username].github.io/[repo-name]/`

## Local Testing
To view the page locally before deploying:
```bash
# Using Python's built-in server
python -m http.server 8000

# Then open in browser: http://localhost:8000
```

## Data Source
World Bank Climate Change Indicators Dataset (1960-2020)
- Repository: https://github.com/light-and-salt/World-Bank-Data-by-Indicators
- Indicator: CO2 emissions (metric tons per capita)
- Countries analyzed: 10 developed nations vs. 10 developing nations

## Key Findings
The project demonstrates that:
- Visual design choices exist on a spectrum from earnest to deceptive
- Even "truthful" techniques involve strategic rhetorical choices
- The most effective persuasion combines transparent structural choices with subtle interpretive framing
- Ethical visualization requires transparency about choices made, not absence of persuasion

