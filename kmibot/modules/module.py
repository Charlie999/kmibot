from typing import TYPE_CHECKING

import discord

if TYPE_CHECKING:
    from kmibot.client import DiscordClient
    from kmibot.api import FerryAPI


class Module:
    def __init__(self, client: "DiscordClient", api_client: "FerryAPI") -> None:
        pass

    async def on_ready(self, client: "DiscordClient") -> None:
        pass

    async def on_scheduled_event_create(
        self,
        client: "DiscordClient",
        event: discord.ScheduledEvent,
    ) -> None:
        pass

    async def on_scheduled_event_update(
        self,
        client: "DiscordClient",
        old_event: discord.ScheduledEvent,
        new_event: discord.ScheduledEvent,
    ) -> None:
        pass

    async def on_scheduled_event_user_add(
        self, client: "DiscordClient", event: discord.ScheduledEvent, user: discord.User
    ) -> None:
        pass

    async def on_scheduled_event_user_remove(
        self, client: "DiscordClient", event: discord.ScheduledEvent, user: discord.User
    ) -> None:
        pass
