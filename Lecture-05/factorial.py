def factorial(n):
    if n == 0:
        return 1 #Base case
    else:
        return n * factorial(n - 1) # Recursive case
# Example usage
print(factorial(5))
# Output: 120


''' อธิบายโครงสร้างโค้ดการนิยามฟังก์ชัน: def factorial(n): 
สร้างฟังก์ชันชื่อ factorial ที่รับค่าอินพุตเป็นจำนวนเต็ม nBase Case (กรณีฐาน): if n == 0: return 1 
เป็นเงื่อนไขสำหรับหยุดการทำงานซ้ำ เมื่อ n ลดลงจนเหลือ 0 จะส่งค่า 1 กลับไป 
เพื่อป้องกันไม่ให้โปรแกรมทำงานวนซ้ำไม่สิ้นสุด 
(Stack Overflow)Recursive Case (กรณีย้อนกลับ): return n * factorial(n - 1) 
ฟังก์ชันจะเรียกตัวเองซ้ำ โดยลดค่า n ลงทีละ 1 แล้วนำมาคูณกับค่า n ปัจจุบันขั้นตอนการทำงานของ factorial(5)
เมื่อสั่ง print(factorial(5)) โปรแกรมจะแตกตัวออกเป็นลำดับขั้น (Call Stack) ดังนี้:factorial(5) 
จะรอผลลัพธ์ของ \(5 \times \text{factorial}(4)\)factorial(4) จะรอผลลัพธ์ของ \(4 \times \text{factorial}(3)\)factorial(3) 
จะรอผลลัพธ์ของ \(3 \times \text{factorial}(2)\)factorial(2) จะรอผลลัพธ์ของ \(2 \times \text{factorial}(1)\)factorial(1) 
จะรอผลลัพธ์ของ \(1 \times \text{factorial}(0)\)factorial(0) ตรงกับเงื่อนไขฐาน (Base Case) จึงส่งค่ากลับเป็น \(1\)
    การคิดคำนวณขากลับเมื่อฟังก์ชันสุดท้ายส่งค่า 1 กลับมา ระบบจะคิดคำนวณย้อนกลับขึ้นไปตามลำดับ:factorial(1) 
    ได้ผลลัพธ์เป็น \(1 \times 1 = 1\)factorial(2) ได้ผลลัพธ์เป็น \(2 \times 1 = 2\)factorial(3) 
    ได้ผลลัพธ์เป็น \(3 \times 2 = 6\)factorial(4) ได้ผลลัพธ์เป็น \(4 \times 6 = 24\)factorial(5) 
    ได้ผลลัพธ์เป็น \(5 \times 24 = 120\)ผลลัพธ์สุดท้ายที่แสดงบนหน้าจอจึงเป็น 120'''