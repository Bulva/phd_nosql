# Úkol č. 1
Srovnání rychlosti vykonání 50 náhodně vygenerovaných BBOXů ve SpatiaLite a MongoDB. Jako univerzální řešení bylo vybráno využití Pythonu, pro který existují API pro obě databáze. Použitá data se nacházejí ve složce *data*.

Bylo vygenerováno 50 BBOXů (*bboxs.csv*) v rozsahu použitých dat (*exported_10000_roads.shp*).
Následně byly z jednotlivých bboxů složeny selecty do databází a byl změřen čas pro jednotlivé SELECTY. Výsledky těchto SELECTů se nacházejí v souborech *spatialite_bbox_time.csv* a *mongodb_bbox_time.csv*.

Z časů vyplývá, že MongoDB je o řád až dva rychlejší, než selecty v rámci Spatilite databáze. Čas byl měřen v rámci Python skriptu, tudíž čas pouze pro SELECT může být o něco málo nižší. Rozsah kódu v rámci těchto dvou selectů není nijak výrazně rozdílný. Spíše záleží na preferenci a zkušenosti uživatele.

# Úkol č. 2
Druhý úkol byl o poznání naročnější. Vzhledem ke špatné funkcionalitě Python API pro Spatialite byla tato databáze nahrazena PostgreSQL. Data z databáze byly pomocí API nahrány do objektové struktury, aby se s nimi dalo lépe pracovat. Jednotlivé obce byly přiřazeny k vodním úsekům pomocí funkce *St_Distance()*. Následně začala rekurzivní iterace napříč povodím za využití funkce *St_Touches()*.

Počty obyvatel se počítaly proti proudu. V souboru s názvem *sum_postgresql.csv* se nachází počty obyvatel pro obce směrem proti proudu. Vzhledem k funkci *St_Touches()* samotné hledání dalších úseků nebylo nijak obtížné. Mnohem náročnější bylo správné vyladění iterace napříč povodím.

Databáze MongoDB se ukázala jako naprosto nevhodná pro řešení geoprostorových analýz. Ačkoliv design databáze vytváří rychlejší dotazování a fungování databáze, lze říci, že absence prostorových funkcí neumožňuje efektivně splnit tento úkol. Není problém ve spojení jednolivých obcí k říčním úsekům, ale problém je iterace povodí vzhledem k tomu, že by se opět musela použít funkce *$near*. Toto se ukázalo jako časově naprosto neefektivní na tvorbu. Kód by obsahoval mnohem větší část Python kódu a byl by celkově mnohem komplexnější.

Závěrem lze tedy říci, že ačkoliv MongoDB a nerelační databáze vykazují vyšší výkon, tak pro strukturovaná data a prostorové analýzy stále zcela vládne PostgreSQL. Stejně tak celý ekosystém je lépe navázán na relační databáze (chybí implementace v IDE, pluginy, import dat je komplikovanější apod.)

Veškeré použité soubory a kódy se nacházejí v repozitáři.

![alt meme](https://memegenerator.net/img/instances/66609673/im-not-sure-why-my-code-works-and-ad-this-point-im-too-afraid-to-debug.jpg "")



