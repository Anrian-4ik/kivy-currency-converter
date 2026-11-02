[app]
title = Конвертер валют
package.name = currencyconverter
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21

[android]
# ... другие настройки ...
android.sdk = 33
android.ndk = r28c
# ВАЖНО: оставь пустым — тогда Buildozer сам выберет совместимую версию build-tools
android.build_tools =
android.arch = arm64-v8a
p4a.branch = master
