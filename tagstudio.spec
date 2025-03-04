# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio/tag_studio.py'],
    pathex=['/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio'],
    binaries=[],
    datas=[('/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio/resources', './resources'), ('/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio/src', './src')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TagStudio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio/resources/icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TagStudio',
)
app = BUNDLE(
    coll,
    name='TagStudio.app',
    icon='/Users/dima/PycharmProjects/assignment-4-ISSUE-RESOLUTION/tagstudio/resources/icon.ico',
    bundle_identifier=None,
)
