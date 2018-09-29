# -*- mode: python -*-

block_cipher = None


a = Analysis(['D9_xls.py'],
             pathex=['C:\\Users\\敲键盘的钢琴师\\Desktop\\mis项目\\子项目\\15.2基于贝叶斯算法的银行用户信用等级评估（程序+文档）'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='D9_xls',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
