from bs4 import BeautifulSoup

html = """
<html>
<head>
<style>
p {
    color: red;
    font-size: 20px;
}
</style>
</head>
<body>
<p>This is a <span style="color: blue;">paragraph</span> with inline CSS.</p>
</body>
</html>
"""

with open('sample.txt', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
text = soup.get_text(separator=' ', strip=True)

print(text)
