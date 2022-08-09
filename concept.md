---
geometry: margin=2.5cm
mainfont: Fira Sans
monofont: Fira Mono
header-includes:
    - \usepackage[polish]{babel}
    - \pagestyle{plain}
---


# Koncepcja tagowania za pomocą DNA

1. Simple TAG
    * Bierzemy z listy trzy primery: `pr_1` , `pr_2` i `pr_3`.
    * Losujemy wartość $l$ z przedziału 100 : 400 z rozdzielczością 50 (100, 150, 200, 250)
    * Losujemy wartość $p$ z przedziału 50 : 600 - $l$
    * Budujemy nić DNA zgodnie ze schematem:
        
        ```txt
                      f_1                          f_2                  f_3
        <pr_1> ******************** <pr_2> ****************** <pr_3> *********
        +      +                  +        +                +        +       +
        0      21                 p+21     p+41             p+41+l   p+61+l 600
        ```
        ```
        tag = pr_1 + f_1 + pr_2 + f_2 + pr_3 + f_3
        ```
        
        Suma $pr_1 + f_1 + pr_2 + f_2 + pr_3  + f_3= 600$, czyli `len(tag) = 600`.
        
    * Udostępniamy użytkownikowi `TAG` jako sekwencję DNA do syntezy.
    
    * Weryfikacja:
      * Dwie reakcje PCR dla par primerów: `pr_1 : pr_3` i `pr_2 : pr_3`.
      * Układ prążków na żelu powinien byc zgodny ze schematem jaki dają wartości $l$ i $p$.
  
2. Data Storage

    * Użytkownik wprowadza ciąg bitów o długości $n$.
    * Ustalamy, że na jednej nici kodujemy $k$ bitów
    * Wyznaczamy ile nici potrzebujemy do zakodowania ciągu: $n/k$ (ostatnia nić może być niepełna, więc będziemy dodawać dopełnienie - losowy ciąg nukleotydów)
    * Dla każdej nici wybieramy z zestawu primerów bity "0" i "1" oraz primery "S" i "E"
    * Dla każdej nici wybieramy $k+1$ primerów jako "binding sites"
    * Schemat dla jednej nici:

        $$
            S - B_1 - s_1 - B_2 - s_2 - \ldots - s_{k-1} - B_k - E
        $$
    * Schemat dla nici $m$-tej:

        $$
            S_m - B_{1:m} - s_{1:m} - B_{2:m} - s_{2:m} - \ldots -
            - s_{k-1:m} - B_{k:m} - E_m
        $$
    * Komponenty:
        
        ```txt
        5' S_1 - B_1 - s_1
        5' s_1 - B_2 - s_2
        ...
        5' s_k - B_k - E
        ```
    * Sekwencje:

        ```txt
        S_1 - B_1 - s_1
        s_1 - B_2 - s_2 **RC**
        s_2 - B_3 - s_3
        s_3 - B_4 - s_4 **RC**
        ```


3. Secure TAG


```
5' ATA - GTA - CAT
5' CAT - TTA - CCG -> RC
5' CCG - ACC - TAT
```

Schemat nici:
```txt
S b s b s b s b e

```