SHORT_SCALE_NUMERIC_NOTATION = NotImplemented
SHORTSCALE_firstcycle_letter_dict = ["", "K", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "Oc", "No", "Dc"]
def Convert_Number_to_Short_Scale_Notation(number):
    pass

def Convert_Short_Scale_Notation_to_Number(short_scale_number_str):
    # Strip whitespace and validate input
    short_scale_number_str = short_scale_number_str.strip()
    if not short_scale_number_str:
        return 0

    # get letters out of short_scale_number_str
    letters = ""
    for char in short_scale_number_str:
        if char.isalpha():
            letters += char
    letters = letters.lower()
    
    # get number out of short_scale_number_str
    number_str = short_scale_number_str
    for letter in letters:
        number_str = number_str.replace(letter.upper(), "").replace(letter.lower(), "")
    
    # Clean up the number string
    number_str = number_str.strip()
    if not number_str:
        number_str = "0"
    
    try:
        # Convert dictionary items to lowercase for comparison
        lower_dict = [x.lower() for x in SHORTSCALE_firstcycle_letter_dict]
        
        if letters in lower_dict:
            index = lower_dict.index(letters)
            multiplier = 10 ** (index * 3)
            return float(number_str) * multiplier
        
        return float(number_str)  # Return original number if no letters match
    except ValueError:
        return 0  # Return 0 if conversion fails

SCIENTIFIC_NOTATION = NotImplemented
ENGINEERING_NOTATION = NotImplemented
LONG_SCALE_NUMERIC_NOTATION = NotImplemented