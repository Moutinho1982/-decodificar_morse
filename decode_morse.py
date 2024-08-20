import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e as palavras por dois espaços
    output : mensagem em texto claro
    '''
    msg_palavras = msg.split("  ")
    msg_claro = []
    for palavra in msg_palavras:
        msg_letras = palavra.split(" ")
        palavra_claro = "".join([dict_morse[letter] for letter in msg_letras])
        msg_claro.append(palavra_claro)
    return " ".join(msg_claro)

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : mensagem escrita em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

if __name__ == "__main__":
    msg_claro = decode_morse(sys.argv[1])
    save_clear_msg_csv_hdr(msg_claro)
