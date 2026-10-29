[app]
title = 小学英语学习助手
package.name = englishstudy
package.domain = org.englishstudy

version = 1.0
version.code = 1

source.dir = .
source.include_exts = py,png,jpg,ttf,json,txt
source.exclude_patterns = __pycache__

# 重点：锁定charset_normalizer旧版本，避开不兼容新版
requirements = python3,kivy==2.3.0,plyer,charset_normalizer==2.0.4
android.build_tools = 34.0.0
android.accept_sdk_license = True
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.minapi = 24
android.debug = True
android.backends = sdl2
orientation = portrait
log_level = info

[buildozer]
log_level = 2
warn_on_root = 0

