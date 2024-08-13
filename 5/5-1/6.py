slug = input()
while "--" in slug:
    slug = slug.replace("--", "-")
print(slug)