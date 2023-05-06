def main():
    prompt = input("File name: ").lower().strip()
    result = extens(prompt)
    print(result)

def extens(w):
    if ".gif" in w:
        return "image/gif"
    elif ".jpeg" in w or ".jpg" in w:
        return "image/jpeg"
    elif ".png" in w:
        return "image/png"
    elif ".pdf" in w:
        return "application/pdf"
    elif ".txt" in w:
        return "text/plain"
    elif ".zip" in w:
        return "application/zip"
    else:
        return "application/octet-stream"

main()