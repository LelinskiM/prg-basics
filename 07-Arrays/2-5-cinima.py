# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   count=0
   for row in seats:
      for seat in row:
         count += 1
   return count

def seats_available(seats):
    countA=0
    for row in seats:
      for seat in row:
         if seat == 'A':
            countA += 1
    return countA

def seats_booked(seats):
    countB=0
    for row in seats:
      for seat in row:
         if seat == 'B':
            countB += 1
    return countB

def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':
      return 'Available'
   else:
      return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))