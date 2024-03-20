import click
import hashlib

@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Password to generate NTLM hash for')
def generate_ntlm_hash(password):
    # Convert password string to bytes
    password_bytes = password.encode('utf-16le')  # NTLM expects UTF-16LE encoding
    
    # Calculate MD4 hash
    hash_obj = hashlib.new('md4')
    hash_obj.update(password_bytes)
    ntlm_hash = hash_obj.digest()
    
    click.echo("NTLM Hash: " + ntlm_hash.hex())

if __name__ == '__main__':
    generate_ntlm_hash()
