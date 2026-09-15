# Electronic Silambam Scoreboard â€” APK Build Guide

This project is a Kivy-based Android scoreboard app for Electronic Silambam matches.
Since APK building requires the Android SDK/NDK (large downloads, long build times),
this guide uses **GitHub Actions** to build the APK for free in the cloud â€”
you don't need to install anything on your own computer.

## What's in this folder

| File | Purpose |
|---|---|
| `main.py` | The Kivy app source code |
| `buildozer.spec` | Build configuration (app name, permissions, Android API level, etc.) |
| `.github/workflows/build-apk.yml` | GitHub Actions workflow that builds the APK automatically |

## Prerequisites

- A free GitHub account. Sign up at https://github.com/join if you don't have one.
- That's it â€” no Python, no Android Studio, no SDK installation needed on your machine.

## Step-by-Step Instructions

### Step 1: Create a new GitHub repository

1. Log in to https://github.com
2. Click the **+** icon (top-right) â†’ **New repository**
3. Name it something like `silambam-app`
4. Set it to **Public** or **Private** (either works)
5. Do **NOT** initialize with a README, .gitignore, or license (leave all checkboxes unchecked)
6. Click **Create repository**

### Step 2: Upload the project files

You have two options:

**Option A â€” Upload via browser (easiest, no coding tools needed)**

1. On your new empty repository page, click **"uploading an existing file"**
2. Drag and drop `main.py` and `buildozer.spec` into the upload box
3. Click **Commit changes**
4. Now you need to create the workflow file in a specific folder path:
   - Click **Add file** â†’ **Create new file**
   - In the file name box, type exactly: `.github/workflows/build-apk.yml`
     (typing the slashes will automatically create the folders)
   - Paste the contents of `build-apk.yml` into the text box
   - Click **Commit changes**

**Option B â€” Upload via Git command line (if you're comfortable with terminal)**

```bash
git clone https://github.com/YOUR_USERNAME/silambam-app.git
cd silambam-app
# copy main.py, buildozer.spec, and the .github folder into this directory
git add .
git commit -m "Add Silambam app and build workflow"
git push
```

### Step 3: Run the build

1. Go to your repository on GitHub
2. Click the **Actions** tab (top menu)
3. You should see a workflow called **"Build APK"** listed on the left
4. Click on it, then click the **Run workflow** button (dropdown on the right) â†’ **Run workflow**
5. A new run will appear in the list â€” click on it to watch the progress

### Step 4: Wait for the build

- The **first build** takes about **20â€“35 minutes** because it downloads and sets up
  the Android SDK, NDK, and all required build tools from scratch.
- Subsequent builds are usually much faster if you don't clear the cache.
- A green checkmark âœ… next to the run means the build succeeded.
- A red X âŒ means it failed â€” click into the run and expand the **Build APK** step
  to read the error log.

### Step 5: Download your APK

1. Click into the completed (green âœ…) workflow run
2. Scroll down to the **Artifacts** section at the bottom of the run summary page
3. Click **silambam-apk** to download a ZIP file
4. Extract the ZIP â€” inside you'll find your `.apk` file
5. Transfer it to your Android phone (via USB, email, Google Drive, WhatsApp, etc.)
   and tap it to install
   (you may need to enable **"Install from unknown sources"** in your phone's settings)

## Making changes later

Any time you edit `main.py` and push the change to the `main` branch, the workflow
will run automatically (because of the `push` trigger in `build-apk.yml`) and build
a fresh APK. You can also always trigger it manually from the Actions tab.

## Troubleshooting

| Problem | Likely cause / fix |
|---|---|
| Build fails at "Install buildozer" step | Usually a transient pip/network issue â€” just click **Re-run all jobs** |
| Build fails at "Build APK" step with a Cython or Kivy error | Check the log for the exact package/version error and share it â€” the `buildozer.spec` `requirements` line may need a version pin |
| APK installs but crashes immediately | Check that `android.permissions` in `buildozer.spec` covers everything the app needs (this app only needs `INTERNET` for the ESP32 WiFi feature) |
| "Install blocked" on your phone | Enable **Settings â†’ Security â†’ Install unknown apps** for the app you used to open the APK file |
| Workflow doesn't appear under Actions tab | Double-check the workflow file path is exactly `.github/workflows/build-apk.yml` (note the leading dot on `.github`) |

## Notes on this app

- **Orientation**: locked to landscape, fullscreen (set in `buildozer.spec` and in `main.py`'s `Config.set`)
- **ESP32 integration**: the app opens a TCP server on port `5005` to receive hit/penalty
  signals from ESP32 boards over WiFi â€” this is why `android.permissions = INTERNET`
  is required in `buildozer.spec`
- **Sounds**: beep sounds are synthesized at runtime (no external audio files needed)

If a build fails, copy the exact error text from the Actions log and share it â€”
the `buildozer.spec` can be adjusted to fix most dependency/version issues.
