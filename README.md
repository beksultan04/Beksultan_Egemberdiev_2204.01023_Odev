# 🧮 Ödev 1 — Dinamik Programlama (DP)  
## Konu: **Factorial (Memoization)** — Python

---

## 📌 1. Problemin Tanımı ve Amaçları

**Problem:** Pozitif bir tam sayı `n` için `n!` (n faktöriyel) değerini hesaplamak.

Tanım olarak:
- `0! = 1`
- `n! = n × (n-1)!`  (n ≥ 1)

**Amaç:**
- Faktöriyel fonksiyonunu **dinamik programlama (memoization)** ile uygulamak.  
- Hesaplanan ara sonuçları saklayarak tekrar eden hesaplamalardan kaçınmak.  
- Zaman ve bellek karmaşıklığını analiz etmek.

---

## 🧩 2. DP Yaklaşımı — Recurrence Relation

**Rekürens formülü:**
\[
F(0) = 1, \quad F(n) = n \times F(n-1)
\]

**Memoization stratejisi:**
- `memo` adlı bir tablo (dictionary) oluşturulur.
- Eğer `memo` içinde `n` değeri varsa doğrudan döndürülür.
- Yoksa `n-1` değeri hesaplanır, çarpım sonucu saklanır.

Bu yaklaşıma **üstten-aşağı (Top-Down DP)** veya **Memoization** denir.

---

## 💻 3. Kod (Python)

```python
# Versiyon A: functools.lru_cache ile kısa çözüm
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_lru(n: int) -> int:
    if n < 0:
        raise ValueError("n negatif olamaz")
    if n == 0:
        return 1
    return n * factorial_lru(n - 1)

print("factorial_lru(6) =", factorial_lru(6))


# Versiyon B: Manuel memoization (ödev için açıklamalı)
def factorial_memo(n: int, memo=None) -> int:
    """
    Üstten-aşağı (top-down) memoization ile faktöriyel hesaplama.
    memo: dict, anahtar: int n, değer: n!
    """
    if n < 0:
        raise ValueError("n negatif olamaz")
    if memo is None:
        memo = {0: 1}
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]

# Örnek çalıştırma
memo_example = {0: 1}
result = factorial_memo(6, memo_example)
print("factorial_memo(6) =", result)
print("Memo tablosu:")
for k in sorted(memo_example.keys()):
    print(f"{k} : {memo_example[k]}")
📊 4. Küçük Bir Örnek (n = 6)
Adım adım factorial_memo(6) çağrısı:

n	memo[n]	Açıklama
0	1	Baz değer
1	1	1 × 1
2	2	2 × 1
3	6	3 × 2
4	24	4 × 6
5	120	5 × 24
6	720	6 × 120

Sonuç: 6! = 720

⏱️ 5. Zaman ve Bellek Karmaşıklığı
Durum	Zaman Karmaşıklığı	Bellek Karmaşıklığı	Açıklama
Tek bir factorial(n) çağrısı	O(n)	O(n)	Rekürsif çağrı derinliği n
Çok sayıda farklı n çağrısı	O(N)	O(N)	En büyük N için bir kere hesaplanır
İteratif versiyon	O(n)	O(1)	Daha az bellek kullanır

Memoization’un avantajı:
Birden fazla factorial(x) çağrısında ara sonuçları saklayarak tekrar hesaplamayı önler.

📘 6. Örnek Çıktı
yaml
Копировать код
factorial_memo(6) = 720
Memo tablosu:
0 : 1
1 : 1
2 : 2
3 : 6
4 : 24
5 : 120
6 : 720
🧠 7. Sonuç
Faktöriyel problemi basit bir rekürsif yapı gösterir.

Memoization, alt problemleri tekrar hesaplamadan daha verimli hale getirir.

DP prensiplerini anlamak için ideal bir başlangıç örneğidir.

📄 Hazırlayan: Beksultan Egemberdiev
💻 Konu: Dinamik Programlama — Factorial (Memoization)
🗓️ Dil: Python
