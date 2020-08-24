from maltego_trx.transform import DiscoverableTransform


class CertificateToPhrase(DiscoverableTransform):
    """
        Receive Certificate from the client, and returns the Phrase with CN of issuer name
        """

    @classmethod
    def create_entities(cls, request, response):
        name = request.getProperty('IssuerName')
        cn = name[name.find('CN='):]
        response.addEntity('maltego.Phrase', cn)
