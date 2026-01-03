def potong_desimal(bilangan, digit_hilangkan):
    digit_tersisa = len(str(bilangan).split('.')[1]) - digit_hilangkan
    return round(bilangan, digit_tersisa) if digit_tersisa > 0 else int(bilangan)
