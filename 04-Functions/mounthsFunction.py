def month(n):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= n <= 12:
        return months[n - 1]
    else:
        return "Invalid month number"