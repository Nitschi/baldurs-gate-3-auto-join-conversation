# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('listen-in-*.png', '.'), ('settings.json', '.'), ('requirements.txt', '.')],
             upx=True,
             upx_exclude=[],
             name='baldurs-gate-3-auto-join-conversation')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='baldurs-gate-3-auto-join-conversation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          version='version_info.txt')
