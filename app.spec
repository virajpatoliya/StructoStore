# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('index.html', '.'), 
        ('expense.html', '.'),
        ('scanning.html', '.'),
        ('backup.html', '.'),
        ('reports.html', '.'),
        ('style.css', '.'),
        ('script.js', '.'),
        ('assets/Logo.jpg', 'assets')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='paragon_software',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    cipher=block_cipher,
    noarchive=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='paragon_software',
)
