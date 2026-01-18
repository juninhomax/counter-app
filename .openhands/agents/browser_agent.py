from openhands.sdk import Agent
from openhands.sdk.tools import BrowserToolSet

class BrowserAgent(Agent):
    def __init__(self):
        super().__init__(
            name="browser-agent",
            tools=[BrowserToolSet()]
        )

    async def run(self):
        page = await self.tools.browser.open("http://localhost:8011")
        text = await page.text_content("body")
        return text
