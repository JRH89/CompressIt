from distutils.core import setup
import py2exe

setup(
    windows=['compression.py'],  # Use "windows" for GUI applications
     options={
        'py2exe': {
            'bundle_files': 1,  # Bundle everything into a single executable
            'compressed': True,  # Compress the library archive
            'includes': ['PIL'],  # Include any specific packages if needed
        }
    },
    zipfile=None,  # No separate zip file
)
