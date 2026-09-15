[app]
title = Electronic Silambam
package.name = silambam
package.domain = org.silambam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
version = 1.0

requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
