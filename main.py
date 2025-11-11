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
