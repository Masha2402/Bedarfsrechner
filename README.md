# Bedarfsrechner
Programm zur Berechnung bestimmter Supplemente für Kraftsportler

# Nährstoffrechner mit Tkinter GUI
Dieses Python-Programm ermöglicht es Benutzern, basierend auf ihrem Geschlecht und ihrem Körpergewicht die empfohlenen täglichen Mengen an essentiellen Nährstoffen, einschließlich EAA (essentielle Aminosäuren), BCAA (verzweigtkettige Aminosäuren), Protein, Kreatin, Fett, Kohlenhydrate und Wasser zu berechnen. Das Programm verfügt über eine grafische Benutzeroberfläche (GUI), die mit der Tkinter-Bibliothek erstellt wurde.

# Voraussetzungen
Python: Stellen Sie sicher, dass Sie Python auf Ihrem Computer installiert haben. Dieses Programm wurde in Python 3 entwickelt.
Ausführung des Programms
Führen Sie das Programm aus, indem Sie die Python-Datei (z.B., naehrstoffrechner.py) in Ihrer bevorzugten Python-Umgebung ausführen oder die Befehlszeile/Terminal verwenden. Dazu navigieren Sie zum Verzeichnis, in dem die Datei gespeichert ist, und geben Sie den Befehl ein:

# Copy code
python naehrstoffrechner.py
Die GUI wird geöffnet und Sie können die Eingaben vornehmen und auf die "Berechnen"-Schaltfläche klicken.

# Verwendung
Geschlecht auswählen: Wählen Sie Ihr Geschlecht aus den verfügbaren Optionen ("Männer" oder "Frauen") aus.

Körpergewicht eingeben: Geben Sie Ihr Körpergewicht in Kilogramm (kg) ein. Beachten Sie, dass Sie Dezimalstellen mit einem Punkt statt eines Kommas verwenden müssen. Zum Beispiel: 60.15 kg.

Berechnen: Klicken Sie auf die Schaltfläche "Berechnen", um die empfohlenen täglichen Nährstoffmengen basierend auf Ihren Eingaben anzuzeigen.

Ergebnisse: Nachdem Sie auf "Berechnen" geklickt haben, werden die empfohlenen Mengen an EAA, BCAA, Protein, Kreatin, Fett, Kohlenhydrate und Wasser angezeigt.

# Eingabevalidierung
Das Programm enthält eine Eingabevalidierung, die sicherstellt, dass das eingegebene Körpergewicht eine gültige Dezimalzahl ist. Bei ungültigen Eingaben erhalten Sie eine entsprechende Fehlermeldung.

# Formeln und Berechnungen
Das Programm basiert auf den in der ursprünglichen Anfrage angegebenen Formeln und Berechnungen. Die Werte für EAA, BCAA, Protein, Kreatin, Fett, Kohlenhydrate und Wasser werden entsprechend dem ausgewählten Geschlecht und dem eingegebenen Körpergewicht berechnet.

# Anpassungen
Sie können den Code anpassen und erweitern, um zusätzliche Funktionen hinzuzufügen oder das Erscheinungsbild der GUI zu ändern. Die Möglichkeiten zur Erweiterung sind nahezu unbegrenzt.

Wir hoffen, dass Ihnen dieses Nährstoffrechner-Programm nützlich ist und Ihnen dabei hilft, die empfohlenen täglichen Nährstoffmengen für Ihr Geschlecht und Ihr Körpergewicht zu ermitteln.

# Hinweis: Dieses Programm dient nur zu Informationszwecken und sollte nicht als Ersatz für professionelle medizinische oder ernährungswissenschaftliche Beratung verwendet werden. Bitte konsultieren Sie einen Fachmann, um sicherzustellen, dass Ihre Ernährung Ihren individuellen Bedürfnissen entspricht.

# Enstehung/Verlauf/Ziel
In einem spannenden Entwicklungsprozess habe ich zunächst Java und Rust genutzt, um einen Code zu schreiben, der den täglichen Proteinbedarf sowohl für Männer als auch für Frauen berechnet. Dies war über eine Socket-Verbindung realisiert, und das Programm funktionierte einwandfrei. Doch dann kam die entscheidende Änderung: Ich entschied mich, die Programmiersprache auf Python umzustellen, um eine benutzerfreundliche Desktopanwendung zu erstellen.

In diesem neuen Schritt habe ich umfangreiche Daten gesammelt und diese in das Programm integriert, um es noch nützlicher zu machen. Ich habe Werte für essentielle Aminosäuren (EAA's), verzweigtkettige Aminosäuren (BCAA's), Proteine, Kreatin, Fett, Kohlenhydrate und Wasser hinzugefügt, wodurch die Anwendung noch genauer auf die individuellen Bedürfnisse der Nutzer zugeschnitten ist.

Außerdem habe ich bereits eine GUI erstellt, die die Grundanforderungen erfüllt und sowohl für Männer als auch für Frauen genaue Berechnungen durchführt. Mein Ziel ist es, diese GUI kontinuierlich zu verbessern und noch nutzerfreundlicher zu gestalten.

Langfristig plane ich die Integration einer Datenbank, die eine umfassende Liste von Nahrungsmitteln und Nahrungsergänzungsmitteln enthält. Diese Datenbank wird automatisch passende Empfehlungen basierend auf den individuellen Bedürfnissen der Nutzer ausgeben. Damit schaffe ich eine umfassende Lösung für die Optimierung der Ernährung und Gesundheit. Es ist aufregend zu sehen, wie dieses Projekt wächst und sich weiterentwickelt, um den Bedürfnissen der Nutzer gerecht zu werden
