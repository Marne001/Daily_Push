# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DailyPush.py'],
             pathex=['C:\\Users\\vanzy\\Desktop\\Programming\\Python\\Daily_Push'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='DailyPush',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='C:\\Users\\vanzy\\Desktop\\Programming\\Python\\Daily_Push\\Alecive-Flatwoken-Apps-Notifications.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DailyPush')
