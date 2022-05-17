import pytest
import requests


class TestUserAgent:
    user_agents = [(
                   'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                   'Mobile', 'No', 'Android'),
                   (
                   'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
                   'Mobile', 'Chrome', 'IOS'),
                   ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                    'Googlebot', 'Unknown', 'Unknown'),
                   (
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
                   'Web', 'Chrome', 'No'),
                   (
                   'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                   'Mobile', 'No', 'iPhone')]

    @pytest.mark.parametrize('user_agent, expected_platform, expected_browser, expected_device', user_agents)
    def test_user_agent(self, user_agent, expected_platform, expected_browser, expected_device):
        link = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        user_agent = {'User-Agent': user_agent}
        response = requests.get(link, headers=user_agent).json()
        actual_platform = response['platform']
        actual_browser = response['browser']
        actual_device = response['device']
        assert actual_platform == expected_platform, f'We wait {expected_platform}, but actually have {actual_platform}'
        assert actual_browser == expected_browser, f'We wait {expected_browser}, but actually have {actual_browser}'
        assert actual_device == expected_device, f'We wait {expected_device}, but actually have {actual_device}'
