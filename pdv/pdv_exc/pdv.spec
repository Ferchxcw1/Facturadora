# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

a = Analysis(['C:\\Users\\Crytex\\Dev\\pdv\\dpv\\main.py'],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=[],
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=0,
)
pyz = PYZ(a.pure)        

exe = EXE(pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pdv',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(exe, Tree('C:\\Users\\Crytex\\Dev\\pdv\\dpv\\'),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pdv',)
