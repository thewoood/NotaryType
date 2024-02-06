def modify_text(text: str) -> str:
    new_text = convert_numbers(text)
    new_text = convert_coma(new_text)
    new_text = delete_breaks(new_text)

    return new_text

def convert_numbers(text):
    newText = text.replace('۱', '1')
    newText = newText.replace('۲', '2')
    newText = newText.replace('۳', '3')
    newText = newText.replace('۴', '4')
    newText = newText.replace('۵', '5')
    newText = newText.replace('۶', '6')
    newText = newText.replace('۷', '7')
    newText = newText.replace('۸', '8')
    newText = newText.replace('۹', '9')
    newText = newText.replace('۰', '0')
    return newText
    
def convert_coma(text):
  newText = text.replace(',', '،').replace('٫', '،')
  return newText

def delete_breaks(text):
  newText = " ".join(text.split())
  return newText


if __name__ == "__main__":
    modify_text()