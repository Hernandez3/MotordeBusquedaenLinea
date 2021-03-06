#Driver para el protocolo de mac de IEEE 802.15.4

from framer import framer_ieee802154

class driver_ieee802154:
  def __init__(self, radio):
    self.__radio = radio
    self.__framer = framer_ieee802154()

  def escr_config_red(self, canal, pan_id, dir_corta):
    #Traslada la configuracion al radio
    self.__radio.escr_canal(canal)
    self.__radio.escr_pan_id(pan_id)
    self.__radio.escr_dir_corta(dir_corta)

    #Traslada la configuracion al framer
    self.__framer.escr_pan_id(pan_id)
    self.__framer.escr_dir_corta(dir_corta)

  def enviar_paquete(self, destino, payload):
    paquete = self.__framer.crear_mpdu(destino, payload)
    return self.__radio.enviar_paquete(paquete)

  def hay_paquete(self):
    return self.__radio.hay_paquete()

  def recibir_paquete(self):
    paquete = self.__radio.recibir_paquete()
    return self.__framer.extraer_payload(paquete)
