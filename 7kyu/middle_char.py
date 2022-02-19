def get_middle(s):
    if len(s)%2==0: #kalimat panjangnya genap sehingga ada 2 nilai tengah
        mid = int(len(s)/2)-1 #mencari titik tengah pada kalimat -1 berperan untuk mengambil indeks asli karakter
        return s[mid]+s[mid+1] # s indek akan ditambah dengan s indeks + 1 karena kalimatnya memiliki panjang genap
    else:
        return s[int(len(s)/2)]
