import qrcode

def gerarQrcode(nome_colaborador):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    
    qr.add_data(nome_colaborador)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nome_colaborador}.png")
