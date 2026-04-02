import polib
import os

def compile_translations():
    locale_dir = 'apts/locale'
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                mo_path = po_path.replace('.po', '.mo')
                po = polib.pofile(po_path)
                po.save_as_mofile(mo_path)
                print(f"Compiled {po_path} to {mo_path}")

if __name__ == "__main__":
    compile_translations()
