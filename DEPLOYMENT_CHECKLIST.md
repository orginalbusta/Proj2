# Project 2 - Final Submission Checklist

## ✅ Pre-Deployment Checklist

### Required Files (All Present ✓)
- [x] `index.html` - Main project webpage
- [x] `viz1_supporting.png` - First supporting visualization
- [x] `viz2_supporting.png` - Second supporting visualization
- [x] `viz1_opposing.png` - First opposing visualization
- [x] `viz2_opposing.png` - Second opposing visualization

### Content Requirements (All Included ✓)
- [x] Proposition statement clearly stated
- [x] Two visualizations supporting the proposition
- [x] Two visualizations opposing the proposition
- [x] 3-5 design decisions for each visualization set
- [x] Scores (-2 to +2 scale) for each design decision
- [x] 2-3 sentence rationale for each decision
- [x] 2-3 paragraph final reflection
- [x] Data source citation

## 📤 Deployment Steps

### Step 1: Choose Deployment Location
Pick one of these options:

**Option A: Add to existing portfolio** (Recommended)
- Navigate to your existing portfolio repository
- Create a `proj2` or `project-2` subdirectory
- Copy all required files to that directory

**Option B: Create new repository**
- Create new repo on GitHub (e.g., `data-viz-project-2`)
- Initialize in this directory

### Step 2: Deploy to GitHub Pages

If adding to existing portfolio:
```bash
cd /path/to/your/portfolio
mkdir proj2
cp /path/to/Proj2/index.html proj2/
cp /path/to/Proj2/viz*.png proj2/
git add proj2/
git commit -m "Add Project 2: Persuasive/Deceptive Visualization"
git push
```

If creating new repository:
```bash
# From this directory (F:\209r\Proj2)
git init
git add index.html viz*.png README.md
git commit -m "Project 2: Persuasive or Deceptive Visualization"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

Then enable GitHub Pages:
1. Go to repository Settings
2. Navigate to "Pages" in left sidebar
3. Under "Source", select "main" branch
4. Select "/" (root) or "/docs" depending on your setup
5. Click "Save"
6. Wait 1-2 minutes for deployment

### Step 3: Verify Deployment
- [ ] Visit your GitHub Pages URL
- [ ] Verify proposition is visible
- [ ] Check all 4 images load correctly (no broken images)
- [ ] Verify design decisions are readable
- [ ] Check reflection paragraphs display properly
- [ ] Test on mobile/different screen sizes
- [ ] Verify data source link works

### Step 4: Submit
- [ ] Copy your final GitHub Pages URL
- [ ] Submit URL on Canvas or required platform
- [ ] Double-check submission deadline (Fri Oct 24, 11:59pm)

## 🔗 Your URLs

Fill in once deployed:

**GitHub Repository:** `https://github.com/YOUR-USERNAME/YOUR-REPO`

**Live GitHub Pages URL:** `https://YOUR-USERNAME.github.io/YOUR-REPO/`
(or `https://YOUR-USERNAME.github.io/YOUR-REPO/proj2/` if subdirectory)

## ⚠️ Common Issues

### Images not loading
- Ensure image filenames match exactly (case-sensitive on Linux/Mac)
- Check that images are in the same directory as index.html
- Verify file paths in HTML don't have extra `/` or `./`

### Page not updating after push
- Wait 1-2 minutes for GitHub Pages to rebuild
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check GitHub Actions tab for build status

### 404 Error
- Verify GitHub Pages is enabled in repository settings
- Check you're using the correct branch (main vs. master)
- Ensure index.html is in the root or specified folder

## 📋 Submission Notes

**What to submit:** Just the public URL to your deployed webpage

**Format:** Something like `https://yourusername.github.io/portfolio/proj2/`

**Deadline:** Friday, October 24, 2025 by 11:59pm

**Note:** The checkpoint PDF was due earlier and doesn't need to be resubmitted

