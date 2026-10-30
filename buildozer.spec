[app]
title = 英语学习

package.name = englishstudy
package.domain = org.englishstudy
source.dir = .
source.include_exts = py,png,jpg,ttf,json
version = 0.1

requirements = python3,kivy==2.2.1,plyer

python_version = 3.11

android.api = 33
android.ndk = 25b
android.sdk = 24
android.ndk_path =
android.sdk_path =
android.archs = arm64-v8a

android.permissions = INTERNET,RECORD_AUDIO
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
