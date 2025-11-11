# Factorial (Memoization) — Python ile
1) Problem tanımı ve amaçlar

Problem: Pozitif tam sayı 
𝑛
n için 
𝑛
!
n! (n faktöriyel) değerini hesaplamak.
Tanım olarak:

0
!
=
1
0!=1

𝑛
!
=
𝑛
×
(
𝑛
−
1
)
!
n!=n×(n−1)! ( 
𝑛
≥
1
n≥1 )

Amaçlar:

Faktöriyel fonksiyonunu dinamik programlama (memoization) ile uygulamak.

Memoization (üstten aşağı DP) ile bir kere hesaplanan ara sonuçları saklayarak tekrarlı hesaplamalardan kaçınmayı göstermek.

Zaman ve bellek karmaşıklığını analiz etmek; memoization’un hangi durumlarda yararlı olduğunu tartışmak.

Not: Tek bir factorial(n) çağrısı için klasik rekürsif çözüm zaten 
𝑂
(
𝑛
)
O(n) çalışır çünkü her seviye yalnızca bir önceki değeri çağırır (yani örtüşen alt problemler yoktur). Ancak memoization, farklı n değerleri için tekrar tekrar çağrılar yapıldığında veya farklı kod parçalarının aynı ara sonuçlara ihtiyaç duyduğu durumlarda (ör. aynı program çalışırken birçok farklı faktöriyel isteniyorsa) faydalıdır.

2) DP yaklaşımı / recurrence relation (yenidenursive ilişki)

Rekreasyon (recurrence):

𝐹
(
0
)
=
1
F(0)=1

𝐹
(
𝑛
)
=
𝑛
×
𝐹
(
𝑛
−
1
)
F(n)=n×F(n−1) ( 
𝑛
≥
1
n≥1 )

Memoization stratejisi:

memo adında bir tablo (sözlük/dictionary) tutarız.

Eğer memo içerisinde n için değer varsa onu doğrudan döndürürüz.

Yoksa F(n-1) hesaplanır, n * F(n-1) elde edilir ve memo[n] olarak saklanır.

Bu yaklaşıma üstten-aşağı (top-down) DP / memoization denir.

3) Kod (Python, memoization ile)

İki versiyon koydum: 1) functools.lru_cache kullanan kısa versiyon, 2) manuel memo sözlüğü ile gösteren versiyon (ödev için anlatımı göstermek açısından faydalı).
