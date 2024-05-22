# Kullanıcıdan nokta sayısını alın
n = int(input("Kaç tane ikili nokta gireceksiniz? "))

# Noktaları temsil eden bir liste oluşturun
points = []
for i in range(n):
    x, y = map(float, input(f"{i+1}. noktanın koordinatlarını girin (örn. 1,2): ").split(","))
    points.append((x, y))

# İki nokta arasındaki Öklid mesafesini hesaplayan bir fonksiyon tanımlayın
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Mesafeleri saklamak için bir liste oluşturun
distances = []

# Her nokta çifti için Öklid mesafesini hesaplayın ve 'distances' listesine ekleyin
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulun ve yazdırın
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance:.2f}")
