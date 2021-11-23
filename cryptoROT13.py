#Fonction remplacant la lettre "l" dans le dictionnaire "d" par sa valeur dans ce même dictionnaire
def chiffrement_lettre(l,d):
    for cle, valeur in d.items():
        if l==cle:
            return valeur
        elif l==' ':
            return ' '

#Fonction parcourant chaque lettre de la phrase "p" pour y appliquer la fonction "chiffrement_lettre" et retourne celle-ci chiffrée
def chiffrement_phrase(p,d):
	chiffrement=""
	for l in p:
		chiffrement+=chiffrement_lettre(l,d)
	return chiffrement

#Fonction inversant les clés et valeurs du dictionnaire "d" dans un nouveau dictionnaire "inv_d"
def inverse_dico(d):

	inv_d= {valeur: cle for cle, valeur in d.items()}
	return inv_d

#Fonction retournant simplement le dictionnaire des lettres de l'alphabet (en clé) associé à leur valeur après un decalage de 13 dans celui-ci (en valeur)
def dico_rot_13():

	d={"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
	return d

def decrypt(pc,ll):
	decrypt=""
	for l in pc:
		decrypt+=chiffrement_lettre(l,ll)
	return decrypt

#Fonction comptant le nombre d'occurences de chaque lettre dans la phrase "p"
def compte_lettres(p):
	
	count= {}

	for i in p:
		count[i]=p.count(i)
	return count

#Fonction ordonnant le nombre d'occurences de chaque lettre dans une phrase "p" dans l'ordre décroissant et renvoyant une liste avec les lettre les moins utilisées jusqu'aux plus utilisées
def tri_bulles_dico(count):
	
	decroissant=sorted(count.items(), key=lambda t: t[1], reverse=True)
	return decroissant

#Fonction combinant deux listes en un dictionnaire avec comme clé les valeurs de la première liste et en valeur les valeurs de la deuxième listes situées aux même emplacement
def arrays2dict(ks, vs):
    combi = {}
    for i in range(0, len(ks)):
        combi[ks[i]] = vs[i]
    return combi

def progPrincipal():

	#Initialisations
	p="phrase a chiffrer"
	pc="or z f kcgrkcgh fnnggh mg ug rofo onaougugna fqgb cn u eorrofu rgswfny or gafoa y cng fnbognng xfuorrg iwpaghafnag ga mfyoh or fqfoa gag woblg ufoh cng hgwog yg ufrlgcwh r fqfoa wgycoa f rf uohgwg ipcw gqoagw r lcuorofaopn yg hgh yghfhawgh or kcoaaf rf npcqgrrg pwrgfnh rf qorrg yg hgh fogcj ga gafdroa hf ygugcwg yfnh r org yg hcrroqfn iwgh blfwrghapn yfnh rf bfwprong yc hcy bgaag org gha ygh irch honscrogwgh grrg n gha scgwg bpuiphgg kcg yg hfdrg yg ugw ga f gnqowpn awpoh uorrgh yg rpns gn rfwsgcw grrg n f mfufoh irch y cn kcfwa yg uorrg grrg gha hgifwgg yc bpnaongna ifw cng bwokcg f igong qohodrg kco xorawg f awfqgwh cng ufhhg yg wphgfcj ga yg qfhg wgnygt qpch lfdoacgr ygh ipcrgh y gfc rf qgsgafaopn bpuug pn igca rg hciiphgw gha ifcqwg pc ipcw fonho yowg nfong pn n z awpcqg ifh y fwdwgh y cng bgwafong yougnhopn qgwh r gjawguoag pbboygnafrg f r gnywpoa pc h grgqgna rg xpwa upcrawog ga kcgrkcgh uohgwfdrgh dfaohhgh yg dpoh lfdoaggh ignyfna r gag ifw rgh sgnh kco xcogna rgh ipchhogwgh ga rgh xogqwgh yg blfwrghapn pn wgnbpnawg or gha qwfo rg ifruogw nfon hgaosgwg ufoh apcag r org f r gjbgiaopn yg bg ipona pbboygnafr ga y cn ghifbg awohag ga drfnblfawg kco dpwyg rf ugw gha bpcqgwag y gifohhgh dwpchhforrgh yg uzwag pypwoxgwfna ho ghaoug ifw rgh lpwaobcragcwh fnsrfoh r fwdchag z upnag hpcqgna f cng lfcagcw yg kcontg pc qonsa iogyh or z xpwug cn aforroh iwghkcg ouigngawfdrg ga blfwsg r fauphilgwg yg hgh ifwxcuh fc irch iwpxpny yg bg aforroh npn rpon yg r gjawguoag pwognafrg yg r org b gha f yowg yg rf irch grposngg rgswfny h gafoa dfao rco ugug cng igaoag lcaag kc or pbbcifoa kcfny ipcw rf iwguogwg xpoh ga ifw lfhfwy mg xoh hf bpnnfohhfnbg bgaag bpnnfohhfnbg ucwoa dogn qoag gn fuoaog bfw or z fqfoa bgwagh yfnh rg blgw wgbrch yg kcpo gjboagw r onagwga ga r ghaoug mg qoh kc or fqfoa wgbc cng xpwag gycbfaopn lgcwgchgugna hgwqog ifw ygh xfbcragh hiowoacgrrgh igc bpuucngh ufoh kc or gafoa onxgbag yg uohfnalwpiog ga hcmga f yg ufrlgcwgchgh fragwnfaoqgh y gnalpchofhug ga yg ugrfnbprog dogn kc or gca blgt rco dgfcbpci yg roqwgh or h gn hgwqfoa wfwgugna hgh iwonboifcj fuchgugnah bpnhohafogna f blfhhgw ga f igblgw pc f xrfngw hcw rf irfsg ga f awfqgwh rgh uzwagh gn kcgag yg bpkcorrfsgh ga y gblfnaorrpnh gnapuprpsokcgh hf bprrgbaopn fcwfoa ic xfowg gnqog f cn hefuugwyfu yfnh bgh gjbcwhopnh or gafoa pwyonfowgugna fbbpuifsng ifw cn qogcj ngswg npuug mcioagw kco fqfoa gag fxxwfnblo fqfna rgh wgqgwh yg rf xfuorrg ufoh kc pn n fqfoa ic ygboygw no ifw ugnfbgh no ifw iwpughhgh f fdfnypnngw hpn mgcng ufhhf eorr or bpnhoygwfoa bpuug hpn ywpoa yg rg hcoqwg ifwapca or n gha ifh ouiwpdfdrg kcg rgh ifwgnah yg rgswfny mcsgfna kcg bgrco bo fqfoa rf agag cn igc ygwfnsgg hg hpogna fiirokcgh f bpnxowugw mcioagw yfnh hpn pdhaonfaopn yfnh rg dca yg ugaawg cng ghigbg yg sfwyogn ga yg hcwqgorrfna fciwgh yc xcsoaox hpch rf rfaoacyg yg r org yg hcrroqfn rgh loqgwh hpna wfwgugna wospcwgcj ga b gha cn gqgngugna kcfny fc ygbron yg r fnngg rg xgc ygqogna onyohignhfdrg bgignyfna qgwh rg uorogc y pbapdwg or z gca cng mpcwngg y cn xwpoy wgufwkcfdrg mchag fqfna rg bpcblgw yc hprgor mg ug xwfzfoh cn blguon f awfqgwh rgh aforroh qgwh rf lcaag yg upn fuo kcg mg n fqfoh ifh qc ygicoh kcgrkcgh hgufongh mg ygugcwfoh frpwh f blfwrghapn f cng yohafnbg yg ngcx uorrgh yg r org ga rgh xfboroagh ipcw frrgw ga wgqgnow gafogna dogn uponh swfnygh kc fcmpcwy lco gn fwwoqfna f rf lcaag mg xwfiifo hgrpn upn lfdoacyg ga ng wgbgqfna ifh yg wgipnhg mg blgwblfo rf brgx pc mg hfqfoh kc grrg gafoa bfblgg m pcqwoh rf ipwag ga m gnawfo cn dgfc xgc xrfudfoa yfnh rg xpzgw b gafoa cng hcwiwohg ga f bpci hcw cng ygh irch fswgfdrgh mg ug ygdfwwfhhfo yg upn ifrgapa mg awfonfo cn xfcagcor fciwgh ygh dcblgh igaorrfnagh ga m faagnyoh ifaoguugna r fwwoqgg yg ugh lpagh igc fiwgh rf apudgg yg rf ncoa orh fwwoqgwgna ga ug xowgna cn fbbcgor apca f xfoa bpwyofr mcioagw apca gn wofna y cng pwgorrg f r fcawg hg ypnnfoa yc upcqgugna ga iwgifwfoa kcgrkcgh ipcrgh y gfc ipcw rg hpcigw rgswfny gafoa yfnh cng yg hgh bwohgh y gnalpchofhug bfw yg kcgr fcawg npu fiigrgw bgrf or fqfoa awpcqg cn doqfrqg onbpnnc xpwufna cn sgnwg npcqgfc ga uogcj gnbpwg or fqfoa blfhhg ga faawfig fqgb r fhhohafnbg yg mcioagw cn hbfwfdgg kc or bwpzfoa apca f xfoa npcqgfc ga hcw rgkcgr or yghowfoa fqpow upn pionopn rg rgnygufon ufaon"
	freq=["e","a","i","t","s","n","l","u","r","o","d","m","c","p","v","q","h","f","b","g","j","x","y","w","z","k"]
	d=dico_rot_13()

	#traitement
	lettre=input("Veuillez entrer une lettre:")
	lettre_chiffree=chiffrement_lettre(lettre,d)
	print(lettre_chiffree)
	
	d_tempo={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a","a":"b"}
	chiffrement=chiffrement_phrase(p,d_tempo)
	print(chiffrement)
	
	inv_d=inverse_dico(d_tempo)
	dechiffrement=chiffrement_phrase(chiffrement,inv_d)
	print(dechiffrement)
	
	chiffrement=chiffrement_phrase(p,d)
	print(chiffrement)
	
	count=compte_lettres(pc)
	tri=tri_bulles_dico(count)
	tri_dico=dict(tri)
	del tri_dico[' ']
	tri_cles=list(tri_dico.keys())
	print(tri_cles)
	
	ll=dict(zip(tri_cles,freq))
	print(ll)
	
	final=decrypt(pc,ll)
	final=final.replace("x","y")
	print(final)
progPrincipal()
