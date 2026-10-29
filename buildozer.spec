[app]
title = 英语学习
package.name = englishstudy
package.domain = org.englishstudy

source.dir = .
source.include_exts = py,png,jpg,jpeg,json,txt
source.exclude_dirs = tests, bin, venv, .git

version = 0.1

requirements = python3,kivy==2.2.1,plyer,charset_normalizer==2.0.4
python = 3.10

android.archs = arm64-v8a

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.ndk = 25b
android.sdk = 33
# 自动同意SDK协议，GitHub Actions无人打包必备
android.accept_sdk_license = True

android.enable_androidx = True
android.gradle_dependencies =
android.add_jars =
android.add_aars =

orientation = portrait
fullscreen = 0

icon.filename =

log_level = info
