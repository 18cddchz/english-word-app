[app]

# 应用包名，只能小写字母数字，不能中文
package.name = englishstudy
package.domain = org.english

# 应用名称（手机桌面显示名字，可以中文）
title = 小学英语学习

# 源码入口文件
source.dir = .
source.include_exts = py,png,jpg,ttf

# 版本
version = 0.1

# 依赖库
requirements = python3,kivy

# Android版本关键配置（已经改成34构建工具，和yml配套！！不要改数字）
android.api = 33
android.ndk = 25b
android.build_tools_version = 34.0.0

# 打包带上字体文件 DroidSansFallback.ttf
android.add_assets = DroidSansFallback.ttf

# 权限
android.permissions = INTERNET,RECORD_AUDIO

# 关闭多余功能，减少打包出错
android.enable_androidx = True
android.use_python_for_android = True

# 方向：竖屏
orientation = portrait

# 不开启全屏（状态栏保留）
fullscreen = 0

# log日志
log_level = 2

# 禁止自动更新buildozer，防止版本变动报错
buildozer.autoupdate = False

# 清除缓存开关
buildozer.clean = False

# 不要自动下载SDK，我们在yml里提前手动下载好
p4a.sdk_dir = %(source.dir)s/.buildozer/android/platform/android-sdk

[buildozer]
# 日志等级
log_level = 2
warn_on_root = 1




