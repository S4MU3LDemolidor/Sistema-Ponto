import cv2
from datetime import datetime
import json

def lerQrcode():
    arquivo = "json/data.json"

    # Verificar se o arquivo já existe, caso contrário, criar um novo
    try:
        with open(arquivo, 'r') as json_file:
            info_existente = json.load(json_file)
    except FileNotFoundError:
        info_existente = []

    # Acessar a webcam
    cap = cv2.VideoCapture(0)
    qrCodeDetector = cv2.QRCodeDetector()  # Inicializa o detector de QR code

    while True:
        # Ler o frame da webcam
        ret, frame = cap.read()

        if not ret:
            print('Não foi possível acessar a câmera')
            break

        else:
            cv2.imshow("Leitor de QR Code", frame)

            informacaoQRcode, bbox, _ = qrCodeDetector.detectAndDecode(frame)

            now = datetime.now()
            horario = now.strftime("%H:%M:%S")

            if informacaoQRcode:

                tipo = "entrada"
                encontrou = False

                for colaborador in info_existente:

                    if colaborador["nome_colaborador"] == informacaoQRcode:
                        tipo = "saida"

                        colaborador["info"] = {
                            "horario": horario,
                            "tipo": tipo
                        }

                        encontrou = True

                if not encontrou:
                    info = {
                        "nome_colaborador": informacaoQRcode,
                        "informacao": {
                            "horario": horario,
                            "tipo": tipo
                        }
                    }

                    info_existente.append(info)

                # Atualizar o arquivo JSON
                with open(arquivo, 'w') as json_file:
                    json.dump(info_existente, json_file, indent=4)

                print(f"Informação coletada: {informacaoQRcode}, horário: {horario}, tipo: {tipo}")
                break

        # Adicionando uma condição para sair com a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
