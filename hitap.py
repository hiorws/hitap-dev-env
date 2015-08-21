# -*- coding: utf_8 -*-
from suds.client import Client

WSDL_URL = "https://hitap.sgk.gov.tr/WS_HizmetTakip/services/Hitap4cWEBBean/wsdl/Hitap4cWEBBean.wsdl"

H_USER = os.environ["HITAP_USER"]
H_PASS = os.environ["HITAP_PASS"]
H_TCNO = os.environ["HITAP_TCNO"]


client = Client(WSDL_URL, retxml=False)
result = client.service.HitapMethod(kullaniciAd = USERNAME, sifre = PASSWORD, tckn = TCNO).HitapServisBean

