Influencer_Name = input("Enter the name of the influencer: ")
Facbook = bool(input("Does the influencer have a Facebook account? (True/False): "))
Instagram = bool(input("Does the influencer have an Instagram account? (True/False): "))
Twiter = bool(input("Does the influencer have a Twitter account? (True/False): "))
count = 0

if Facbook == True:
    count += 1
if Instagram == True:
    count += 1
if Twiter == True:
    count += 1  
if count >= 2:
    print(f"{Influencer_Name} is a good influencer.")