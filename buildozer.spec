[app]

# (str) Title of your application
title = Electronic Silambam

# (str) Package name
package.name = silambam

# (str) Package domain (needed for android packaging)
package_domain = org.silambam

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Customized icon, any
#icon.filename = %(source.dir)s/data/icon.png

# (str) Customized splash screen, any
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, Should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.ndk = 25b

# (str) Android SDK Build-tools version
android.build_tools_version = 33.0.0

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then skip trying to update the android sdk
# This can be useful to avoid interactive prompts during builds
android.skip_update = False

# (bool) Automatically accept Android SDK license to fix CI/CD and GitHub Actions build errors
android.accept_sdk_license = True

# (bool) If True, then allow backup of data in app
android.allow_backup = True

[buildozer]

# (int) Log level: (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if run as root (0 = False, 1 = True)
warn_on_root = 1
