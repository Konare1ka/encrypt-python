#main file that parses arguments using the native argparse library, 
#providing subsequent calls to encryption/decryption functions and passing arguments

#Python Libraries
import argparse
import importlib

parser = argparse.ArgumentParser(prog="cryptograph",
                                                         description="Utility for encryption by common ciphers",
                                                         epilog="""
To encrypt text with a Caesar cipher enter shift, text
example: --text \"Hello world!\" ceaser --shift 3 
""",
                                                          formatter_class=argparse.RawTextHelpFormatter)
subparser = parser.add_subparsers(dest='cipher', required=True, help='Choose cipher:')

ceaserCipher = subparser.add_parser('ceaser', help='Ceaser cipher mode')
vigenereCipher = subparser.add_parser('vigenere', help='Vigenere cipher mode')
reshufflesCipher = subparser.add_parser('reshuffles', help='Reshuffles cipher mode')

parser.add_argument('--text', type=str, help='Enter text for encryption', required=True)

ceaserCipher.add_argument('--shift', type=int, help='Enter shift for Ceaser encryption')
vigenereCipher.add_argument('--key', type=str, help='Enter string key')

args = parser.parse_args()

#CEASER
if args.cipher == 'ceaser':
    if args.text and args.shift:
        print(f"Encryption text \"{args.text}\" by Ceaser with shift \"{args.shift}\"")
        ceaser = importlib.import_module("ceaser")
        ceaser.ceaserEncrypt(args.text, args.shift)
            #вызов функции шифрования цезарем
    else: print("To encrypt by a Caesar cipher specify --text and --shift")
#VIGENERE
elif (args.cipher).lower() == 'vigenere':
    if args.text and args.key:
        if not any(char.isdigit() for char in args.text):
            print(f"Encryption text \"{args.text}\" by Vigenere with key \"{args.key}\"")     
            vigenere = importlib.import_module("vigenere")
            vigenere.vigenereEncrypt(args.text, args.key)
        else: print("Key must be a sequence of letters")
    else: print("To encrypt by Vigenere cipher specify --text and --key")

