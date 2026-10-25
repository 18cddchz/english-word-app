[app]
package.name = englishstudy
package.domain = org.english.learn

source.dir = .
source.include_exts = py,png,jpg,ttf,json
source.exclude_dirs = tests, bin, .git

# 重点修改：只保留64位，去掉armeabi-v7a！！
android.api = 33
android.ndk = 25b
android.sdk = 24
android.archs = arm64-v8a

requirements = python3,kivy,jnius

android.permissions = INTERNET,ACCESS_NETWORK_STATE
title = 小学英语点读学习

p4a.bootstrap = sdl2
p4a.source_dir =
p4a.local_recipes =

[buildozer]
log_level = 2
warn_on_root = 1
