[app]

# 包名，不要中文、空格
package.name = englishstudy
package.domain = org.englishstudy

# 版本号
version = 1.0
version.code = 1

# 入口文件
source.dir = .
source.include_exts = py,png,jpg,ttf,json,txt
source.exclude_patterns = __pycache__

# 依赖
requirements = python3,kivy,plyer
# 固定build-tools到34.0.0，避开37许可弹窗问题
android.build_tools = 34.0.0
android.accept_sdk_license = True
android.sdk_path =
android.ndk = 25b
android.ndk_path =

# 只打包64位，减少编译报错
android.archs = arm64-v8a

# 应用设置
android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.minapi = 24
android.debug = True
android.wakelock = False
android.backends = sdl2

# 图标（没有图标也能打包，不影响）
icon.filename = icon.png

# 方向
orientation = portrait

# 日志
log_level = info

[buildozer]
log_level = 2
warn_on_root = 0
