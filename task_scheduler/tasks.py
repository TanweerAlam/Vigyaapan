import datetime

def pinging_google():

    print('Hello, I am a shecduled task ', datetime.datetime.today())

def ping_all_search_engines(sitemap_url=None):
    """
    Pings the popular search engines, Google, Yahoo, ASK, and
    Windows Live, to let them know that you have updated your
    site's sitemap. Returns successfully pinged servers.
    """
    from django.contrib.sitemaps import ping_google
    SEARCH_ENGINE_PING_URLS = (
        ('google', 'http://www.google.com/webmasters/tools/ping'),
        ('yahoo', 'http://search.yahooapis.com/SiteExplorerService/V1/ping'),
        ('ask', 'http://submissions.ask.com/ping'),
        ('live', 'http://webmaster.live.com/ping.aspx'),
    )
    successfully_pinged = []
    for (site, url) in SEARCH_ENGINE_PING_URLS:
        try:
            ping_google(sitemap_url=sitemap_url, ping_url=url)
            pinged = True
        except:
            pinged = False
        if pinged:
            successfully_pinged.append(site)
    print('successfully_pinged at ', successfully_pinged)
    return successfully_pinged