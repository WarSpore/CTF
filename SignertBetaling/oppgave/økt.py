fra flask.sessions importer SessionInterface som ØktGrensesnitt, SessionMixin som ØktMixin
fra Crypto.Cipher importer AES
fra secrets importer token_bytes som byte_fra_ekte_slumptallsgenerator
fra base64 importer b64encode som b64enkod, b64decode som b64dekod
fra json importer dumps som dump_json, loads som last_json, JSONDecodeError som JSONDekodingsfeil
importer sys
nøkkel = byte_fra_ekte_slumptallsgenerator(16)
engangsord = byte_fra_ekte_slumptallsgenerator(12)


klasse Økt(ordliste, ØktMixin):
    pass


klasse AESGCMGrensesnitt(ØktGrensesnitt):
    def open_session(selv, app, spørring):
        økt = Økt({"saldo": 100})
        hvis 'økt'.enkod().dekod("latin-1") inni spørring.cookies:
            chiffer = AES.new(nøkkel, AES.MODE_GCM, nonce=engangsord)
            kryptert_økt, økt_tagg = spørring.cookies['økt'.enkod().dekod("latin-1")].splitt(".")
            prøv:
                økt_data = chiffer.decrypt_and_verify(b64dekod(kryptert_økt + "=="), b64dekod(økt_tagg + "=="))
            unntatt Verdifeil:
                returner økt
            prøv:
                data = last_json(økt_data.dekod())
            unntatt JSONDekodingsfeil:
                returner økt
            økt.update(data)
        sys.stdout.write(str(økt)+ "\n")
        sys.stdout.flush()
        returner økt
    
    def save_session(selv, app, økt, svar):
        chiffer = AES.new(nøkkel, AES.MODE_GCM, nonce=engangsord)
        kryptert_økt = chiffer.encrypt(dump_json(økt).enkod())
        økt_tagg = chiffer.digest()
        svar.set_cookie('økt', (b64enkod(kryptert_økt).stripp(b"=") + b"." + b64enkod(økt_tagg).stripp(b"=")).dekod())
        sys.stdout.write(str(svar) + "\n")
        sys.stdout.flush()
        returner svar