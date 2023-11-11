# Tạo một từ điển để lưu trữ tần số của các nốt
note_frequencies = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
}
# Nhập tần số từ người dùng
frequency = float(input("Nhập một tần số (theo Hz): "))
closest_note = None
min_difference = 1  # Trong vòng 1 Hertz

for note, note_frequency in note_frequencies.items():
  difference = abs(frequency - note_frequency)
  if difference <= min_difference:
    closest_note = note
    min_difference = difference

if closest_note:
  print(f"Nốt gần nhất với {frequency} Hz là {closest_note}.")
else:
  print("Tần số không tương ứng với một nốt nào trong bảng.")