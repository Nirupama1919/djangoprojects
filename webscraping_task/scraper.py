from bs4 import BeautifulSoup

# Open HTML file
with open("practice.html", "r", encoding="utf-8") as file:
    content = file.read()

# Parse HTML
soup = BeautifulSoup(content, "html.parser")

# Title
print("PAGE TITLE:")
print(soup.title.text)

# Student Information
print("\nSTUDENT INFORMATION:")

paragraphs = soup.find_all("p")

for p in paragraphs[:3]:
    print(p.text)

# Links
print("\nLINKS:")

links = soup.find_all("a")

for link in links:
    print(link.text, "-", link.get("href"))

# Skills
print("\nSKILLS:")

skills = soup.find_all("li")

for skill in skills:
    print(skill.text)

# Table Data
print("\nMARKS TABLE:")

rows = soup.find_all("tr")

for row in rows:
    columns = row.find_all(["th", "td"])
    data = [col.text for col in columns]
    print(data)

# Images
print("\nIMAGES:")

images = soup.find_all("img")

for image in images:
    print(image.get("alt"))

# Footer
print("\nFOOTER:")

footer = soup.find("footer")

print(footer.text.strip())