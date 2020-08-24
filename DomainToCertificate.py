from maltego_trx.transform import DiscoverableTransform
import requests


class DomainToCertificate(DiscoverableTransform):
    """
        Receive Domain from the client, and find certificates belonging to domain.
        """

    @classmethod
    def create_entities(cls, request, response):
        domain = request.Value
        url = 'https://crt.sh/'
        params = dict(
            CN=domain,
            output='json'
        )
        resp = requests.get(url=url, params=params)
        data = resp.json()
        for cert in data:
            e = response.addEntity('maltego.Certificate', cert['id'])
            e.addProperty('IssuedTo', 'Issued To', 'loose', cert['name_value'])
            e.addProperty('IssuerName', 'Name of Issuer', 'loose', cert['issuer_name'])
            e.addProperty('IssuerID', 'ID of Issuer', 'loose', cert['issuer_ca_id'])
            e.addProperty('ExpiryDate', 'Date of Expiry', 'loose', cert['not_after'])
