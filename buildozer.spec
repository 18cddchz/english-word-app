[app]

# 包名，不要中文
package.name = englishstudy
package.domain = org.englishstudy

source.dir = .
source.include_exts = py,png,jpg,ttf,json,txt
source.exclude_dirs = tests, bin, venv, .git

# 版本号，每次更新可以改
version = 0.1

requirements = python3,kivy==2.3.0,plyer,charset_normalizer==2.0.4
python = 3.11

# 只打包64位，避开32位编译一堆坑
android.archs = arm64-v8a

# 安卓权限（TTS朗读需要）
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO
android.api = 33
android.ndk = 25b
android.sdk = 24

# 关闭没用的东西，减少编译报错
android.enable_androidx = True
android.gradle_dependencies = 
android.add_jars = 
android.add_aars = 

# 全屏、横屏竖屏，你这个学习软件竖屏
orientation = portrait
fullscreen = 0

# 图标，没有图标也没关系，会自动生成
icon.filename = 

# 日志
log_level = 2

# 不要自动升级python版本
p4a.bootstrap = sdl2
p4a.local_recipes = 
p4a.branch = master

# 清理缓存相关
buildozer.debug = True
