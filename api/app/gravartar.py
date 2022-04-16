# from xmlrpc.client import ServerProxy, Fault
from urllib.parse import urlparse, urlencode
from hashlib import md5


class Gravatar(object):
    """
    This class encapsulates all the unauthenticated methods from the API.
    """

    DEFAULT_IMAGE_SIZE = 80
    DEFAULT_IMAGE = [
        "404",
        "mm",
        "mp",
        "identicon",
        "monsterid",
        "wavatar",
        "retro",
        "robohash",
        "blank",
    ]
    RATINGS = [
        "g",
        "pg",
        "r",
        "x",
    ]
    PROFILE_FORMATS = ["json", "xml", "php", "vcf", "qr"]

    def __init__(self, email):
        self.email = sanitize_email(email)
        self.email_hash = md5_hash(self.email)

    def get_image(
        self,
        size=DEFAULT_IMAGE_SIZE,
        default="",
        force_default=False,
        rating="",
        filetype_extension=False,
        use_ssl=True,
    ):
        """
        Returns an URL to the user profile image.
        >>> g = Gravatar('myemailaddress@example.com')
        >>> g.get_image()
        'https://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'
        With *size* you can request a specific image size, by default, images are presented at 80px by 80px.
        You may request image anywhere from 1px up to 2048px.
        The *default* parameter is used to supply a default image when an email address has no match Gravatar image.
        *default* can be an URL or one of the built in options *404*, *mm*, *mp*, *identicon*, *monsterid*, *wavatar*, *robohash*, *retro* or *blank*.
        *force_default* force the default image to always load.
        *rating* can be used to request images by audience type. Possible values are *g*, *pg*, *r* or *x*.
        By default, only *g* rated images are displayed.
        *filetype_extension* add an optional `.jpg` extension.
        *use_ssl* can be used to request images via SSL.
        See more details on `Gravatar Image Requests <http://en.gravatar.com/site/implement/images/>`_.
        """
        base_url = "{protocol}://www.gravatar.com/avatar/" "{hash}{extension}{params}"

        params_dict = {
            "size": size,
            "default": default,
            "forcedefault": force_default,
            "rating": rating,
        }

        if params_dict["size"] == self.DEFAULT_IMAGE_SIZE:
            del params_dict["size"]
        else:
            if not (0 < params_dict["size"] < 2048):
                raise ValueError("Invalid image size.")
        if params_dict["default"] == "":
            del params_dict["default"]
        else:
            if not params_dict["default"] in self.DEFAULT_IMAGE:
                if not default_url_is_valid(params_dict["default"]):
                    raise ValueError(
                        "Your URL for the default image is not valid.")
        if params_dict["forcedefault"]:
            params_dict["forcedefault"] = "y"
        else:
            del params_dict["forcedefault"]
        if params_dict["rating"] == "":
            del params_dict["rating"]
        else:
            if not params_dict["rating"] in self.RATINGS:
                raise ValueError("Invalid rating value.")

        params = urlencode(params_dict)

        protocol = "https"
        if not use_ssl:
            protocol = "http"

        extension = ".jpg" if filetype_extension else ""
        params = "?%s" % params if params else ""
        data = {
            "protocol": protocol,
            "hash": self.email_hash,
            "extension": extension,
            "params": params,
        }
        return base_url.format(**data)

    def get_profile(self, data_format="", use_ssl=True):
        """
        Returns an URL to the profile information associated with the Gravatar account.
        >>> g = Gravatar('myemailaddress@example.com')
        >>> g.get_profile()
        'https://www.gravatar.com/0bc83cb571cd1c50ba6f3e8a78ef1346'
        See more details on `Gravatar Profile Requests <http://en.gravatar.com/site/implement/profiles/>`_.
        """
        protocol = "https"
        if not use_ssl:
            protocol = "http"

        base_url = "{protocol}://www.gravatar.com/{hash}{data_format}"

        if data_format and data_format in self.PROFILE_FORMATS:
            data_format = ".%s" % data_format

        data = {
            "protocol": protocol,
            "hash": self.email_hash,
            "data_format": data_format,
        }
        return base_url.format(**data)


def sanitize_email(email):
    """
    Returns an e-mail address in lower-case and strip leading and trailing
    whitespaces.
    >>> sanitize_email(' MyEmailAddress@example.com ')
    'myemailaddress@example.com'
    """
    return email.lower().strip()


def md5_hash(string):
    """
    Returns a md5 hash from a string.
    >>> md5_hash('myemailaddress@example.com')
    '0bc83cb571cd1c50ba6f3e8a78ef1346'
    """
    return md5(string.encode("utf-8")).hexdigest()


def default_url_is_valid(url):
    """
    Gravatar conditions for valid default URLs.
    >>> default_url_is_valid('http://example.com/images/avatar.jpg')
    True
    """
    result = urlparse(url)

    if result.scheme == "http" or result.scheme == "https":
        path = result.path.lower()
        if (
            path.endswith(".jpg")
            or path.endswith(".jpeg")
            or path.endswith(".gif")
            or path.endswith(".png")
        ):
            if not result.query:
                return True
    return False
