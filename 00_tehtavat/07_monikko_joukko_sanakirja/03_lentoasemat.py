# IDEA
# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, 
    # ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee haun, 
    # ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
    # (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

import os
# from random import randint
airlines = [("Tirana Airport" 	              ,    "LATI"),
("Yerevan Zvartnots Airport" 	  ,    "UDYZ"),
("Graz Airport" 	                  ,"LOWG"),
("Innsbruck Airport" 	          ,    "LOWI"),
("Klagenfurt Airport" 	          ,    "LOWK"),
("Linz Airport" 	                  ,"LOWL"),
("Salzburg Airport" 	              ,"LOWS"),
("Vienna Airport" 	              ,    "LOWW"),
("Baku Airport" 	                  ,"UBBB"),
("Minsk Airport" 	              ,    "UMMS"),
("Antwerp Airport" 	              ,"EBAW"),
("Brussels Airport" 	              ,"EBBR"),
("Charleroi Airport" 	          ,    "EBCI"),
("Liege Airport" 	              ,    "EBLG"),
("Ostend Bruges Airport" 	      ,    "EBOS"),
("Sarajevo Airport" 	              ,"LQSA"),
("Tuzla Airport" 	              ,    "LQTZ"),
("Burgas Airport" 	              ,    "LBBG"),
("Sofia Airport" 	              ,    "LBSF"),
("Varna Airport" 	              ,    "LBWN"),
("Dubrovnik Airport" 	          ,    "LDDU"),
("Pula Airport" 	                  ,"LDPL"),
("Rijeka Krk Airport" 	          ,    "LDRI"),
("Split Airport" 	              ,    "LDSP"),
("Zadar Airport" 	              ,    "LDZD"),
("Zagreb Airport" 	              ,    "LDZA"),
("Larnaca Airport" 	              ,"LCLK"),
("Paphos Airport" 	              ,    "LCPH"),
("Brno Airport" 	                  ,"LKTB"),
("Prague Airport" 	              ,    "LKPR"),
("Aalborg Airport" 	              ,"EKYT"),
("Aarhus Airport" 	              ,    "EKAH"),
("Billund Airport" 	              ,"EKBI"),
("Copenhagen Airport" 	          ,    "EKCH"),
("Vágar Airport" 	              ,    "EKVG"),
("Tallinn Airport" 	              ,"EETN"),
("Helsinki Airport" 	              ,"EFHK"),
("Kittilä Airport" 	              ,"EFKT"),
("Oulu Airport" 	                  ,"EFOU"),
("Rovaniemi Airport" 	          ,    "EFRO"),
("Tampere Airport" 	              ,"EFTP"),
("Turku Airport" 	              ,    "EFTU"),
("Vaasa Airport" 	              ,    "EFVA"),
("Ajaccio Airport" 	              ,"LFKJ"),
("Bastia Airport" 	              ,    "LFKB"),
("Bergerac Airport" 	              ,"LFBE"),
("Biarritz Airport" 	              ,"LFBZ"),
("Bordeaux Airport" 	              ,"LFBD"),
("Brest Bretagne Airport" 	      ,    "LFRB"),
("Figari South Corsica Airport" 	  ,"LFKF"),
("Lille Airport" 	              ,    "LFQQ"),
("Lyon-Saint Exupéry Airport" 	  ,    "LFLL"),
("Marseille Airport" 	          ,    "LFML"),
("Montpellier Airport" 	          ,"LFMT"),
("Nantes Airport" 	              ,    "LFRS"),
("Nice Airport" 	                  ,"LFMN"),
("Paris Beauvais Airport" 	      ,    "LFOB"),
("Paris Charles de Gaulle Airport" ,  "LFPG"),
("Paris Orly Airport" 	          ,    "LFPO"),
("Rennes Bretagne Airport" 	      ,"LFRN"),
("Réunion Roland Garros Airport" ,	  "FMEE"),
("Strasbourg Airport" 	          ,    "LFST"),
("Toulon-Hyères Airport" 	      ,    "LFTH"),
("Toulouse Blagnac Airport" 	      ,"LFBO"),
("Kutaisi Airport" 	              ,"UGKO"),
("Tbilisi Airport" 	              ,"UGTB"),
("Allgäu Airport Memmingen" 	      ,"EDJA"),
("Berlin Brandenburg Airport" 	  ,    "EDDB"),
("Bremen Airport" 	              ,    "EDDW"),
("Cologne Bonn Airport" 	          ,"EDDK"),
("Dortmund Airport" 	              ,"EDLW"),
("Dresden Airport" 	              ,"EDDC"),
("Düsseldorf Airport" 	          ,    "EDDL"),
("Frankfurt Airport" 	          ,    "EDDF"),
("Frankfurt-Hahn Airport" 	      ,    "EDFH"),
("Friedrichshafen Airport" 	      ,"EDNY"),
("Hamburg Airport" 	              ,"EDDH"),
("Hanover Airport" 	              ,"EDDV"),
("Karlsruhe Baden-Baden Airport" ,	  "EDSB"),
("Leipzig Halle Airport" 	      ,    "EDDP"),
("Munich Airport" 	              ,    "EDDM"),
("Münster Osnabrück Airport" 	  ,    "EDDG"),
("Nuremberg Airport" 	          ,    "EDDN"),
("Paderborn Lippstadt Airport" 	  ,"EDLP"),
("Stuttgart Airport" 	          ,    "EDDS"),
("Weeze Airport" 	              ,    "EDLV"),
("Aktion Airport" 	              ,    "LGPZ"),
("Athens Airport" 	              ,    "LGAV"),
("Chania Airport" 	              ,    "LGSA"),
("Corfu Airport" 	              ,    "LGKR"),
("Heraklion Airport" 	          ,    "LGIR"),
("Kefalonia Airport" 	          ,    "LGKF"),
("Kos Airport" 	                  ,"LGKO"),
("Lesvos Mytilene Airport" 	      ,"LGMT"),
("Mykonos Airport" 	              ,"LGMK"),
("Rhodes Airport" 	              ,    "LGRP"),
("Samos Airport" 	              ,    "LGSM"),
("Santorini Airport" 	          ,    "LGSR"),
("Skiathos Airport" 	              ,"LGSK"),
("Thessaloniki Airport" 	          ,"LGTS"),
("Zante Airport" 	              ,    "LGZA"),
("Budapest Airport" 	              ,"LHBP"),
("Debrecen Airport" 	              ,"LHDC"),
("Keflavik Airport" 	              ,"BIKF"),
("Cork Airport" 	                  ,"EICK"),
("Dublin Airport" 	              ,    "EIDW"),
("Irland West Airport Knock" 	  ,    "EIKN"),
("Kerry Airport" 	              ,    "EIKY"),
("Shannon Airport" 	              ,"EINN"),
("Alghero Airport" 	              ,"LIEA"),
("Ancona Airport" 	              ,    "LIPY"),
("Bari Airport" 	                  ,"LIBD"),
("Bergamo Airport" 	              ,"LIME"),
("Bologna Airport" 	              ,"LIPE"),
("Brindisi Airport" 	              ,"LIBR"),
("Cagliari Airport" 	              ,"LIEE"),
("Catania Fontanarossa Airport" 	  ,"LICC"),
("Comiso Airport" 	              ,    "LICB"),
("Florence Airport" 	              ,"LIRQ"),
("Genoa Airport" 	              ,    "LIMJ"),
("Lamezia Terme Airport" 	      ,    "LICA"),
("Milan Linate Airport" 	          ,"LIML"),
("Milan Malpensa Airport" 	      ,    "LIMC"),
("Naples Airport" 	              ,    "LIRN"),
("Olbia Costa Smeralda Airport" 	  ,"LIEO"),
("Palermo Airport" 	              ,"LICJ"),
("Perugia Airport" 	              ,"LIRZ"),
("Pescara Airport" 	              ,"LIBP"),
("Pisa Airport" 	                  ,"LIRP"),
("Rome Ciampino Airport" 	      ,    "LIRA"),
("Rome Fiumicino Airport" 	      ,    "LIRF"),
("Trapani Airport" 	              ,"LICT"),
("Treviso Airport" 	              ,"LIPH"),
("Trieste Airport" 	              ,"LIPQ"),
("Turin Airport" 	              ,    "LIMF"),
("Venice Airport" 	              ,    "LIPZ"),
("Verona Airport" 	              ,    "LIPX"),
("Almaty Airport" 	              ,    "UAAA"),
("Nursultan Nazarbayev Airport" 	  ,"UACC"),
("Pristina Airport" 	              ,"BKPR"),
("Riga Airport" 	                  ,"EVRA"),
("Kaunas Airport" 	              ,    "EYKA"),
("Vilnius Airport" 	              ,"EYVI"),
("Luxembourg Airport" 	          ,    "ELLX"),
("Malta Airport" 	              ,    "LMML"),
("Chisinau Airport" 	              ,"LUKK"),
("Podgorica Airport" 	          ,    "LYPG"),
("Tivat Airport" 	              ,    "LYTV"),
("Amsterdam Airport Schiphol" 	  ,    "EHAM"),
("Eindhoven Airport" 	          ,    "EHEH"),
("Groningen Airport Eelde" 	      ,"EHGG"),
("Maastricht Aachen Airport" 	  ,    "EHBK"),
("Rotterdam The Hague Airport" 	  ,"EHRD"),
("Skopje Airport" 	              ,    "LWSK"),
("Ålesund Airport" 	              ,"ENAL"),
("Bergen Airport" 	              ,    "ENBR"),
("Bodø Airport" 	                  ,"ENBO"),
("Haugesund Airport" 	          ,    "ENHD"),
("Kristiansand Airport" 	          ,"ENCN"),
("Oslo Airport" 	                  ,"ENGM"),
("Sandefjord Airport Torp" 	      ,"ENTO"),
("Stavanger Airport" 	          ,    "ENZV"),
("Tromsø Airport" 	              ,    "ENTC"),
("Trondheim Airport" 	          ,    "ENVA"),
("Gdansk Airport" 	              ,    "EPGD"),
("Katowice Airport" 	              ,"EPKT"),
("Kraków Airport" 	              ,    "EPKK"),
("Poznan Airport" 	              ,    "EPPO"),
("Szczecin-Goleniów Airport" 	  ,    "EPSC"),
("Warsaw Airport" 	              ,    "EPWA"),
("Warsaw Modlin Airport" 	      ,    "EPMO"),
("Wroclaw Airport" 	              ,"EPWR"),
("Faro Airport" 	                  ,"LPFR"),
("Lisbon Airport" 	              ,    "LPPT"),
("Madeira Airport" 	              ,"LPMA"),
("Ponta Delgada Airport" 	      ,    "LPPD"),
("Porto Airport" 	              ,    "LPPR"),
("Bucharest Henri Coanda Airport" ,	  "LROP"),
("Cluj-Napoca Airport" 	          ,"LRCL"),
("Iasi Airport" 	                  ,"LRIA"),
("Sibiu Airport" 	              ,    "LRSB"),
("Timisoara Airport" 	          ,    "LRTR"),
("Krasnodar Airport" 	          ,    "URKK"),
("Moscow Domodedovo Airport" 	  ,    "UUDD"),
("Moscow Sheremetyevo Airport" 	  ,"UUEE"),
("Moscow Vnukovo Airport" 	      ,    "UUWW"),
("Saint Petersburg Pulkovo Airport", "ULLI"),
("Sochi Airport" 	              ,    "URSS"),
("Belgrade Nikola Tesla Airport" ,	  "LYBE"),
("Niš Airport" 	                  ,"LYNI"),
("Bratislava Airport" 	          ,    "LZIB"),
("Košice Airport" 	              ,    "LZKZ"),
("Ljubljana Airport" 	          ,    "LJLJ"),
("Alicante Airport" 	              ,"LEAL"),
("Almeria Airport" 	              ,"LEAM"),
("Asturias Airport" 	              ,"LEAS"),
("Barcelona Airport" 	          ,    "LEBL"),
("Bilbao Airport" 	              ,    "LEBB"),
("Fuerteventura Airport" 	      ,    "GCFV"),
("Girona Airport" 	              ,    "LEGE"),
("Gran Canaria Airport" 	          ,"GCLP"),
("Granada-Jaén Airport" 	          ,"LEGR"),
("Ibiza Airport" 	              ,    "LEIB"),
("Jerez Airport" 	              ,    "LEJR"),
("La Palma Airport" 	              ,"GCLA"),
("Lanzarote Airport" 	          ,    "GCRR"),
("Madrid Barajas Airport" 	      ,    "LEMD"),
("Malaga Airport" 	              ,    "LEMG"),
("Menorca Airport" 	              ,"LEMH"),
("Palma de Mallorca Airport" 	  ,    "LEPA"),
("Región de Murcia Airport" 	      ,"LEMI"),
("Reus Airport" 	                  ,"LERS"),
("Santander Airport" 	          ,    "LEXJ"),
("Santiago de Compostela Airport" ,	  "LEST"),
("Seville Airport" 	              ,"LEZL"),
("Tenerife North Airport" 	      ,    "GCXO"),
("Tenerife South Airport" 	      ,    "GCTS"),
("Valencia Airport" 	              ,"LEVC"),
("Zaragoza Airport" 	              ,"LEZG"),
("Gothenburg Landvetter Airport" ,	  "ESGG"),
("Malmö Airport" 	              ,    "ESMS"),
("Stockholm Arlanda Airport" 	  ,    "ESSA"),
("Stockholm Bromma Airport" 	      ,"ESSB"),
("Stockholm Skavsta Airport" 	  ,    "ESKN"),
("Basel Mulhouse Freiburg Airport" ,"LFSB"),
("Geneva Airport" 	              ,    "LSGG"),
("Zurich Airport" 	              ,    "LSZH"),
("Ankara Esenboga Airport" 	      ,"LTAC"),
("Antalya Airport" 	              ,"LTAI"),
("Çukurova Airport" 	              ,"LTDB"),
("Dalaman Airport" 	              ,"LTBS"),
("Istanbul Airport" 	              ,"LTFM"),
("Istanbul Sabiha Gökcen Airport" ,	  "LTFJ"),
("Izmir Adnan Menderes Airport" 	  ,"LTBJ"),
("Milas-Bodrum Airport" 	          ,"LTFE"),
("Trabzon Airport" 	              ,"LTCG"),
("Kharkiv Airport" 	              ,"UKHH"),
("Kiev Boryspil Airport" 	      ,    "UKBB"),
("Kiev Zhuliany Airport" 	      ,    "UKKK"),
("Lviv Airport" 	                  ,"UKLL"),
("Odessa Airport" 	              ,    "UKOO"),
("Aberdeen Airport" 	              ,"EGPD"),
("Belfast City Airport" 	          ,"EGAC"),
("Belfast International Airport" ,	  "EGAA"),
("Birmingham Airport" 	          ,    "EGBB"),
("Bristol Airport" 	              ,"EGGD"),
("Cardiff Airport" 	              ,"EGFF"),
("East Midlands Airport" 	      ,    "EGNX"),
("Edinburgh Airport" 	          ,    "EGPH"),
("Exeter Airport" 	              ,    "EGTE"),
("Glasgow Airport" 	              ,"EGPF"),
("Glasgow Prestwick Airport" 	  ,    "EGPK"),
("Jersey Airport" 	              ,    "EGJJ"),
("Leeds Bradford Airport" 	      ,    "EGNM"),
("Liverpool Airport" 	          ,    "EGGP"),
("London City Airport" 	          ,"EGLC"),
("London Gatwick Airport" 	      ,    "EGKK"),
("London Heathrow Airport" 	      ,"EGLL"),
("London Luton Airport" 	          ,"EGGW"),
("London Southend Airport" 	      ,"EGMC"),
("London Stansted Airport" 	      ,"EGSS"),
("Manchester Airport" 	          ,    "EGCC"),
("Newcastle Airport" 	          ,    "EGNT"),
("Southampton Airport" 	          ,"EGHI")]
def find_airport():
    icao_koodi: str = None
    while not icao_koodi:
        # INPUT
        os.system("cls")
        icao_koodi = input("Anna lentoasema ICAO-koodi: ")
    for airline in airlines:
        if airline[1] == icao_koodi:
            print(airline[0])
            print(airline[1])
def add_airport():
    lentoasema: str = None
    icao_koodi: str = None
    while not lentoasema:
        # INPUT
        os.system("cls")
        lentoasema = input("Anna lentoasema nimi: ")
    while not icao_koodi:
        # INPUT
        os.system("cls")
        icao_koodi = input("Anna lentoasema icao-koodi: ")
    airlines.append((lentoasema,icao_koodi))
# INTRO
os.system("cls")
# LOGIC
while True:
    print("Choose a option:")
    print("""
          
0 - Exit program
1 - Insert new airport
2 - Search for an airport
          
          """)
    option = input()
    if not option or option == "0":
        break
    elif option == "1":
        add_airport()
    elif option == "2":
        find_airport()

#EXIT
os.system("cls")