# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

src_dir = os.path.abspath('.')
packages_dir = r'./venv/Lib/site-packages'

a = Analysis(['cli.py'],
             pathex=[src_dir],
             binaries=[
                (packages_dir + '/prokaryote/*.jar', './prokaryote'),
                (packages_dir + '/bioformats/jars/*.*', './bioformats/jars'),
                (packages_dir + '/javabridge/jars/*.*', './javabridge/jars'),
                ],
             datas=[
                ('cellprofiler/data', 'cellprofiler/data'),
                ('cellprofiler/modules', 'cellprofiler/modules'),
                ],
             hiddenimports=[
                'scipy.special',
                'scipy.special.cython_special',
                'cellprofiler.utilities',
                'cellprofiler.utilities.morphology',
                'cellprofiler.utilities.rules',
                'cellprofiler_core.modules',
                'cellprofiler_core.modules.align',
                'centrosome',
                'centrosome.bg_compensate',
                'centrosome.fastemd',
                'centrosome.fastemd',
                'centrosome.haralick',
                'centrosome.kirsch',
                'centrosome.lapjv',
                'centrosome.propagate',
                'centrosome.radial_power_spectrum',
                'centrosome.threshold',
                'centrosome.zernike',
                'inflect',
                'mahotas',
                'sqlite3',
                ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# Multi-file version (debug)
# exe = EXE(pyz,
          # a.scripts,
          # [],
          # exclude_binaries=True,
          # name='CellProfiler',
          # icon='./cellprofiler/data/icons/CellProfiler.ico',
          # debug=False,
          # bootloader_ignore_signals=False,
          # strip=False,
          # upx=False,
          # console=True )
# coll = COLLECT(exe,
               # a.binaries,
               # a.zipfiles,
               # a.datas,
               # strip=False,
               # upx=False,
               # upx_exclude=[],
               # name='cli')

# Single exe version
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CellProfiler',
          icon='./cellprofiler/data/icons/CellProfiler.ico',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )