# encoding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class KickStarterIE(InfoExtractor):
    _VALID_URL = r'https?://www\.kickstarter\.com/projects/(?P<id>[^/]*)/.*'
    _TESTS = [{
        'url': 'https://www.kickstarter.com/projects/1404461844/intersection-the-story-of-josh-grant?ref=home_location',
        'md5': 'c81addca81327ffa66c642b5d8b08cab',
        'info_dict': {
            'id': '1404461844',
            'ext': 'mp4',
            'title': 'Intersection: The Story of Josh Grant by Kyle Cowling',
            'description': (
                'A unique motocross documentary that examines the '
                'life and mind of one of sports most elite athletes: Josh Grant.'
            ),
        },
    }, {
        'note': 'Embedded video (not using the native kickstarter video service)',
        'url': 'https://www.kickstarter.com/projects/597507018/pebble-e-paper-watch-for-iphone-and-android/posts/659178',
        'info_dict': {
            'id': '78704821',
            'ext': 'mp4',
            'uploader_id': 'pebble',
            'uploader': 'Pebble Technology',
            'title': 'Pebble iOS Notifications',
        }
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_regex(
            r'<title>\s*(.*?)(?:\s*&mdash; Kickstarter)?\s*</title>',
            webpage, 'title')
        video_url = self._search_regex(
            r'data-video-url="(.*?)"',
            webpage, 'video URL', default=None)
        if video_url is None:  # No native kickstarter, look for embedded videos
            return {
                '_type': 'url_transparent',
                'ie_key': 'Generic',
                'url': url,
                'title': title,
            }

        return {
            'id': video_id,
            'url': video_url,
            'title': title,
            'description': self._og_search_description(webpage),
            'thumbnail': self._og_search_thumbnail(webpage),
        }
