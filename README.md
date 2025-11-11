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
# Versiyon A: functools.lru_cache ile (kısa ve pratik)
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_lru(n: int) -> int:
    if n < 0:
        raise ValueError("n negatif olamaz")
    if n == 0:
        return 1
    return n * factorial_lru(n - 1)

# Test
print("factorial_lru(6) =", factorial_lru(6))
# LRU cache içeriğini görmek için:
print("Cached keys:", list(factorial_lru.cache_info().__dict__.get('currsize', 'unknown')))


# Versiyon B: Manuel memoization ile (eğitici)
def factorial_memo(n: int, memo=None) -> int:
    """
    Üstten-aşağı (top-down) memoization ile faktoriyel.
    memo: dict, anahtar: int n, değer: n!
    """
    if n < 0:
        raise ValueError("n negatif olamaz")
    if memo is None:
        memo = {0: 1}  # baza
    if n in memo:
        return memo[n]
    # hesapla, sakla, döndür
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]

# Manuel örnek ve memo'yu gösterme
memo_example = {0: 1}
result = factorial_memo(6, memo_example)
print("factorial_memo(6) =", result)
print("Memo tablosu (anahtar: değer):")
for k in sorted(memo_example.keys()):
    print(f"  {k} : {memo_example[k]}")
Not: lru_cache kullanınca Python otomatik cache tutar; manuel versiyon ödev için adım adım izlemesi daha açıktır.

4) Küçük bir örnekle tablo gösterimi (n = 6)

İsterseniz factorial_memo(6) çağrısının nasıl çalıştığını adım adım gösterelim. memo başlangıçta {0:1}.

Çağrı akışı (üstten aşağı — rekürsif):

fact(6) → 6 * fact(5)

fact(5) → 5 * fact(4)

fact(4) → 4 * fact(3)

fact(3) → 3 * fact(2)

fact(2) → 2 * fact(1)

fact(1) → 1 * fact(0)

fact(0) → baz = 1 (memo zaten {0:1})

Unwind (geri dönüş) ve memo’ya yazma sırası:

fact(1) hesaplanır: 1 * 1 = 1 → memo[1] = 1

fact(2) hesaplanır: 2 * memo[1] = 2 → memo[2] = 2

fact(3) hesaplanır: 3 * memo[2] = 6 → memo[3] = 6

fact(4) → 4 * 6 = 24 → memo[4] = 24

fact(5) → 5 * 24 = 120 → memo[5] = 120

fact(6) → 6 * 120 = 720 → memo[6] = 720

Son memo tablosu (sıralı):
n	memo[n]
0	1
1	1
2	2
3	6
4	24
5	120
6	720
Bu tablo özetle n! değerlerini tutar; ileride factorial(4) gibi çağrılar olursa doğrudan memo[4] döner, tekrar hesaplama gerekmez.

5) Zaman ve bellek karmaşıklığı (analysis)

Tek bir factorial(n) çağrısı için:

Zaman karmaşıklığı (Time): 
𝑂
(
𝑛
)
O(n).

Sebep: rekürsif olarak n den 0 a kadar bir kere çağrı yapılıyor; her seviye sabit miktarda iş yapıyor (çarpma).

Not: Basit rekürsif (memo kullanmadan) çözüm de tek çağrı için 
𝑂
(
𝑛
)
O(n) dır — burada memoization asimptotik süre iyileştirmesi getirmez.

Bellek karmaşıklığı (Space): 
𝑂
(
𝑛
)
O(n) (rekürsif çağrı yığını + memo saklama).

memo içinde n+1 tane anahtar olabilir (0..n) → O(n).

Rekürsiyon derinliği n → O(n) stack.

Birden fazla farklı n çağrısı yapılıyorsa (ör. program boyunca farklı n değerlerine tekrar tekrar ihtiyaç varsa):

Memoization çok faydalıdır: ilk çağrıda 
𝑂
(
𝑛
)
O(n) çalışılır, sonraki çağrılar (kullandığınız n'den küçük değerler için) O(1) zaman alır (sadece lookup).

Genel senaryo: birden çok n değeri için toplam maliyet, en büyük N için 
𝑂
(
𝑁
)
O(N) olur; tekrarlar bedava.

Alternatif (iterative bottom-up)

İteratif bir döngü ile sadece son sonucu istiyorsanız zaman 
𝑂
(
𝑛
)
O(n), ekstra bellek 
𝑂
(
1
)
O(1) (sadece bir değişken tutarak) elde edebilirsiniz. Eğer bütün ara faktöriyel değerlerini saklamak isterseniz, O(n) bellek gerekir.

Özet tavsiye:

Eğer sadece tek bir n için faktöriyel istiyorsanız — iteratif çözüm daha basit ve daha az stack kullanır.

Eğer program içinde birçok farklı n için faktöriyel isteniyorsa veya aynı fonksiyon birçok kez çağrılıyorsa — memoization yararlıdır.

Bonus: Örnek çıktı (manuel versiyon çalıştırıldığında)
factorial_memo(6) = 720
Memo tablosu (anahtar: değer):
  0 : 1
  1 : 1
  2 : 2
  3 : 6
  4 : 24
  5 : 120
  6 : 720
