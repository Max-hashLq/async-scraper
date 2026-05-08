from playwright.async_api import async_playwright, Browser, BrowserContext
from config.settings import HEADLESS, PROXY
from config.user_agents import USER_AGENTS
from scraper.utils import get_random_user_agent


class BrowserManager:
    def __init__(self, logger):
        self.logger = logger
        self.playwright = None
        self.browser: Browser | None = None

    async def start(self):
        self.playwright = await async_playwright().start()

        launch_kwargs = {
            "headless": HEADLESS,
            "args": [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        }

        if PROXY:
            launch_kwargs["proxy"] = PROXY
            self.logger.info("Using proxy: %s", PROXY.get("server"))

        self.browser = await self.playwright.chromium.launch(**launch_kwargs)
        self.logger.info("Browser started")

    async def new_context(self) -> BrowserContext:
        if not self.browser:
            raise RuntimeError("Browser is not started")

        user_agent = get_random_user_agent(USER_AGENTS)

        context = await self.browser.new_context(
            user_agent=user_agent,
            viewport={"width": 1366, "height": 768},
            locale="ru-RU",
            extra_http_headers={
                "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8"
            }
        )

        # 🔥 FULL STEALTH FIX
        await context.add_init_script("""
            // hide webdriver
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            // fake plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });

            // fake languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['ru-RU', 'ru', 'en-US']
            });

            // fake chrome object
            window.chrome = {
                runtime: {}
            };

            // permissions spoof
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications'
                    ? Promise.resolve({ state: Notification.permission })
                    : originalQuery(parameters)
            );
        """)

        self.logger.info("Created new browser context with UA: %s", user_agent)

        return context

    async def stop(self):
        if self.browser:
            await self.browser.close()
            self.logger.info("Browser closed")

        if self.playwright:
            await self.playwright.stop()
            self.logger.info("Playwright stopped")