# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Vincent\\Desktop\\Gestt\\Menu'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('fleche.png','C:\\Users\\Vincent\\Desktop\\Gestt\\Menu\\fleche.png','DATA'),
				('plus4.png','C:\\Users\\Vincent\\Desktop\\Gestt\\Menu\\plus4.png','DATA'),
					('loupe.jpg','C:\\Users\\Vincent\\Desktop\\Gestt\\Menu\\loupe.jpg','DATA'),
						('deco.jpg','C:\\Users\\Vincent\\Desktop\\Gestt\\Menu\\deco.jpg','DATA'),
							('graphe.png','C:\\Users\\Vincent\\Desktop\\Gestt\\Menu\\graphe.png','DATA'),
								('logo1.ico','C:\\Users\\Vincent\\Desktop\\Gestt\\logo1.ico','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon="icon.ico"
		  )
