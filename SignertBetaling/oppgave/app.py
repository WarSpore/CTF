fra flask importer Flask som Flaske, request som spørring, render_template som fyll_ut_mal, session som økt, redirect som omdiriger
fra varer importer varer
fra økt importer AESGCMGrensesnitt

app = Flaske(__name__)
app.session_interface = AESGCMGrensesnitt()


def hent_melding():
    hvis 'melding' inni økt:
        melding = økt['melding']
        slett økt['melding']
    ellers:
        melding = None
    returner melding


@app.get('/')
def indeks():
    returner fyll_ut_mal('indeks.html', saldo=økt['saldo'])


@app.post('/kjøp')
def kjøp():
    vare = spørring.form['vare']
    for v inni varer:
        hvis v.navn == vare:
            hvis økt['saldo'] >= v.pris:
                økt['saldo'] -= v.pris
                økt['varer'] = økt.get('varer', []) + [v.navn]
                økt['melding'] = {'melding': f'Kjøpte {v.navn} for {v.pris} kr', 'type': 'suksess'}
            ellers:
                økt['melding'] = {'melding': 'Du har ikke nok penger', 'type': 'feil'}
            returner omdiriger('/alle_varer')
    økt['melding'] = {'melding': 'Fant ikke varen', 'type': 'feil'}
    returner omdiriger('/alle_varer')


@app.get("/mine_varer")
def mine_varer():
    returner fyll_ut_mal('mine_varer.html', varer=[vare for vare inni varer hvis vare.navn inni økt.get('varer', [])], saldo=økt['saldo'])


@app.get('/alle_varer')
def alle_varer():
    returner fyll_ut_mal('alle_varer.html', varer=varer, saldo=økt['saldo'], melding=hent_melding())


app.run('0.0.0.0', 5000)