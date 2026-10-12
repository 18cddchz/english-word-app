[app]
# 应用基础信息
package.name = englishword
package.domain = org.englishword
source.dir = .
source.include_exts = py,png,jpg,ttf,json
source.include_patterns = assets/*,images/*

# 应用版本
version = 0.1

# 依赖库
requirements = python3,kivy

# 安卓配置
android.add_assets = DroidSansFallback.ttf
android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 34.0.0
android.archs = arm64-v8a

# 应用界面
orientation = portrait
fullscreen = 0

# 应用名称（手机桌面显示的名字）
title = 小学英语单词练习

# 图标(暂时不用可以留空，后续想加图片再填)
icon.filename = 

# 打包日志
log_level = 2

[buildozer]
# 调试日志
log_level = 2



