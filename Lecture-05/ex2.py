def generate_primes(n):
    primes = []
    for num in range(2, n + 1): #Set ให้ num เริ่มจาก 2 ถึง n
        is_prime = True #ตั้งให้ ตัวแปร เป็น True
        for prime in primes: #สร้างลูบวน for เพื่อเช็คว่า num เป็นจำนวนเฉพาะหรือไม่
            if prime * prime > num: #ถ้า prime ยกกำลังสองมากกว่า num ให้หยุดการเช็คด้วยคำสั่ง break
                break
            #ถ้า num หารลงตัวเท่ากับ 0 ให้ตั้ง is_prime เป็น False และหยุดการเช็คด้วยคำสั่ง break
            if num % prime == 0: 
                is_prime = False
                break
        if is_prime: #
            primes.append(num)
    return primes

print(generate_primes(10))  # Output: [2, 3, 5, 7]
print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(generate_primes(1))
print(generate_primes(2))