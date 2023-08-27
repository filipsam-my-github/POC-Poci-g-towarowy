the task
Bajtek i Bitek uwielbiają obserwować pociągi przejeżdżające niedaleko ich domu. Największą miłością pałają do
tych towarowych, bo są zwykle bardzo długie i mają różnorodne wagony. Chłopcy postanowili dokumentować
to, z jakich rodzajów wagonów składają się pociągi. Dla uproszczenia, potencjalne rodzaje wagonów będziemy
numerować od 1 do k. Wagony o tym samym rodzaju są dla chłopców nierozróżnialne.
Gdy pociąg przejeżdża, obaj chłopcy w swoich zeszytach notują rodzaje kolejnych wagonów. Bajtek jest
starszy i potrafi już bezbłędnie zanotować rodzaje wszystkich wagonów. Bitek jest młodszy i nie ma jeszcze
takiej wprawy w pisaniu. Zdarza się, że zanim zdąży zanotować rodzaj wagonu, przez przejazd przejadą już
kolejne wagony, których Bitek nie zauważy. Zatem na liście Bitka niektóre z wagonów mogą zostać pominięte.
Chłopcy analizują teraz swoje zapisy i zastanawiają się, które z wagonów pociągu Bitek mógł zanotować,
a które na pewno zostały przez niego przeoczone.
Wejście
Pierwszy wiersz wejścia zawiera trzy liczby całkowite n, m oraz k (1 ≤ n, m, k ≤ 300 000), oznaczające kolejno
długość listy Bajtka (równą liczbie wagonów w pociągu), długość listy Bitka oraz liczbę różnych rodzajów
wagonów.
W drugim wierszu znajduje się ciąg długości n złożony z liczb całkowitych z przedziału [1, k], oznaczających
kolejne rodzaje wagonów na liście Bajtka. W trzecim wierszu znajduje się ciąg długości m w takim samym
formacie – lista Bitka.
Możesz założyć, że Bitek być może pominął niektóre wagony z listy Bajtka, ale nie dopisał nic „dodatkowo”.
Innymi słowy, dane wejściowe dobrane są tak, że da się zmazać pewną liczbę wagonów (być może zero) z listy
Bajtka i uzyskać listę Bitka.
Wyjście
Na wyjście należy wypisać n liczb całkowitych pooddzielanych pojedynczymi odstępami: i-ta z tych liczb
ma być równa 1, jeśli i-ty wagon mógł zostać zanotowany przez Bitka, lub 0 jeśli na pewno nie mógł być
zanotowany.
Przykład
Dla danych wejściowych:
9 4 3
1 3 2 1 2 3 1 3 2
1 3 1 2
poprawnym wynikiem jest:
1 1 0 1 1 1 1 0 1
Wyjaśnienie przykładu: Bitek mógł zanotować wagony o numerach:
• 1, 2, 4 i 5,
• 1, 2, 4 i 9,
• 1, 2, 7 i 9,
• 1, 6, 7 i 9,
• albo 4, 6, 7 i 9.